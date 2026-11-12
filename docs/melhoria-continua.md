# Plano de Melhoria Contínua — GovDesk

## 1. Não conformidades

| ID | Achado | Requisito violado | Evidência | Gravidade |
|----|--------|-------------------|-----------|-----------|
| NC1 | A responsabilidade específica pela atividade de classificação de prioridade dos chamados ainda não está explicitada na Matriz RACI. | raci.md (cada atividade deve possuir um único "A" de Accountable) | A Matriz RACI apresenta responsáveis para as atividades gerais do projeto, mas não possui uma atividade específica de classificação de prioridade. | Média |
| NC2 | O formulário de abertura de chamados permite o preenchimento de descrições livres, sem validação específica para impedir o envio desnecessário de dados pessoais sensíveis. | lgpd.md / LGPD, princípios da Finalidade e da Necessidade | O campo de descrição permite a inserção de texto livre. Embora exista um aviso sobre a LGPD, não foram confirmadas validações adicionais para esse campo. | Alta |
| NC3 | Não há definição documentada de prazos de atendimento (SLA) para as etapas do ciclo de vida dos chamados. | Requisitos de atendimento e gestão de chamados | Os documentos disponíveis não apresentam prazos definidos para atendimento e resolução das solicitações. | Baixa |
| NC4 | Alguns critérios de aceite do backlog ainda precisam de validação técnica para garantir que as entregas estejam descritas de maneira verificável. | backlog.md / Padrão de definição de histórias | O backlog foi atualizado com critérios de aceite mais específicos, mas alguns itens ainda dependem da confirmação das funcionalidades e de seus respectivos resultados. | Baixa |
| NC5 | Os chamados são registrados com status inicial "aberto", sem atribuição automática de um técnico responsável pelo atendimento. | Processo de atendimento / Requisitos de gestão de chamados | O registro do chamado ocorre no sistema, mas não foi confirmada a existência de uma regra automática de distribuição ou atribuição de responsáveis. | Média |

## 2. Causa raiz (5 Porquês)

### NC2 (Coleta de dados sem controle específico na descrição)

1. **Por quê?** O usuário pode inserir informações pessoais sensíveis ou desnecessárias no campo de descrição do chamado.
2. **Por quê?** O formulário permite o preenchimento de texto livre e apresenta um aviso de privacidade, mas não possui validações específicas confirmadas para esse tipo de informação.
3. **Por quê?** O desenvolvimento inicial priorizou a disponibilização das funcionalidades essenciais de abertura e registro de chamados.
4. **Por quê?** O escopo inicial do MVP concentrou-se no funcionamento do cadastro, sem aprofundar os mecanismos automatizados de proteção de dados na entrada das informações.
5. **Causa raiz:** A necessidade de incorporar mecanismos adicionais de proteção de dados desde a entrada das informações não foi totalmente contemplada no escopo inicial do desenvolvimento.

### NC5 (Chamados abertos sem atribuição automática de responsável)

1. **Por quê?** Os chamados são registrados com status "aberto", sem um técnico automaticamente associado à solicitação.
2. **Por quê?** A implementação atual realiza o registro do chamado, mas não possui uma regra confirmada de distribuição automática por setor ou prioridade.
3. **Por quê?** O escopo inicial priorizou o cadastro e a consulta dos chamados, deixando a automação da distribuição para uma evolução futura.
4. **Por quê?** O MVP utiliza uma estrutura de armazenamento em memória e ainda não contempla todos os mecanismos necessários para uma gestão automatizada do atendimento.
5. **Causa raiz:** O escopo funcional inicial do GovDesk foi concentrado no registro e acompanhamento básico das solicitações, sem incluir a automação da atribuição de responsáveis.

## 3. BSC (Balanced Scorecard)

| Perspectiva | Objetivo | Indicador | Meta | Iniciativa | Dono |
|-------------|----------|-----------|------|------------|------|
| Financeira | Reduzir custos com retrabalho de suporte | Horas gastas refazendo chamados incorretos | Redução de 30% | Implementar melhorias na triagem e no preenchimento das solicitações | Eduarda Lima (PO) |
| Clientes | Garantir agilidade e satisfação no atendimento | % de chamados resolvidos dentro do prazo de SLA | ≥ 85% | Definir prazos de atendimento e acompanhar o cumprimento das metas | Nathalia Cappellini (QA) |
| Processos | Reduzir gargalos e chamados sem andamento | Quantidade de chamados parados por mais de 1 dia | 0 chamados | Implementar mecanismos de acompanhamento e alertas visuais | Cauê Mayo (Dev Lead) |
| Aprendizado | Capacitar a equipe em conformidade e segurança | Integrantes com treinamento em LGPD e governança | 100% da equipe | Realizar oficina interna de alinhamento sobre LGPD e governança | Vitor Lopes (DevOps/Sec) |

