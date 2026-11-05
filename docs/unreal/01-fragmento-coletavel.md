# Guia 01 — Fragmento coletável (BP_Fragmento)

**Objetivo:** um pedaço de tabuleta que brilha e gira na estepe. Quando Gilgamesh ou Enkidu encosta, o jogo pausa, mostra o texto do fragmento lido da DataTable, registra que ele foi coletado e o fragmento some.
**Tempo:** 1 h 30 a 2 h · **Pré-requisitos:** projeto criado e DataTables importadas (`unreal/README.md`).
**Status:** escrito pelo celular, **ainda não testado no Unreal**. Se algum nome de nó ou menu estiver diferente na sua versão, anote o que apareceu na tela, e eu corrijo o guia.

> Os nomes de menus e nós estão em inglês, que é o idioma padrão do editor. Se o seu editor estiver em português, use a busca: os nós continuam com o nome em inglês por baixo.

---

## Passo 1 — Pastas

No **Content Browser**, dentro de `Content`, crie (botão direito → **New Folder**):

```
Content/Gilgamesh/
├── Core/        (GameInstance)
├── Dados/       (structs e DataTables)
├── Fragmentos/  (BP_Fragmento)
└── UI/          (widgets)
```

Mova as structs `S_*` e as DataTables `DT_*` para `Gilgamesh/Dados`.

## Passo 2 — GameInstance (onde fica o progresso)

1. Em `Gilgamesh/Core`: botão direito → **Blueprint Class** → em "All Classes", busque **GameInstance** → nome `BP_GameInstance`.
2. Abra. No painel **My Blueprint**, em **Variables**, clique em **+**:
   - Nome: `FragmentosColetados`
   - Tipo: **Name**. Depois clique no ícone ao lado do tipo e escolha **Set** (ícone de chaves `{}`).
3. Em **Functions**, clique em **+** e crie `ColetarFragmento`:
   - Selecione a função e, no painel **Details**, em **Inputs**, adicione `Id` do tipo **Name**.
   - Dentro da função: arraste `FragmentosColetados` para o grafo → **Get**. Puxe um fio dele e busque **Add** (o Add de Set). Ligue `Id` em **New Item**. Ligue a execução: entrada da função → Add → **Return Node**.
4. Crie outra função, `JaColetou`:
   - Input `Id` (Name); Output `Resultado` (Boolean).
   - Marque **Pure** no Details.
   - `FragmentosColetados` (Get) → **Contains** (com `Id`) → ligue em `Resultado`.
5. **Compile** e **Save**.
6. Menu **Edit → Project Settings → Maps & Modes → Game Instance Class** → escolha `BP_GameInstance`.

## Passo 3 — Widget do fragmento (WBP_Fragmento)

1. Em `Gilgamesh/UI`: botão direito → **User Interface → Widget Blueprint** → **User Widget** → nome `WBP_Fragmento`.
2. Na aba **Designer**, monte esta hierarquia (arrastando da **Palette**):

```
Canvas Panel
└── Border            (Anchors: centro · Alignment 0,5 / 0,5 · Size 640 × 420 · cor marrom escuro, opacidade 0,92)
    └── Vertical Box
        ├── Text  "TxtKicker"   (tamanho 14, cor dourada)
        ├── Text  "TxtTitulo"   (tamanho 30)
        ├── Text  "TxtTexto"    (tamanho 22, Auto Wrap Text ligado, itálico)
        ├── Text  "TxtEfeito"   (tamanho 16, Auto Wrap Text ligado)
        └── Button "BtnContinuar"
            └── Text "Continuar"
```

   Em cada Text, marque **Is Variable** (no topo do Details) para poder mudar o texto pelo grafo.
3. Aba **Graph**: crie quatro variáveis do tipo **String**: `Id`, `Texto`, `Efeito` e `Tabuleta`. Em cada uma, marque **Instance Editable** e **Expose on Spawn**.
4. No evento **Event Construct**:
   - `TxtKicker` → **SetText (Text)** ← **Format Text** com `Fragmento · Tabuleta {T}` ligando `Tabuleta` no pino T.
   - `TxtTitulo` → SetText ← `Id` (o Unreal cria sozinho o conversor de String para Text).
   - `TxtTexto` → SetText ← `Texto`.
   - `TxtEfeito` → SetText ← `Efeito`.
   - Ligue os quatro SetText em sequência na execução.
5. Selecione `BtnContinuar` → no Details, em **Events**, clique no **+** de **On Clicked**:
   - **Set Game Paused** (desmarcado = false)
   - **Get Player Controller** → **Set Input Mode Game Only**
   - Get Player Controller → **Set Show Mouse Cursor** (desmarcado)
   - **Remove from Parent**
6. Compile e Save.

## Passo 4 — O ator BP_Fragmento

