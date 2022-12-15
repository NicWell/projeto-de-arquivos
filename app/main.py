import time
from cliente import Cliente
from funcionario import Funcionario

def acesso (user, password):
    list = []
    with open('base/adm.txt', 'r') as adm:
        for v in adm.readlines():
            list.append(str(v))
    usuario = list[0].replace('\n','')
    senha = list[1]
    if(user == usuario and password == senha):
        return True
    else:
        return False


while True:
    print("#"*50)
    print("\n--- ESCOLHA UMA DAS OPÇÕES ---\n")
    print("1 - CAIXA \n")
    print("2 - CADASTRO\n")
    print("3 - DELETAR\n")
    print("4 - ATUALIZAR\n")
    print("5 - CONFERÊNCIA\n")
    print("6 - SAIR\n")
    try:
        opcao = int(input("Digite o número ao lado da operação: "))
        match(opcao):
            case 1:
                while True:
                    print("SEJA BEM VINDO!!")
                    print("")
                    break
            case 2: 
                print("\nDigite seu usuário administrador !!\n")
                user = str(input(": "))
                print("Digite sua senha: ")
                passwd = str(input(": "))
                if(acesso(user, passwd)):
                    print("#"*50)
                    while True:
                        print("\nSEJA BEM VINDO A TELA DE CADASTRO\n")
                        print("SELECIONE A OPÇÃO DE CADASTRO!")
                        print("\n--- ESCOLHA UMA DAS OPÇÕES ---\n")
                        print("1 - CLIENTE\n")
                        print("2 - FUNCIONÁRIO\n")
                        print("3 - PRODUTO\n")
                        print("4 - SAIR\n")
                        op = int(input("Digite o número ao lado da operação: "))
                        if(op == 4):
                            break
                        elif(op == 2):
                            nome = str(input("Digite o nome do funcionario a ser cadastrado: "))
                            cpf = str(input("Digite o cpf do funcionario (apenas os numeros): "))
                            senha = str(input("Senha do funcionario: "))
                            funcionario = Funcionario(nome, cpf, senha)
                            funcionario.cadastra_func()
                            time.sleep(1)
                        elif(op == 1):
                            nome = str(input("Digite o nome do cliente a ser cadastrado: "))
                            cpf = str(input("Digite o cpf do cliente (apenas os numeros): "))
                            cli = Cliente(nome, cpf)
                            cli.cadastra_cliente()
                            time.sleep(1)
                        else:
                            print("Invalido!!")
                else:
                    print("\nUSUARIO OU SENHA INCORRETO!!")
            case 3:
                print("\nDigite seu usuário administrador !!\n")
                user = str(input(": "))
                print("Digite sua senha: ")
                passwd = str(input(": "))
                if(acesso(user, passwd)):
                    while True:
                        print("#"*50)
                        print("SELECIONE A OPÇÃO DE DELECAO!")
                        print("\n--- ESCOLHA UMA DAS OPÇÕES ---\n")
                        print("1 - CLIENTE\n")
                        print("2 - FUNCIONÁRIO\n")
                        print("3 - PRODUTO\n")
                        print("4 - SAIR\n")
                        op = int(input("Digite o número ao lado da operação: "))
                        if(op == 4):
                            break
                        elif(op == 2):
                            cpf = str(input("Digite o cpf do funcionario (apenas os numeros): "))
                            funDelete = Funcionario(None, cpf, None)
                            funDelete.deleta_func(cpf)
                            time.sleep(1)
                        elif(op == 1):
                            cpf = str(input("Digite o cpf do cliente (apenas os numeros): "))
                            cldel = Cliente(None, cpf)
                            cldel.deleta_cliente(cpf)
                            time.sleep(1)
                        else:
                            print("Invalido!!")
                else:
                    print("\nUSUARIO OU SENHA INCORRETO!!")
            case 4:
                print("\nDigite seu usuário administrador !!\n")
                user = str(input(": "))
                print("Digite sua senha: ")
                passwd = str(input(": "))
                if(acesso(user, passwd)):
                    print("#"*50)
                    while True:
                        print("SELECIONE A OPÇÃO PARA ATUALIZAR!")
                        print("\n--- ESCOLHA UMA DAS OPÇÕES ---\n")
                        print("1 - CLIENTE\n")
                        print("2 - FUNCIONÁRIO\n")
                        print("3 - PRODUTO\n")
                        print("4 - SAIR\n")
                        op = int(input("Digite o número ao lado da operação: "))
                        if(op == 4):
                            break
                        elif(op == 1):
                            print('')
                            print('--------------------------------')
                            print("OBS: O CPF VAI IDENTIFICAR O CLIENTE A SER ATUALIZADO!!\nDIGITE UM CPF QUE JÁ FOI CADASTRADO!!!")
                            print('------------------------------------------------------------------------------\n')
                            nome = str(input("Digite o nome do cliente a ser atualizado: "))
                            cpf = str(input("Digite o cpf do cliente a ser atualizado: "))
                            cliAtt = Cliente(nome, cpf)
                            cliAtt.atualiza_Clientes(cpf, nome)
                            time.sleep(1)
                        elif(op == 2):
                            print('')
                            print('------------------------------------------------------------------------------')
                            print("OBS: O CPF VAI IDENTIFICAR O FUNCIONÁRIO A SER ATUALIZADO!!\nDIGITE UM CPF QUE JÁ FOI CADASTRADO!!!")
                            print('------------------------------------------------------------------------------\n')
                            nome = str(input("Digite o nome do funcionário a ser atualizado: "))
                            cpf = str(input("Digite o cpf do funcionário a ser atualizado: "))
                            senha = str(input("Senha do funcionário a ser atualizado: "))
                            funcAtt = Funcionario(nome, cpf, senha)
                            funcAtt.atualiza_func(nome, cpf, senha)
                        else:
                            print("OPERAÇÃO INVÁLIDA!!")
                else:
                    print("\nUSUARIO OU SENHA INCORRETO!!")
            case 5:
                while True:
                    print("\nSELECIONE A OPÇÃO PARA LISTAR!\n")
                    print("\n--- ESCOLHA UMA DAS OPÇÕES ---\n")
                    print("1 - CLIENTE\n")
                    print("2 - FUNCIONÁRIO\n")
                    print("3 - PRODUTO\n")
                    print("4 - SAIR\n")
                    op = int(input("DIGITE O NÚMERO DA OPÇÃO ESCOLHIDA PARA VERIFICAÇÃO: "))
                    if(op == 4):
                        break
                    elif(op == 1):
                        lisCli = Cliente(None, None)
                        lisCli.lista_Clientes()
                        time.sleep(1)
                    elif(op == 2):
                        lisFun = Funcionario(None, None, None)
                        lisFun.lista_func()
                    else:
                        print("OPERAÇÃO INVÁLIDA!\n")
            case 6:
                break
    except:
        print("\n>>> DIGITE O NÚMERO AO LADO DA OPÇÃO!!! <<<")
        print("#"*50)
    finally:
        print(">>> Obrigado por usar nosso sistema!!! <<<")