import tkinter as tk

def mostrar_texto():
    texto_digitado = campo_entrada.get()
    rotulo_feedback.config(texto=f"voce digitou: {mostrar_texto}")

janela = tk.Tk

janela.title('n sei')

janela.geometry('150x150')


janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=3)

rotulo_instrucao = tk.Label(janela, text="digite seu nome")
rotulo_instrucao.grid(row=0, column=0, padx=10, sticky="EW")

janela.mainloop()