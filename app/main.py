import time
from cliente import Cliente

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
    print("3 - CONFERÊNCIA\n")
    print("4 - SAIR\n")
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
                        elif(op == 1):
                            nome = str(input("Digite o nome do cliente a ser cadastrado: "))
                            cpf = str(input("Digite o cfp do cliente (apenas os numeros): "))
                            cli = Cliente(nome, cpf)
                            cli.cadastra_cliente()
                        else:
                            print("Invalido!!")
                else:
                    print("\nUSUARIO OU SENHA INCORRETO!!")
            case 3:
                while True:
                    print("Teste 3")
                    break
            case 4:
                break
    except:
        print("\n>>> DIGITE O NÚMERO AO LADO DA OPÇÃO!!! <<<")
        print("#"*50)
    finally:
        print(">>> Obrigado por usar nosso sistema!!! <<<")