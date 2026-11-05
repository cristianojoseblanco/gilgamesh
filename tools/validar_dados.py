#!/usr/bin/env python3
"""Valida os dados do jogo em data/ (fontes, tabuletas, episódios, fragmentos, Codex).

Uso:  python3 tools/validar_dados.py
Sai com código 1 se houver erro. Avisos não bloqueiam.
"""
import csv
import sys
from pathlib import Path

import yaml

RAIZ = Path(__file__).resolve().parent.parent
DADOS = RAIZ / "data"

CAMADAS = {"evidencia", "interpretacao", "invencao"}
TIPOS_CODEX = {"personagem", "lugar", "objeto", "versao", "conceito"}
VERSOES = {"padrao-babilonica", "babilonica-antiga", "sumeria"}
STATUS = {"a_conferir", "consultada", "conferida"}

erros, avisos = [], []


def erro(msg):
    erros.append(msg)


def aviso(msg):
    avisos.append(msg)


def carregar_yaml(nome):
    with open(DADOS / nome, encoding="utf-8") as f:
        dados = yaml.safe_load(f) or []
    if not isinstance(dados, list):
        erro(f"{nome}: o arquivo deve ser uma lista")
        return []
    return dados


def ids_unicos(itens, nome):
    vistos = set()
    for it in itens:
        i = it.get("id")
        if not i:
            erro(f"{nome}: item sem id: {it}")
        elif i in vistos:
            erro(f"{nome}: id repetido: {i}")
        vistos.add(i)
    return vistos


def checar_fontes(refs, onde, fontes):
    for ref in refs or []:
        fid = ref.split(":", 1)[0].strip()
        if fid not in fontes:
            erro(f"{onde}: fonte desconhecida '{fid}'")


# --- fontes.csv
with open(DADOS / "fontes.csv", encoding="utf-8", newline="") as f:
    linhas = list(csv.DictReader(f))
colunas = {"id", "autor", "titulo", "edicao", "ano", "paginas", "url", "licenca", "status"}
if linhas and set(linhas[0].keys()) != colunas:
    erro(f"fontes.csv: colunas esperadas {sorted(colunas)}")
fontes = set()
for ln in linhas:
    if ln["id"] in fontes:
        erro(f"fontes.csv: id repetido {ln['id']}")
    fontes.add(ln["id"])
    if not ln["licenca"]:
        erro(f"fontes.csv: {ln['id']} sem licença")
    if ln["status"] not in STATUS:
        erro(f"fontes.csv: {ln['id']} com status inválido '{ln['status']}'")
    elif ln["status"] != "conferida":
        aviso(f"fonte {ln['id']} ainda não conferida ({ln['status']})")

# --- tabuletas
tabuletas = carregar_yaml("tabuletas.yaml")
ids_tab = ids_unicos(tabuletas, "tabuletas.yaml")
esperadas = {f"T{n:02d}" for n in range(1, 13)}
if ids_tab != esperadas:
    erro(f"tabuletas.yaml: faltam {sorted(esperadas - ids_tab)} / sobram {sorted(ids_tab - esperadas)}")
for t in tabuletas:
    for campo in ("titulo", "resumo", "versoes", "lacunas", "fontes", "status"):
        if not t.get(campo):
            erro(f"tabuleta {t.get('id')}: campo '{campo}' vazio")
    for v in t.get("versoes", []):
        if v not in VERSOES:
            erro(f"tabuleta {t['id']}: versão desconhecida '{v}'")
    checar_fontes(t.get("fontes"), f"tabuleta {t.get('id')}", fontes)

# --- episódios e fragmentos
episodios = carregar_yaml("episodios.yaml")
fragmentos = carregar_yaml("fragmentos.yaml")
ids_ep = ids_unicos(episodios, "episodios.yaml")
ids_fr = ids_unicos(fragmentos, "fragmentos.yaml")

for e in episodios:
    onde = f"episódio {e.get('id')}"
    if e.get("tabuleta") not in ids_tab | {"moldura"}:
        erro(f"{onde}: tabuleta '{e.get('tabuleta')}' não existe")
    for v in e.get("versoes", []):
        if v not in VERSOES:
            erro(f"{onde}: versão desconhecida '{v}'")
    if e.get("lacuna"):
        fr = e.get("fragmento")
        if not fr:
            erro(f"{onde}: marcado com lacuna mas sem fragmento")
        elif fr not in ids_fr:
            erro(f"{onde}: fragmento '{fr}' não existe")
    if e.get("tabuleta") != "moldura" and not e.get("fontes"):
        erro(f"{onde}: sem fontes")
    checar_fontes(e.get("fontes"), onde, fontes)
    if not str(e.get("cena", "")).startswith("res://"):
        erro(f"{onde}: cena deve começar com res://")

completados = {}
for fr in fragmentos:
    onde = f"fragmento {fr.get('id')}"
    if fr.get("completa") not in ids_ep:
        erro(f"{onde}: episódio '{fr.get('completa')}' não existe")
    completados.setdefault(fr.get("completa"), []).append(fr["id"])
    if fr.get("tabuleta") not in ids_tab:
        erro(f"{onde}: tabuleta '{fr.get('tabuleta')}' não existe")
    if fr.get("versao_origem") not in VERSOES:
        erro(f"{onde}: versão de origem inválida")
    for campo in ("onde", "texto", "efeito", "fontes"):
        if not fr.get(campo):
            erro(f"{onde}: campo '{campo}' vazio")
    checar_fontes(fr.get("fontes"), onde, fontes)
for ep, frs in completados.items():
    if len(frs) > 1:
        aviso(f"episódio {ep} é completado por mais de um fragmento: {frs}")
usados = {e.get("fragmento") for e in episodios if e.get("fragmento")}
for f_id in ids_fr - usados:
    aviso(f"fragmento {f_id} não é citado por nenhum episódio")

# --- Codex
codex = carregar_yaml("codex.yaml")
ids_unicos(codex, "codex.yaml")
for c in codex:
    onde = f"Codex {c.get('id')}"
    if c.get("tipo") not in TIPOS_CODEX:
        erro(f"{onde}: tipo inválido '{c.get('tipo')}'")
    cam = c.get("camadas") or []
    if not cam or any(x not in CAMADAS for x in cam):
        erro(f"{onde}: camadas inválidas {cam}")
    if not c.get("fontes"):
        erro(f"{onde}: sem fontes")
    checar_fontes(c.get("fontes"), onde, fontes)
    if c.get("libera") not in ids_ep | ids_fr:
        erro(f"{onde}: 'libera' aponta para '{c.get('libera')}', que não existe")

# --- resumo
print(f"fontes: {len(fontes)} · tabuletas: {len(ids_tab)} · episódios: {len(ids_ep)} · "
      f"fragmentos: {len(ids_fr)} · Codex: {len(codex)}")
for a in avisos:
    print("AVISO:", a)
for e in erros:
    print("ERRO:", e)
print("OK" if not erros else f"{len(erros)} erro(s)")
sys.exit(1 if erros else 0)
