from random import randint
import time
itens = ('Pedra', 'Papel', 'tesoura')
aleatório = randint(0,2)
c = 1
while c == 1:
    print('\033[1;34;40m O jogo começou:\033[m')
    print('''Suas opções
    [ 0 ] pedra
    [ 1 ] papel
    [ 2 ] tesoura''')
    jogador = int(input('Qual é sua jogada: '))
    print('JO')
    time.sleep(1)
    print('KEN')
    time.sleep(1)
    print('PO!!!')
    print('-='*11)
    print('computador jogou {}'.format(itens[aleatório]))
    if jogador == 0 or jogador == 1 or jogador == 2:
        print('jogador jogou {}'.format(itens[jogador]))
    else:
        print('JOGADA INVÁLIDA!!!!')
    print('-='*11)
    if aleatório == 0: #computador jogou pedra
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        elif jogador == 2:
            print('VOCÊ PERDEU!')
        else:
            print('tente novamente!')
    elif aleatório == 1: #computador jogou papel
        if jogador == 0:
            print('VOCÊ PERDEU!')

        elif jogador == 1:
            print('DEU EMPATE!')

        elif jogador == 2:
            print('VOCÊ VENCEU!')

        else:
            print('tente novamente!')
    elif aleatório == 2: #computador jogou tesoura
        if jogador == 0:
            print('VOCÊ VENCEU!')

        elif jogador == 1:
            print('VOCÊ PERDEU!')

        elif jogador == 2:
            print('DEU EMPATE!')

        else:
            print('tente novamente!')
    print('~'*30)
    c = int(input('''Quer jogar novamente?
[1] Sim
[2] Não
'''))
    print('~'*30)
print('FIM!!!!')