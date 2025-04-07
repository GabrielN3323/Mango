itens = []
while True:
    pedir = input('insira algo: ')
    if pedir == 'fim':
        break
    else:
        itens.append(itens)
        print('a lista tem:',len(itens),'itens')