lista = ['caio', 'luan', 'bolas']

for i,item in enumerate(lista):
    print(i,  item,)

lista.sort()

print(len(lista))

if "luan" in lista:
    posicao = lista.index("luan")
    lista[posicao] = "marcola"

print(lista)