
# Melhoria Contínua

## 1. Identificação de Não Conformidades

A análise do GovDesk e de sua documentação permitiu identificar pontos que podem ser aprimorados para melhorar a organização dos processos, a segurança das informações e a gestão dos chamados.

| ID | Não Conformidade | Referência | Evidência / Justificativa | Prioridade |
|---|---|---|---|---|
| NC1 | A Matriz RACI não contempla uma atividade específica para definir a responsabilidade pela classificação da prioridade dos chamados de suporte. | `raci.md` / Clareza na definição de responsabilidades | A matriz apresenta responsabilidades relacionadas à priorização do backlog do projeto, mas não estabelece quem deve ser responsável pela classificação da prioridade dos chamados registrados no GovDesk. | Média |
| NC2 | O formulário de abertura de chamados permite o preenchimento de informações em texto livre, sem orientações específicas para evitar o envio de dados pessoais desnecessários. | Documentação LGPD / Princípios da finalidade e necessidade | Embora exista um aviso relacionado à proteção de dados, podem ser incluídas orientações mais claras para evitar o compartilhamento de informações pessoais que não sejam necessárias para o atendimento. | Alta |
| NC3 | Não há níveis de serviço (SLA) formalmente definidos para o atendimento e a resolução dos chamados. | PETI / Gestão de serviços de TI | O sistema permite acompanhar os chamados e seus status, mas ainda não possui prazos de atendimento e resolução estabelecidos para cada nível de prioridade. | Média |
| NC4 | Alguns critérios de aceitação do backlog precisam ser detalhados para permitir uma validação mais objetiva das funcionalidades. | `backlog.md` / Critérios de aceitação | Critérios pouco específicos podem dificultar a verificação de que uma funcionalidade foi implementada corretamente e atende ao resultado esperado. | Baixa |
| NC5 | O sistema não possui um mecanismo automático de atribuição dos chamados aos responsáveis pelo atendimento. | Processo de chamados / Fluxo de atendimento | Os chamados são registrados e armazenados no banco de dados SQLite, mas ainda não existe uma regra de distribuição ou atribuição automática para os responsáveis pelo suporte. | Média |

## 2. Análise de Causa Raiz — 5 Porquês

A técnica dos 5 Porquês foi utilizada para investigar as causas de duas não conformidades identificadas durante a análise.

### NC2 — Ausência de orientações específicas para evitar o envio de dados pessoais desnecessários

| Pergunta | Resposta |
|---|---|
| 1. Por que o formulário pode receber informações pessoais desnecessárias? | Porque o campo de descrição permite que o usuário escreva livremente as informações que considerar relevantes. |
| 2. Por que o campo permite esse tipo de preenchimento? | Porque não existem orientações específicas próximas ao campo indicando quais informações devem ou não ser compartilhadas. |
| 3. Por que essas orientações não foram incluídas? | Porque o desenvolvimento inicial priorizou as funcionalidades essenciais de abertura e consulta dos chamados. |
| 4. Por que a proteção de dados não foi detalhada nessa etapa? | Porque os cuidados com a privacidade foram considerados de forma geral, sem detalhar todas as orientações necessárias para o preenchimento do formulário. |
| 5. Qual é a causa raiz? | A necessidade de detalhar melhor as medidas de orientação e prevenção relacionadas ao tratamento de dados pessoais no formulário de abertura de chamados. |

**Causa raiz identificada:** necessidade de aprimorar as orientações de privacidade e os cuidados relacionados ao preenchimento dos campos de texto livre.

### NC5 — Ausência de atribuição automática dos chamados

| Pergunta | Resposta |
|---|---|
| 1. Por que os chamados não são atribuídos automaticamente? | Porque o sistema ainda não possui uma funcionalidade de distribuição ou atribuição de chamados. |
| 2. Por que essa funcionalidade não existe? | Porque não foi implementada uma regra para direcionar os chamados aos responsáveis pelo atendimento. |
| 3. Por que essa regra não foi implementada? | Porque o desenvolvimento inicial priorizou o cadastro, a consulta e o acompanhamento dos chamados. |
| 4. Por que a atribuição não foi incluída no escopo inicial? | Porque a distribuição dos chamados foi considerada uma melhoria posterior, não sendo definida como requisito essencial para a primeira versão. |
| 5. Qual é a causa raiz? | O escopo inicial do projeto não contemplou a implementação de um mecanismo de atribuição e distribuição dos chamados. |

