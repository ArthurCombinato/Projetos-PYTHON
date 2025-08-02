total = 0
cont = 0
cont2 = 0
menor = 0
barato =''
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    cont2 += 1
    preço = int(input('Preço: R$'))
    total += preço
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()
    if preço > 100:
        cont += 1
    if cont2 == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome

    if resp == 'N':
        break
print('Total da compra foi R${}'.format(total))
print('Temos {} produtos custando mais de R$1000.00'.format(cont))
print(f'O produto mais barato foi {barato} que custa R${menor}')