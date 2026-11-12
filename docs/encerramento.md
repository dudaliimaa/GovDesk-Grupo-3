# Termo de Encerramento — GovDesk

## Escopo

**Planejado:**
Desenvolvimento de uma aplicação web em Python com Flask para a gestão de chamados de suporte técnico de TI (GovDesk), integrada a um conjunto completo de artefatos de Governança de TI ao longo de 10 semanas (PETI, conformidade LGPD, matriz RACI, template de solicitação de mudança, código de conduta, backlog de histórias de usuário, estrutura WBS, modelagem de processos em BPMN e plano de melhoria contínua com Balanced Scorecard e 5W2H).

**Entregue:**
- **Sistema Funcional (Flask):** Aplicação operacional com rotas em `app.py` para listagem de chamados, formulário de abertura com aviso de privacidade LGPD, avanço de status de chamados (Aberto, Em Andamento, Resolvido) e banco de dados provisório (`database.db`).
- **Documentação de Governança (`docs/`):**
  - `docs/peti.md`: Plano Estratégico de TI alinhando objetivos de negócio e tecnologia.
  - `docs/lgpd.md`: Mapeamento de dados pessoais, finalidades, bases legais e tratamento de dados sensíveis.
  - `docs/raci.md`: Matriz de responsabilidades garantindo 1 único *Accountable* (A) por atividade.
  - `docs/template-mudanca.md`: Formulário padronizado para controle e aprovação de alterações de escopo.
  - `docs/backlog.md` e `docs/wbs.md`: Decomposição do trabalho e histórias com critérios de aceite.
  - `docs/processo-chamados.md`: Fluxo de atendimento TO-BE modelado em BPMN com raias coerentes com a RACI.
  - `docs/melhoria-continua.md`: Auditoria de não conformidades, 5 Porquês, Balanced Scorecard (BSC) em 4 perspectivas, avaliação de maturidade (0 a 5), plano 5W2H e roadmap em 3 fases.
  - `docs/encerramento.md` e `docs/licoes-aprendidas.md`: Encerramento formal do projeto e lições aprendidas da equipe.


## Resultados e indicadores

- **Cobertura de Governança:** 100% dos artefatos documentais previstos na ementa da disciplina ITI004 entregues e vinculados ao repositório GitHub.
- **Rastreabilidade dos Chamados:** Transição do suporte de TI de "sem controle" para 100% dos chamados registrados e monitorados por ID e status.
- **Conformidade com a LGPD:** 100% dos formulários com aviso visível aos usuários e finalidade descrita para todos os dados coletados.
- **Clareza de Papéis (RACI x BPMN):** Eliminação de ambiguidades operacionais com a definição de responsabilidade única (*Accountable*) para cada tarefa do projeto.
- **Metas do BSC:** Definição de metas estratégicas para tempo de atendimento (SLA ≥ 85%), redução de retrabalho (-30%) e capacitação em proteção de dados (100% da equipe).


## Pendências e riscos residuais

| Item | Impacto | Plano |
|------|---------|-------|
| **Persistência em Banco Relacional Definitivo** | Médio | Migração do banco provisório (`database.db`) para SQLite com SQLAlchemy/PostgreSQL agendada para a Fase 2 do Roadmap (1–3 meses). |
| **Autenticação e Perfis de Acesso (RBAC)** | Médio | Implementação de níveis de acesso (Solicitante, Atendente, Administrador) alocada para a Fase 2 do Roadmap (1–3 meses). |
| **Notificações Automáticas de SLA** | Baixo | Automação do envio de e-mails/webhooks para alertas de vencimento de prazo alocada para a Fase 3 do Roadmap (3–6 meses). |


## Sustentação

**Dono do sistema:** Product Owner / CIO — Eduarda de Lima Sales  
**Suporte:** Dev Lead — Cauê Mayo Simões (Manutenção do Código) & DevOps — Vitor Lopes Ribeiro (Infraestrutura e Segurança)  
**Aprovador de mudanças:** Product Owner / CIO — Eduarda de Lima Sales (conforme fluxo do `docs/template-mudanca.md`)  


## Aceite

**Product Owner:** Eduarda de Lima Sales  
**Data:** 12 de Novembro de 2026  
