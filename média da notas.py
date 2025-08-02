import emoji

n1 = float(input('primeira nota:'))
n2 = float(input('segunda nota:'))

#calcular média
média = (n1 + n2)/2
print('Sua média foi {}'.format(média))

if média< 5:
    print(emoji.emojize('Você foi reprovado!😭'))
elif média >5 and média<= 6.9:
    print(emoji.emojize('Você está de recuperação!🙁'))
else:
    print(emoji.emojize('Parabens!! Você foi aprovado!🥳'))