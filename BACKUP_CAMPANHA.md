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

### 🛡️ REGRAS ANTI-BUG (obrigatórias, adicionadas em 2026-07-24 a pedido do jogador)

**A. Mensagens duplicadas:** A interface às vezes reenvia a mesma mensagem do
jogador duas vezes. Se receber uma mensagem idêntica (ou quase idêntica) à
anterior, trate como **falha técnica**: ignore a duplicata SILENCIOSAMENTE e
não reaja a ela dentro da história (nada de NPCs comentando "você repetiu").
Se houver dúvida se foi duplicata ou intenção, pergunte fora da narrativa.

**B. Agência do jogador (regra estrita):**
- O narrador NUNCA decide ações, falas, emoções ou intenções do personagem
  do jogador. Isso inclui micro-decisões ("você decide soltar seu qi",
  "você sente vontade de..."). Somente o jogador declara o que Mu-Jin faz,
  diz, pensa e sente.
- Quando o jogador escolhe uma opção (A/B/C), o narrador executa APENAS o que
  a opção descrevia — sem adicionar decisões extras do personagem. Se a
  execução exigir uma decisão não coberta pela opção, PAUSAR e perguntar.
- Falas do personagem: o narrador só coloca palavras na boca do PC se o
  jogador as escreveu, ou se a opção escolhida as descrevia explicitamente
  (e mesmo assim, mantendo-se fiel ao descrito).
- NPCs, mundo e consequências são do narrador; o corpo, a voz e a vontade
  do PC são exclusivamente do jogador.

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

### Sessão 3 — Capítulo 2: Um Ano de Treino / O Retorno do Cobrador (2026-07-24)
- **Salto temporal de 1 ano** (Mu-Jin: 6 → 7 anos). Downtime rolado:
  - **Train/Cultivo (Attune 2d): [6,6] = SUCESSO CRÍTICO** — dominou o método do cofre do clã, **Sopro da Andorinha Celeste**, e atingiu a **3ª camada de Condensação de Qi** em um ano (inaudito). Breakthrough clock 2/8.
  - **Train/Espada (Blitz 1d): [6] = SUCESSO PLENO** — fundamentos da **Espada da Andorinha Celeste** dominados; footwork já supera discípulos adolescentes.
  - Habilidade inicial do Ascendant definida: **Ímpeto do Ascendente** (push dá +1d E +1 efeito em ações do talento, 1x/cena).
  - **Fortuna/dinheiro da dívida (1d): [2] = RESULTADO RUIM** — ano cruel: colheitas taxadas, caravana da família materna saqueada, território arrendado perdido. **O clã NÃO tem o dinheiro.** Clock da dívida: ◼◼◼◼◼☐ (5/6).
- Situação atual: **Dokgo Hwan retornou** com comitiva armada da Seita do Punho de Ferro aos portões do Clã Yeon. Conselho reunido na véspera; mãe escreveu cartas à família mercante; Mu-Hyuk (13) quer lutar.
- Aguardando: como Mu-Jin age no dia da cobrança.
- **Declaração do jogador (postura de vida):** Mu-Jin passa os dias **treinando e vivendo bem, como gostaria de ter vivido na vida passada** — comendo bem, aproveitando a família, treinando por prazer e não por fuga. Isso expressa a crença central ("Viva de verdade") → **+1 XP** concedido (gatilho decidido pelo jogador, regra BoTI). A Deusa está satisfeita; a condição dela segue plenamente honrada — o talento continua florescendo.

### Sessão 4 — Capítulo 2: A Cobrança (2026-07-24)
- Mu-Jin decidiu **espiar a negociação** do telhado do pavilhão de hóspedes.
- **Action Roll (Mask 0d, pool zero): [5,6]→menor 5 = SUCESSO COM CONSEQUÊNCIAS.**
- O que ele ouviu: dívida = **8.000 taéis de prata** (principal + juros de 3 anos, vencendo hoje); o pai ofereceu a rota do rio (recusada com deboche); **a dívida é pretexto** — o Senhor Sectário do Punho de Ferro quer apenas uma coisa: *"Entreguem o menino da andorinha, e a dívida morre hoje."*
- NPC novo revelado: **Ancião Cheol** — cultivador do Punho de Ferro, qi de "represa fechada", MUITO acima do patriarca; veio pessoalmente por ordem do Senhor Sectário.
- **Consequência do 5:** Dokgo Hwan percebeu Mu-Jin no telhado e o expôs diante do pátio inteiro, convidando-o a descer. Todos olhando; o pai lívido.
- Aguardando: reação de Mu-Jin exposto no telhado.
- Mu-Jin **desceu e cruzou os braços**, encarando a comitiva. **Sway 1d: [1] = RUIM** → Ancião Cheol interpretou como insolência e liberou pressão de qi calibrada para dobrar os joelhos do menino diante do pátio (consequência: humilhação pública + condição "Abalado").
- Mu-Jin escolheu **responder** (Ímpeto do Ascendente: push 2 Stress → +1d/+1 efeito): **Attune 3d: [2,6,1] = SUCESSO PLENO (com efeito ampliado)** — meio joelho dobrou... e então o qi da 3ª camada explodiu de volta em espiral de andorinha. Mu-Jin ficou DE PÉ, braços cruzados, encarando Cheol. O pátio inteiro viu o menino de 7 anos aguentar a pressão de um Ancião do Punho de Ferro.
- Efeitos: lenda da Marca da Andorinha decuplicada; nível real de Mu-Jin parcialmente revelado à seita (3ª camada aos 7 anos — informação valiosíssima nas mãos de Dokgo Hwan); Cheol fechou a "represa" com um brilho de cobiça nos olhos; o pai chegou e se pôs entre Mu-Jin e a comitiva.
- Stress: 2/9. Situação: negociação em ponto de ruptura — a seita viu EXATAMENTE o que queria comprar.
- **Mu-Jin interveio na negociação:** pediu ao pai que perguntasse a oferta da seita, declarando que "dependendo, iria de bom grado".
- **Fortuna (reação do pai, 1d): [3] = RUIM** — Baek-San sentiu como traição/facada: o filho se oferecendo como mercadoria na frente do clã; reagiu com dor e fúria contida ("Yeon Mu-Jin, CALE-SE"), mas a fala do menino JÁ abriu a porta da negociação — impossível fechá-la.
- **Fortuna (qualidade da oferta, 2d): [2,1] = RUIM** — a seita, vendo interesse do próprio menino, LEU FRAQUEZA e baixou a oferta: Dokgo Hwan ofereceu apenas **perdão da dívida + 500 taéis "de cortesia"** — e a exigência humilhante de Mu-Jin como **discípulo EXTERNO** (servo com aulas, sem proteção de discípulo interno, sem direito a visitas por 5 anos). Oferta objetivamente insultante para um talento daquele nível.
- Situação aberta: o pai à beira de explodir; Cheol observando divertido; a oferta insultante na mesa; Mu-Jin decide como responder (aceitar, recusar, contra-ofertar, provocar...).

