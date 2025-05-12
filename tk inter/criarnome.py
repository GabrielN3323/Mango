import tkinter as tk

def mostrar_texto():
    texto_digitado = campo_entrada.get()
    print(f"texto digitado: {texto_digitado}")
    rotulo_feedback.config(text= f"voce digitou: {texto_digitado}")

janela = tk.Tk()

janela.title("entrada pelo usuario")
janela.geometry("400x300")

rotulo_instrucao = tk.Label(janela, text="digite seu nome")
rotulo_instrucao.pack()

campo_entrada = tk.Entry(janela)
campo_entrada.pack()

botao = tk.Button(janela, text="enviar", command=mostrar_texto)
botao.pack()

rotulo_feedback = tk.Label(text="")
rotulo_feedback.pack()

janela.mainloop()