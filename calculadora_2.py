import tkinter as tk
from tkinter import messagebox

def calcular_resultado():
    """Executa o cálculo final."""
    try:
        resultado = eval(entrada1.get())
        caixa_resultado.config(text=str(resultado))
    except Exception as e:
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

# Definindo a cor de fundo azul claro
janela.config(bg="#A8D0E6")

# Layout
entrada1 = tk.Entry(janela, bg="#C2E0F2", font=("Arial", 14), bd=2, width=20, justify="right")
entrada1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botões numéricos
numeros = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("0", 4, 1)
]

for (texto, linha, coluna) in numeros:
    tk.Button(janela, text=texto, bg="#A0C6E3", font=("Arial", 12), width=5, height=2, 
              command=lambda t=texto: atualizar_entrada(t)).grid(row=linha, column=coluna, padx=5, pady=5)

# Botões de operações
operacoes = [
    ("+", 1, 3), ("-", 2, 3), ("*", 3, 3), ("/", 4, 3),
    ("=", 4, 2)
]

for (texto, linha, coluna) in operacoes:
    tk.Button(janela, text=texto, bg="#A0C6E3", font=("Arial", 12), width=5, height=2, 
              command=lambda t=texto: atualizar_entrada(t)).grid(row=linha, column=coluna, padx=5, pady=5)

# Botões "C" e "CE" lado a lado
tk.Button(janela, text="C", bg="#A0C6E3", font=("Arial", 12), width=5, height=2, command=limpar).grid(row=4, column=0, padx=5, pady=5)
tk.Button(janela, text="CE", bg="#A0C6E3", font=("Arial", 12), width=5, height=2, command=apagar_ultimo).grid(row=4, column=1, padx=5, pady=5)

# Caixa de resultado (usando Label para aumentar altura)
caixa_resultado = tk.Label(janela, width=25, bg="#C2E0F2", font=("Arial", 18), bd=2, anchor="e", height=2)
caixa_resultado.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Inicia a aplicação
janela.mainloop()
