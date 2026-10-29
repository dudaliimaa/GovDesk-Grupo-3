"""
GovDesk - Semana 1
Projeto da disciplina Gestao e Governanca de TI (ITI004)
"""

import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = os.environ.get(
    "SECRET_KEY",
    "govdesk-chave-local-desenvolvimento"
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "database.db")


def conectar_banco():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def inicializar_banco():
    with conectar_banco() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS SOLICITANTE (
                id_solicitante INTEGER PRIMARY KEY AUTOINCREMENT,
                nm_solicitante TEXT NOT NULL,
                senha TEXT NOT NULL,
                email TEXT,
                telefone TEXT,
                cpf TEXT NOT NULL
            )
        """)

        conn.execute("""
            CREATE TABLE IF NOT EXISTS CHAMADO (
                id_chamado INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                id_solicitante INTEGER NOT NULL,
                prioridade TEXT NOT NULL,
                status TEXT NOT NULL,
                FOREIGN KEY (id_solicitante)
                    REFERENCES SOLICITANTE(id_solicitante)
            )
        """)


inicializar_banco()

equipe = [
    {"nome": "Eduarda de Lima Sales", "papel": "Product Owner / CIO"},
    {"nome": "Cauê Mayo Simões", "papel": "Dev Lead"},
    {"nome": "Nathalia Cappellini Pereira", "papel": "QA / Auditoria"},
    {"nome": "Vitor Lopes Ribeiro", "papel": "DevOps & Security Analyst"}
]

PRIORIDADES = ["baixa", "média", "alta"]


@app.route("/")
def index():
    chamados = getChamados()
    return render_template(
        "index.html",
        chamados=chamados,
        total=len(chamados)
    )


@app.route("/sobre")
def sobre():
    return render_template("sobre.html", equipe=equipe)


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    erro = None

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip().lower()
        cpf = request.form.get("cpf", "").strip()
        telefone = request.form.get("telefone", "").strip()
        senha = request.form.get("senha", "")
        confirmar_senha = request.form.get("confirmar_senha", "")

        if not nome or not email or not cpf or not senha:
            erro = "Preencha todos os campos obrigatórios."

        elif senha != confirmar_senha:
            erro = "As senhas não coincidem."

        elif len(senha) < 8:
            erro = "A senha deve ter pelo menos 8 caracteres."

        else:
            try:
                with conectar_banco() as conn:
                    existente = conn.execute("""
                        SELECT id_solicitante
                        FROM SOLICITANTE
                        WHERE LOWER(email) = ? OR cpf = ?
                    """, (email, cpf)).fetchone()

                    if existente:
                        erro = "Este e-mail ou CPF já está cadastrado."
                    else:
                        senha_hash = generate_password_hash(senha)

                        conn.execute("""
                            INSERT INTO SOLICITANTE
                                (nm_solicitante, senha, email, telefone, cpf)
                            VALUES (?, ?, ?, ?, ?)
                        """, (
                            nome,
                            senha_hash,
                            email,
                            telefone,
                            cpf
                        ))

                if erro is None:
                    flash("Cadastro realizado com sucesso! Faça seu login.")
                    return redirect(url_for("login"))

            except sqlite3.Error:
                erro = "Não foi possível realizar o cadastro. Tente novamente."

    return render_template("cadastro.html", erro=erro)


@app.route("/login", methods=["GET", "POST"])
def login():
    erro = None

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        senha = request.form.get("senha", "")

        with conectar_banco() as conn:
            usuario = conn.execute("""
                SELECT id_solicitante, nm_solicitante, email, senha
                FROM SOLICITANTE
                WHERE LOWER(email) = ?
            """, (email,)).fetchone()

        if usuario and check_password_hash(usuario["senha"], senha):
            session.clear()
            session["id_solicitante"] = usuario["id_solicitante"]
            session["nome_solicitante"] = usuario["nm_solicitante"]

            return redirect(url_for("index"))

        erro = "E-mail ou senha incorretos."

    return render_template("login.html", erro=erro)


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


@app.route("/novo", methods=["GET", "POST"])
def novo():
    erro = None

    if "id_solicitante" not in session:
        flash("Entre na sua conta para registrar um chamado.")
        return redirect(url_for("login"))

    if request.method == "POST":
        titulo = request.form.get("titulo", "").strip()
        descricao = request.form.get("descricao", "").strip()
        prioridade = request.form.get("prioridade", "média")

        if not titulo:
            erro = "Preencha o título do chamado."

        elif prioridade not in PRIORIDADES:
            erro = "Prioridade inválida."

        else:
            solicitante = session["id_solicitante"]

            try:
                addChamado(titulo, descricao, solicitante, prioridade)
                flash("Chamado criado com sucesso!")
                return redirect(url_for("index"))

            except sqlite3.Error:
                erro = "Não foi possível criar o chamado. Tente novamente."

    return render_template(
        "novo.html",
        erro=erro,
        prioridades=PRIORIDADES,
        dados=request.form
    )


def addChamado(titulo, descricao, solicitante, prioridade):
    with conectar_banco() as conn:
        conn.execute("""
            INSERT INTO CHAMADO
                (titulo, descricao, id_solicitante, prioridade, status)
            VALUES (?, ?, ?, ?, ?)
        """, (titulo, descricao, solicitante, prioridade, "aberto"))


def getChamados():
    with conectar_banco() as conn:
        linhas = conn.execute("""
            SELECT
                c.id_chamado AS id,
                c.titulo AS titulo,
                s.nm_solicitante AS solicitante,
                c.prioridade AS prioridade,
                c.status AS status
            FROM CHAMADO AS c
            INNER JOIN SOLICITANTE AS s
                ON c.id_solicitante = s.id_solicitante
            ORDER BY c.id_chamado DESC
        """).fetchall()

    return [dict(linha) for linha in linhas]


if __name__ == "__main__":
    porta = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=porta, debug=True)