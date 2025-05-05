def cadastro (nome="Jao", ciaade="São Paulo"):
    print(f"{nome} mora em {ciaade}")
cadastro()

def desconto (preco, porcentual= 10):
    qbq = preco * porcentual/100
    valor_final = preco - qbq
    return valor_final
preco = desconto(100)

print(preco)


def prestacao (valor, dias, taxa= 0.01 ):
    return valor * (dias * taxa)

valor = float(input('Digite o valor da prestação: '))
dias = int(input('Quantos dias ja?: '))

resultado = prestacao(valor,dias)

print(f"o valor da sua multa é {resultado}")