preço = float(input('Qual é o preço do produto?'))
condição = (input('Qual é  condição de pagamento?'))

#dinheiro ou cheque
dc = preço-(preço*0.10)

# à vista no cartão
Ca = preço-(preço*0.05)

#2x no cartão
cx1 = preço/2

#3x no cartão
cx = (preço* 0.20)+(preço/3)
total = cx * 3

if condição == 'dinheiro' or condição == 'cheque':
    print('o valor total ficou {}reais com 10% de desconto'.format(dc))
elif condição == 'cartão':
    print('o valor total ficou {}reais com 5% de desconto'.format(Ca))
elif condição == '2x no cartão':
    print('o valor de cada parcela ficou {}reais sem juros'.format(cx1))
else:
    print(' o valor de cada parcela ficou {:.2f}reais com 20% de juros\n O valor total ficou {:.2f}'
          .format(cx, total))
