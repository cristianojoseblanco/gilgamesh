#!/usr/bin/env python3
"""Monta a prévia jogável do Ato 1 (previa-web/ato1/index.html).

Junta três partes:
  1. o motor da cidade, copiado de previa-web/index.html (entre os marcadores abaixo);
  2. os dados do jogo em data/*.yaml, convertidos para JSON;
  3. o roteiro e a interface em previa-web/ato1/fonte.html.

Uso:  python3 tools/montar_previa.py
Rode tools/validar_dados.py antes: dados inválidos não devem entrar na prévia.
"""
import json
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
MOTOR_ARQ = RAIZ / "previa-web" / "index.html"
FONTE = RAIZ / "previa-web" / "ato1" / "fonte.html"
SAIDA = RAIZ / "previa-web" / "ato1" / "index.html"
INICIO = "// PARÂMETROS DA CIDADE"
FIM = "// gazelas e Enkidu"
DADOS = ["tabuletas", "episodios", "fragmentos", "codex"]


def extrair_motor(texto):
    linhas = texto.splitlines()
    ini = next(i for i, l in enumerate(linhas) if l.startswith(INICIO))
    fim = next(i for i, l in enumerate(linhas) if l.startswith(FIM))
    if fim <= ini:
        raise SystemExit("marcadores do motor fora de ordem")
    return "\n".join(linhas[ini - 1:fim])  # inclui a linha de "=====" antes do título


def main():
    motor = extrair_motor(MOTOR_ARQ.read_text(encoding="utf-8"))
    dados = {}
    for nome in DADOS:
        with open(RAIZ / "data" / f"{nome}.yaml", encoding="utf-8") as f:
            dados[nome] = yaml.safe_load(f)
    fonte = FONTE.read_text(encoding="utf-8")
    for marca in ("/*@MOTOR@*/", "/*@DADOS@*/"):
        if fonte.count(marca) != 1:
            raise SystemExit(f"marcador {marca} deve aparecer uma vez em {FONTE.name}")
    saida = fonte.replace("/*@MOTOR@*/", motor).replace("/*@DADOS@*/", json.dumps(dados, ensure_ascii=False))
    SAIDA.write_text(saida, encoding="utf-8")
    print(f"{SAIDA.relative_to(RAIZ)}: {len(saida) // 1024} KB, motor com {motor.count(chr(10)) + 1} linhas")


if __name__ == "__main__":
    main()
