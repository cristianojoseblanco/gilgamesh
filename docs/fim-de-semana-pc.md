# Fim de semana no PC: instalação e primeiras sessões no Unreal

Objetivo do fim de semana: sair com o projeto Unreal criado, no GitHub, e com Gilgamesh andando dentro de uma Uruk em escala real.

## Antes de ir (pelo celular)

- [ ] Pedir ao amigo as especificações do PC: processador, RAM, placa de vídeo (modelo e memória) e espaço livre em SSD. A Epic recomenda Windows 11, 32 GB de RAM e 8 GB de memória de vídeo.
- [ ] Combinar que vão ficar livres **pelo menos 150 GB em SSD** (engine, cache de shaders e projeto).
- [ ] Criar a conta Epic Games, se ainda não tiver, e ativar a verificação em duas etapas.
- [ ] Confirmar que a internet de lá aguenta baixar dezenas de GB. Se puder, peça ao amigo para começar a baixar o Unreal antes de você chegar.

## O que instalar (nesta ordem)

1. **Driver de vídeo** atualizado (NVIDIA ou AMD, versão estável mais recente).
2. **Epic Games Launcher** → aba Unreal Engine → Biblioteca → instalar a versão estável mais recente (5.7 ou mais nova). É o download mais longo: comece por ele.
3. **Git for Windows** (já vem com o Git LFS). Na instalação, aceite os padrões.
4. **GitHub Desktop** (opcional, mas mais fácil que a linha de comando). Entre com a sua conta. **No fim do fim de semana, saia da conta** no PC do amigo.
5. **Blender** (versão estável mais recente). Não é urgente; serve para ajustar modelos depois.
6. **Visual Studio**: só se formos usar C++. **Pule por enquanto**: o primeiro protótipo é todo em Blueprints. Se for instalar, use a versão indicada na página de requisitos da Epic para a versão do Unreal instalada.

## Sábado — sessão 1: projeto e repositório (2 a 3 h)

1. Clonar `cristianojoseblanco/gilgamesh` com o GitHub Desktop numa pasta curta, por exemplo `C:\dev\gilgamesh`. Caminhos longos dão problema no Unreal.
2. No terminal da pasta: `git lfs install` (só uma vez por máquina).
3. No Unreal: **Games → Third Person**, tipo **Blueprint**, qualidade **Maximum**, **Starter Content desligado**. Nome do projeto: `Gilgamesh`. Pasta: dentro do clone, ficando `C:\dev\gilgamesh\Gilgamesh\Gilgamesh.uproject`.
4. Abrir o projeto uma vez e fechar. Conferir que as pastas `Binaries`, `DerivedDataCache`, `Intermediate` e `Saved` **não** aparecem como mudanças no GitHub Desktop (o `.gitignore` já cuida disso).
5. Commit "Projeto Unreal criado" e push.

## Sábado — sessão 2: Uruk em escala real (2 a 3 h)

Siga `unreal/README.md`, seção "Blockout de Uruk":

1. Criar um nível novo do tipo **Open World** (já vem com céu, luz e World Partition).
2. **File → Import Into Level** → `unreal/importar/uruk_blockout.glb`.
3. Ativar colisão nas malhas, pôr um **Player Start** no pátio de Eanna e apertar Play.
4. Andar de Eanna até a porta sul e subir o zigurate. Anotar o FPS (comando `stat fps` no console, tecla `` ` ``).
5. Commit e push.

**Teste decisivo:** se o editor ficar inutilizável aqui, mesmo com Settings → Engine Scalability em Medium, conversamos antes de seguir.

## Domingo — sessão 3: realismo, primeiro passo (3 a 4 h)

1. Na Fab (dentro do editor), adicionar à biblioteca materiais de **terra seca**, **tijolo de barro ou adobe**, **reboco de barro** e **água de rio**. Aplicar no blockout nas categorias Terreno, Tijolo, Reboco e Água.
2. Luz de fim de tarde: Directional Light baixa e alaranjada, Exponential Height Fog leve. Tirar prints do zigurate e da porta sul para comparar com a prévia web.
3. Criar um MetaHuman de teste para Gilgamesh (barba longa e escura, pele morena, cabelo longo). Ainda sem roupa de época: isso exige pesquisa e modelagem, e vem depois.
4. Commit e push. **Não** adicionar ao Git os assets baixados da Fab (ver `unreal/README.md`).

## Domingo — sessão 4: dados e primeiro Blueprint (2 a 3 h)

1. Criar as structs e importar as DataTables (`unreal/importar/DT_*.json`), conforme `unreal/README.md`.
2. Blueprint `BP_Fragmento`: brilho, gatilho de proximidade e um widget simples que mostra o `texto` da linha da DataTable.
3. Colocar o fragmento F01-02 na estepe, na posição de `data/layout_uruk.json` (`fragmentos_ato1`).
4. Commit e push, **sair do GitHub e da Epic** no PC do amigo se não for voltar logo.

## O que continuo fazendo pelo celular, em paralelo

- GDD versão 1.1 (Unreal e realismo).
- Pesquisa visual com fontes para roupas, penteados, armas e arquitetura do Dinástico Arcaico, para orientar MetaHuman e modelagem.
- Blueprints e lógica descritos passo a passo para você montar no PC.
- Prévia web continua sendo o lugar para testar roteiro e ritmo.