**Causa raiz identificada:** ausência de um requisito específico para a atribuição dos chamados aos responsáveis pelo atendimento durante a definição do escopo inicial.

## 3. Indicadores Estratégicos — BSC

O Balanced Scorecard (BSC) é utilizado para acompanhar objetivos estratégicos a partir de diferentes perspectivas. Para o GovDesk, foram definidos indicadores e metas que poderão orientar futuras melhorias na gestão dos serviços de TI.

| Perspectiva | Objetivo Estratégico | Indicador | Meta Proposta | Iniciativa | Responsável |
|---|---|---|---|---|---|
| Financeira | Reduzir custos relacionados ao retrabalho no atendimento de chamados. | Horas gastas com correções e retrabalho. | Reduzir em 30% o tempo de retrabalho. | Melhorar o formulário de abertura e o processo de triagem dos chamados. | Eduarda |
| Clientes | Melhorar a satisfação dos usuários com o atendimento de TI. | Percentual de chamados resolvidos dentro do SLA. | Atingir 85% de chamados resolvidos dentro do prazo estabelecido. | Definir níveis de serviço e acompanhar os prazos de atendimento. | Nathalia |
| Processos Internos | Melhorar o acompanhamento e a continuidade do atendimento. | Quantidade de chamados sem atualização por mais de um dia. | Reduzir a zero os chamados sem atualização por mais de um dia. | Implementar mecanismos de acompanhamento e alertas de chamados parados. | Cauê |
| Aprendizado e Crescimento | Desenvolver o conhecimento da equipe sobre governança e proteção de dados. | Percentual da equipe capacitada em LGPD e governança de TI. | Capacitar 100% dos integrantes da equipe. | Realizar treinamentos e compartilhar orientações sobre boas práticas. | Vitor |

**Observação:** os indicadores, valores e metas apresentados são propostas para futuras etapas de evolução do projeto. Eles não representam resultados já alcançados pelo GovDesk. A página `/indicadores` existente no sistema apresenta informações sobre os chamados registrados, como total, chamados abertos e chamados resolvidos. Os indicadores estratégicos do BSC possuem uma finalidade mais ampla e poderão ser acompanhados conforme novas funcionalidades forem implementadas.

## 4. Avaliação de Maturidade

A avaliação de maturidade permite identificar o nível de organização dos processos relacionados ao GovDesk e apontar oportunidades de evolução.

Foi adotada uma escala de 0 a 5:

| Nível | Classificação | Descrição |
|---|---|---|
| 0 | Inexistente | Não há processo ou prática estabelecida. |
| 1 | Inicial | Existem ações pontuais, mas sem padronização. |
| 2 | Parcialmente definido | Existem práticas implementadas, mas ainda há lacunas na organização. |
| 3 | Definido e documentado | Os processos estão documentados e possuem responsabilidades estabelecidas. |
| 4 | Monitorado e controlado | Os processos são acompanhados por indicadores e mecanismos de controle. |
| 5 | Otimizado | Os processos são avaliados continuamente e aprimorados com base nos resultados. |

### Situação atual e nível desejado

| Processo Avaliado | Nível Atual | Nível Desejado | Justificativa |
|---|---:|---:|---|
| Gestão de chamados | 2 | 3 | O sistema permite registrar, consultar e acompanhar chamados, mas ainda precisa de melhorias no fluxo de atendimento e na definição de responsabilidades operacionais. |
| Proteção de dados e LGPD | 1 | 3 | Existem cuidados iniciais relacionados à privacidade, mas as orientações e medidas de prevenção podem ser aprimoradas e documentadas. |
| Gestão de mudanças | 1 | 2 | Existem responsabilidades relacionadas à aprovação de mudanças no projeto, mas o processo ainda pode ser mais detalhado e padronizado. |

**Observação:** os níveis apresentados representam uma avaliação inicial dos processos e práticas identificados no projeto. Os níveis desejados indicam objetivos de evolução, não resultados já alcançados. A avaliação considera a organização dos processos e da documentação, não apenas as funcionalidades técnicas do sistema.

## 5. Plano de Ação — 5W2H

O plano de ação apresenta as atividades propostas para tratar as não conformidades identificadas e melhorar os processos relacionados ao GovDesk.

