bd_pessoa = []

def cadastrodepessoa():

    linha = []

    print('bem vindo ao cadastro de pessoa')

    while True:

        print('se quiser voltar ao menu digite: "00"')

        opção = input('processeguir com o cadastro?')

        print()

        if opção == 00:
            break
        nome = input('digite o nome da pessoa: ')
        linha.append(nome)

cadastrodepessoa()