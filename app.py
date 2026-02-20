from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def conectar_db():
    return sqlite3.connect("portfolio.db")

@app.route("/")
def index():
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()
    conexao.close()
    return render_template("index.html", projetos=projetos)


@app.route("/novo", methods=["GET", "POST"])
def novo():
    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        tecnologias = request.form["tecnologias"]
        link_github = request.form["link_github"]
        link_site = request.form["link_site"]
        status = request.form["status"]

        conexao = conectar_db()
        cursor = conexao.cursor()
        cursor.execute("""
            INSERT INTO projetos (nome, descricao, tecnologias, github, site, status)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, descricao, tecnologias, link_github, link_site, status))
        conexao.commit()
        conexao.close()

        return redirect(url_for("index"))

    return render_template("novo.html")


@app.route("/excluir/<int:id>")
def excluir(id):
    conexao = conectar_db()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM projetos WHERE id = ?", (id,))
    conexao.commit()
    conexao.close()
    return redirect(url_for("index"))


@app.route("/editar/<int:id>", methods=["GET", "POST"])
def editar(id):
    conexao = conectar_db()
    cursor = conexao.cursor()

    if request.method == "POST":
        nome = request.form["nome"]
        descricao = request.form["descricao"]
        tecnologias = request.form["tecnologias"]
        link_github = request.form["link_github"]
        link_site = request.form["link_site"]
        status = request.form["status"]

        cursor.execute("""
            UPDATE projetos
            SET nome = ?, descricao = ?, tecnologias = ?, github = ?, site = ?, status = ?
            WHERE id = ?
        """, (nome, descricao, tecnologias, link_github, link_site, status, id))

        conexao.commit()
        conexao.close()
        return redirect(url_for("index"))

    cursor.execute("SELECT * FROM projetos WHERE id = ?", (id,))
    projeto = cursor.fetchone()
    conexao.close()

    return render_template("editar.html", projeto=projeto)


if __name__ == "__main__":
    app.run(debug=True)