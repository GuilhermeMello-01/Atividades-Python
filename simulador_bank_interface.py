import tkinter as tk
from tkinter import simpledialog, messagebox, scrolledtext

# Dados
saldo = 0.0
historico = []

# Funções
def ver_saldo():
    messagebox.showinfo("💰 Saldo", f"Seu saldo atual é: R$ {saldo:.2f}")

def depositar():
    global saldo
    try:
        valor = float(simpledialog.askstring("💵 Depósito", "Digite o valor a depositar:"))
        if valor > 0:
            saldo += valor
            historico.append(f"Depósito: R${valor:.2f}")
            messagebox.showinfo("✅ Sucesso", f"Depósito de R${valor:.2f} realizado!")
        else:
            messagebox.showwarning("⚠️ Atenção", "Digite um valor maior que zero.")
    except:
        messagebox.showerror("Erro", "Entrada inválida.")

def sacar():
    global saldo
    try:
        valor = float(simpledialog.askstring("🏧 Saque", "Digite o valor a sacar:"))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            historico.append(f"Saque: R${valor:.2f}")
            messagebox.showinfo("✅ Sucesso", f"Saque de R${valor:.2f} realizado!")
        else:
            messagebox.showwarning("⚠️ Atenção", "Valor inválido ou saldo insuficiente.")
    except:
        messagebox.showerror("Erro", "Entrada inválida.")

def realizar_pix():
    global saldo
    try:
        nome = simpledialog.askstring("PIX ✉️", "Nome do destinatário:")
        valor = float(simpledialog.askstring("PIX 💸", "Valor do PIX:"))
        if valor > 0 and valor <= saldo:
            saldo -= valor
            historico.append(f"PIX: R${valor:.2f} para {nome}")
            messagebox.showinfo("✅ PIX enviado", f"PIX de R${valor:.2f} enviado para {nome}.")
        else:
            messagebox.showwarning("⚠️ Atenção", "Valor inválido ou saldo insuficiente.")
    except:
        messagebox.showerror("Erro", "Dados inválidos.")

def ver_historico():
    historico_janela = tk.Toplevel(janela)
    historico_janela.title("📜 Histórico de Transações")
    historico_janela.geometry("400x300")
    historico_janela.config(bg="white")

    texto = "\n".join(historico) if historico else "Nenhuma transação realizada ainda."
    caixa_texto = scrolledtext.ScrolledText(historico_janela, font=("Arial", 12), wrap=tk.WORD, bg="#f7f7f7")
    caixa_texto.insert(tk.END, texto)
    caixa_texto.config(state="disabled")
    caixa_texto.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

def sair():
    janela.quit()

# Janela principal
janela = tk.Tk()
janela.title("💰 Simulador Bancário")
janela.geometry("350x500")
janela.configure(bg="#E3F2FD")  # azul claro

# Título
titulo = tk.Label(janela, text="💰 Simulador de Banco", font=("Arial", 18, "bold"), bg="#E3F2FD", fg="#0D47A1")
titulo.pack(pady=20)

# Função para criar botões estilizados
def criar_botao(texto, comando, cor="#1976D2"):
    return tk.Button(janela, text=texto, command=comando, width=25, height=2, bg=cor, fg="white",
                     activebackground="#1565C0", font=("Arial", 11, "bold"), bd=0, cursor="hand2")

# Botões
criar_botao("Ver Saldo 💳", ver_saldo).pack(pady=8)
criar_botao("Depositar Dinheiro 📥", depositar, cor="#388E3C").pack(pady=8)
criar_botao("Sacar Dinheiro 📤", sacar, cor="#E64A19").pack(pady=8)
criar_botao("PIX ✉️", realizar_pix, cor="#0288D1").pack(pady=8)
criar_botao("Ver Histórico 📜", ver_historico, cor="#5D4037").pack(pady=8)
criar_botao("Sair ❌", sair, cor="#B71C1C").pack(pady=20)

# Rodapé
rodape = tk.Label(janela, text="Desenvolvido por Guilherme Mello 🖥️", bg="#E3F2FD", font=("Arial", 9))
rodape.pack(side="bottom", pady=10)

# Iniciar app
janela.mainloop()
