# GovDesk — Sistema de Gestão de Chamados de Suporte de TI

O **GovDesk** é uma aplicação web desenvolvida em Python com Flask para a gestão e acompanhamento de chamados de suporte técnico de TI. O projeto foi construído como parte da disciplina **Gestão e Governança de TI (ITI004)**, ministrada pelo **Prof. Vagner Macedo**, com o objetivo de demonstrar como evoluir o suporte de TI de uma situação sem controle para um ambiente estruturado, transparente e alinhado aos princípios e frameworks de Governança de TI.

---

## 👥 Equipe e Papéis (Grupo 3)

| Integrante | Papel | Responsabilidade Principal |
| :--- | :--- | :--- |
| **Eduarda de Lima Sales** | Product Owner / CIO | Alinhamento estratégico, priorização do backlog de negócios e aceite de entregas. |
| **Cauê Mayo Simões** | Dev Lead | Arquitetura da aplicação Flask, estruturação de rotas e estabilidade do código. |
| **Nathalia Cappellini Pereira** | QA / Auditoria | Testes funcionais, conformidade documental (RACI/LGPD) e verificação de qualidade. |
| **Vitor Lopes Ribeiro** | DevOps & Security Analyst | Infraestrutura, ambiente de execução, segurança e boas práticas de implantação. |

---

## 📌 Status do Projeto

- [x] **Semana 1** — Setup inicial, esqueleto Flask no ar e definição de papéis
- [x] **Semana 2** — PETI do projeto (`docs/peti.md`)
- [x] **Semana 3** — Checklist LGPD e proteção de dados (`docs/lgpd.md`)
- [x] **Semana 4** — Matriz RACI + Template de Mudança (`docs/raci.md` e `docs/template-mudanca.md`)
- [x] **Semana 5** — Código de Conduta do time (`docs/codigo-conduta.md`)
- [x] **Semana 6** — Backlog no board + WBS e critérios de aceite (`docs/backlog.md` e `docs/wbs.md`)
- [ ] **Semana 7 e 8** — Fluxo BPMN TO-BE implementado
- [x] **Semana 9** — Plano de Melhoria Contínua, BSC, Maturidade e 5W2H (`docs/melhoria-continua.md`)
- [x] **Semana 10** — Termo de Encerramento, Lições Aprendidas e Apresentação Final (`docs/encerramento.md`)

---

## 🚀 Como Executar a Aplicação

### Pré-requisitos

- Python 3.8 ou superior instalado.
- Gerenciador de pacotes `pip`.

### Passo a Passo

1. **Clonar o repositório:**
   ```bash
   git clone https://github.com/dudaliimaa/GovDesk-Grupo-3.git
   cd GovDesk-Grupo-3
   ```
   
2. **Instalar as dependências:**
   ```bash
   pip install -r requirements.txt
   ```
   
3. **Executar a aplicação:**
   ```bash
   python app.py
   ```
   
4. **Acessar o sistema:**
   Abra o navegador e acesse o endereço exibido no terminal (por padrão http://192.168.1.9:8080).

---

## 🔗 Links do Projeto

- 📋 Board Kanban (Trello): [Acessar Trello do Projeto](https://trello.com/invite/b/6a90c400cfe2d0146ed82934/ATTI386a7fb701f0faed9693b66535f186c933C1B3F8/projeto-govdesk-sala-3)
- 🎨 Protótipo Interativo (Figma): [Acessar Protótipo no Figma](https://www.figma.com/proto/BCqQVfeHlm0Xj0RXUsJeIv/Prot%C3%B3tipo-GovDesk---Grupo-3?node-id=3-3342&p=f&t=kyIA5N1eXUvbA889-1&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=3%3A3342)

---

## 📚 Documentação de Governança (`docs/`)

O projeto GovDesk possui um arcabouço completo de governança estruturado ao longo de 10 semanas de desenvolvimento:

| Semana | Artefato | Descrição | Link do Documento |
| :---: | :--- | :--- | :--- |
| **Semana 1** | Setup & Esqueleto Flask | Estrutura inicial do projeto, rotas base e definição de papéis no README | [`app.py`](./app.py) |
| **Semana 2** | PETI | Plano Estratégico de TI (objetivos de negócio, TI e indicadores de sucesso) | [`docs/peti.md`](./docs/peti.md) |
| **Semana 3** | Conformidade LGPD | Mapeamento de dados pessoais, bases legais, retenção e riscos de dados sensíveis | [`docs/lgpd.md`](./docs/lgpd.md) |
| **Semana 4** | RACI & Mudanças | Matriz de responsabilidades e formulário de solicitação de mudança | [`docs/raci.md`](./docs/raci.md) / [`docs/template-mudanca.md`](./docs/template-mudanca.md) |
| **Semana 5** | Código de Conduta | Diretrizes éticas e combinados de trabalho em equipe | [`docs/codigo-conduta.md`](./docs/codigo-conduta.md) |
| **Semana 6** | Backlog & WBS | Decomposição do trabalho, histórias de usuário e critérios de aceite | [`docs/backlog.md`](./docs/backlog.md) / [`docs/wbs.md`](./docs/wbs.md) |
| **Semana 7/8** | Processo BPMN | - | - |
| **Semana 9** | Melhoria Contínua & BSC | Auditoria de não conformidades, 5 Porquês, Balanced Scorecard e plano 5W2H | [`docs/melhoria-continua.md`](./docs/melhoria-continua.md) |
| **Semana 10** | Encerramento & Lições | Termo de encerramento formal do projeto e lições aprendidas da equipe | [`docs/encerramento.md`](./docs/encerramento.md) / [`docs/licoes-aprendidas.md`](./docs/licoes-aprendidas.md) |

---

## 🔮 Backlog Futuro e Roadmap de Evolução

As melhorias futuras do GovDesk estão organizadas em 3 fases estruturantes:

- **Fase 1 (0–30 dias - Quick Wins):** Correção de divergências documentais, inclusão de validações estritas no formulário e alertas visuais de SLA.
- **Fase 2 (1–3 meses - Projetos Estruturantes):** Migração para banco de dados relacional SQLite/PostgreSQL com SQLAlchemy e controle de acesso baseado em perfis (RBAC: Solicitante, Atendente e Admin).
- **Fase 3 (3–6 meses - Otimização):** Automação de notificações por e-mail/webhooks para prazos estourados e integração com ferramentas de comunicação.

---
