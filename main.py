from lib.interface import *
from lib.data_base import *
from time import sleep
import sqlite3


while True:
    r = menu(['Cadastrar nova pessoa', 'Listar pessoas', 'Busar pessoa', 'Remover pessoa','Atualizar dados', 'Sair do programa'])
    if r == 1:
        cabeçalho('CADASTRAR NOVA PESSOA')
        nome = input("Nome: ").strip()
        tel = input("Telefone: ").strip()
        email = input("E-mail: ").strip()
        cadastrar(nome, tel, email)
    elif r == 2:
        cabeçalho('LISTAR PESSOAS')
        listar()
    elif r == 3:
        cabeçalho('BUSCAR PESSOA')
        num = leiaint("ID: ")
        buscar(num)
    elif r == 4:
        cabeçalho('REMOVER PESSOA')
        num = leiaint("ID: ")
        remover(num)
    elif r == 5:
        cabeçalho('ATUALIZAR DADOS')
        num = leiaint('ID: ')
        atualizar(num)
    elif r == 6:
        cabeçalho('SAINDO DO SISTEMA... VOLTE LOGO!')
        break
    input("Aperte ENTER para continuar!")
conexao.close()