**Observação:** As metas e os indicadores apresentados são propostas para a evolução do GovDesk. Eles não representam resultados já alcançados ou métricas atualmente disponíveis no sistema.

## 4. Maturidade (0 a 5)

| Processo | Atual | Alvo | Evidência |
|----------|-------|------|-----------|
| Atendimento de chamados (Incidentes) | 2 | 3 | O sistema permite o registro e a consulta de chamados, mas ainda existem oportunidades de melhoria relacionadas à atribuição de responsáveis, aos prazos de atendimento e ao acompanhamento do processo. |
| Proteção de dados e privacidade (LGPD) | 1 | 3 | Há um aviso sobre o tratamento de dados pessoais no formulário de cadastro, mas ainda são necessárias avaliações e melhorias nos mecanismos de proteção, validação e controle das informações inseridas. |
| Gestão de mudanças (Change Management) | 1 | 2 | O template de solicitação de mudança (`template-mudanca.md`) está presente no repositório, mas ainda é necessário consolidar sua utilização e o registro das alterações realizadas no projeto. |

## 5. Plano 5W2H

| O quê | Por quê | Quem | Quando | Como | Custo | Tipo (QW/Projeto) | NC |
|-------|---------|------|--------|------|-------|-------------------|----|
| Refinar o aviso e avaliar validações adicionais de LGPD no formulário | Reduzir o envio desnecessário de dados pessoais e fortalecer a proteção das informações | Dev Lead / DevOps & Security | Fase 1 | Revisar o aviso de privacidade e avaliar mecanismos de validação no formulário e no registro dos chamados | R$ 0 | Quick Win (QW) | NC2 |
| Revisar a Matriz RACI para explicitar a responsabilidade pela classificação de prioridade | Garantir clareza na atribuição de responsabilidades durante o atendimento | PO | Fase 1 | Avaliar a inclusão da atividade de classificação de prioridade na matriz, definindo um único responsável Accountable | R$ 0 | Quick Win (QW) | NC1 |
| Definir prazos de atendimento para os chamados (SLA) | Estabelecer parâmetros para acompanhar o tempo de atendimento e resolução das solicitações | PO / QA | Fase 1 | Definir prazos por prioridade e documentar as regras de atendimento | R$ 0 | Quick Win (QW) | NC3 |
| Revisar e consolidar os critérios de aceite do backlog | Melhorar a rastreabilidade e permitir a verificação das funcionalidades entregues | QA | Fase 1 | Revisar os critérios de aceite em `docs/backlog.md`, verificando sua clareza e possibilidade de validação | R$ 0 | Quick Win (QW) | NC4 |
| Implementar armazenamento persistente em banco de dados relacional | Evitar a perda dos registros após a reinicialização da aplicação | Dev Lead | Fase 2 | Migrar a estrutura de armazenamento em memória para uma solução com banco de dados relacional, como SQLite e SQLAlchemy | R$ 0 | Projeto | NC5 |
| Desenvolver mecanismos de atribuição e distribuição de chamados | Organizar o fluxo de atendimento e facilitar a identificação dos responsáveis | Dev Lead | Fase 2 | Implementar regras de distribuição dos chamados conforme critérios definidos pela equipe de suporte | R$ 0 | Projeto | NC5 |
| Desenvolver uma página de indicadores de processo (`/indicadores`) | Permitir o acompanhamento dos prazos e do desempenho do atendimento | Dev Lead | Fase 2 | Criar uma rota e um template para apresentar indicadores de atendimento, após a definição dos dados necessários | R$ 0 | Projeto | NC3 |

## 6. Roadmap

* **Fase 1 (0–30 dias - Quick Wins):** Revisão das responsabilidades relacionadas à classificação de prioridade, aprimoramento das orientações de LGPD, definição dos prazos de atendimento e consolidação dos critérios de aceite do backlog.

* **Fase 2 (1–3 meses - Projetos Estruturantes):** Evolução da estrutura do sistema por meio da migração do armazenamento em memória para um banco de dados relacional, implementação de mecanismos de atribuição de responsáveis e desenvolvimento de indicadores de desempenho.

* **Fase 3 (3–6 meses - Otimização e Maturidade):** Avaliação contínua dos processos por meio do ciclo PDCA, aprimoramento dos controles de segurança e privacidade, evolução da maturidade dos processos e implementação de práticas de integração e entrega contínuas (CI/CD).