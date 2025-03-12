saldo = 0.0  

def exibir_menu():
    print("\n === Simulador De Banco ===")
    print("1. Ver saldo")
    print("2. Depositar dinheiro")
    print("3. Sacar dinheiro")
    print("4. PIX")
    print("5. Sair") 

def realizar_pix(valor, nome): 
    global saldo
    if valor > 0 and valor <= saldo: 
        saldo -= valor
        print(f"PIX de R${valor:.2f} realizado com sucesso para {nome}!")
    else:
        print(f"Erro: O valor do PIX R${valor:.2f} é maior que o saldo disponível!")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção (1-5): ")

    if opcao == "1":
        print(f"Seu saldo atual é: R$ {saldo:.2f}")

    elif opcao == "2":
        valor = float(input("Quanto quer depositar?: "))
        if valor > 0:
            saldo += valor  
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Digite um valor válido! Maior que zero.")

    elif opcao == "3":
        valor = float(input("Quanto deseja sacar?: "))
        if valor > 0 and valor <= saldo: 
            saldo -= valor
            print(f"Saque de: R${valor:.2f} realizado com sucesso!")
        else:
            print(f"Erro: O valor do saque R${valor:.2f} é maior que o saldo disponível!")

    elif opcao == "4":
        nome = input("Digite o nome do destinatário: ")  
        valor = float(input("Quanto deseja transferir para o PIX?: "))
        realizar_pix(valor, nome)  

    elif opcao == "5":  
        print("Encerrando o programa...")
        break  

    else:
        print("Opção inválida! Escolha 1, 2, 3, 4 ou 5")