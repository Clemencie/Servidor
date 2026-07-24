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

- **Mundo:** **Murim** (mundo de artes marciais estilo manhwa coreano/wuxia) — seitas, clãs, o mundo marcial (Kangho/Gangho).
- **Premissa:** o protagonista é um **reencarnado** — morreu na Terra (vida moderna) e renasce no Murim, mantendo as memórias da vida anterior. A campanha abre diante da **Deusa da Reencarnação** (bela e provocante), no vazio entre vidas, onde ele negocia os termos do seu renascimento.
- **Tom da campanha:** ação de artes marciais + progressão de cultivo, humor de isekai/manhwa, drama de seitas.
- **Sistema de cultivo da mesa (Reinos BoTI → escala Murim):**
  | Reino BoTI | Estágio Murim |
  |---|---|
  | 0 | Terceira/Segunda Classe (aprendiz; qi rudimentar) |
  | 1 | Primeira Classe (일류) |
  | 2 | Ápice — Jeoljeong (절정) |
  | 3 | Super Ápice — Choejeoljeong (초절정) |
  | 4 | Hwagyeong (화경) — mestre transcendente |
  | 5 | Hyeongyeong (현경) |
  | 6 | Saengsagyeong (생사경) — domínio sobre vida e morte |
- **Local atual:** O Vazio Entre Vidas (salão da Deusa da Reencarnação).
- **Data/hora no jogo:** antes do renascimento.

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
| **A Deusa da Reencarnação** | Divindade belíssima e provocante que administra o ciclo de renascimentos; conduz a barganha do renascimento do PC | Primeira "conhecida" entre vidas; potencial patrona/observadora recorrente | Ativa — conduzindo a reencarnação |

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

**Última cena:** Prólogo prestes a começar — o personagem (recém-morto na Terra)
está diante da **Deusa da Reencarnação** no Vazio Entre Vidas, decidindo os
termos do seu renascimento no mundo Murim. Falta definir na criação:
playbook, nome, causa da morte na Terra, e as escolhas feitas diante da Deusa
(origem do renascimento, dons/handicaps). O playbook **Inheritor** foi sugerido
como encaixe natural para reencarnado (legado/memórias de outra vida), mas o
jogador ainda não escolheu.
