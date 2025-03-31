numero = int(input("Digite um numero positivo: "))
while numero <= 0:
    print("Valor invalido")
    numero = int(input("Digite um numero positivo:-1 "))
print(f"Você digitou: {numero}")