# Estrutura Analítica do Projeto (WBS / EAP) — GovDesk

## GovDesk — MVP

* **1. Cadastro de Chamados**
  * **1.1** Acesso autenticado à plataforma e formulário de abertura de chamados na rota `/novo`
  * **1.2** Associação automática dos dados do usuário autenticado ao chamado e validação do campo obrigatório Título
  * **1.3** Seleção de prioridades no cadastro do chamado, com prioridade padrão "Média"
  * **1.4** Aviso explicativo sobre a LGPD no formulário de abertura de chamados

* **2. Acompanhamento e Gestão de Chamados**
  * **2.1** Exibição da lista de chamados com informações de identificação e acompanhamento, como ID, Título, Solicitante, Prioridade e Status
  * **2.2** Formatação visual dos status por meio de cores distintas para facilitar a identificação da situação dos chamados

* **3. Governança, Segurança e Infraestrutura**
  * **3.1** Versionamento e organização do Backlog e da EAP em `docs/`
  * **3.2** Elaboração e manutenção da Matriz RACI e do Template de Solicitação de Mudança em `docs/`
  * **3.3** Verificação de conformidade no tratamento de dados pessoais e prevenção do envio desnecessário de dados sensíveis
  * **3.4** Verificação do repositório e da esteira de integração no GitHub