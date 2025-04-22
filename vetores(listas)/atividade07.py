listaComidas = []

print('seja Bem-vindo ao Icomidas')

def InserirComida(comida):
    if comida != "":
        listaComidas.append(comida)
        print(f'A {comida} foi adicionada no carrinho')

    else:
        print('não temos isso')

def RemoverComida(comida):
    if comida in listaComidas:
        listaComidas.remove(comida)
        print(f'{comida} foi tirada do carrinho')
    else:
        print('Digite algo que tenha no carrinhp')

def ListarComida():
    for index, comida in enumerate(listaComidas):
        print(index, comida)

while True:

    print('Escolha uma das opções: '
          'Adicionar item [1], '
          'Remover Item[2], '
          'Listar itens[3], '
          'Sair do Aplicativo[4] ')

    opções = input('escolhe uma das opções acima: ')

    if opções == "1":
        comida = input('Digite a comida: ')

        InserirComida(comida)

    elif opções == "2":
        pessoa = input('Digite a comida que deseja ser removida: ')

        RemoverComida(comida)

    elif opções == "3":
        print(ListarComida())

    elif opções == "4":
        print('saindo')
        exit()



    else:
        print('invalido')
