while True:
    entrada = input("Digite sua nota ou 'sair' para encerrar: ")

    if entrada.lower() == "sair":  
        print("Encerrando o programa...")
        break

    nota = int(entrada)  
    if nota >= 90:
        print("Excelente")
    elif nota >= 80:
        print("Muito bom")
    elif nota >= 70:
        print("Bom")
    else:
        print("Precisa melhorar")
