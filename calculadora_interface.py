import tkinter as tk

def calcular_resultado():
    """Executa o cálculo final."""
    try:
        resultado = eval(entrada1.get())
        caixa_resultado.config(text=str(resultado))
    except Exception:
        caixa_resultado.config(text="Erro")

def atualizar_entrada(valor):
    """Atualiza a entrada com o número ou operação clicada."""
    entrada1.insert(tk.END, valor)

def limpar():
    """Limpa a entrada e o resultado."""
    entrada1.delete(0, tk.END)
    caixa_resultado.config(text="")

def apagar_ultimo():
    """Apaga o último caractere da entrada."""
    entrada1.delete(len(entrada1.get()) - 1, tk.END)

# Criando a janela
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.config(bg="white")

# Título acima da entrada
titulo = tk.Label(janela, text="Calculadora", bg="white", fg="black", font=("Arial", 16, "bold"))
titulo.grid(row=0, column=0, columnspan=4, pady=(10, 0))

# Campo de entrada
entrada1 = tk.Entry(janela, bg="white", fg="black", font=("Arial", 16), bd=2, width=25, justify="right", highlightbackground="black", highlightthickness=1)
entrada1.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

# Caixa de resultado
caixa_resultado = tk.Label(janela, width=30, bg="white", fg="black", font=("Arial", 18), bd=2, anchor="e", height=2, relief="solid", highlightbackground="black", highlightthickness=1)
caixa_resultado.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Botões numéricos
numeros = [
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2),
    ("0", 5, 1)
]

for (texto, linha, coluna) in numeros:
    tk.Button(janela, text=texto, bg="white", fg="black", font=("Arial", 12), width=7, height=2, 
              relief="solid", bd=1, highlightbackground="black",
              command=lambda t=texto: atualizar_entrada(t)).grid(row=linha, column=coluna, padx=5, pady=5)

# Botões de operações
operacoes = [
    ("+", 2, 3), ("-", 3, 3), ("*", 4, 3), ("/", 5, 3),
    ("=", 5, 2)
]

for (texto, linha, coluna) in operacoes:
    tk.Button(janela, text=texto, bg="white", fg="black", font=("Arial", 12), width=7, height=2, 
              relief="solid", bd=1, highlightbackground="black",
              command=lambda t=texto: atualizar_entrada(t) if t != "=" else calcular_resultado()).grid(row=linha, column=coluna, padx=5, pady=5)

# Botões C e CE
tk.Button(janela, text="C", bg="white", fg="black", font=("Arial", 12), width=7, height=2, relief="solid", bd=1,
          highlightbackground="black", command=limpar).grid(row=5, column=0, padx=5, pady=5)
tk.Button(janela, text="CE", bg="white", fg="black", font=("Arial", 12), width=7, height=2, relief="solid", bd=1,
          highlightbackground="black", command=apagar_ultimo).grid(row=5, column=1, padx=5, pady=5)

# Inicia a aplicação
janela.mainloop()
