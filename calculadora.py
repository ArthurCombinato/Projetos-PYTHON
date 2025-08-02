n1 =1
n2 = 1
o=0

while o != 1 and o != 2 and o!=3 and o != 5:
    n1 = int(input('Primeiro valor:  '))
    n2 = int(input('Segundo valor:   '))
    o = int(input('''
    [1] Somar:
    [2] Multiplicar:
    [3] maior
    [4] Novos números
    [5] sair do programa
    Escolha uma opção:   '''))
    soma = n1 + n2
    multiplicação = n1 * n2

    if o ==1:
         print('   A soma vale {}'.format(soma))
    if o ==2:
        print('A multiplicação vale {} '.format(multiplicação))
    if o ==3:
        if n1>n2:
            print('O maior valor é o {}'.format(n1))
        else:
            print('O maior valor é o {}'.format(n2))