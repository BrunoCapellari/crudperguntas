import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *



def iniciar_interface():
    janela = tk.Tk()
    janela.title("CRUD de Perguntas")
    janela.geometry("850x500")


    # == Interface ==
    pergunta = StringVar()
    opcao1 = StringVar()
    opcao2= StringVar()
    opcao3= StringVar()
    correta= IntVar()

    frame = Frame(janela)
    frame.pack(fill="x", padx=10, pady=10)

    Label(janela, text="Cadastro / Edição de perguntas").pack()

    Label(frame, text="Pergunta:").grid(row=0, column=0)
    Entry(frame, textvariable=pergunta, width=30).grid(row=0, column=1, padx=10,)

    Label(frame, text="Opção 1: ").grid(row=1, column=0)
    Entry(frame, textvariable=opcao1, width=30).grid(row=1,column=1, padx=10)

    Label(frame, text="Opção 2: ").grid(row=1, column=2)
    Entry(frame, textvariable=opcao2,width=30).grid(row=1, column=3, padx=10)
    
    Label(frame, text="Opção 3: ").grid(row=2, column=0)
    Entry(frame, textvariable=opcao3, width=30).grid(row=2,column=1, padx=10)

    Label(frame, text="Alternativa Correta: ").grid(row=2, column=2)
    Entry(frame, textvariable=correta,width=30).grid(row=2,column=3,padx=10)

    treeview = ttk.Treeview(janela, columns=("pergunta", "opcao1", "opcao2", "opcao3", "correta"), show="headings")
    treeview.heading("pergunta",text="pergunta")
    treeview.heading("opcao1", text="Opção 1")
    treeview.heading("opcao2", text="Opção 2")
    treeview.heading("opcao3", text="Opção 3")
    treeview.heading("correta",text="Resposta")
    treeview.pack(fill="both",padx=10,pady=10)

    janela.mainloop()
iniciar_interface()