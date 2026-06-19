from biblioteca.data_base import *


while True:
    limpar_tela()
    r = menu(['Cadastrar nova pessoa', 'Listar pessoas', 'Busar pessoa', 'Remover pessoa','Atualizar dados', 'Sair do programa'])
    if r == 1:
        cabeçalho('CADASTRAR NOVA PESSOA')
        cadastrar()
    elif r == 2:
        cabeçalho('LISTAR PESSOAS')
        listar()
    elif r == 3:
        cabeçalho('BUSCAR PESSOA')
        buscar()
    elif r == 4:
        cabeçalho('REMOVER PESSOA')
        remover()
    elif r == 5:
        cabeçalho('ATUALIZAR DADOS')
        atualizar()
    elif r == 6:
        cabeçalho('SAINDO DO SISTEMA... VOLTE LOGO!')
        break
    else:
        print("Opção inválida")
    input("Aperte ENTER para continuar!")
conexao.close()