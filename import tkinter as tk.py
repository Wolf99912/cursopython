import tkinter as tk
from tkinter import ttk

def processar():
    nome = entry_nome.get()
    label_resultado.config(texto=f"Dados processado "
                           f"até mais: {nome}")
    
janela = tk.Tk()
janela.title("Captura Dados")

label_nome = ttk.Label(janela, text="Nome: ")
label_nome.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_nome = ttk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)

botao_calcular = ttk.Button(janela, text="Processar", 
                            command=processar)
botao_calcular.grid(row=2, columnspan=2, padx=10, pady=10)
janela.mainloop()