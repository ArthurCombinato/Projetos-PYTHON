peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura em metros?'))

#calculo do imc
imc = peso/(altura**2)
print(' Seu imc é de {:.2f}'.format(imc))

if imc<18.5:
    print('Você está abaixo do peso!')
elif imc >= 18.5 and imc<=25:
    print('Você está no peso ideal')
elif imc > 25 and imc<= 30:
    print('Você está a cima do peso')
elif imc > 30 and imc <= 40:
    print('VOcê está com obesidade')
else:
    print('Você está com obesidade mórbida')