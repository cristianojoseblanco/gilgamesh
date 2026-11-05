# GDD 1.1 — Adendo: Unreal Engine e realismo

**Data:** 5 de novembro de 2026 · **Base:** `docs/GDD-v1.0.pdf` · **Decisões:** 001 (escala real), 002 (fase 0), 003 (Unreal e realismo)

Este adendo substitui as seções do GDD 1.0 listadas abaixo. O que não aparece aqui continua valendo como está no PDF: história, estrutura em atos, personagens, mecânicas, rigor histórico, modelo de dados, protótipo e papéis.

---

## 8.1 Estilo visual (substitui)

**Realista**, com luz de cinema e materiais fotográficos, sem perder a regra do Codex: tudo o que aparece tem origem declarada (evidência, interpretação ou invenção).

- **Referência de época:** `docs/pesquisa/visual-dinastico-arcaico.md`. Base principal nas estátuas de Tell Asmar (Dinástico Arcaico I–II); empréstimos do Dinástico Arcaico III (Ur, Lagash) marcados como interpretação.
- **Assinatura visual:** tijolo plano-convexo em fiadas inclinadas, reboco de barro, canais com barcos de junco e betume, poeira dourada de fim de tarde, multidões.
- **Paleta por ato** (mantida, agora como gradação de cor e luz): ocre e dourado (Uruk), verde-escuro e névoa (floresta), vermelho e cinzas (Touro e luto), azul-noite (Mashu), branco e azul (águas e ilha).
- **Sonhos:** continuam com estilo próprio, mas dentro do realismo: escala distorcida, névoa colorida, luz sem fonte. Nada de contorno de desenho.
- **Risco do realismo:** personagem "quase humano" que incomoda (vale da estranheza) e anacronismos mais visíveis. Cada MetaHuman passa por uma ficha com fonte antes de virar personagem.

## 10. Ferramentas e pipeline (substitui)

| Ferramenta | Papel | Observações |
|---|---|---|
| Unreal Engine 5 (estável mais recente, 5.7+) | Motor: níveis, Blueprints, animação, cinemáticas, áudio | Grátis até US$ 1 milhão de receita bruta por produto; depois, royalty de 5% (vendas na Epic Games Store isentas) |
| Blueprints | Lógica de jogo | Linguagem principal no começo. C++ só se um sistema pedir |
| World Partition + PCG | Uruk em escala real, casas, vegetação | O blockout (`unreal/importar/uruk_blockout.glb`) e a planta (`data/layout_uruk.json`) alimentam o PCG |
| Lumen e Nanite | Luz global e geometria densa | Configurar escalabilidade para hardware médio |
| MetaHuman | Personagens realistas | Incluído na licença do Unreal. Roupas e cabelo de época feitos à parte |
| Fab (Megascans) | Materiais e objetos fotográficos | Licença conferida por item; não entra no Git |
| Blender | Roupas, objetos de época, ajustes de malha | Exporta FBX ou glTF |
| Git + GitHub + Git LFS | Versão | Cota grátis do LFS: 10 GiB de armazenamento e 10 GiB de banda por mês |
| Python | Validar dados, exportar DataTables e blockout | `tools/validar_dados.py`, `exportar_unreal.py`, `exportar_blockout.py` |
| Prévia web (three.js) | Testar roteiro, ritmo e escala pelo celular | `previa-web/` |

### 10.1 Hardware de desenvolvimento (substitui)

- Recomendado pela Epic: Windows 11, 32 GB de RAM, 8 GB de memória de vídeo, SSD. Reservar 150 GB ou mais.
- Controle de videogame para testar.
- **Situação atual:** sem PC próprio. O trabalho no PC acontece em sessões na casa de um amigo, e tudo vive no GitHub. O celular fica com roteiro, pesquisa, dados, prévia web e guias passo a passo.

### 10.2 Fluxo de um asset (substitui)

1. **Ficha:** o que é, de onde vem a referência (com fonte) e grau de invenção.
2. **Blocagem cinza no Unreal:** tamanho, colisão, leitura de câmera.
3. **Base:** Fab ou MetaHuman quando existir algo adequado. Blender quando for peça de época sem equivalente.
4. **Material:** a partir de Megascans, ajustado à paleta de barro e betume.
5. **Teste de desempenho** (Nanite, LOD, custo de sombras) e revisão da ficha.
6. **Registro em `LICENSES_AND_CREDITS.md`** com a origem e a licença.

## 11. Arquitetura técnica (substitui)

| Camada | Responsabilidade no Unreal |
|---|---|
| Estado global | `BP_GameInstance` com subsistemas: progresso, Codex, fragmentos e opções. Sobrevive à troca de nível |
| Save | `SaveGame` com 3 slots manuais mais o automático. Guarda ato, posição, fragmentos, Codex, escolhas e opções |
| Mundo | Um nível com World Partition para Uruk e arredores. Níveis separados para floresta, Mashu, ilha e Nínive |
| Personagens | `BP_HumanoideBase`, herdado de Character, com movimento, vida, fôlego e interação. Gilgamesh e Enkidu herdam dele. Troca de personagem por Possess |
| Companheiro | Enkidu com IA (Behavior Tree ou StateTree): seguir, lutar, ajudar |
| Combate | Golpes como dados (DataAsset): dano, alcance, janela de esquiva. Chefes com fases |
| Narrativa | Diálogos e fragmentos via DataTables geradas de `data/*.yaml`. Cutscenes no Sequencer. Gatilhos por volume |
| Interface | UMG: HUD mínimo, Codex, mesa do escriba, legendas, acessibilidade |
| Entrada | Enhanced Input, com teclado, mouse e controle remapeáveis |

