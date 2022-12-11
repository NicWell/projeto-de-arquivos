def acesso (user, password):
    print("Usuário passado:", user, "\nSenha:", password)
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
                        print("\nSEJA BEM VINDO A TELA DE CADASTRO\n ")
                        break
                else:
                    print("\nUSUARIO OU SENHA INCORRETO!!")
            case 3:
                while True:
                    print("Teste 3")
                    break
            case 4:
                print("Obrigado por usar nosso sistema!!")
                break
    except:
        print("\n>>> DIGITE O NÚMERO AO LADO DA OPÇÃO!!! <<<")
        print("#"*50)