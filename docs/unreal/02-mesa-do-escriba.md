# Guia 02 — Mesa do escriba (WBP_MesaEscriba)

**Objetivo:** o minijogo de abertura (episódio E00 do roteiro). O jogador vê a tabuleta rachada, **toca na peça solta e depois no canto que falta** para encaixar, e em seguida **toca nos três sinais da primeira linha, na ordem**. No fim, aparece a fala do escriba e o jogo segue.
**Tempo:** 2 a 3 h · **Pré-requisito:** Guia 01 feito (pastas e GameInstance).
**Status:** escrito pelo celular, **não testado no Unreal**. Anote no diário o que estiver diferente.

> Na prévia web a peça é arrastada. Aqui ela é **tocada e depois encaixada com um segundo toque**, porque assim só precisamos de botões. Arrastar com Drag and Drop do UMG fica para a fase 4, se fizer falta.

---

## Passo 1 — Importar as imagens

1. Crie a pasta `Content/Gilgamesh/UI/Escriba`.
2. Arraste para ela os três arquivos de `unreal/importar/ui/`: `T_Tabuleta_Base.png`, `T_Tabuleta_Peca.png` e `T_Sinal_Destaque.png`.
3. Em cada textura, abra e mude **Texture Group = UI** e **Compression Settings = UserInterface2D**. Salve.

As medidas estão em `unreal/importar/ui/peca_posicao.txt`. A base tem 840 × 1040 px, e a peça encaixa em **X 540, Y 40** (tamanho 261 × 261).

## Passo 2 — Montar o widget (Designer)

Em `Gilgamesh/UI/Escriba`: **User Interface → Widget Blueprint → User Widget** → `WBP_MesaEscriba`.

Hierarquia:

```
Canvas Panel
├── Image "Fundo"            Anchors: tela toda (último preset) · Offsets todos 0 · cor marrom muito escuro (#120A05)
├── Scale Box "Escala"       Anchors: centro · Alignment 0,5/0,5 · Size 840 × 1040 · Stretch = Scale To Fit
│   └── Canvas Panel "Mesa"  (é dentro dele que as posições em pixel valem)
│       ├── Image  "Base"           Position 0,0 · Size 840 × 1040 · Brush = T_Tabuleta_Base
│       ├── Button "BtnBuraco"      Position 540,40 · Size 261 × 261 · estilo transparente (ver nota)
│       ├── Button "BtnPeca"        Position 90,700 · Size 261 × 261 · estilo transparente
│       │   └── Image "ImgPeca"     Brush = T_Tabuleta_Peca
│       ├── Button "BtnSinal1"      Position 33,36  · Size 64 × 64 · transparente, Visibility = Hidden
│       │   └── Image                Brush = T_Sinal_Destaque
│       ├── Button "BtnSinal2"      Position 268,36 · Size 64 × 64 · (igual)
│       └── Button "BtnSinal3"      Position 418,36 · Size 64 × 64 · (igual)
├── Text   "TxtFala"         Anchors: base centro · Position 0,-140 · Size 900 × 120 · Auto Wrap · centralizado · tamanho 22
└── Button "BtnContinuar"    Anchors: base centro · Position 0,-50 · Visibility = Collapsed
    └── Text "Continuar"
```

**Nota sobre o botão transparente:** no Details do botão, em **Style → Normal, Hovered e Pressed**, ponha **Tint** com Alpha 0 (ou Draw As = None). Assim só a imagem de dentro aparece.

Marque **Is Variable** em `BtnBuraco`, `BtnPeca`, `ImgPeca`, `BtnSinal1/2/3`, `TxtFala` e `BtnContinuar`.

## Passo 3 — Variáveis (Graph)

| Variável | Tipo | Valor inicial |
|---|---|---|
| `Etapa` | Integer | 0 (0 = encaixe · 1 = sinais · 2 = fim) |
| `PecaSelecionada` | Boolean | false |
| `ProximoSinal` | Integer | 1 |

E um **Event Dispatcher** chamado `AoTerminar` (painel My Blueprint → Event Dispatchers → +). É por ele que a mesa avisa a fase quando acabar.

