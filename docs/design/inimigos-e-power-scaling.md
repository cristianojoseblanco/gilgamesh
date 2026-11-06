# Inimigos e power scaling

Status: rascunho de design (nov/2026). Números de linha e detalhes marcados "a conferir" devem ser checados em George (2003) e Brandão (2017).

## Ideia central: power scaling invertido

A força de combate de Gilgamesh cresce ao longo do jogo, mas os inimigos que importam no fim (morte, sono, a serpente) não se vencem na força. O jogo deve fazer o jogador sentir isso: quanto mais forte ele fica, mais claro fica que força não resolve.

## Ranking (do mais forte ao mais fraco)

| # | Inimigo | Tabuleta | Papel no jogo | Combate? |
|---|---------|----------|---------------|----------|
| 1 | Deuses (Anu, Enlil, Ishtar, Shamash) | várias | Forças que decidem a história | Não |
| 2 | Morte, Sono, Serpente | XI | Derrotas inevitáveis (provas, não lutas) | Não |
| 3 | Casal de homens-escorpião | IX | Guardiões do portão de Mashu | Só se o jogador provocar (ver abaixo) |
| 4 | Demônio do submundo (sonho de Enkidu) | VII | Sequência de pesadelo, impossível de vencer | Não (encenado) |
| 5 | Humbaba | V | Chefe mais difícil; exige os 13 ventos de Shamash | Sim |
| 6 | Touro do Céu | VI | Chefe; a dupla vence sozinha | Sim |
| 7 | Enkidu como rival | II | Luta que termina empatada | Sim (roteirizada) |
| 8 | Os "de pedra" (šūt abnī) | X | Gilgamesh destrói em fúria; isso atrapalha a travessia | Sim, com consequência |
| 9 | Leões | II, IX | Inimigos fortes de campo | Sim |
| 10 | Lobos e feras | geral | Inimigos comuns | Sim |

Curva: no texto, Humbaba (Ato 2) é mais forte que o Touro (Ato 3). O jogo explica isso porque contra Humbaba a ajuda de Shamash é obrigatória, e contra o Touro a dupla já está experiente e luta sem ajuda.

## Homens-escorpião (Tabuleta IX) — decisão

**No poema:** guardam o portão de Mashu, o olhar deles "é morte", reconhecem que Gilgamesh é dois terços deus, interrogam, avisam das 12 léguas de escuridão e deixam passar.

**No jogo:**

- Caminho padrão (fiel ao poema): encontro de guardiões, sem combate. O olhar deles aumenta o Pavor; o jogador passa pelo diálogo (contar o luto por Enkidu).
- **Se o jogador atacar:** eles revidam.
  - Invulneráveis: nenhum dano os afeta (os golpes batem e não fazem nada, faíscas na carapaça, sem barra de vida).
  - Matam Gilgamesh em 2 ou 3 golpes, em qualquer nível.
  - Ao morrer, o jogador volta antes do portão (checkpoint), com uma fala curta dos guardiões na volta, reconhecendo a tentativa. Sem punição além disso.
  - Opcional: o Codex ganha uma entrada (camada "invenção") sobre o que aconteceu, e uma conquista escondida.
- Objetivo: ensinar, na prática, o tema do power scaling invertido. Este é o primeiro ponto do jogo em que a força do jogador não serve para nada.

### Implementação no Unreal (rascunho)

- `BP_GuardiaoEscorpiao`: `bCanBeDamaged = false` (ou ignora `AnyDamage`); ao receber `OnHit` do jogador, muda o estado para Hostil.
- StateTree: Vigiar → Interrogar (diálogo) → Hostil (ataque com dano maior que a vida máxima / 2) → Deixar passar.
- Hostil é permanente até o jogador morrer; no respawn volta para Vigiar.
- Pavor: o olhar soma Pavor por segundo enquanto o jogador olha para eles (ver `medo-a-caminho-da-floresta.md`).

## A conferir

- Linhas exatas da Tabuleta IX (encontro com os escorpiões, ~IX 37–135) e da luta com leões.
- Detalhes dos "de pedra" na Tabuleta X (o que são exatamente, segundo George).
- Descrição do demônio no sonho de Enkidu (Tabuleta VII).
