# Como trabalhamos em dupla

Duas pessoas no mesmo projeto Unreal, com PC de uso constante. O problema número 1 do Unreal em dupla: **arquivos `.uasset` e `.umap` não se juntam**. Se os dois mexem no mesmo Blueprint ou no mesmo nível ao mesmo tempo, o trabalho de um se perde. As regras abaixo existem para isso não acontecer.

## 1. Acesso

- [ ] Cristiano adiciona o amigo como colaborador: GitHub → repositório `gilgamesh` → **Settings → Collaborators → Add people**.
- [ ] Cada um usa a própria conta GitHub e a própria conta Epic. Nada de conta compartilhada.
- [ ] No PC: `git lfs install` uma vez. Cada um configura nome e e-mail no Git (`git config user.name` e `git config user.email`). Se usarem o mesmo PC, com perfis de usuário separados no Windows.

## 2. Travas de arquivo (o mais importante)

O `.gitattributes` já marca `.uasset` e `.umap` como **lockable** no Git LFS. Antes de editar um Blueprint, material ou nível:

```
git lfs lock Gilgamesh/Content/Gilgamesh/Fragmentos/BP_Fragmento.uasset
```

Ao terminar, depois do push:

```
git lfs unlock Gilgamesh/Content/Gilgamesh/Fragmentos/BP_Fragmento.uasset
```

`git lfs locks` mostra o que está travado e por quem. Opcionalmente, o plugin **Git LFS 2** do Unreal (controle de versão no editor) mostra as travas direto no Content Browser. Ele pode ser avaliado na fase 1.

**Níveis:** o World Partition permite **One File Per Actor**, já ativo nos níveis Open World. Assim, cada ator do nível vira um arquivo separado, e os dois podem mexer em partes diferentes de Uruk sem conflito.

## 3. Ramos

- `main`: sempre abre e roda.
- Um ramo por tarefa: `cristiano/mesa-do-escriba`, `amigo/materiais-tijolo`.
- Ao terminar: abrir um Pull Request para o outro revisar (nem que seja só abrir o projeto e apertar Play) e juntar na `main`.
- Dados (`data/*.yaml`), roteiro e documentos podem ir direto na `main`, com commits pequenos.

## 4. Divisão sugerida

| Frente | Quem puxa | O que inclui |
|---|---|---|
| Sistemas | um | Blueprints de jogo: movimento, combate, fragmentos, Codex, save, IA de Enkidu |
| Mundo e arte | o outro | Uruk (PCG, materiais, iluminação), MetaHumans, roupas, animação, cinemáticas |
| Roteiro, dados e pesquisa | os dois, com o Claude | YAML, Codex, fontes, fichas de personagem e de asset |

Revezem a cada fase se os dois quiserem aprender tudo. O importante é que **cada arquivo tenha um dono por vez**.

## 5. Convenção de nomes no Unreal

| Prefixo | Tipo | Exemplo |
|---|---|---|
| `BP_` | Blueprint de ator | `BP_Fragmento`, `BP_Gilgamesh` |
| `WBP_` | Widget | `WBP_Fragmento`, `WBP_Codex` |
| `S_` | Struct | `S_Fragmento` |
| `DT_` | DataTable | `DT_Fragmentos` |
| `E_` | Enum | `E_Camada` |
| `SM_` | Static Mesh | `SM_Uruk_Tijolo_0_0` |
| `SK_` | Skeletal Mesh | `SK_Gilgamesh` |
| `M_` / `MI_` | Material / instância | `M_TijoloPlanoConvexo`, `MI_Reboco_Claro` |
| `T_` | Textura | `T_Tijolo_D` (cor), `_N` (normal), `_ORM` |
| `A_` | Áudio | `A_Vento_Estepe` |
| `L_` | Nível | `L_Uruk`, `L_Floresta` |
| `ABP_` | Animation Blueprint | `ABP_Humanoide` |

Pastas por assunto em `Content/Gilgamesh/` (Core, Dados, Personagens, Mundo, Fragmentos, UI, Audio), nunca na raiz de `Content`.

## 6. Ritual de cada sessão

1. **Começo:** `git pull`. Conferir `git lfs locks`. Travar o que vai editar.
2. **Durante:** commits pequenos, com mensagem dizendo o que mudou.
3. **Fim:** push, destravar arquivos e escrever 2 ou 3 linhas em `docs/diario.md` (o que foi feito, o que travou, o próximo passo). O diário é o que o Claude lê para continuar de onde vocês pararam.