| O quê? (What) | Por quê? (Why) | Onde? (Where) | Quando? (When) | Quem? (Who) | Como? (How) | Quanto? (How much) |
|---|---|---|---|---|---|---|
| Revisar as orientações de privacidade do formulário. | Reduzir o envio de dados pessoais desnecessários. | Formulário de abertura de chamados e documentação LGPD. | Próxima etapa de melhoria. | Vitor e Nathalia. | Revisar o aviso de privacidade e incluir orientações claras sobre o preenchimento da descrição. | Sem custo adicional previsto. |
| Revisar a Matriz RACI para avaliar a necessidade de detalhar responsabilidades relacionadas à classificação da prioridade dos chamados. | Melhorar a clareza das responsabilidades no processo de atendimento. | Documentação do projeto e processo de chamados. | Próxima revisão documental. | Eduarda e Nathalia. | Avaliar a lacuna identificada e registrar a responsabilidade adequada no processo correspondente, sem confundir as atividades operacionais com as responsabilidades do grupo no projeto. | Sem custo adicional previsto. |
| Definir níveis de serviço (SLA). | Estabelecer prazos para atendimento e resolução dos chamados. | Documentação de gestão de serviços de TI. | Próxima etapa de planejamento. | Eduarda e Nathalia. | Definir prazos de atendimento e resolução considerando a prioridade dos chamados. | Sem custo adicional previsto. |
| Revisar os critérios de aceitação do backlog. | Tornar a validação das funcionalidades mais objetiva. | `backlog.md`. | Próxima revisão do backlog. | Cauê e Nathalia. | Reescrever os critérios de forma clara, verificável e alinhada ao comportamento esperado do sistema. | Sem custo adicional previsto. |
| Implementar um mecanismo de atribuição dos chamados. | Organizar a distribuição das solicitações entre os responsáveis pelo suporte. | Sistema GovDesk. | Evolução futura do sistema. | Cauê e Vitor. | Desenvolver uma funcionalidade que permita atribuir chamados aos responsáveis pelo atendimento. | Depende do esforço de desenvolvimento. |
| Aprimorar a página de indicadores existente. | Ampliar o acompanhamento dos chamados e permitir a análise dos prazos de atendimento. | Página `/indicadores`. | Após a definição dos SLAs. | Cauê e Nathalia. | Evoluir os indicadores atuais para incluir informações sobre prazos, tempo de atendimento e cumprimento dos SLAs. | Depende do esforço de desenvolvimento. |

## 6. Roadmap de Melhorias

O roadmap organiza as melhorias propostas em etapas, considerando as necessidades identificadas durante a análise do projeto.

### Fase 1 — Organização e documentação

- Revisar a Matriz RACI e avaliar a documentação das responsabilidades relacionadas ao processo de atendimento.
- Aprimorar as orientações de privacidade e proteção de dados no formulário de abertura de chamados.
- Definir níveis de serviço (SLA) para o atendimento e a resolução dos chamados.
- Revisar os critérios de aceitação do backlog para facilitar a validação das funcionalidades.

### Fase 2 — Evolução das funcionalidades

- Implementar um mecanismo de atribuição e distribuição dos chamados aos responsáveis pelo atendimento.
- Aprimorar a página `/indicadores`, incluindo informações sobre tempo de atendimento e cumprimento dos SLAs.
- Melhorar o acompanhamento dos chamados sem atualização.
- Avaliar melhorias no fluxo de atendimento e na organização das solicitações.

### Fase 3 — Governança e aprimoramento contínuo

- Fortalecer as práticas de segurança da informação e proteção de dados.
- Acompanhar os indicadores estratégicos definidos no BSC.
- Reavaliar periodicamente os níveis de maturidade dos processos.
- Aplicar o ciclo PDCA (Planejar, Executar, Verificar e Agir) para orientar as melhorias contínuas.
- Evoluir as práticas de integração e entrega contínua (CI/CD), conforme a necessidade do projeto.

## 7. Considerações Finais

A análise de melhoria contínua permitiu identificar oportunidades de evolução no GovDesk, tanto em relação às funcionalidades do sistema quanto à organização dos processos e da documentação do projeto.

As não conformidades identificadas demonstram a importância de estabelecer responsabilidades claras, aprimorar os cuidados com a proteção de dados, definir níveis de serviço e melhorar os mecanismos de acompanhamento dos chamados.

As ações propostas no plano 5W2H e no roadmap servem como direcionamento para futuras etapas de desenvolvimento e organização. Dessa forma, o GovDesk poderá evoluir de maneira estruturada, contribuindo para uma gestão mais eficiente dos serviços de suporte de TI.