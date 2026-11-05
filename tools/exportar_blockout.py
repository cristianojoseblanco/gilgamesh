#!/usr/bin/env python3
"""Exporta o blockout de Uruk (glTF) e a planta (JSON) a partir da prévia do Ato 1.

Requisitos: Playwright com Chrome e a prévia servida por HTTP com a three.js local,
porque o importmap precisa resolver "three" e "three/addons/" sem CDN. Exemplo:
  sed "s#https://cdn.jsdelivr.net/npm/three@0.170.0/#/node_modules/three/#g" previa-web/ato1/index.html > PASTA/ato1.html
  (PASTA com node_modules/three instalado) e python3 -m http.server 8765 dentro de PASTA.

Uso:  python3 tools/exportar_blockout.py unreal/importar/uruk_blockout.glb data/layout_uruk.json
"""
from playwright.async_api import async_playwright
BAKE = r"""
async () => {
  const THREE = await import('three');
  const { GLTFExporter } = await import('three/addons/exporters/GLTFExporter.js');
  const { mergeGeometries } = await import('three/addons/utils/BufferGeometryUtils.js');
  const X = window.__exp;
  const cats = new Map([[X.M.brick, 'Tijolo'], [X.M.plaster, 'Reboco'], [X.M.white, 'TemploBranco'], [X.M.wood, 'Madeira'], [X.waterMat, 'Agua'], [X.bankMat, 'Margem']]);
  const cores = { Tijolo: 0xa5805a, Reboco: 0xc9a682, TemploBranco: 0xebe3d4, Madeira: 0x6b4a2e, Agua: 0x3d5a4f, Margem: 0x5e4630, Terreno: 0xb8966c, Campos: 0x7d8547 };
  const buckets = new Map(); const m4 = new THREE.Matrix4(), c = new THREE.Vector3();
  const limpa = g => { const n = new THREE.BufferGeometry(); n.setAttribute('position', g.attributes.position.clone()); n.setAttribute('normal', g.attributes.normal.clone()); n.setIndex(g.index.clone()); return n; };
  const add = (cat, g) => { g.computeBoundingBox(); g.boundingBox.getCenter(c); const k = cat === 'Terreno' ? cat : `${cat}_${Math.floor(c.x / 800)}_${Math.floor(c.z / 800)}`; if (!buckets.has(k)) buckets.set(k, { cat, geos: [] }); buckets.get(k).geos.push(g); };
  let skipped = 0;
  for (const o of X.scene.children) {
    if (!o.isMesh) continue;
    let cat = cats.get(o.material);
    if (!cat && o.isInstancedMesh && o.geometry === X.unitBox && o.material.map === X.groundTex) cat = 'Campos';
    if (!cat && !o.isInstancedMesh && o.material.vertexColors && o.geometry.parameters && o.geometry.parameters.width === 10000) cat = 'Terreno';
    if (!cat) continue;
    if (!o.geometry.index) { skipped++; continue; }
    const base = limpa(o.geometry); o.updateMatrixWorld();
    if (o.isInstancedMesh) { for (let i = 0; i < o.count; i++) { o.getMatrixAt(i, m4); m4.premultiply(o.matrixWorld); add(cat, base.clone().applyMatrix4(m4)); } }
    else add(cat, base.clone().applyMatrix4(o.matrixWorld));
  }
  const out = new THREE.Scene(); const mats = {}; let verts = 0;
  for (const [k, b] of [...buckets.entries()].sort()) { const g = mergeGeometries(b.geos); verts += g.attributes.position.count;
    mats[b.cat] = mats[b.cat] || new THREE.MeshStandardMaterial({ name: 'M_' + b.cat, color: cores[b.cat], roughness: .95 });
    const me = new THREE.Mesh(g, mats[b.cat]); me.name = 'SM_Uruk_' + k; out.add(me); }
  const glb = await new GLTFExporter().parseAsync(out, { binary: true });
  const bytes = new Uint8Array(glb); let s = ''; for (let i = 0; i < bytes.length; i += 0x8000) s += String.fromCharCode.apply(null, bytes.subarray(i, i + 0x8000));
  const r2 = v => Math.round(v * 100) / 100;
  const layout = {
    unidade: 'metros; x = leste, z = sul, y = altura (converter para cm e eixos do Unreal ao importar)',
    cidade: X.CITY, muralha: X.wallPts.map(p => [r2(p[0]), r2(p[1])]), portas: X.gatePts.map(p => [r2(p[0]), r2(p[1])]),
    aguas: X.waters.map(w => ({ largura: w.w, pontos: w.pts.map(p => [r2(p[0]), r2(p[1])]) })), ruas: X.streets.map(s => s.map(p => [r2(p[0]), r2(p[1])])),
    pontes: X.bridges.map(b => ({ x: r2(b.x), z: r2(b.z), angulo: r2(b.ang), comprimento: r2(b.len), largura: b.w })),
    plataformas: X.plats, rampas: X.ramps, eanna: X.E, anu: X.A,
    casas_campos: ['x', 'z', 'meia_largura', 'meia_profundidade', 'angulo', 'altura'], casas: X.houses.map(h => [r2(h.x), r2(h.z), r2(h.hw), r2(h.hd), r2(h.ang), r2(h.h)]),
    lugares_ato1: Object.fromEntries(Object.entries(X.LUGAR).filter(([k, v]) => v && v.isVector3).map(([k, v]) => [k, [r2(v.x), r2(v.z)]])),
    fragmentos_ato1: Object.fromEntries(Object.entries(X.FPOS).map(([k, v]) => [k, [r2(v.x), r2(v.z)]])),
  };
  return { glb: btoa(s), layout: JSON.stringify(layout), meshes: out.children.length, verts, skipped };
}
"""
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/usr/bin/google-chrome', args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
        pg = await b.new_page(viewport={'width':400,'height':400})
        pg.on('pageerror', lambda e: print('ERR', e, flush=True))
        await pg.goto('http://localhost:8765/ato1.html')
        await pg.wait_for_function("document.getElementById('start').disabled===false", timeout=180000)
        r = await pg.evaluate(BAKE)
        open(sys.argv[1], 'wb').write(base64.b64decode(r['glb']))
        open(sys.argv[2], 'w').write(r['layout'])
        print('meshes', r['meshes'], 'verts', r['verts'], 'skipped', r['skipped'], flush=True)
        await b.close()
asyncio.run(main())
