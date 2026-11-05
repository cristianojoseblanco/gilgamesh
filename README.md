# Gilgamesh: Aquele que viu o abismo

Jogo 3D de ação e aventura narrativa baseado na Epopeia de Gilgamesh. Nome de trabalho.

- Documento de design: [`docs/GDD-v1.0.pdf`](docs/GDD-v1.0.pdf)
- Decisões: [`docs/decisoes/`](docs/decisoes/)

## Prévia web

`previa-web/index.html` é uma prévia técnica feita em three.js, só com geometria e texturas geradas por código. Serve para testar escala, luz e ritmo pelo celular antes do protótipo no Godot. Não é arte final.

- **v2 (atual):** Uruk em escala real, com muralha de ~9 km, braço do Eufrates, canais com barcos de junco, Eanna com zigurate, terraço de Anu com o Templo Branco, cerca de 17 mil casas, minimapa e 4 fragmentos de Codex.
- **v1:** `previa-web/v1-portao/`, só o portão, um trecho de cidade e a estepe.

Para abrir localmente, sirva a pasta por HTTP (`python3 -m http.server`) e abra `previa-web/index.html`. A three.js vem de CDN.

## Dados e roteiro

- `data/`: fontes (`fontes.csv`), resumos das 12 tabuletas, episódios, fragmentos e Codex do protótipo, em YAML.
- `docs/roteiro/ato1.md`: roteiro do protótipo (Tabuletas I e II).
- `tools/validar_dados.py`: confere ids, referências cruzadas, camadas do Codex e fontes. Rode com `python3 tools/validar_dados.py` (precisa de PyYAML).

## Estado

- Fase 0 (fundação): estrutura do repositório e decisões da seção 21.2 feitas. Falta conferir as fontes (todas estão `a_conferir`) e definir nome final e GPU.
- Fase 2 (roteiro do protótipo): rascunho 1 pronto, a revisar com George 2003 e Brandão 2017.
- Próximo: fase 1 (Godot e Blender) no PC.
