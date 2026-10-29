# Estrutura Analítica do Projeto (WBS / EAP) — GovDesk

## GovDesk — MVP

* **1. Cadastro de Chamados**
  * **1.1** Formulário de abertura de chamados na rota `/novo`
  * **1.2** Validação de campos obrigatórios e tratamento de erros
  * **1.3** Seleção de prioridades no cadastro do chamado
  * **1.4** Aviso explicativo da LGPD no formulário

* **2. Acompanhamento e Gestão de Chamados**
  * **2.1** Exibição da lista de chamados com as colunas ID, Título, Solicitante, Prioridade e Status
  * **2.2** Formatação visual de status coloridos

* **3. Governança, Segurança e Infraestrutura**
  * **3.1** Versionamento de Backlog e EAP em `docs/`
  * **3.2** Matriz RACI e Políticas de Mudança em `docs/`
  * **3.3** Verificação de conformidade de dados sensíveis
  * **3.4** Validação do repositório e esteira no GitHub

* **4. Autenticação e Gestão de Usuários**
  * **4.1** Cadastro de usuário (solicitante) na rota  `/cadastro`, com nome, e-mail, CPF, telefone (opcional) e senha
  * **4.2** Validação do cadastro: campos obrigatórios, confirmação de senha, mínimo de 8 caracteres e bloqueio de e-mail ou CPF já cadastrados
  * **4.3** Armazenamento seguro da senha com hash (Werkzeug)
  * **4.4** Login na rota /login e logout na rota /logout, com controle de sessão
  * **4.5** Proteção da rota /novo: somente usuário autenticado abre chamado, e o solicitante é identificado pela sessão