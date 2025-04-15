def aprensentar(nome,idade,hobbie,voz):
    if voz == False:
        return ('precisa de interprete.')
    else:
        return(f'Olá, me chamo {nome}, tenho {idade} anos e meu hobbie é {hobbie}')

#print(aprensentar('Gabriel',15,'dormir',True))
#print(aprensentar('jose',45,'jogar',True))

def soma(numero1, numero2):
    return numero1 + numero2
resultado = soma(88,2)

print(resultado)
