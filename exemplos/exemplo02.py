lista = ['caio', 'luan', 'bolas']

for i,item in enumerate(lista):
    print(i,  item,)

lista.sort()

print(len(lista))

if "luan" in lista:
    print("esta aqui")
else:
    print("ele nao esta aqui")