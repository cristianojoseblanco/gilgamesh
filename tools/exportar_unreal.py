#!/usr/bin/env python3
"""Exporta os dados de data/*.yaml como JSON no formato de DataTable do Unreal.

Cada arquivo vira unreal/importar/DT_<Nome>.json: uma lista de objetos com a chave
"Name" (nome da linha) mais os campos da struct. Listas viram texto separado por "; "
para caber em campos FString simples. As structs a criar no Unreal estão em
unreal/README.md.

Uso:  python3 tools/exportar_unreal.py
"""
import json
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
SAIDA = RAIZ / "unreal" / "importar"

# arquivo YAML -> (nome da tabela, campos exportados na ordem da struct)
TABELAS = {
    "tabuletas": ("Tabuletas", ["titulo", "ato", "resumo", "versoes", "lacunas", "fontes", "status"]),
    "episodios": ("Episodios", ["tabuleta", "ato", "local", "personagens", "jogavel_como", "versoes", "lacuna", "fragmento", "fontes"]),
    "fragmentos": ("Fragmentos", ["tabuleta", "completa", "onde", "texto", "efeito", "versao_origem", "fontes", "status"]),
    "codex": ("Codex", ["tipo", "titulo", "camadas", "texto", "fontes", "libera", "status"]),
}


def valor(v):
    if v is None:
        return ""
    if isinstance(v, list):
        return "; ".join(str(x) for x in v)
    if isinstance(v, bool):
        return v
    return v if isinstance(v, (int, float)) else str(v)


def main():
    SAIDA.mkdir(parents=True, exist_ok=True)
    for arq, (nome, campos) in TABELAS.items():
        with open(RAIZ / "data" / f"{arq}.yaml", encoding="utf-8") as f:
            itens = yaml.safe_load(f)
        linhas = []
        for it in itens:
            linha = {"Name": it["id"]}
            for c in campos:
                v = it.get(c)
                if c == "ato":  # "epilogo" e números viram texto
                    v = str(v) if v is not None else ""
                linha[c] = valor(v) if c != "lacuna" else bool(v)
            linhas.append(linha)
        destino = SAIDA / f"DT_{nome}.json"
        destino.write_text(json.dumps(linhas, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"{destino.relative_to(RAIZ)}: {len(linhas)} linhas")


if __name__ == "__main__":
    main()
