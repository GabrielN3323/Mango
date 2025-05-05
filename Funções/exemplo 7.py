def calcular_desconto(preco, percentual=10):
    desconto =preco * float(percentual/100)
    valor_final = preco - desconto
    return valor_final

preco1 = calcular_desconto(100)
preco2 = calcular_desconto(100, 20)

print(f"Preoço com 10$ de desconto: R${preco2}")