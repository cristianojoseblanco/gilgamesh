# Unreal: importação e regras do repositório

O projeto Unreal fica em `Gilgamesh/` (criado no PC; ver `docs/fim-de-semana-pc.md`). Esta pasta guarda o que é gerado fora do Unreal para ser importado nele.

## O que entra e o que não entra no Git

| Entra | Não entra |
|---|---|
| `Gilgamesh/Config`, `Gilgamesh/Content` (só conteúdo próprio), `Gilgamesh/Gilgamesh.uproject`, `Source` (se houver C++) | `Binaries`, `DerivedDataCache`, `Intermediate`, `Saved`, `.vs` |
| Blueprints, níveis, materiais e modelos feitos pelo projeto | Assets baixados da Fab ou Megascans (`Content/Fab`, `Content/Megascans`): baixe de novo em cada máquina |
| Arquivos de `unreal/importar/` | MetaHumans gerados (`Content/MetaHumans`): são grandes; exportar de novo pelo MetaHuman Creator quando precisar. Revisar essa regra quando os personagens estiverem prontos. |

Arquivos binários (`.uasset`, `.umap`, `.glb`, `.fbx`, imagens, áudio) vão pelo Git LFS (ver `.gitattributes`). A cota grátis do GitHub é de 10 GiB de armazenamento e 10 GiB de banda por mês. Acompanhe em Settings → Billing.

## Blockout de Uruk

`importar/uruk_blockout.glb` é a Uruk da prévia web em escala real, assada em 73 malhas sem textura (cerca de 820 mil triângulos):

| Prefixo da malha | O que é |
|---|---|
| `SM_Uruk_Terreno` | chão de 10 por 10 km com colinas ao longe |
| `SM_Uruk_Tijolo_*` | muralha (~9 km), torres, portas, recinto de Eanna, zigurate e terraço de Anu |
| `SM_Uruk_Reboco_*` | cerca de 17 mil casas |
| `SM_Uruk_TemploBranco_*` | templos brancos |
| `SM_Uruk_Agua_*`, `SM_Uruk_Margem_*` | braço do Eufrates e canais |
| `SM_Uruk_Madeira_*` | pontes |
| `SM_Uruk_Campos_*` | campos irrigados fora da muralha |

As malhas estão divididas em blocos de 800 m (o número no fim do nome) para o World Partition carregar por região. Gerado por `tools/` a partir da prévia; para refazer, peça para rodar a exportação de novo.

**Importar:**
1. Nível novo do tipo **Open World**.
2. **File → Import Into Level** → `uruk_blockout.glb`. O glTF está em metros; o importador do Unreal converte para centímetros. Se a cidade aparecer 100 vezes menor ou maior, ajuste a escala de importação.
3. **Colisão:** selecione todas as malhas `SM_Uruk_*` no Content Browser → botão direito → **Asset Actions → Bulk Edit via Property Matrix** → **Collision Complexity = Use Complex Collision As Simple**. Para o blockout isso basta; para o jogo final, cada peça terá colisão própria.
4. **Player Start** no pátio de Eanna. As posições estão em `data/layout_uruk.json`, em `lugares_ato1`, e em metros, com x para leste e z para sul. No Unreal, confira o eixo depois de importar.

`data/layout_uruk.json` guarda a planta em dados: muralha, portas, águas, ruas, pontes, plataformas, as 17 mil casas (x, z, meia largura, meia profundidade, ângulo, altura) e os lugares e fragmentos do Ato 1. Serve para trocar as caixas por casas de verdade com PCG ou script.

## DataTables

Gere os JSONs com `python3 tools/exportar_unreal.py`. Eles saem em `importar/DT_*.json`.

No Unreal, crie uma struct para cada tabela (**Content Browser → Add → Blueprint → Structure**), com os campos abaixo, todos **String**, menos onde indicado. Os nomes têm que ser idênticos.

| Struct | Campos |
|---|---|
| `S_Tabuleta` | titulo, ato, resumo, versoes, lacunas, fontes, status |
| `S_Episodio` | tabuleta, ato, local, personagens, jogavel_como, versoes, **lacuna (Boolean)**, fragmento, fontes |
| `S_Fragmento` | tabuleta, completa, onde, texto, efeito, versao_origem, fontes, status |
| `S_Codex` | tipo, titulo, camadas, texto, fontes, libera, status |

Depois arraste cada `DT_*.json` para o Content Browser, escolha **DataTable** e a struct correspondente. Quando os dados mudarem no YAML: rode o exportador e, no Unreal, use **Reimport** na DataTable.

Listas (versões, fontes, personagens, camadas) vêm como texto separado por `; `.
