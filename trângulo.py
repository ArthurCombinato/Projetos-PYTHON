n1= int(input('primeira reta:'))
n2 = int(input('segunda reta'))
n3 = int(input('terceira reta'))


if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print('estas retas podem formar um triângulo ', end='')
    if n1== n2== n3:
        print('Equilátero')
    elif n1 != n2 != n3:
        print('Escaleno')
    else:
        print('Isóceles')

else:
    print('estas retas não podem formar um triângulo')
