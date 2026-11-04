# Plano de Melhoria Contínua — GovDesk

## 1. Não conformidades
| ID | Achado | Requisito violado | Evidência | Gravidade |
|----|--------|-------------------|-----------|-----------|
| NC1 | Atividade “Classificar prioridade” sem um único “A” claro ou responsabilidade ambígua no fluxo inicial | raci.md (cada atividade deve possuir um único “A” de Accountable) | Linha de atribuição do processo de triagem inicial | Média |
| NC2 | Formulário de abertura de chamados coleta descrições livres sem validação explícita de dados pessoais excessivos | lgpd.md / LGPD Art. 6º (Princípio da Finalidade e Minimização) | Campo de descrição aberto no `novo.html` sem restrição de LGPD mais rígida | Alta |
| NC3 | Etapas de encerramento de chamados no processo BPMN / fluxo operacional sem prazos de SLA definidos | processo-chamados.md / Requisitos de atendimento | Tabela de transição de status sem coluna de tempo limite (SLA) | Baixa |
| NC4 | Histórias do backlog inicial sem o detalhamento completo de alguns critérios de aceite técnicos | backlog.md / Padrão de definição de histórias | Itens iniciais com verificação genérica de sistema | Baixa |
| NC5 | Chamados abertos no sistema ficam sem triagem automática ou atribuição imediata de técnico responsável | Processo TO-BE / Requisitos de Gestão de Incidentes (ITIL) | Sistema grava com status "aberto" mas não direciona para um responsável na criação | Média |

## 2. Causa raiz (5 Porquês)

### NC2 (Coleta de dados sem controle rigoroso de finalidade na descrição)
1. **Por quê?** O usuário pode digitar qualquer informação sensível no campo de texto livre.
2. **Por quê?** O formulário possui apenas um aviso textual simples de privacidade, mas nenhuma validação ou máscara.
3. **Por quê?** O projeto focou inicialmente apenas no MVP funcional de cadastro sem travas de sanitização avançadas.
4. **Por quê?** O escopo inicial da Sprint 1 priorizou a entrega rápida da rota `/novo` em Flask sem backend relacional complexo.
5. **Causa raiz:** Ausência de diretrizes automatizadas de LGPD na camada de entrada de dados e falta de treinamento focado em privacy-by-design para os desenvolvedores na fase de modelagem inicial.

### NC5 (Chamados abertos ficam sem triagem automática ou responsável)
1. **Por quê?** Os chamados entram no sistema com status "aberto" sem um dono definido.
2. **Por quê?** O código atual (`app.py`) apenas insere o registro na lista em memória sem regra de atribuição por setor ou prioridade.
3. **Por quê?** A matriz RACI define responsabilidades gerais, mas o sistema não automatiza o encadeamento do papel "Accountable" para o atendimento.
4. **Por quê?** O protótipo utiliza uma estrutura baseada em listas Python em memória, sem persistência relacional robusta (como SQLite/SQLAlchemy).
5. **Causa raiz:** Desalinhamento temporário entre a governança teórica dos papéis (RACI) e a implementação lógica restrita do MVP na camada de software.

## 3. BSC (Balanced Scorecard)
| Perspectiva | Objetivo | Indicador | Meta | Iniciativa | Dono |
|-------------|----------|-----------|------|------------|------|
| Financeira  | Reduzir custos com retrabalho de suporte | Horas gastas refazendo chamados incorretos | Redução de 30% | Implementar triagem rigorosa na abertura | Eduarda Lima (PO) |
| Clientes    | Garantir agilidade e satisfação no atendimento | % de chamados resolvidos no prazo de SLA | $\geq 85\%$ | Automatizar prioridades e prazos no sistema | Nathalia Cappellini (QA) |
| Processos   | Eliminar gargalos e chamados parados | Quantidade de chamados parados $> 1$ dia | 0 chamados | Criar botão "Avançar" e alertas visuais | Cauê Mayo (Dev Lead) |
| Aprendizado | Capacitar a equipe em conformidade e segurança | Integrantes com treinamento em LGPD e governança | 100% da equipe | Realizar oficina interna de alinhamento | Vitor Lopes (DevOps/Sec) |

## 4. Maturidade (0 a 5)
| Processo | Atual | Alvo | Evidência |
|----------|-------|------|-----------|
| Atendimento de chamados (Incidentes) | 2 | 3 | O fluxo repete-se corretamente pelo sistema Flask, mas carece de automação de prazos e relatórios de SLA. |
| Proteção de dados e privacidade (LGPD) | 1 | 3 | Há um aviso textual básico na tela de cadastro, mas faltam logs de auditoria e termo de consentimento explícito. |
| Gestão de mudanças (Change Management) | 1 | 2 | O template de solicitação de mudança (`template-mudanca.md`) existe no repositório, porém o uso ainda é esporádico. |

## 5. Plano 5W2H
| O quê | Por quê | Quem | Quando | Como | Custo | Tipo (QW/Projeto) | NC |
|-------|---------|------|--------|------|-------|-------------------|----|
| Refinar aviso e validação de LGPD no formulário | Atender rigorosamente à LGPD e mitigar riscos | Dev Lead | Fase 1 (Sprint 3) | Atualizar `novo.html` e validações no `app.py` | R$ 0 | Quick Win (QW) | NC2 |
| Revisar e consolidar os papéis "A" no RACI | Garantir responsabilização clara das tarefas | PO | Fase 1 (Sprint 3) | Atualizar o arquivo `docs/raci.md` | R$ 0 | Quick Win (QW) | NC1 |
| Implementar o banco de dados relacional (SQLite/SQLAlchemy) | Evitar perda de dados ao reiniciar o app | Dev Lead | Fase 2 | Migrar estruturas em memória para ORM | R$ 0 | Projeto | NC5 |
| Desenvolver a página de indicadores de processo (`/indicadores`) | Medir prazos e desempenho em tempo real | Dev Lead | Fase 2 | Criar rota e template de indicadores (bônus) | R$ 0 | Projeto | NC5 |
| Realizar auditoria completa de critérios de aceite no backlog | Padronizar a rastreabilidade das entregas | QA | Fase 1 (Sprint 3) | Revisar e atualizar `docs/backlog.md` | R$ 0 | Quick Win (QW) | NC4 |

## 6. Roadmap
* **Fase 1 (0–30 dias - Quick Wins):** Correção das não conformidades críticas e médias identificadas na auditoria (ajustes no RACI, refinamento do aviso LGPD e padronização dos critérios do backlog). Execução imediata alinhada à Sprint 3.
* **Fase 2 (1–3 meses - Projetos Estruturantes):** Migração do armazenamento em memória para banco de dados relacional (SQLite/SQLAlchemy), implementação de perfis de acesso e desenvolvimento da página de indicadores de desempenho (`/indicadores`).
* **Fase 3 (3–6 meses - Otimização e Maturidade):** Avaliação de ciclo completo do PDCA, subida de nível nos processos de maturidade (alcançando o nível 3 consolidado) e integração contínua avançada (CI/CD).