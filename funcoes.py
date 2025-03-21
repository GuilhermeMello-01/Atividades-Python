lista_colaboradores = [
    {"nome": "Cesar", "CPF": "509.944.754-45", "cargo": "Gerente", "salario": 3000},
    {"nome": "Gabi", "CPF": "515.675.123-54", "cargo": "Caixa", "salario": 1500},
    {"nome": "Bruno", "CPF": "654.768.124-66", "cargo": "Vendedor", "salario": 2500},
    {"nome": "Guilherme", "CPF": "543.218.122-65", "cargo": "Estoquista", "salario": 2000}
]

def lista():
    print("\nLista de colaboradores:")
    for colaborador in lista_colaboradores:
        print(f"Nome: {colaborador['nome']}, CPF: {colaborador['CPF']}, Cargo: {colaborador['cargo']}, Salário: R${colaborador['salario']:.2f}")

def ordem_alfabetica():
    print("\nLista em ordem alfabética:")
    for colaborador in sorted(lista_colaboradores, key=lambda x: x["nome"]):
        print(f"Nome: {colaborador['nome']}, CPF: {colaborador['CPF']}, Cargo: {colaborador['cargo']}, Salário: R${colaborador['salario']:.2f}")

def ordem_salario():
    print("\nLista por ordem de salário:")
    for colaborador in sorted(lista_colaboradores, key=lambda x: x["salario"]):
        print(f"Nome: {colaborador['nome']}, CPF: {colaborador['CPF']}, Cargo: {colaborador['cargo']}, Salário: R${colaborador['salario']:.2f}")

def lista_de_cargos():
    print("\nCargos existentes:")
    cargos = sorted(set(colaborador["cargo"] for colaborador in lista_colaboradores))
    for cargo in cargos:
        print(f"- {cargo}")

def listar_por_cargo():
    while True:
        cargo_desejado = input("\nDigite o cargo desejado (ou 'sair' para voltar ao menu): ").strip().lower()
        if cargo_desejado == "sair":
            print("\nVocê saiu da listagem por cargo.")
            break

        colaboradores_filtrados = [colaborador for colaborador in lista_colaboradores if colaborador["cargo"].lower() == cargo_desejado]

        if colaboradores_filtrados:
            print("\nColaboradores com esse cargo:")
            for colaborador in colaboradores_filtrados:
                print(f"Nome: {colaborador['nome']}, CPF: {colaborador['CPF']}, Salário: R${colaborador['salario']:.2f}")
        else:
            print("Nenhum colaborador encontrado com esse cargo.")