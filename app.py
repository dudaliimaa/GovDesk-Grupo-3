"""
GovDesk - Semana 1
Projeto da disciplina Gestao e Governanca de TI (ITI004)

Objetivo desta semana: apenas colocar o esqueleto do projeto no ar.
Ainda NAO ha banco de dados nem cadastro real de chamados - isso vem
nas proximas semanas. Por enquanto, os dados ficam "hardcoded" em
memoria mesmo, so para termos algo rodando e visivel no navegador.
"""

import os
from flask import Flask, render_template

app = Flask(__name__)

# "Banco de dados" provisorio (sera substituido nas proximas semanas)
chamados = [
    {"id": 1, "titulo": "Impressora do 2o andar nao liga", "status": "aberto"},
    {"id": 2, "titulo": "Sistema de vendas lento", "status": "em andamento"},
    {"id": 3, "titulo": "Solicitacao de acesso ao ERP", "status": "resolvido"},
]

# Equipe do grupo - cada grupo preenche com os proprios nomes e papeis
equipe = [
    {"nome": "Eduarda de Lima Sales", "papel": "Product Owner / CIO"},
    {"nome": "Cauê Mayo Simôes", "papel": "Dev Lead"},
    {"nome": "Nathalia Cappellini Pereira e Vitor Lopes Ribeiro", "papel": "QA / Auditoria"},
]


@app.route("/")
def index():
    return render_template("index.html", chamados=chamados, total=len(chamados))


@app.route("/sobre")
def sobre():
    return render_template("sobre.html", equipe=equipe)


if __name__ == "__main__":
    # Replit expoe a porta pela variavel de ambiente PORT quando existe;
    # 8080 e usado como padrao para rodar local tambem, se precisar.
    porta = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=porta, debug=True)
