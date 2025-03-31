entrada = input("Digite um Número: ")

try:
    A = float(entrada)
    
    if A<1 or A>35:
        print("O número é menor que 1 ou maior que 35")

    else:
        print(f"A soma de {A}+30 é: {A+10}")

except ValueError:
    print("Você dgitou um número inválido")
    
