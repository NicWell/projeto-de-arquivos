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
                    print("Teste 1")
                    break
            case 2: 
                while True:
                    print("Teste 2")
                    break
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
    break