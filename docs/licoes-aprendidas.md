# Lições Aprendidas — GovDesk

| # | Situação | Causa | Ação Recomendada | Responsável |
|---|---|---|---|---|
| **1** | Retrabalho na especificação e desenvolvimento de protótipos | Histórias de usuário criadas no backlog sem critérios de aceite claros | Exigir critérios de aceite formalizados antes de puxar para a sprint | Eduarda Sales (PO) |
| **2** | Divergência entre a matriz RACI e os papéis definidos no BPMN | Documentos de governança atualizados de forma isolada em momentos diferentes | Realizar revisão cruzada e checklist de auditoria (QA) a cada entrega de documento | Nathalia Cappellini (QA) |
| **3** | Dificuldades no tratamento de dados nulos no cadastro de chamados | Falta de validações preventivas no backend Flask antes da gravação | Implementar validações rigorosas de formulário e mensagens amigáveis de erro no frontend | Cauê Mayo (Dev Lead) |
| **4** | Sobrecarga e acúmulo de tarefas de documentação na véspera das entregas | Falta de alinhamento síncrono intermediário durante a semana acadêmica | Estabelecer marcos semanais com congelamento de commits 24 horas antes do prazo final | Grupo 3 (Todos) |

## O que funcionou

- **Comunicação Transparente e Uso do Board Kanban:** A organização do Trello permitiu que todos acompanhassem o progresso das tarefas das semanas 1 a 10 de forma clara.
- **Definição Clara de Responsabilidades (RACI):** Saber exatamente quem era a pessoa Accountable por cada entrega evitou conflitos e tomadas de decisão ambíguas.
- **Stack Tecnológico Leve e Ágil:** A escolha de Python com Flask permitiu colocar o esqueleto do sistema no ar na Semana 1 e evoluir a aplicação rapidamente sem complexidade excessiva de infraestrutura.
- **Colaboração Interdisciplinar:** Integração fluida entre visões de negócio (PO), técnica (Dev), auditoria (QA) e infraestrutura (DevOps).

## O que não funcionou

- **Atualização Descentralizada de Documentos:** Criar e atualizar arquivos Markdown em momentos distintos gerou descompassos temporários entre o BPMN, o backlog e a RACI.
- **Excesso de Tarefas na Reta Final das Sprints:** O acúmulo de refinamentos na documentação próximo aos horários de aula gerou pico de pressão na equipe.
- **Falta de Critérios de Aceite Detalhados no Início:** Histórias de usuário simplificadas causaram ambiguidades temporárias no desenvolvimento do protótipo da Semana 6.

## O que mudaríamos

- **Automação de Checklists de QA:** Implementar pipelines CI/CD com linters e testes automatizados para validar links, tabelas e código Flask a cada pull request.
- **Reuniões Curtas de Sincronização (Daily/Sync):** Adotar encontros rápidos de 10 minutos no meio da semana para alinhar preventivamente documentação e código.
- **Auditoria Contínua de LGPD e RACI:** Realizar verificações de conformidade a cada nova rota ou campo de banco de dados adicionado, em vez de auditar apenas ao final das semanas de entrega.