---

## 🏮 VIDA COTIDIANA NO CLÃ YEON (retrato aos 7 anos)

- **Mansão:** complexo no alto de colina na Província de Hanam; muros brancos gastos, telhados azuis com andorinhas reais; metade dos pavilhões fechada (clã reduzido a ~80 pessoas, já foram 300).
- **Pai (Yeon Baek-San):** orgulho incontido + medo silencioso de que o talento do filho atraia predadores; demonstra afeto corrigindo a postura da espada ("ajuste o cotovelo").
- **Mãe (Seo Hwa-Ryun):** administra as finanças de fato; sofre preconceito dos anciões por ser de família mercante; afeto prático (chá, pratos favoritos); é a ÚNICA que desconfia sutilmente de que Mu-Jin "tem gente demais atrás dos olhos" — nunca perguntou.
- **Irmão (Mu-Hyuk, 13):** herdeiro; talento mediano, esforço brutal; zero inveja — exibe o irmão com orgulho, invade o quarto dele à noite, chama-o de "Jin-ah". Quem mais o ama e menos desconfia.
- **Anciões:** tratam Mu-Jin como relíquia/bilhete de salvação (pressão não-dita crescente — ironia do pedido de "sem responsabilidades").
- **Criados:** o adoram; fofocam que ele "fala palavras estranhas dormindo" (português).
- **Velho Gok:** cozinheiro surdo de uma orelha; único que o trata como criança normal; rumores de um passado perigoso.
- **Rotina:** cultivo de manhã (sozinho), espada à tarde (com o pai quando possível), "hora livre" no fim da tarde, cultivo secreto à noite; visitas ocasionais da voz da Deusa no limiar do sono.

---

## 👥 NPCs CONHECIDOS

| Nome | Quem é | Relação com o personagem | Status |
|------|--------|--------------------------|--------|
| **A Deusa da Reencarnação** | Divindade belíssima e provocante; selou a barganha do renascimento | Patrona secreta; condição "Viva de verdade"; observa-o | Ativa (invisível ao mundo) |
| **Yeon Baek-San** | Patriarca do Clã Yeon, espadachim orgulhoso | Pai | Vivo |
| **Dama Seo Hwa-Ryun** | De família mercante; prática e afetuosa | Mãe | Viva |
| **Yeon Mu-Hyuk** | Herdeiro do clã; talento mediano, esforço enorme | Irmão mais velho (+6 anos) | Vivo |
| **Dokgo Hwan** | Emissário da Seita do Punho de Ferro (credora do Clã Yeon); frio, calculista | Testemunhou o talento de Mu-Jin no teste; percebeu-o espionando a cobrança | Ativo — no pátio do clã |
| **Ancião Cheol** | Cultivador poderoso do Punho de Ferro (qi de "represa fechada", muito acima do patriarca); executor do Senhor Sectário | Veio garantir a "cobrança" — ou seja, Mu-Jin | Ativo — no pátio do clã |

---

## 🗺️ LOCAIS VISITADOS

| Local | O que aconteceu lá | Pendências |
|-------|--------------------|------------|
| —     | —                  | —          |

---

## 🎯 MISSÕES / OBJETIVOS

| Objetivo | Status | Observações |
|----------|--------|-------------|
| **A Dívida do Clã Yeon** (Seita do Punho de Ferro) | Clock ◼◼◼◼◼☐ (5/6) | PRAZO VENCIDO — Dokgo Hwan está nos portões com comitiva armada; o clã não tem o dinheiro |
| Honrar a condição da Deusa ("Viva de verdade") | Contínuo | Crença central do personagem |

---

## 🔑 SEGREDOS, PISTAS E GANCHOS PENDENTES

- _(nenhum ainda)_

---

## ⏸️ ESTADO EXATO DE ONDE PARAMOS

> Esta seção deve SEMPRE descrever o momento exato da última cena,
> para retomar sem perder nada.

**Última cena:** Pátio, negociação aberta POR Mu-Jin (pediu ao pai que ouvisse a
oferta; disse que "dependendo, iria de bom grado"). Pai reagiu com dor/fúria
(fortuna [3]) mas a porta abriu. A seita leu fraqueza e fez oferta INSULTANTE
(fortuna [2,1]): perdão da dívida + 500 taéis + Mu-Jin como discípulo EXTERNO
(servo com aulas, sem visitas por 5 anos). Cheol se diverte; o pai está à beira
de explodir. Mu-Jin decide a resposta à oferta.
