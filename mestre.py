#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MESTRE.PY — Painel de estado da mesa (a "espinha dorsal" executável).

Lê os arquivos-verdade do repositório e imprime um resumo do estado da
campanha: personagem, clocks, últimas rolagens, sessões e o checklist do
ciclo do mestre. Não altera nada; é somente leitura + verificação.

Uso:  python3 mestre.py
"""

import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).parent
FICHA = RAIZ / "FICHA_PERSONAGEM.md"
BACKUP = RAIZ / "BACKUP_CAMPANHA.md"
SISTEMA = RAIZ / "SISTEMA_BOTI.md"
NUCLEO = RAIZ / "MESTRE_NUCLEO.md"
LOG = RAIZ / "rolagens_log.jsonl"
RETRATOS = RAIZ / "retratos"

LARG = 66


def titulo(txt):
    print("\n" + "═" * LARG)
    print(f"  {txt}")
    print("═" * LARG)


def campo_tabela(texto, rotulo):
    """Extrai '| **rotulo** | valor |' de um markdown."""
    m = re.search(r"\|\s*\*\*" + re.escape(rotulo) + r"\*\*\s*\|\s*(.+?)\s*\|", texto)
    return m.group(1).strip() if m else "?"


def main():
    faltando = [p.name for p in (FICHA, BACKUP, SISTEMA, NUCLEO) if not p.exists()]
    print("┌" + "─" * (LARG - 2) + "┐")
    print("│  🧠 NÚCLEO DO MESTRE — PAINEL DE ESTADO DA MESA".ljust(LARG - 1) + "│")
    print("└" + "─" * (LARG - 2) + "┘")

    # --- Integridade dos arquivos ---
    titulo("📁 INTEGRIDADE DOS ARQUIVOS-VERDADE")
    for p in (FICHA, BACKUP, SISTEMA, NUCLEO, LOG):
        estado = "✅" if p.exists() else "❌ FALTANDO"
        print(f"  {estado}  {p.name}")
    n_retratos = len(list(RETRATOS.glob("*.png"))) if RETRATOS.exists() else 0
    print(f"  {'✅' if n_retratos else '⚠️ '}  retratos/ ({n_retratos} imagens)")
    if faltando:
        print(f"\n  ⚠️  ATENÇÃO: arquivos essenciais faltando: {', '.join(faltando)}")

    # --- Personagem ---
    if FICHA.exists():
        f = FICHA.read_text(encoding="utf-8")
        titulo("🎭 PERSONAGEM")
        print(f"  Nome:     {campo_tabela(f, 'Nome do cultivador')}")
        print(f"  Playbook: {campo_tabela(f, 'Playbook')}")
        print(f"  Reino:    {campo_tabela(f, 'Reino atual')}")
        print(f"  Camada:   {campo_tabela(f, 'Camada / Reino menor')}")
        m = re.search(r"\*\*Stress:\*\*\s*(\d+\s*/\s*\d+)", f)
        print(f"  Stress:   {m.group(1) if m else '?'}")
        m = re.search(r"\*\*Condition Track:\*\*\s*(.+)", f)
        print(f"  Condição: {m.group(1).strip() if m else '?'}")
        m = re.search(r"\*\*Scars.*?:\*\*\s*(.+)", f)
        print(f"  Scars:    {m.group(1).strip() if m else '?'}")
        m = re.search(r"\*\*XP de personagem:\*\*\s*(\d+)", f)
        print(f"  XP:       {m.group(1) if m else '?'}")

    # --- Campanha ---
    if BACKUP.exists():
        b = BACKUP.read_text(encoding="utf-8")
        titulo("📖 CAMPANHA")
        sessoes = re.findall(r"^### (Sess\ão \d+.*)$", b, re.MULTILINE)
        print(f"  Sessões no diário: {len(sessoes)}")
        for s in sessoes[-3:]:
            print(f"    • {s}")
        npcs = re.findall(r"^\|\s*\*\*(.+?)\*\*\s*\|", b, re.MULTILINE)
        npcs = [n for n in npcs if n not in ("Nome",)]
        print(f"  NPCs registrados: {len(set(npcs))} -> {', '.join(dict.fromkeys(npcs))}")
        clocks = re.findall(r"^\|\s*\*\*(.+?)\*\*.*?\|\s*(Clock [◼☐]+[^|]*)\|", b, re.MULTILINE)
        if clocks:
            print("  Clocks ativos:")
            for nome, c in clocks:
                print(f"    ⏰ {nome}: {c.strip()}")
        m = re.search(r"\*\*Última cena:\*\*\s*(.+?)(?:\n\n|\Z)", b, re.DOTALL)
        if m:
            resumo = re.sub(r"\s+", " ", m.group(1)).strip()
            print(f"\n  ⏸️  ONDE PARAMOS: {resumo[:400]}{'…' if len(resumo) > 400 else ''}")

    # --- Rolagens ---
    titulo("🎲 ÚLTIMAS ROLAGENS (auditáveis)")
    if LOG.exists():
        linhas = LOG.read_text(encoding="utf-8").strip().splitlines()
        print(f"  Total no log: {len(linhas)}")
        for ln in linhas[-5:]:
            r = json.loads(ln)
            dados = r.get("dados", r.get("rolagens"))
            saida = r.get("resultado") or f"total {r.get('total')}"
            print(f"    {r['quando_utc']}  {r['expressao']:<10} {str(dados):<18} => {saida}")
    else:
        print("  (nenhuma rolagem registrada ainda)")

    # --- Checklist do ciclo ---
    titulo("🔄 CHECKLIST DO CICLO (a cada turno)")
    for item in (
        "0. Mensagem duplicada? → ignorar em silêncio",
        "1. Reler estado (backup + ficha + log)",
        "2. Interpretar o jogador — agência é dele",
        "3. Julgar pelo sistema (rolagem? posição? efeito?)",
        "4. Rolar via rolador.py — saída bruta sempre",
        "5. Consequências honestas + clocks",
        "6. Persistir tudo nos arquivos + commit",
        "7. Devolver a mão ao jogador (ritmo dele)",
    ):
        print(f"  ☐ {item}")

    print("\n" + "═" * LARG)
    print("  Sinergia OK: memória = repositório, acaso = rolador, corpo do")
    print("  PC = jogador, mundo = mestre. Bom jogo. 🏮")
    print("═" * LARG + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
