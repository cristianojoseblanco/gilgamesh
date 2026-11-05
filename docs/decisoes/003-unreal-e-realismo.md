# 003 — Unreal Engine e estilo realista

**Data:** 5 de novembro de 2026
**Status:** decidido
**Substitui:** a engine (Godot) do GDD v1.0 e o estilo "estilizado e pintado" da decisão 002.

## Decisão

- **Engine:** Unreal Engine 5, na versão estável mais recente no momento da instalação (5.7 em diante).
- **Estilo:** realista. Luz, materiais e personagens buscam aparência fotográfica, sem perder a regra de transparência histórica do Codex.

## Por quê

- O jogo depende de impacto visual: uma Uruk em escala real, ao entardecer, com multidões e água.
- O Unreal entrega isso com menos esforço de arte: iluminação global (Lumen), geometria densa (Nanite), mundos grandes (World Partition) e geração procedural (PCG).
- Personagens realistas viáveis para uma pessoa só via MetaHuman, incluído na licença do Unreal.
- Materiais fotográficos de terra, tijolo de barro, junco e palmeira disponíveis na Fab (antigo Megascans).

## Custos aceitos

| Custo | Como lidar |
|---|---|
| Hardware exigente. A Epic recomenda 32 GB de RAM e 8 GB de memória de vídeo. | Conferir o PC do amigo antes do fim de semana. Abaixo disso, trabalhar com escalabilidade baixa no editor. |
| Curva de aprendizado maior. | Começar só com Blueprints. C++ entra depois, se for preciso. |
| Projeto pesado e binário (.uasset, .umap). | Git com LFS e regras claras do que entra no repositório (ver abaixo). |
| GitHub LFS grátis tem 10 GiB de armazenamento e 10 GiB de banda por mês. | Assets da Fab **não** entram no Git (dá para baixar de novo). Só entra conteúdo próprio. Se passar do limite, avaliar um plano pago ou outro servidor (Perforce, Azure DevOps). |
| Royalty de 5% sobre a receita bruta acima de US$ 1 milhão (vendas na Epic Games Store isentas). | Irrelevante até lá. Registrar o projeto no formulário de lançamento da Epic quando for publicar. |
| Trabalho no PC de outra pessoa. | Tudo vive no GitHub. Ao fim de cada sessão: commit e push. Nada fica só na máquina do amigo. |
| Realismo aumenta o risco de anacronismo visual (roupas, penteados e arquitetura "genéricos de antiguidade"). | Toda referência visual de personagem e objeto passa pelo Codex e por `assets/referencias/`, com fonte. Nada de MetaHuman com roupa moderna ou romana. |

## O que continua valendo

- Roteiro, dados (`data/*.yaml`), Codex, fragmentos e as três camadas (evidência, interpretação, invenção).
- Escala real de Uruk (decisão 001): a planta da prévia vira o blockout inicial no Unreal (`unreal/importar/uruk_blockout.glb` e `data/layout_uruk.json`).
- A prévia web continua como ferramenta para validar roteiro e ritmo pelo celular.

## O que muda

- Estrutura do repositório: o projeto Unreal entra em `Gilgamesh/` na raiz; a pasta `game/` (pensada para o Godot) sai.
- Os dados entram no Unreal como DataTables, exportados por `tools/exportar_unreal.py`.
- O GDD precisa de uma versão 1.1: seções de engine, estilo, pipeline de arte, requisitos não funcionais de desempenho e o plano de fases.

## Quando reconsiderar

Se o PC disponível não rodar o editor de forma utilizável com escalabilidade média, ou se o custo de arte realista travar o protótipo do Ato 1 por mais de dois meses.
