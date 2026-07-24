# 📦 BACKUP DA CAMPANHA — PACOTE DE TRANSFERÊNCIA

> **PARA QUE SERVE:** Se esta conversa atingir o limite, copie TODO o conteúdo
> deste arquivo (junto com `FICHA_PERSONAGEM.md`) e cole na nova conversa.
> O novo agente terá tudo que precisa para continuar exatamente de onde paramos.

---

## 🧭 INSTRUÇÕES PARA O PRÓXIMO AGENTE (leia primeiro)

1. Você é o **narrador/mestre** desta campanha de RPG. O jogador joga, você narra.
2. **NUNCA invente resultados de dados.** Toda rolagem é feita executando
   o script `rolador.py`. Para Blades of the Immortals use o modo pool:
   `python3 rolador.py pool 3` (rola 3d6, pega o maior, interpreta o resultado).
   Pool 0: `python3 rolador.py pool 0` (2d6, pega o menor).
   Mostre sempre a saída bruta do script ao jogador. O script usa o módulo
   `secrets` e grava log de auditoria em `rolagens_log.jsonl`.
3. **Atualize este arquivo** ao fim de cada cena/sessão importante:
   resumo dos eventos, NPCs, itens, decisões e estado atual.
4. **Atualize `FICHA_PERSONAGEM.md`** sempre que a ficha mudar
   (dano, XP, itens, dinheiro, condições).
5. Respeite a agência do jogador: não decida ações pelo personagem dele.

---

## ⚙️ SISTEMA DE REGRAS

- **Sistema:** **Blades of the Immortals v0.3.2** (Jagganoth) — motor **Forged in the Dark**, gênero xiānxiá (fantasia de cultivo).
- **Resumo completo das regras:** ver arquivo **`SISTEMA_BOTI.md`** neste repositório (leitura obrigatória para o narrador).
- **Essência:** pools de d6, pega o maior. 6 = sucesso; dois 6 = crítico; 4-5 = sucesso com consequências; 1-3 = ruim. Posição/Efeito, Stress, Resistência, Clocks, Panoply (técnicas + tesouros), Reinos de Cultivo (0-6), estrutura Missão → Downtime.
- **Regras da casa (house rules):** modo solo — 1 jogador cultivador + GM-agente; facção movida narrativamente pelo GM; rolagens sempre via `rolador.py pool N`.

---

## 🌍 CENÁRIO / AMBIENTAÇÃO

- **Mundo:** _(a definir)_
- **Tom da campanha:** _(a definir)_
- **Local atual:** _(a definir)_
- **Data/hora no jogo:** _(a definir)_

---

## 📖 DIÁRIO DA CAMPANHA (resumo cronológico)

> Formato: cada sessão/cena ganha uma entrada. A mais recente fica por último.

### Sessão 0 — Preparação (2026-07-24)
- Repositório configurado: rolador de dados, backup e ficha criados.
- Sistema definido: **Blades of the Immortals v0.3.2** (Forged in the Dark, xiānxiá). Guia completo em `SISTEMA_BOTI.md`.
- Rolador atualizado com modo `pool` (d6, pega o maior) nativo do sistema.
- Ficha convertida para o formato BoTI.
- Próximo passo: jogador escolhe playbook e criamos o cultivador + cenário.

---

## 👥 NPCs CONHECIDOS

| Nome | Quem é | Relação com o personagem | Status |
|------|--------|--------------------------|--------|
| —    | —      | —                        | —      |

---

## 🗺️ LOCAIS VISITADOS

| Local | O que aconteceu lá | Pendências |
|-------|--------------------|------------|
| —     | —                  | —          |

---

## 🎯 MISSÕES / OBJETIVOS

| Objetivo | Status | Observações |
|----------|--------|-------------|
| —        | —      | —           |

---

## 🔑 SEGREDOS, PISTAS E GANCHOS PENDENTES

- _(nenhum ainda)_

---

## ⏸️ ESTADO EXATO DE ONDE PARAMOS

> Esta seção deve SEMPRE descrever o momento exato da última cena,
> para retomar sem perder nada.

**Última cena:** A campanha ainda não começou. Sistema Blades of the Immortals
aprendido e registrado em `SISTEMA_BOTI.md`. Próximo passo: o jogador escolhe
o playbook (Ascendant, Assassin, Assured, Beast, Exorcist, Fanatic, Inheritor,
Scholar ou Witch), depois criamos o cultivador, a facção e o sistema de cultivo
do cenário juntos.
