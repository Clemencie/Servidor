# Servidor — Mesa de RPG

Estrutura da campanha:

| Arquivo | Função |
|---------|--------|
| `rolador.py` | Rolador de dados 100% aleatório (módulo `secrets`, sem seed, sem manipulação). Uso: `python3 rolador.py 1d20+3` |
| `rolagens_log.jsonl` | Log de auditoria automático de todas as rolagens (data/hora, dados, total). |
| `BACKUP_CAMPANHA.md` | Backup completo da história — copie para outra conversa se o limite for atingido. |
| `FICHA_PERSONAGEM.md` | Ficha detalhada e permanente do personagem, com histórico de alterações. |
