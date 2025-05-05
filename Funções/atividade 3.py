def multiplicacao(a,b):
    return(a * b)

resultado = multiplicacao(5,2)

print(resultado)

def media(nota1, nota2):
    return (nota1 * nota2)/2

resultad = media(10, 5)

print(resultad)

def calcularIMC(peso, altura ):
    imc = (peso / altura ** 2)
    return imc

iMc = calcularIMC(79, 1.78)

print(iMc)

if iMc <= 16:
    print('magreza grave')

elif iMc <= 25:
    print("peso ideal")

elif iMc <= 30:
    print('acima da media')

else:
    print('muito gordo')