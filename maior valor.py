n1 = int(input('primeiro número: '))
n2 = int(input('segundo número: '))
n3 = int(input('terceiro número'))

if n1>n2 and n1>n3:
    print('maior número: {}'.format(n1))
if n2>n1 and n2>n3:
    print('maior número: {}'.format(n2))
if n3>n1 and n3>n2:
    print('maior número: {}'.format(n3))

if n1<n2 and n1<n3:
    menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('menor valor: {}'.format(menor))