1. Em `Gilgamesh/Fragmentos`: **Blueprint Class → Actor** → `BP_Fragmento`.
2. Aba **Components**, botão **+ Add**:
   - **Static Mesh** `Tabuleta`: Mesh = `Cube` (do Engine; marque "Show Engine Content" no filtro se não aparecer). **Scale 0,42 · 0,10 · 0,55** (o cubo padrão tem 100 cm). Location Z = 110.
   - **Point Light** `Brilho`: anexado à Tabuleta. Cor laranja-dourada (R 255, G 190, B 110), Intensity 800, Attenuation Radius 400, Cast Shadows desligado.
   - **Sphere Collision** `Area`: Sphere Radius 150, Location Z = 110.
   - **Rotating Movement**: Rotation Rate Z = 45.
3. Variável `Fragmento`:
   - Tipo: **Data Table Row Handle**. Marque **Instance Editable**.
   - **Compile**. No Details da variável, em Default Value, escolha Data Table = `DT_Fragmentos`.
4. Aba **Event Graph**: selecione o componente `Area` → Details → **On Component Begin Overlap (+)**. Monte nesta ordem:

```
On Component Begin Overlap (Area)
 → Cast To Character   (Object ← Other Actor)          [se falhar, não faz nada]
 → Do Once
 → Get Data Table Row   (Data Table ← DT_Fragmentos, Row Name ← Fragmento.RowName)
     [Row Found] → Break S_Fragmento
 → Create Widget        (Class ← WBP_Fragmento)
       Id       ← Fragmento.RowName (Name → String)
       Texto    ← texto     (do Break)
       Efeito   ← efeito    (do Break)
       Tabuleta ← tabuleta  (do Break)
 → Add to Viewport
 → Get Player Controller → Set Input Mode UI Only (Widget to Focus ← o widget criado)
 → Get Player Controller → Set Show Mouse Cursor (marcado)
 → Set Game Paused (marcado)
 → Get Game Instance → Cast To BP_GameInstance → Coletar Fragmento (Id ← Fragmento.RowName)
 → Destroy Actor
```

   Dicas:
   - Para ler `Fragmento.RowName`, arraste a variável `Fragmento` e use **Break DataTableRowHandle**.
   - O **Get Data Table Row** só mostra os pinos certos depois de você escolher `DT_Fragmentos` na caixa Data Table.
5. Ainda no Event Graph, no **Event BeginPlay**: se o fragmento já foi coletado (por exemplo, ao carregar um save), ele não deve aparecer.

```
Event BeginPlay
 → Get Game Instance → Cast To BP_GameInstance → Ja Coletou (Id ← Fragmento.RowName)
 → Branch (Condition ← Resultado)
     True → Destroy Actor
```

6. Compile e Save.

## Passo 5 — Pôr o F01-02 no mapa

1. Arraste `BP_Fragmento` para o nível. No Details, em **Fragmento → Row Name**, escolha `F01-02`.
2. **Posição.** O `data/layout_uruk.json` usa metros, com x para leste e z para sul. O Unreal usa centímetros, e os eixos dependem de como o glTF foi convertido. Para descobrir a conversão:
   1. No layout, o centro do zigurate de Eanna está em **x = 380, z = −110** (em `plataformas`, o primeiro item: x de 352 a 408, z de −130 a −90).
   2. No Unreal, clique no zigurate e anote a Location do ponto central do topo (ou ponha um ator vazio em cima dele).
   3. Compare: provavelmente vale **X_unreal = ±x × 100** e **Y_unreal = ±z × 100**, ou com os eixos trocados. Os sinais você descobre pelo zigurate.
   4. Aplique a mesma regra a `fragmentos_ato1 → F01-02` no layout.
   5. Me mande os números que você anotou. Eu fecho a fórmula e já devolvo as posições de todos os lugares e fragmentos do Ato 1.
3. Ajuste a altura (Location Z) para o fragmento ficar no chão.

## Passo 6 — Testar

1. **Play**. Ande até o fragmento.
2. Esperado: a tela pausa, o card mostra "Fragmento · Tabuleta T01", "F01-02" e o texto sobre Aruru, e **Continuar** volta ao jogo com o fragmento sumido.
3. **Commit** com a mensagem "BP_Fragmento e WBP_Fragmento" e **push**.

## Se der errado

| Sintoma | Causa provável |
|---|---|
| Nada acontece ao encostar | O personagem não colide com a esfera. Na `Area`, confira Collision Preset = OverlapAllDynamic e Generate Overlap Events ligado |
| Abre duas vezes | Faltou o **Do Once** |
| O botão Continuar não responde | Faltou **Set Input Mode UI Only** ou **Show Mouse Cursor** |
| Texto vazio | Row Name errado ou a DataTable não usa `S_Fragmento`. Abra o `DT_Fragmentos` e confira se as colunas estão preenchidas |
| O jogo continua pausado | No **On Clicked**, o **Set Game Paused** tem que estar desmarcado |

## Próximo guia

`02-mesa-do-escriba.md`: o minijogo de encaixar a peça e copiar os sinais, com a mesma lógica da prévia web.
