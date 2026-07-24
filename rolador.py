#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ROLADOR DE DADOS — 100% aleatório, sem interferência narrativa.

Regras de integridade:
  1. Usa o módulo `secrets` (gerador criptográfico do sistema operacional).
     Não existe seed manual — é IMPOSSÍVEL prever ou manipular o resultado.
  2. Toda rolagem é gravada automaticamente em `rolagens_log.jsonl`
     com data/hora UTC, expressão, resultados individuais e total.
     O log serve de auditoria: nada pode ser apagado/alterado sem deixar rastro.
  3. O script apenas imprime números. Zero narrativa, zero ajuste.

Uso:
    python3 rolador.py 1d20              -> rola 1 dado de 20 faces
    python3 rolador.py 3d6+2             -> rola 3d6 e soma +2
    python3 rolador.py 2d10-1            -> rola 2d10 e subtrai 1
    python3 rolador.py 1d20 vantagem     -> rola 2d20, pega o MAIOR
    python3 rolador.py 1d20 desvantagem  -> rola 2d20, pega o MENOR
    python3 rolador.py 1d20 3d6+2 1d100  -> várias rolagens de uma vez

Modo BLADES OF THE IMMORTALS (Forged in the Dark):
    python3 rolador.py pool 3            -> rola 3d6, pega o MAIOR
    python3 rolador.py pool 0            -> pool zero: rola 2d6, pega o MENOR

    Interpretação automática (regras do BoTI):
      dois+ 6 = SUCESSO CRÍTICO | 6 = SUCESSO PLENO
      4-5 = SUCESSO COM CONSEQUÊNCIAS | 1-3 = RESULTADO RUIM
      (pool 0 nunca dá crítico)
"""

import json
import re
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path

LOG = Path(__file__).parent / "rolagens_log.jsonl"
PADRAO = re.compile(r"^(\d+)d(\d+)([+-]\d+)?$", re.IGNORECASE)


def rolar(expressao: str, modo: str = "normal") -> dict:
    m = PADRAO.match(expressao.strip())
    if not m:
        raise ValueError(f"Expressão inválida: '{expressao}' (use formato XdY, XdY+Z ou XdY-Z)")

    qtd, faces = int(m.group(1)), int(m.group(2))
    mod = int(m.group(3) or 0)
    if not (1 <= qtd <= 1000) or not (2 <= faces <= 1000):
        raise ValueError("Limites: 1-1000 dados, 2-1000 faces.")

    if modo in ("vantagem", "desvantagem") and qtd == 1:
        r1 = [secrets.randbelow(faces) + 1]
        r2 = [secrets.randbelow(faces) + 1]
        escolhido = max(r1[0], r2[0]) if modo == "vantagem" else min(r1[0], r2[0])
        registro = {
            "quando_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "expressao": expressao,
            "modo": modo,
            "rolagens": [r1[0], r2[0]],
            "escolhido": escolhido,
            "modificador": mod,
            "total": escolhido + mod,
        }
    else:
        dados = [secrets.randbelow(faces) + 1 for _ in range(qtd)]
        registro = {
            "quando_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "expressao": expressao,
            "modo": "normal",
            "dados": dados,
            "modificador": mod,
            "total": sum(dados) + mod,
        }

    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")
    return registro


def rolar_pool(qtd: int) -> dict:
    """Rolagem estilo Forged in the Dark (Blades of the Immortals):
    rola qtd d6 e pega o MAIOR. Pool 0 = rola 2d6 e pega o MENOR (sem crítico)."""
    if not (0 <= qtd <= 20):
        raise ValueError("Pool deve ser entre 0 e 20 dados.")

    if qtd == 0:
        dados = [secrets.randbelow(6) + 1, secrets.randbelow(6) + 1]
        maior = min(dados)
        critico = False
    else:
        dados = [secrets.randbelow(6) + 1 for _ in range(qtd)]
        maior = max(dados)
        critico = dados.count(6) >= 2

    if critico:
        resultado = "SUCESSO CRÍTICO"
    elif maior == 6:
        resultado = "SUCESSO PLENO"
    elif maior >= 4:
        resultado = "SUCESSO COM CONSEQUÊNCIAS"
    else:
        resultado = "RESULTADO RUIM"

    registro = {
        "quando_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "expressao": f"pool {qtd}d",
        "modo": "pool_fitd",
        "dados": dados,
        "maior": maior,
        "critico": critico,
        "resultado": resultado,
    }
    with LOG.open("a", encoding="utf-8") as f:
        f.write(json.dumps(registro, ensure_ascii=False) + "\n")
    return registro


def formatar(r: dict) -> str:
    if r["modo"] == "pool_fitd":
        zero = " (pool 0: 2d6, pega o menor)" if r["expressao"].startswith("pool 0") else ""
        return (f"{r['expressao']}{zero}: dados {r['dados']} -> maior {r['maior']} "
                f"=> {r['resultado']}")
    mod = r["modificador"]
    smod = f" {'+' if mod >= 0 else '-'} {abs(mod)}" if mod else ""
    if r["modo"] in ("vantagem", "desvantagem"):
        return (f"{r['expressao']} ({r['modo'].upper()}): rolou {r['rolagens']} "
                f"-> escolhido {r['escolhido']}{smod} = TOTAL {r['total']}")
    return f"{r['expressao']}: dados {r['dados']}{smod} = TOTAL {r['total']}"


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 1

    args = argv[1:]

    if args[0].lower() == "pool":
        for n in (args[1:] or ["1"]):
            try:
                print(formatar(rolar_pool(int(n))))
            except ValueError as e:
                print(f"ERRO: {e}")
        return 0

    modo = "normal"
    if args and args[-1].lower() in ("vantagem", "desvantagem"):
        modo = args[-1].lower()
        args = args[:-1]

    for exp in args:
        try:
            print(formatar(rolar(exp, modo)))
        except ValueError as e:
            print(f"ERRO: {e}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
