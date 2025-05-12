import tkinter as tk

janela = tk.Tk()
janela.title("Gabriel")
janela.geometry("800x600")

plo = tk.Label(janela, text="oi")
plo.pack()

def oloko ():
    print("botao foi feito")
    plo.config(text="me chamo Gabriel,"
                            "tenho 15 anos e "
                            "sla")

botao = tk.Button(janela, text="clique aqui", command=oloko)
botao.pack()

janela.mainloop()