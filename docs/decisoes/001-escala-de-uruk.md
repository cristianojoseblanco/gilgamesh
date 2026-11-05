# 001 — Escala de Uruk

**Data:** 5 de novembro de 2026
**Status:** decidido (opção 1), com a opção 2 guardada como alternativa

## Contexto

A primeira prévia (pasta `previa-web/v1-portao`) tinha uma Uruk de uns 180 por 150 metros. A cidade real do Dinástico Arcaico era mais de 100 vezes maior em área:

- Muralha de tijolo de barro com cerca de 9 km, provavelmente erguida no Dinástico Arcaico I, na primeira metade do 3º milênio a.C. (CDLI, verbete "Uruk (mod. Warka)").
- Área dentro da muralha estimada entre uns 400 e 550 hectares, ou seja, de 4 a 5,5 km², conforme a fonte. A população fica em algumas dezenas de milhares, talvez 40 mil a 50 mil pessoas.
- Um braço do Eufrates passava pela cidade. Eanna fica a leste do antigo curso do rio. A prospecção magnética (Fassbinder e Becker, a partir de 2001) mostrou uma rede de canais que funcionava como as artérias principais da cidade. Hoje o rio corre longe e o sítio é seco.

## Opções

### Opção 1 — Escala real em tudo (ESCOLHIDA)
- Muralha de ~9 km, braço do Eufrates e canais, Eanna e o terraço de Anu nas posições gerais certas.
- Bairros próximos do jogador com detalhe; o resto vira casario simples, visível do alto do zigurate até o horizonte.
- Barcos de junco pelos canais como meio de transporte. É a assinatura visual do jogo.
- Custos: muita área genérica; precisa de recorte por distância, mapa e locomoção rápida.

### Opção 2 — Escala comprimida (GUARDADA)
- Mesma planta e proporções reais, reduzidas a uns 30–40% (muralha de 3 a 3,5 km).
- Cidade mais densa e mais fácil de encher de detalhe à mão; é o que a maioria dos jogos históricos faz.
- Quando reconsiderar: se o protótipo no Godot mostrar que a escala real fica vazia ou cansativa, ou se o custo de arte por km² ficar alto demais. A troca é de parâmetro (`CITY.wallPerimeter`, `CITY.ellipseA/B`, posições de Eanna e Anu), sem refazer a lógica.

## O que é interpretação na prévia

Traçado exato de ruas e canais, largura do braço do rio, número e posição das portas, tamanho das casas, posição relativa de Eanna e Anu. Tudo isso está marcado no Codex como interpretação.

## Fontes a conferir

- CDLI, "Uruk (mod. Warka)": https://cdli.ox.ac.uk/wiki/uruk_mod._warka
- Fassbinder, J. W. E. "Beneath the Euphrates Sediments: Magnetic Traces of the Mesopotamian Megacity Uruk-Warka". *The Ancient Near East Today* 8.6, 2020: https://anetoday.org/beneath-euphrates-sediments/
- RFE/RL, entrevista com M. van Ess e J. Fassbinder, 2003: https://www.rferl.org/a/1099592.html
- Crüsemann et al. (orgs.), *Uruk: First City of the Ancient World*, Getty, 2019.
- Liverani, *Antigo Oriente*.
