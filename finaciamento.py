valor = float(input('qual é o valora da casa?'))
salário = float(input('qual seu salário?'))
anos = float(input('em quantos anos deseja pagar?'))

#calculando o valor da prestação
prestação = valor/anos
mês = prestação/12

#calculando 30% do salário
s2 = salário * 0.30

if s2> mês:
    print('Seu financiamento foi aprovado')
else:
    print("infelizmente você não pode pagar")