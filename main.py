import funcoes

def menu():
    print("\nEscolha uma das opções:")
    print("1. Listar Colaboradores")
    print("2. Relatório de Colaboradores em Ordem Alfabética")
    print("3. Relatório de Colaboradores por Ordem de Salário")
    print("4. Listar Colaboradores por Cargo")
    print("5. Fechar o programa")

    while True:
        opcao = input("\nEscolha uma das opções (1-5): ")

        if opcao == "1":
            funcoes.lista()
        elif opcao == "2":
            funcoes.ordem_alfabetica()
        elif opcao == "3":
            funcoes.ordem_salario()
        elif opcao == "4":
            funcoes.lista_de_cargos()
            funcoes.listar_por_cargo()
        elif opcao == "5":
            print("Byee...")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

menu()