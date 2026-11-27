import tkinter as tk
from tkinter import messagebox

def calcular(operacao):
    try:
        # Pega os valores inseridos e converte para float (permitindo decimais)
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        match operacao:
            case "+":
                res = num1 + num2
            case "-":
                res = num1 - num2
            case "*":
                res = num1 * num2
            case "/":
                if num2 != 0:
                    res = num1 / num2
                else:
                    messagebox.showerror("Erro", "Divisão por zero não permitida!")
                    return
        
        # Exibe o resultado na tela
        lbl_resultado.config(text=f"Resultado: {res}")
        
    except ValueError:
        messagebox.showerror("Erro", "Por favor, digite apenas números válidos.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("300x300")
janela.config(padx=20, pady=20)

# Campo para o primeiro número
tk.Label(janela, text="Primeiro número:").pack(anchor="w")
entry_num1 = tk.Entry(janela, width=25)
entry_num1.pack(pady=5)

# Campo para o segundo número
tk.Label(janela, text="Segundo número:").pack(anchor="w")
entry_num2 = tk.Entry(janela, width=25)
entry_num2.pack(pady=5)

# Frame para agrupar os botões de operação lado a lado
frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=10)

btn_soma = tk.Button(frame_botoes, text="+", width=5, command=lambda: calcular("+"))
btn_soma.grid(row=0, column=0, padx=2)

btn_sub = tk.Button(frame_botoes, text="-", width=5, command=lambda: calcular("-"))
btn_sub.grid(row=0, column=1, padx=2)

btn_mult = tk.Button(frame_botoes, text="*", width=5, command=lambda: calcular("*"))
btn_mult.grid(row=0, column=2, padx=2)

btn_div = tk.Button(frame_botoes, text="/", width=5, command=lambda: calcular("/"))
btn_div.grid(row=0, column=3, padx=2)

# Rótulo para mostrar o resultado
lbl_resultado = tk.Label(janela, text="Resultado: ", font=("Arial", 12, "bold"))
lbl_resultado.pack(pady=20)

# Inicia o loop da aplicação
janela.mainloop()