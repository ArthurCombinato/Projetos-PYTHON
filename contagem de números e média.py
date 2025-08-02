c=1
n1 = 0
soma = 0
cont = 0
maior = 0
menor = 0
while c == 1:
    n1 = int(input('digite um número: '))
    print('-'*30)
    soma += n1
    cont += 1
    c = int(input('''Deseja continuar?
    [1] sim
    [2] não
    '''))
    print('-'*30)
    if cont == 1:
        maior = n1
        menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1


print(' Você escreveu {} números e a média entre eles foi {:.2f}'.format(cont,soma/cont))
print('''
Maior número: {}
Menor nùmero: {}'''.format(maior,menor))
