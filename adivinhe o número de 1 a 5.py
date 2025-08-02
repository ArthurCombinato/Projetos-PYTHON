import random
n1 = int(input('digite um número de 1 a 5  '))

lista = (1,2,3,4,5)

escolha = random.choice(lista)
if n1 == escolha:
    print('PARABÉNS você acertou!')
else:
    print('vecê errou! Tente novamente')