## Passo 4 — Lógica

### 4.1 Event Construct

```
Event Construct
 → TxtFala.SetText("Toque na peça solta e depois no canto que falta.")
```

### 4.2 Tocar na peça — BtnPeca → On Clicked

```
Branch (Etapa == 0)
  True → Set PecaSelecionada = true
       → ImgPeca.SetColorAndOpacity(R 1, G 0.85, B 0.55, A 1)     (fica dourada = selecionada)
```

### 4.3 Tocar no buraco — BtnBuraco → On Clicked

```
Branch (Etapa == 0 AND PecaSelecionada)
  True →
    Get BtnPeca → Slot as Canvas Slot → Set Position (540, 40)     (encaixa)
    ImgPeca.SetColorAndOpacity(1,1,1,1)
    BtnPeca.SetIsEnabled(false)
    Set Etapa = 1
    BtnSinal1.SetVisibility(Visible)
    TxtFala.SetText("Agora toque nos sinais da primeira linha, na ordem.")
    Play Sound 2D (opcional: um som de argila)
```

`Slot as Canvas Slot` aparece ao puxar um fio de `BtnPeca`. Ele dá acesso a `Set Position`.

### 4.4 Os três sinais

Crie uma função `TocarSinal` com input `Numero` (Integer):

```
Branch (Etapa == 1 AND Numero == ProximoSinal)
  True →
    Switch on Int (Numero)
      1 → BtnSinal1.SetIsEnabled(false) → BtnSinal2.SetVisibility(Visible)
      2 → BtnSinal2.SetIsEnabled(false) → BtnSinal3.SetVisibility(Visible)
      3 → BtnSinal3.SetIsEnabled(false) → chama a função Concluir
    Set ProximoSinal = ProximoSinal + 1
```

Em `BtnSinal1 → On Clicked` chame `TocarSinal(1)`; no 2, `TocarSinal(2)`; no 3, `TocarSinal(3)`.

### 4.5 Concluir

Função `Concluir`:

```
Set Etapa = 2
TxtFala.SetText("“Ele que viu o abismo… A primeira linha está inteira. Já é alguma coisa.”")
BtnContinuar.SetVisibility(Visible)
```

`BtnContinuar → On Clicked`:

```
Call AoTerminar          (dispara o Event Dispatcher)
Remove from Parent
```

Quem abriu a mesa trata o resto: tirar a pausa, devolver o controle, trocar de cena.

## Passo 5 — Quem abre a mesa

Para o protótipo, abra a mesa direto no **Level Blueprint** do nível de Nínive (ou do nível de teste):

```
Event BeginPlay
 → Create Widget (WBP_MesaEscriba)  → guarde em variável "Mesa"
 → Add to Viewport
 → Get Player Controller → Set Input Mode UI Only (Widget to Focus = Mesa)
 → Get Player Controller → Set Show Mouse Cursor (true)
 → Bind Event to AoTerminar (Target = Mesa)  ← ligue um Custom Event "MesaTerminou"

Custom Event MesaTerminou
 → Set Input Mode Game Only
 → Set Show Mouse Cursor (false)
 → Open Level (L_Uruk)            (ou só continuar no mesmo nível, no teste)
```

## Passo 6 — Teste

- [ ] Tocar no buraco antes da peça **não** faz nada.
- [ ] Tocar na peça a deixa dourada; tocar no buraco a encaixa.
- [ ] Os sinais aparecem um de cada vez; tocar fora de ordem não faz nada.
- [ ] Depois do terceiro, aparece a fala e o botão Continuar.
- [ ] Funciona com mouse e com toque. No PC, teste também com o controle: o foco precisa andar entre os botões. Se não andar, configure **Navigation** nos botões (fase 3).

Commit, push e anotação no diário.

## Depois (não agora)

- Fala do mestre antes do encaixe, como na prévia (textos em `data/`, não no Blueprint).
- Animação de encaixe (Widget Animation, 0,3 s) e som de argila.
- No fim do Ato 1, reusar o mesmo widget para escrever "Tabuleta II. Não está completa."
