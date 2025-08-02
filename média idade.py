somaidade = 0
media = 0
maioridadehomen = 0
nomevelho = ''
mulher = 0
for p in range(1,5):
    print('{}ª pessoa:'.format(p))
    nome = str(input('nome: ')).strip()
    idade = int(input('idade: '))
    sexo = str(input('sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomen:
        maioridadehomen = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulher += 1


media = somaidade/4
print('A media de idade do grupo é de {} anos.'.format(media))
print('O homen mais velho tem {} anos e se chama {}.'.format(maioridadehomen,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(mulher))
