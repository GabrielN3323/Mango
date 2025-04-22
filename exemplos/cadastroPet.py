listaNomePet = []

def listarPet():
    for index,nome in enumerate(listaNomePet):
        print(index, nome)

def inserirNome(nomePet):

    if nomePet != "":
        listaNomePet.append(nomePet)
        print(f'O pet {nomePet} foi cadastrado')
        listarPet()
    else:
        print('Insira o nome do Pet')

def removerPet(nomePet):
    if nomePet in listaNomePet:
        listaNomePet.remove(nomePet)
        print(f'O pet {nomePet} foi removido com sucesso')
    else:
        print('Digite um nome valido')

while True:

         print('Escreva uma das opções: Adicionar nome/ Remover nome/ Listar nome ')

         opções = input('escolhe uma das opções acima: ')

         if opções == "Adicionar nome":
             nomePet = input('Digite nome do pet: ')

             inserirNome(nomePet)

         elif opções == "Remover nome":

             nomePet = input('qual pet voce quuer remover?')

             removerPet(nomePet)

         elif opções == "listar nome":
             listarPet()
         else:
             print('invalido')
             break