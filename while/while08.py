while True:
    numero1 = float(input("coloque o numero: "))
    numero2 = float(input("coloque o numero: "))
    operação = input("coloque a operação: ")

    if operação == '+':
        print(numero1 + numero2)

    elif operação == '-':
        print(numero1 - numero2)

    elif operação == '*':
        print(numero1 * numero2)

    elif operação == '/':
        print(numero1 / numero2)

        break

    else:
        print('erro')