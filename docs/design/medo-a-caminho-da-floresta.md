# Design: o medo a caminho da Floresta de Cedros

**Pedido:** a viagem até Humbaba e o começo do combate devem passar o medo que o poema passa, com tensão de jogo de terror e visão turva como ansiedade.
**Atos:** 2 (Tabuletas IV e V) · **Status:** proposta 1 · trechos do texto a conferir com George 2003 e Brandão 2017.

---

## 1. O que o poema faz (e que o jogo precisa imitar)

O medo na Tabuleta IV não vem de monstros. Vem de **repetição**. A viagem é contada em ciclos quase idênticos:

1. Andam uma distância enorme por dia. O texto marca as etapas com números fixos de léguas, onde partem o pão e onde acampam.
2. Cavam um poço diante do sol.
3. Gilgamesh sobe a montanha, derrama farinha como oferenda e pede à montanha um sonho.
4. Enkidu monta para ele uma "casa do deus do sonho" e faz o ritual.
5. Gilgamesh dorme sentado, com o queixo nos joelhos.
6. **Acorda no meio da noite** e faz ao amigo as mesmas perguntas: se Enkidu o chamou, se o tocou, se um deus passou, por que o corpo está dormente. As palavras são quase as mesmas toda vez (formulação exata a conferir).
7. Conta um sonho **pior que o anterior**. Os resumos mais usados falam numa montanha que desaba, num touro selvagem, numa tempestade de raios e fogo, e numa ave monstruosa que cospe fogo. Parte desses sonhos está em trechos quebrados da tabuleta.
8. **Enkidu sempre interpreta o sonho como bom sinal.** O leitor percebe que as imagens parecem descrever Humbaba, e essa negação aumenta a tensão.

Na borda da floresta, os dois **hesitam e precisam encorajar um ao outro** (detalhes a conferir).

O fragmento da Tabuleta V publicado em 2014 (Al-Rawi e George) mudou a imagem da floresta. Andrew George resumiu assim: a Floresta de Cedros não é um lugar de clareiras serenas e silenciosas; está cheia de pássaros barulhentos e cigarras, e macacos gritam nas árvores. Segundo ele, Humbaba trata essa cacofonia como uma espécie de entretenimento da sua corte. (Live Science, 2015; Al-Rawi e George, *JCS* 66, 2014.)

**Consequência para o design:** o terror não precisa de sustos. Ele vem de três coisas:
- A **antecipação** que cresce a cada noite igual.
- O **contraste de som**: silêncio na viagem, barulho ensurdecedor na floresta e um **silêncio súbito** quando Humbaba se aproxima.
- A **amizade como único remédio**: no texto, um sozinho trava, e os dois juntos seguem.

---

## 2. Pilares

1. **A repetição é a mecânica.** O jogador faz o mesmo ritual cinco vezes. O que muda é o que ele sente, não o que ele faz.
2. **O medo é percepção, não vida.** A barra de Pavor nunca mata. Ela muda o que se vê e se ouve, e só no combate pesa um pouco no fôlego.
3. **Enkidu é o antídoto.** Perto dele, o Pavor cai. Longe dele, sobe. O jogador aprende sozinho a não se afastar, o que prepara o Ato 3 (a morte de Enkidu dói mais).
4. **Sem susto barato.** Nada de rosto aparecendo com grito alto. O medo vem do que **não** aparece.
5. **Fiel ao texto.** As falas repetidas são do poema; a variação fica na direção (câmera, som, luz, ritmo da legenda).

---

## 3. O sistema de Pavor (0 a 100)

### O que faz subir e descer

| Sobe | Desce |
|---|---|
| Noite e escuridão | Estar a menos de 5 m de Enkidu |
| Ficar longe de Enkidu (sobe rápido acima de 15 m) | Fogo do acampamento |
| Sons sem fonte visível (estalo atrás, passos que não são seus) | Completar o ritual da noite (poço, farinha, casa do sonho) |
| Acordar à meia-noite (salto) | **Encorajar** (ação a dois, ver item 5) |
| Cada sonho (salto maior a cada noite) | Luz do sol de manhã |
| Volume da cacofonia na floresta | Os ventos de Shamash (no combate) |
| Silêncio súbito da floresta (salto) | |

**Piso de pavor:** a cada noite, o valor mínimo sobe (0 → 10 → 20 → 30 → 40). O jogador sente que a manhã alivia cada vez menos.

### O que o Pavor faz na tela e no som

