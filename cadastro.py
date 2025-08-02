print('-'*30)
print('     Cadastre uma pessoa')
print('-'*30)
cont1 = 0 # mais de 18 anos
cont2 = 0 # quantidade de homens cadastratos
cont3 = 0 # quantidade de melheres com mens de 20 anos
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [M/F] ')).strip().upper()[0]
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar?  [S/N]')).strip().upper()[0]
    print('~'*30)
    if idade > 18:
        cont1 += 1
    if sexo in 'Mm':
        cont2 += 1
    if sexo in 'Ff' and idade < 20:
        cont3 += 1
    if continuar in 'Nn':
        break
print('==== Fim do programa ====')
print('total de pessoas com mais de 18 anos: {}'.format(cont1))
print('Ao todo temos {} homens cadastrados'.format(cont2))
print('E temos {} mulheres com menos de 20 anos'.format(cont3))


