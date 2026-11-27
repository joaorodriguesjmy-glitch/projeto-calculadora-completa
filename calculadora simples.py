import tkinter as tk
from tkinter import messagebox

class CalculadoraCompleta:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora Completa")
        master.geometry("320x440")
        master.config(padx=15, pady=15)
        
        self.expressao = ""
        
        # Display de entrada e resultado
        self.display = tk.Entry(master, font=("Arial", 22), justify="right", bd=5, relief=tk.SUNKEN)
        self.display.pack(fill=tk.X, pady=(0, 15), ipady=10)
        
        # Frame para os botões
        self.frame_botoes = tk.Frame(master)
        self.frame_botoes.pack(fill=tk.BOTH, expand=True)
        
        # Matriz de botões da calculadora
        botoes_grid = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "C", "+"]
        ]
        
        # Criando e posicionando os botões em grade
        for linha_idx, linha in enumerate(botoes_grid):
            self.frame_botoes.rowconfigure(linha_idx, weight=1)
            for coluna_idx, texto in enumerate(linha):
                self.frame_botoes.columnconfigure(coluna_idx, weight=1)
                
                # Definindo cores especiais para o botão 'C'
                cor_fundo = "#ffcccc" if texto == "C" else "#f0f0f0"
                
                btn = tk.Button(self.frame_botoes, text=texto, font=("Arial", 16, "bold"), 
                                bg=cor_fundo,
                                command=lambda t=texto: self.clique_botao(t))
                btn.grid(row=linha_idx, column=coluna_idx, sticky="nsew", padx=3, pady=3)
        
        # Botão de igual em destaque na parte inferior
        self.btn_igual = tk.Button(master, text="=", font=("Arial", 18, "bold"), bg="#4CAF50", fg="white",
                                   command=self.calcular_resultado)
        self.btn_igual.pack(fill=tk.X, pady=(10, 0), ipady=8)

    def clique_botao(self, valor):
        if valor == "C":
            self.expressao = ""
            self.display.delete(0, tk.END)
        else:
            self.expressao += str(valor)
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, self.expressao)

    def calcular_resultado(self):
        try:
            # A função eval calcula a expressão matemática digitada no display
            resultado = str(eval(self.expressao))
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, resultado)
            self.expressao = resultado
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não é permitida.")
            self.expressao = ""
            self.display.delete(0, tk.END)
        except Exception:
            messagebox.showerror("Erro", "Expressão inválida.")
            self.expressao = ""
            self.display.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraCompleta(root)
    root.mainloop()