import sqlite3
from biblioteca.interface import *

conexao = sqlite3.connect("banco.db")
cursor = conexao.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS usuario (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
nome TEXT NOT NULL,
tel TEXT NOT NULL,
email TEXT NOT NULL UNIQUE
)""")
conexao.commit()

def cadastrar(n, t, e):

    while True:
        try:
            cursor.execute("""
            INSERT INTO usuario
            (nome, tel, email)
            VALUES (?, ?, ?)
            """, (n, t, e))

            conexao.commit()
            print(f"{n} cadastrado com sucesso!")
            break

        except sqlite3.IntegrityError:
            print("Esse e-mail já está cadastrado!")
            e = input("Digite outro e-mail: ")

def listar():
    cursor.execute("""SELECT * FROM usuario""")
    contas = cursor.fetchall()
    print(f"{'ID':<5}{'NOME':<25}{'TELEFONE':<18}{'EMAIL'}")
    print("-" * 80)
    for dado in contas:
        print(f"{dado[0]:<5}{dado[1]:<25}{dado[2]:<18}{dado[3]}")

def buscar(id):
    cursor.execute("""
    SELECT * FROM usuario
    WHERE id = ?
    """, (id,))
    dado = cursor.fetchone()

    if dado is None:
        print("Não existe usuário com este ID!")
        return

    print(f"{'ID':<5}{'NOME':<25}{'TELEFONE':<18}{'EMAIL'}")
    print("-" * 80)
    #for dado in contas:
    print(f"{dado[0]:<5}{dado[1]:<25}{dado[2]:<18}{dado[3]}")

def remover(id):
    id_usuario = id
    cursor.execute("""DELETE FROM usuario WHERE ID = ?""", (id_usuario,))
    conexao.commit()
    if cursor.rowcount > 0:
        print("Usuário deletado!")
    else:
        print("ID não encontrado!")

def atualizar(id):
    id_usuario = id
    r = menu_atu(['Nome','Telefone', 'E-mail'])
    if r == 1:
        nome_novo = input("Novo nome: ")
        cursor.execute("""UPDATE usuario 
        SET nome = ?
        WHERE id = ?""", (nome_novo, id_usuario))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Alterado com sucesso!")
        else:
            print("ID não encontrado!")
    elif r == 2:
        tel_novo = input("Novo telefone: ")
        cursor.execute("""UPDATE usuario 
        SET tel = ?
        WHERE id = ?""", (tel_novo, id_usuario))
        conexao.commit()
        if cursor.rowcount > 0:
            print("Alterado com sucesso!")
        else:
            print("ID não encontrado!")
    elif r == 3:
        while True:
            email_novo = input("Novo E-mail: ")
            try:
                cursor.execute("""
                    UPDATE usuario
                    SET email = ?
                    WHERE id = ?
                    """, (email_novo, id_usuario))

                conexao.commit()

                if cursor.rowcount > 0:
                    print("Alterado com sucesso!")
                else:
                    print("ID não encontrado!")

                break

            except sqlite3.IntegrityError:
                print("Esse e-mail já está cadastrado!")
    else:
        print("Opção invalida!")