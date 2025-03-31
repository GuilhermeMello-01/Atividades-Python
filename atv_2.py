while True:

    print("\n Escolha uma das opções:")
    print("1. Diga 'Olá'")
    print("2. Quem é você?")
    print("3. Que horas são?")
    print("4. Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        diga_olá = input("Diga Olá:")
        print("Você digitou:", diga_olá)
    elif opcao == "2":
        quem_é_você = input ("Diga quem é você: ")
        print("Eu sou ", quem_é_você)
    elif opcao == "3":
        hora = input ("Digite a hora atual: ")
    elif opcao == "4":
        print("Encerrando...")
        break
    else:
        print("Opção Inválida. Digite Novamente.")