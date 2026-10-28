"""
GovDesk - Semana 1
Projeto da disciplina Gestao e Governanca de TI (ITI004)

Objetivo desta semana: apenas colocar o esqueleto do projeto no ar.
Ainda NAO ha banco de dados nem cadastro real de chamados - isso vem
nas proximas semanas. Por enquanto, os dados ficam "hardcoded" em
memoria mesmo, so para termos algo rodando e visivel no navegador.
"""

import os
import sqlite3
import json
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Conexão/criação do banco de dados
try:
    with sqlite3.connect("database.db") as conn:
        print("Banco de dado aberto")
except sqlite3.OperationalError as e:
    print("Falha ao conectar com o banco de dados: ", e)
cursor = conn.cursor()


### Criação das tabelas (se não já existirem) ###
## Tabela dos solicitantes (empregados)
comando = """CREATE TABLE IF NOT EXISTS SOLICITANTE(
id_solicitante INTEGER PRIMARY KEY AUTOINCREMENT, 
nm_solicitante TEXT NOT NULL, 
senha TEXT NOT NULL, 
email TEXT, 
telefone TEXT, 
cpf TEXT NOT NULL)"""
cursor.execute(comando)
    
## Tabela dos chamados
comando = """CREATE TABLE IF NOT EXISTS CHAMADO(
id_chamado INTEGER PRIMARY KEY AUTOINCREMENT, 
titulo TEXT NOT NULL, 
descricao TEXT,
id_solicitante INTEGER NOT NULL, 
prioridade TEXT NOT NULL, 
status TEXT NOT NULL,
CONSTRAINT fk_cha_solic FOREIGN KEY (id_solicitante) REFERENCES SOLICITANTE(id_solicitante))"""
cursor.execute(comando)
print("Tabelas criadas/verificadas")


### Inserção de dados mas tabelas ###
## PS: esse comando deve ser executado apenas uma vez, comentar tudo depois de usar
# ## Solicitante ##
# comando = """INSERT INTO SOLICITANTE(nm_solicitante, senha, cpf) VALUES
# ('Nenhum', '123', 'Nenhum'),
# ('João Carlos', '123', '849.021.902-40'),
# ('Ana Maria', '123', '901.379.284-96'),
# ('Eduardo dos Santos', '123', '590.278.971-13')"""
# cursor.execute(comando)
# conn.commit()
 
# ## Chamado ##
# comando = """INSERT INTO CHAMADO(titulo, id_solicitante, prioridade, status) VALUES
# ('Impressora do 2o andar nao liga', 2, 'alta', 'aberto'),
# ('Sistema de vendas lento', 3, 'média', 'em andamento'),
# ('Solicitacao de acesso ao ERP', 4, 'baixa','resolvido')"""
# cursor.execute(comando)
# conn.commit()
# print("Dados inseridos")

cursor.close

# Equipe do grupo
equipe = [
    {"nome": "Eduarda de Lima Sales", "papel": "Product Owner / CIO"},
    {"nome": "Cauê Mayo Simões", "papel": "Dev Lead"},
    {"nome": "Nathalia Cappellini Pereira", "papel": "QA / Auditoria"},
    {"nome": "Vitor Lopes Ribeiro", "papel": "DevOps & Security Analyst"}
]

PRIORIDADES = ["baixa", "média", "alta"]

@app.route("/")
def index():
    return render_template("index.html", chamados=getChamados(), total=len(getChamados()))


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

        if not titulo:
            erro = "Preencha o título do chamado."
        elif prioridade not in PRIORIDADES:
            erro = "Prioridade inválida."
        else:
            solicitante = 1 ## TEMPORÁRIO --- MUDAR QUANDO ADICIONAR LOGIN ##
            addChamado(titulo,descricao,solicitante,prioridade)
            return redirect(url_for("index"))

    # Em caso de erro, devolve o que a pessoa digitou (request.form)
    return render_template("novo.html", erro=erro, prioridades=PRIORIDADES,
    dados=request.form)



#TODO: Adicionar classe para lidar com banco de dados
def addChamado(titulo,descricao,solicitante,prioridade):
    try:
        with sqlite3.connect("database.db") as conn:
            print("Banco de dado aberto")
    except sqlite3.OperationalError as e:
        print("Falha ao conectar com o banco de dados: ", e)
    cursor = conn.cursor()
    comando=f"INSERT INTO CHAMADO(titulo,descricao,id_solicitante, prioridade, status) VALUES('{titulo}','{descricao}',{solicitante},'{prioridade}','aberto')"
    cursor.execute(comando)
    conn.commit()
    cursor.close()
    print("Chamado adicionado!")

def getChamados():
    try:
        with sqlite3.connect("database.db") as conn:
            print("Banco de dado aberto")
    except sqlite3.OperationalError as e:
        print("Falha ao conectar com o banco de dados: ", e)
    cursor = conn.cursor()
    comando = """SELECT c.id_chamado as id, c.titulo as 'titulo', s.nm_solicitante as 'solicitante', c.prioridade as 'prioridade', c.status as 'status'
    FROM chamado as c INNER JOIN solicitante as s ON c.id_solicitante = s.id_solicitante"""
    cursor.execute(comando)
    linhas = cursor.fetchall()
    colunas = [column[0] for column in cursor.description]

    chamados = []
    for linha in linhas:
        linha_dict = {colunas[i]: linha[i] for i in range(len(colunas))}
        chamados.append(linha_dict)

    cursor.close()
    return chamados



if __name__ == "__main__":
    # Replit expoe a porta pela variavel de ambiente PORT quando existe;
    # 8080 e usado como padrao para rodar local tambem, se precisar.
    porta = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=porta, debug=True)
