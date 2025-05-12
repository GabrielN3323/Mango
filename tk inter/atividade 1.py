import tkinter as tk

janela = tk.Tk()

def soma():
    num1= int(entrada1.get())
    num2= int(entrada2.get())
    print(f"Resultado: {num1}")
    print(f"Resultado: {num2}")

    rotulo_feedback.config(text=f"Resultado: {num1 + num2}")

janela.title("soma")
janela.geometry("400x300")

num1 = tk.Label(janela, text="numero 1")
num1.pack()

entrada1 = tk.Entry(janela)
entrada1.pack()

num2 = tk.Label(janela, text="numero 2")
num2.pack()

entrada2 = tk.Entry(janela)
entrada2.pack()

botao = tk.Button(janela, text="somar", command=soma)
botao.pack()

rotulo_feedback = tk.Label(text="")
rotulo_feedback.pack()

janela.mainloop()