**Regra que continua valendo:** nenhuma frase de roteiro, fragmento ou entrada do Codex dentro de Blueprint. Tudo vem das DataTables, que vêm do YAML validado.

## 13. Requisitos não funcionais (altera RNF-01, RNF-02 e RNF-08)

| ID | Requisito |
|---|---|
| RNF-01 | Windows primeiro (Linux opcional depois). 60 quadros por segundo em hardware médio, 30 no mínimo, com escalabilidade (baixa, média, alta, épica) |
| RNF-02 | World Partition com carregamento por região; Nanite onde couber; LOD e HLOD para a cidade vista de longe |
| RNF-08 | Offline e sem serviço pago obrigatório. Plano pago do GitHub LFS só se a cota grátis estourar |

Os demais RNF (dados separados do código, acessibilidade, idiomas, rastreabilidade de fontes, licenças) seguem iguais.

## 15. Plano por fases (substitui)

Estimativa para **mais de 10 horas por semana**, com acesso ao PC em sessões. O tempo de PC é o gargalo: tudo o que não precisa de PC é feito antes, pelo celular.

| Fase | Entregas | Onde | Prazo estimado |
|---|---|---|---|
| 0 — Fundação | Repositório, decisões, fontes, dados | Celular | **Feita** (falta conferir fontes) |
| 1 — Aprender Unreal | Projeto criado, Uruk importada, personagem andando, primeiro Blueprint | PC | 3 a 5 fins de semana |
| 2 — Roteiro do protótipo | Tabuletas I e II, diálogos, Codex, fragmentos | Celular | **Rascunho 1 feito**; revisão com George e Brandão |
| 3 — Protótipo cinza | Todo o Ato 1 jogável sem arte, seguindo a prévia web | PC | 8 a 12 semanas |
| 4 — Arte e som do protótipo | Materiais de época, MetaHumans com roupa de época, animação, áudio | PC + celular | 12 a 20 semanas |
| 5 — Teste e polimento | 5 a 10 pessoas jogando, desempenho, acessibilidade | PC | 3 a 4 semanas |
| 6 — Decisão | Seguir, reduzir ou parar | — | 1 semana |
| 7 — Atos 2 a 5 | Jogo completo | PC | 18 a 30 meses |
| 8 — Lançamento | Inglês, loja, trailer | PC | 2 a 3 meses |

**Leitura honesta:** o realismo encarece a fase 4 e a fase 7. Personagens de época realistas (roupa, cabelo, animação facial) são o item mais caro do projeto. O protótipo realista deve levar de **8 a 12 meses**, e o jogo completo de **3 a 4 anos**, se o acesso ao PC for regular. Se o acesso ao PC for só em alguns fins de semana por mês, esses prazos crescem na mesma proporção. Conseguir um PC próprio é a mudança que mais encurta o projeto.

## 17. Orçamento (altera)

| Item | Custo estimado |
|---|---|
| Unreal Engine, MetaHuman, Blender, Git | Grátis (Unreal com royalty de 5% acima de US$ 1 milhão por produto) |
| Fab / Megascans | Muito conteúdo grátis; pacotes pagos opcionais |
| Git LFS | Grátis até 10 GiB de armazenamento e 10 GiB de banda por mês; depois, cobrança por uso |
| PC capaz de rodar Unreal 5 | O maior custo potencial do projeto. Não é obrigatório enquanto houver acesso ao PC do amigo |
| Steam, itch.io, classificação indicativa | Como no GDD 1.0 |

## 18. Riscos (acrescenta)

| Risco | Mitigação |
|---|---|
| Acesso ao PC só em sessões | Tudo no GitHub; preparação pelo celular (guias, dados, blockout) para que o tempo de PC seja só de execução; avaliar PC próprio na fase 6 |
| Hardware do amigo abaixo do recomendado | Escalabilidade média no editor; Lumen em modo software; menos Nanite |
| Vale da estranheza nos personagens | Câmera e luz que favoreçam silhueta; poucas cenas de rosto muito perto no protótipo; testar cedo |
| Anacronismo visual mais visível no realismo | Ficha com fonte para cada asset; lista "o que evitar" da pesquisa visual |
| Repositório estoura a cota do LFS | Assets da Fab e MetaHumans fora do Git; revisar o uso em Settings → Billing a cada mês |
| Curva de aprendizado do Unreal | Só Blueprints no começo; guias passo a passo em `docs/unreal/` |

## 19. Estrutura do repositório (substitui)

```
gilgamesh/
├── Gilgamesh/            projeto Unreal (criado no PC)
├── data/                 YAML do roteiro, Codex e fragmentos; fontes.csv; layout_uruk.json
├── docs/
│   ├── GDD-v1.0.pdf, GDD-1.1-adendo.md
│   ├── decisoes/         001, 002, 003…
│   ├── roteiro/          ato1.md…
│   ├── pesquisa/         visual-dinastico-arcaico.md…
│   ├── unreal/           guias passo a passo de Blueprints
│   └── fim-de-semana-pc.md
├── unreal/
│   ├── README.md         importação e regras do Git
│   └── importar/         blockout glTF e DataTables JSON
├── previa-web/           prévia jogável no navegador
├── tools/                validação e exportação
└── assets/referencias/   links e fichas de referência (sem imagens de terceiros)
```