| Faixa | Visão | Som | Corpo e câmera |
|---|---|---|---|
| 0–25 | normal | ambiente normal | normal |
| 25–50 | vinheta leve; cores um pouco mais frias e menos saturadas | coração distante, uns 70 batimentos por minuto | câmera um pouco mais pesada para virar |
| 50–75 | **visão de túnel**: bordas desfocadas e escuras; leve aberração cromática nas bordas; o campo de visão "respira" no ritmo do coração | ambiente abafado (filtro passa-baixa); coração a uns 100 bpm; respiração curta de Gilgamesh | pequenos tremores de câmera; a mão treme no modo exame; o controle vibra no ritmo do coração |
| 75–100 | o centro também perde nitidez; brilhos sangram; cor quase só no centro | quase só coração, respiração e um zumbido agudo e baixo | passos mais lentos; a interface some; demora meio segundo para a câmera obedecer |

**O que nunca acontece:** perda total de controle por mais de 2 segundos, flashes estroboscópicos, tela totalmente preta.

### No combate

Com Pavor acima de 60, o fôlego regenera 30% mais devagar e a janela de esquiva fica um pouco menor. Encorajar ou ficar perto de Enkidu desfaz isso.

---

## 4. Estrutura da viagem: cinco noites

Cada ciclo leva de 6 a 10 minutos. A viagem inteira, uns 40 minutos.

| Etapa | O que o jogador faz | Direção |
|---|---|---|
| **Caminhar** | Anda com Enkidu por um trecho curto e jogável; o resto é viagem encenada com marcos na tela: "Vinte léguas: partiram o pão." "Trinta léguas: acamparam." | A paisagem muda a cada noite: estepe, colinas, rochas, primeiros cedros, montanha. Os animais vão sumindo |
| **Poço** | Cavar diante do sol (segurar o botão) | Luz do fim de tarde. Sempre o mesmo enquadramento |
| **Montanha** | Subir, derramar farinha, pedir o sonho | Sempre a mesma frase. Na terceira noite, o vento leva a farinha de volta no rosto dele (invenção do jogo) |
| **Casa do sonho** | Ajudar Enkidu a montar o abrigo | Enkidu fala menos a cada noite |
| **Dormir** | Gilgamesh senta com o queixo nos joelhos | Corte para preto. Silêncio |
| **Meia-noite** | Gilgamesh acorda e faz as perguntas | **Mesmo plano, mesmas palavras, toda noite.** O que muda: a câmera começa um pouco mais perto do rosto, a legenda demora um pouco mais por palavra e o Pavor de partida é maior. Na quarta noite, o jogador já sabe as falas antes delas aparecerem, e é isso que dá medo |
| **Sonho** | Jogável, curto (1 a 3 min) | Cada um com uma regra: (1) a montanha que cai: fugir de pedras num corredor que se fecha; (2) o touro: a terra racha a cada mugido; (3) tempestade: chuva de fogo, a cinza apaga a visão; (4) a ave de fogo: sombra enorme que passa e volta; (5) **sonho quebrado**: a tabuleta está danificada, e o jogo mostra só pedaços (efeito de lacuna, com um fragmento para achar no Ato 2) |
| **Interpretação** | Enkidu diz que é bom sinal | **Sempre com a mesma calma e a mesma fórmula.** Na quarta noite, a câmera fica no rosto de Enkidu um segundo a mais depois que ele termina. Nenhuma fala extra: o silêncio basta |
| **Manhã** | Sol, Pavor cai até o piso da noite | O piso sobe a cada noite |

---

## 5. A borda da floresta: "Encorajar"

Os dois chegam ao portão da floresta e **travam**. Mecânica nova, só deste trecho:

- O Pavor dos dois passa de 80. Gilgamesh anda devagar; Enkidu para.
- Aparece a ação **Encorajar** quando o jogador está colado a Enkidu e olhando para ele. Segurar o botão por 2 segundos (respiração sincronizada no som).
- Os dois se encorajam **em turnos**: primeiro Gilgamesh encoraja Enkidu, depois Enkidu encoraja Gilgamesh. É o único momento do jogo em que o jogador **recebe** ajuda e tem que esperar por ela.
- As falas vêm do poema, e a formulação está a conferir. Sem falas novas do jogo aqui.
- Depois do segundo Encorajar, o Pavor cai para 40 e os dois entram juntos.

---

## 6. Dentro da floresta

