# Gilgamesh: Aquele que viu o abismo

Jogo 3D de ação e aventura narrativa baseado na Epopeia de Gilgamesh. Nome de trabalho.

- Documento de design: [`docs/GDD-v1.0.pdf`](docs/GDD-v1.0.pdf) + [`docs/GDD-1.1-adendo.md`](docs/GDD-1.1-adendo.md) (Unreal e realismo)
- Pesquisa visual de época: [`docs/pesquisa/visual-dinastico-arcaico.md`](docs/pesquisa/visual-dinastico-arcaico.md)
- Guias de Blueprints: [`docs/unreal/`](docs/unreal/)
- Decisões: [`docs/decisoes/`](docs/decisoes/). Engine: **Unreal Engine 5**, estilo realista (decisão 003).
- Primeira ida ao PC: [`docs/fim-de-semana-pc.md`](docs/fim-de-semana-pc.md)
- Importação no Unreal (blockout de Uruk, DataTables, regras do Git): [`unreal/README.md`](unreal/README.md)

## Prévia web

`previa-web/index.html` é uma prévia técnica feita em three.js, só com geometria e texturas geradas por código. Serve para testar escala, luz e ritmo pelo celular antes do protótipo no Unreal. Não é arte final.

- **v2 (atual):** Uruk em escala real, com muralha de ~9 km, braço do Eufrates, canais com barcos de junco, Eanna com zigurate, terraço de Anu com o Templo Branco, cerca de 17 mil casas, minimapa e 4 fragmentos de Codex.
- **v1:** `previa-web/v1-portao/`, só o portão, um trecho de cidade e a estepe.
- **Ato 1 jogável:** `previa-web/ato1/index.html`, o roteiro de `docs/roteiro/ato1.md` em 8 capítulos, com mesa do escriba, estepe, sonho, combate e a luta à porta. É montado por `tools/montar_previa.py` a partir de `previa-web/ato1/fonte.html` (roteiro e interface), do motor da cidade em `previa-web/index.html` e dos dados de `data/`. Não edite o `index.html` do Ato 1 à mão.

Para abrir localmente, sirva a pasta por HTTP (`python3 -m http.server`) e abra `previa-web/index.html`. A three.js vem de CDN.

## Dados e roteiro

- `data/`: fontes (`fontes.csv`), resumos das 12 tabuletas, episódios, fragmentos e Codex do protótipo, em YAML.
- `docs/roteiro/ato1.md`: roteiro do protótipo (Tabuletas I e II).
- `tools/validar_dados.py`: confere ids, referências cruzadas, camadas do Codex e fontes. Rode com `python3 tools/validar_dados.py` (precisa de PyYAML).

## Estado

- Fase 0 (fundação): estrutura do repositório e decisões da seção 21.2 feitas. Falta conferir as fontes (todas estão `a_conferir`) e definir nome final e GPU.
- Fase 2 (roteiro do protótipo): rascunho 1 pronto, a revisar com George 2003 e Brandão 2017.
- Próximo: fase 1 no PC com Unreal (ver `docs/fim-de-semana-pc.md`).
