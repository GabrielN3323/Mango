listaPessoa = []

def InserirNome(Nome):
    if Nome != "":
        listaPessoa.append(Nome)
        print(f'O {Nome} está presente')

def removerNome(NomePessoa):
    if NomePessoa in listaPessoa:
        listaPessoa.remove(NomePessoa)
        print(f'O {NomePessoa} se retirou')
    else:
        print('Digite um nome valido')

def listar():
    for index,nome in enumerate(listaPessoa):
        print(index, nome)


while True:

         print('Escolha uma das opções: Procurar pessoa/ Remover pessoa/ Listar nome ')

         opções = input('escolhe uma das opções acima: ')

         if opções == "Procurar pessoa":
             pessoa = input('Digite nome da pessoa: ')

             InserirNome(pessoa)

         elif opções == "Remover pessoa":
             pessoa = input('Digite nome da pessoa que deseja ser removida: ')

             removerNome(pessoa)

         elif opções == "Listar nome":
             print(listar())

         else:
             print('invalido')