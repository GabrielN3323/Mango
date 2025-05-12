import tkinter as tk

janela = tk.Tk()

janela.title("primeira janela")

janela.geometry("800x600")

rotulo = tk.Label(janela, text="Olá Mundo")

rotulo.pack()

def acao ():
    print("O botão foi printado")
    rotulo.config(text="botao clicado")

botao = tk.Button(janela, text="clique", command=acao)
botao.pack()

janela.mainloop()
