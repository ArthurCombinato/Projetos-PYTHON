n1= int(input('qual a velocidade do seu carro'))
#caucular a multa
m = (n1-80)*7
if n1 >80:
    print('Você foi multado')
    print('A multa custará {}reais'.format(m))
else:
    print('OK! Boa viagem')