1. **Beleza primeiro (2 a 3 min):** cedros imensos, luz entrando em colunas, resina no ar (partículas), um caminho largo. O Pavor desce um pouco. É o respiro antes do fim.
2. **A cacofonia (3 a 5 min):** macacos, cigarras e pássaros vão ficando cada vez mais altos e de todas as direções. Os sons não têm rosto: veem-se galhos balançando, nunca o bicho inteiro. O volume puxa o Pavor para cima. O Codex abre a entrada do fragmento de 2014: a "orquestra" da corte de Humbaba.
3. **O silêncio:** de uma vez, todos os sons param. Só ficam o coração, a respiração e os passos dos dois. O Pavor salta para 90. Câmera e controle ficam pesados. É o momento mais assustador do jogo, e nele **não aparece nada**.
4. **O grito:** o grito de Humbaba vem de longe, e as árvores tremem (no Ato 1, Enkidu disse que esse grito é o dilúvio). Ainda não se vê Humbaba.

---

## 7. Começo do combate com Humbaba

**Fase 1, as auras (Pavor máximo):** Humbaba aparece envolto em sete auras ou fulgores (o tema das auras está nas versões suméria e babilônica; o número e a descrição estão a conferir). No jogo, cada aura é uma onda de distorção, como ar quente, que **turva a visão a cada pulso**. Não dá para acertar Humbaba enquanto as auras estão de pé. O jogador sobrevive esquivando e ficando perto de Enkidu, e Encorajar mantém a visão utilizável.

**Fase 2, a prece:** quando Encorajar dá certo três vezes, Gilgamesh pode **rezar a Shamash** (no texto, Shamash ajuda os heróis).

**Fase 3, os treze ventos:** Shamash manda **treze ventos** que prendem Humbaba (a conferir a lista na Tabuleta V). No jogo, **o vento literalmente limpa a tela**: a névoa vai embora, o desfoque some e a cor volta. O Pavor cai a zero pela primeira vez desde Uruk. Humbaba fica preso, e o combate vira o diálogo moral (o pedido de clemência, Enkidu insistindo).

Assim o efeito visual do medo não é enfeite: ele é o inimigo, e o vento de Shamash é a vitória sobre ele.

---

## 8. Acessibilidade (RNF-04)

- Menu **"Efeitos de medo"** com controles separados: desfoque, aberração cromática, vinheta, tremor de câmera, vibração do controle e "respiração" do campo de visão. Cada um vai de 0 a 100%.
- Predefinição **"Sem enjoo"**: desliga tremor, respiração do campo de visão e desfoque de movimento.
- **Nada de estrobo.** Todos os pulsos ficam abaixo de 3 por segundo.
- Nenhuma informação só por som. O coração tem um indicador visual discreto (pulso na borda da tela) para quem joga sem som ou com deficiência auditiva.
- Legenda dos sons importantes: "[o canto dos pássaros para de repente]".

---

## 9. Como fazer no Unreal

| Peça | Implementação |
|---|---|
| Valor de Pavor | `AC_Pavor` (Actor Component) no personagem, de 0 a 100, com piso, taxa de subida e descida e eventos de salto |
| Fontes | `BP_ZonaDePavor` (volume que soma por segundo); distância até Enkidu calculada pelo próprio componente; sons sem fonte disparam `AdicionarPavor` |
| Visual | Material Parameter Collection `MPC_Pavor` com o valor normalizado; Post Process Material `PP_Pavor` (vinheta, desfoque radial nas bordas, aberração cromática, dessaturação); os ajustes de acessibilidade multiplicam cada canal |
| Campo de visão | Timeline ou função senoidal no FOV da câmera, com a frequência do coração |
| Som | MetaSound do coração com parâmetro de bpm; Submix com filtro passa-baixa controlado pelo Pavor; respiração em camadas |
| Controle | Force Feedback curto a cada batida acima de 50 |
| Floresta | Áudio espacial com dezenas de emissores de pássaros, macacos e cigarras; um `BP_Silencio` que, por gatilho, zera todos com fade de 0,2 s |
| Auras | Material de distorção (refração) em esferas ao redor de Humbaba; cada pulso soma Pavor |
| Ventos | Niagara de vento e folhas, mais animação do `MPC_Pavor` de volta a 0 em 4 s |

---

## 10. Próximo passo

Dá para testar a sensação **antes do PC**: posso fazer na prévia web uma cena curta com uma noite do ciclo e a entrada na floresta com cacofonia, silêncio e o grito, usando o mesmo sistema de Pavor (vinheta, desfoque, coração). Assim vocês ajustam o ritmo do medo pelo celular, e no Unreal é só reproduzir.
