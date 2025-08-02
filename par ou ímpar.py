import random
lista = [1,2,3,4,5,6,7,8,9,10]
aleatório = random.choice(lista)
cont1 = 0
cont2 = 0
while True:
    n = int(input('Digite um valor: '))
    c = str(input('Par ou ìmpar? [P/I] ')).upper()
    print('-'*30)
    print('Voce Jogou {} e o computador {}. '.format(n,aleatório), end='')
    if (n + aleatório)%2 == 0:
        print('Total de {} deu par'.format(n+aleatório))
        print('-'*30)
        if c in 'Pp':
            print('VOCÊ VENCEU!!!')
            print('Vamos jogar novamente...')
            print('-='*30)
            cont1 += 1
        else:
            break
    else:
        print('Total de {} deu ímpar'.format(n + aleatório))
        if c in 'Ii':
            print('VOCÊ VENCEU!!!')
            print('Vamos jogar novamente...')
            print('-=' * 30)
            cont2 += 1
        else:
            break

print('GAME OVER! Você venceu {} vezes'.format(cont1+cont2))


