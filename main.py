import sqlite3


def criar_banco():
    conexao = sqlite3.connect("portfolio.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        descricao TEXT,
        tecnologias TEXT,
        github TEXT,
        site TEXT,
        status TEXT
    )
    """)

    conexao.commit()
    conexao.close()


def cadastrar_projeto():
    nome = input("Nome do projeto: ")
    descricao = input("Descrição: ")
    tecnologias = input("Tecnologias utilizadas: ")
    github = input("Link do GitHub: ")
    site = input("Link do site/projeto online: ")
    status = input("Status do projeto (Ex: Em desenvolvimento, Concluído): ")

    conexao = sqlite3.connect("portfolio.db")
    cursor = conexao.cursor()

    cursor.execute("""
    INSERT INTO projetos (nome, descricao, tecnologias, github, site, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, descricao, tecnologias, github, site, status))

    conexao.commit()
    conexao.close()

    print("Projeto cadastrado com sucesso! 🎉")


def listar_projetos():
    conexao = sqlite3.connect("portfolio.db")
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM projetos")
    projetos = cursor.fetchall()

    if not projetos:
        print("Nenhum projeto cadastrado ainda.")
    else:
        for projeto in projetos:
            print(f"""
ID: {projeto[0]}
Nome: {projeto[1]}
Descrição: {projeto[2]}
Tecnologias: {projeto[3]}
GitHub: {projeto[4]}
Site: {projeto[5]}
Status: {projeto[6]}
--------------------------
""")

    conexao.close()


def menu():
    criar_banco()

    while True:
        print("""
===== ORGANIZADOR DE PORTFÓLIO DEV =====
1 - Cadastrar projeto
2 - Listar projetos
3 - Editar projeto
4 - Excluir projeto
5 - Sair
""")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_projeto()
        elif opcao == "2":
            listar_projetos()
        elif opcao == "3":
            listar_projetos()
            editar_projeto()
        elif opcao == "4":
            listar_projetos()
            excluir_projeto()
        elif opcao == "5":
            print("Até mais! 🚀")
            break
        else:
            print("Opção inválida!")
def editar_projeto():
    id_projeto = input("Digite o ID do projeto que deseja editar: ")

    nome = input("Novo nome do projeto: ")
    descricao = input("Nova descrição: ")
    tecnologias = input("Novas tecnologias: ")
    link_github = input("Novo link do GitHub: ")
    link_site = input("Novo link do site: ")
    status = input("Novo status: ")

    conexao = sqlite3.connect("portfolio.db")
    cursor = conexao.cursor()

    cursor.execute("""
    UPDATE projetos
    SET nome = ?, descricao = ?, tecnologias = ?, github = ?, site = ?, status = ?
    WHERE id = ?
""", (nome, descricao, tecnologias, link_github, link_site, status, id_projeto))

    conexao.commit()
    conexao.close()
    print("✏️ Projeto atualizado com sucesso!")
def excluir_projeto():
    id_projeto = input("Digite o ID do projeto que deseja excluir: ")

    conexao = sqlite3.connect("portfolio.db")
    cursor = conexao.cursor()

    cursor.execute("DELETE FROM projetos WHERE id = ?", (id_projeto,))

    conexao.commit()
    conexao.close()
    print("🗑️ Projeto excluído com sucesso!")
