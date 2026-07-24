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

### Sessão 1 — Prólogo: O Vazio Entre Vidas (2026-07-24)
- O jogador (vida passada: solitária, morreu de **depressão**, sonhava viver em outro mundo) enfrentou as 3 perguntas da Deusa da Reencarnação.
- Escolhas: playbook **Ascendant**; renascer **desde bebê**; **segundo filho de clã nobre** (sem fardo de herdeiro).
- Fortunas roladas: clã em **declínio** (2d=ruim); talento inato **gênio de uma geração** (2d=6); presságios do nascimento **auspiciosos** (2d=6).
- **Condição da Deusa** (preço do talento): *"Viva. De verdade."* — se ele desistir da vida como na anterior, a raiz marcial murcha. Ela o observa (Connection Clock).
- Nascimento: **Clã Yeon** (Clã da Andorinha), casa nobre de espadachins em declínio. Pai: **Yeon Baek-San** (patriarca). Mãe: **Dama Seo Hwa-Ryun**. Irmão: **Yeon Mu-Hyuk** (herdeiro, +6 anos). Nome dado pelos pais: **YEON MU-JIN (연무진)**.
- Presságio público: revoada de andorinhas cobriu a lua no nascimento — a província comenta que "nasceu uma estrela no Clã Yeon" (fama + atenção indesejada).

### Sessão 2 — Capítulo 1: O Teste da Raiz Marcial (2026-07-24)
- Salto temporal: Mu-Jin aos **6 anos**. Cerimônia pública no Salão Ancestral: teste da raiz marcial com o **Orbe de Jade da Andorinha** (relíquia que mede talento).
- Ações iniciais distribuídas na ficha (Attune 2, Blitz 1, Endure 1, Force 1, Study 1, Sway 1) — ajustáveis até o fim do Cap. 1.
- **Action Roll (Attune 2d): [5,4] = SUCESSO COM CONSEQUÊNCIAS** — o orbe revelou talento lendário (brilho jamais visto em gerações), MAS o qi de Mu-Jin foi forte demais: **o Orbe de Jade rachou** diante do clã inteiro e de convidados — entre eles **Dokgo Hwan**, emissário da **Seita do Punho de Ferro** (credora do clã), que testemunhou tudo.
- Mu-Jin **aceitou a consequência** e usou a mente adulta: ajoelhou-se e declarou que "o orbe não suportou sua devoção ao clã".
- **Action Roll (Sway 1d): [5] = SUCESSO COM CONSEQUÊNCIAS** — O clã comprou a narrativa: anciões emocionados, o pai proclamou o dia como "o dia em que o Céu abençoou o Clã Yeon"; a rachadura virou lenda ("a marca da andorinha"). CONSEQUÊNCIA: Dokgo Hwan não se comoveu — viu a *atuação perfeita demais* de uma criança de 6 anos. Antes de partir, sussurrou ao patriarca uma proposta: **a Seita do Punho de Ferro oferece "perdoar parte da dívida" em troca de levar Mu-Jin como discípulo externo**. O pai recusou na hora — mas a dívida continua, e a seita agora tem um alvo.
- Gancho criado: a Seita do Punho de Ferro quer Mu-Jin; prazo da dívida vence em 1 ano (clock de campanha 6: ☐☐☐☐☐☐).

---

## 👥 NPCs CONHECIDOS

| Nome | Quem é | Relação com o personagem | Status |
|------|--------|--------------------------|--------|
| **A Deusa da Reencarnação** | Divindade belíssima e provocante; selou a barganha do renascimento | Patrona secreta; condição "Viva de verdade"; observa-o | Ativa (invisível ao mundo) |
| **Yeon Baek-San** | Patriarca do Clã Yeon, espadachim orgulhoso | Pai | Vivo |
| **Dama Seo Hwa-Ryun** | De família mercante; prática e afetuosa | Mãe | Viva |
| **Yeon Mu-Hyuk** | Herdeiro do clã; talento mediano, esforço enorme | Irmão mais velho (+6 anos) | Vivo |
| **Dokgo Hwan** | Emissário da Seita do Punho de Ferro (credora do Clã Yeon); frio, calculista | Testemunhou o talento de Mu-Jin no teste | Ativo — interesse desconhecido |

---

## 🗺️ LOCAIS VISITADOS

| Local | O que aconteceu lá | Pendências |
|-------|--------------------|------------|
| —     | —                  | —          |

---

## 🎯 MISSÕES / OBJETIVOS

| Objetivo | Status | Observações |
|----------|--------|-------------|
| **A Dívida do Clã Yeon** (Seita do Punho de Ferro) | Clock ☐☐☐☐☐☐ (6) | Prazo ~1 ano em jogo; a seita quer Mu-Jin como "pagamento" |
| Honrar a condição da Deusa ("Viva de verdade") | Contínuo | Crença central do personagem |

---

## 🔑 SEGREDOS, PISTAS E GANCHOS PENDENTES

- _(nenhum ainda)_

---

## ⏸️ ESTADO EXATO DE ONDE PARAMOS

> Esta seção deve SEMPRE descrever o momento exato da última cena,
> para retomar sem perder nada.

**Última cena:** Fim da cerimônia do Teste. Mu-Jin (6 anos) virou lenda local:
talento nunca registrado + "marca da andorinha" no orbe. Dokgo Hwan partiu após
ter sua proposta (levar Mu-Jin como discípulo em troca de abatimento da dívida)
recusada pelo patriarca — mas deixou claro que a Seita do Punho de Ferro
voltará quando a dívida vencer (~1 ano; clock 6 criado). Dokgo Hwan desconfia
que Mu-Jin não é uma criança normal. Próximos passos possíveis: cenas de
treinamento (definir habilidade inicial do Ascendant + Método de Cultivo no
Panoply), vida familiar, ou salto temporal até a crise da dívida.
