from time import sleep
def lin():
    print('-'*40)


#Variaveis
pessoas = list()
dados = dict()

#Código principal
print("CADASTRO".center(40, '-'))
#Menu
while True:
    #Validação do Menu
    while True:
        esco = int(input("""Escolha a opção desejada:
 0 - Encerrar
 1 - Cadastrar 
 2 - Listar 
 3 - buscar 
 4 - Remover  
 Escolha: """))
        if esco <0 or esco > 4:
            print("Erro! Opção inválida!")
            sleep(1)
            lin()
        else:
            lin()
            break
    #Encerra o programa
    if esco == 0:
        break
    #Cadastrar pessoa
    elif esco == 1:
        dados.clear()
        dados['Nome'] = str(input("Nome: "))
        dados['Idade'] = int(input("Idade: "))
        dados['Telefone'] = str(input("Telefone: "))
        dados['E-mail'] = str(input("E-mail: "))
        pessoas.append(dados.copy())
        print(">>Pessoa cadastrada!")
        lin()
        sleep(2)
    #Listar pessoas
    elif esco == 2:
        while True:
            print("COD NOME       IDADE TELEFONE        EMAIL")
            for c, p in enumerate(pessoas):
                print(f"{c:<3} {p['Nome']:<10} {p['Idade']:<5} {p['Telefone']:<15} {p['E-mail']}")
            lin()
            #Validar volta para menu
            while True:
                resp = int(input("Para voltar ao menu digite 0:"))
                if resp != 0:
                    print("ERRO! Valor invalido.")
                else:
                    lin()
                    break
            break
    #Buscar pessoas
    elif esco == 3:
        while True:
            while True:
                cod = int(input("Digite o código da pessoa: "))
                if cod >= len(pessoas):
                    print("Código inválido!")
                    lin()
                else:
                    break
            for k, v in pessoas[cod].items():
                print(f"{k}: {v}")
            lin()
            # Validar volta para menu
            while True:
                resp = int(input("Para voltar ao menu digite 0:"))
                if resp != 0:
                    print("ERRO! Valor invalido.")
                else:
                    lin()
                    break
            break
    #Remover pessoa
    elif esco == 4:
        while True:
            cod = int(input("Digite o código da pessoa para deletar: "))
            if cod >= len(pessoas):
                print("Código inválido!")
            else:
                break
        del pessoas[cod]
        print("Pessoa removida com sucesso!")
        lin()
        sleep(2)
print("<<< Programa encerrado >>>")
