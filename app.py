"""
GovDesk - Semana 1
Projeto da disciplina Gestao e Governanca de TI (ITI004)

Objetivo desta semana: apenas colocar o esqueleto do projeto no ar.
Ainda NAO ha banco de dados nem cadastro real de chamados - isso vem
nas proximas semanas. Por enquanto, os dados ficam "hardcoded" em
memoria mesmo, so para termos algo rodando e visivel no navegador.
"""

import os
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

# "Banco de dados" provisorio (sera substituido nas proximas semanas)
chamados = [
    {"id": 1, "titulo": "Impressora do 2o andar nao liga","solicitante": "João Carlos","prioridade": "alta", "status": "aberto"},
    {"id": 2, "titulo": "Sistema de vendas lento","solicitante": "Ana Maria","prioridade": "media", "status": "em andamento"},
    {"id": 3, "titulo": "Solicitacao de acesso ao ERP","solicitante": "Eduardo dos Santos","prioridade": "baixa", "status": "resolvido"},
]

# Equipe do grupo - cada grupo preenche com os proprios nomes e papeis
equipe = [
    {"nome": "Eduarda de Lima Sales", "papel": "Product Owner / CIO"},
    {"nome": "Cauê Mayo Simões", "papel": "Dev Lead"},
    {"nome": "Nathalia Cappellini Pereira e Vitor Lopes Ribeiro", "papel": "QA / Auditoria"},
]

PRIORIDADES = ["baixa", "média", "alta"]

@app.route("/")
def index():
    return render_template("index.html", chamados=chamados, total=len(chamados))


@app.route("/sobre")
def sobre():
    return render_template("sobre.html", equipe=equipe)

@app.route("/novo", methods=["GET", "POST"])
def novo():
    erro = None
    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        solicitante = request.form.get("solicitante", "").strip()
        prioridade = request.form.get("prioridade", "média")

        if not titulo or not solicitante:
            erro = "Preencha o título e o nome do solicitante."
        elif prioridade not in PRIORIDADES:
            erro = "Prioridade inválida."
        else:
            novo_id = max((c["id"] for c in chamados), default=0) + 1
            chamados.append({
                "id": novo_id,
                "titulo": titulo,
                "descricao": descricao,
                "solicitante": solicitante,
                "prioridade": prioridade,
                "status": "aberto",
            })
            return redirect(url_for("index"))

    # Em caso de erro, devolve o que a pessoa digitou (request.form)
    return render_template("novo.html", erro=erro, prioridades=PRIORIDADES,
    dados=request.form)


if __name__ == "__main__":
    # Replit expoe a porta pela variavel de ambiente PORT quando existe;
    # 8080 e usado como padrao para rodar local tambem, se precisar.
    porta = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=porta, debug=True)
