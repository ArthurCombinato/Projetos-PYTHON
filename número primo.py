n1 = int(input('digite um número: '))
tot = 0
for c in range(1, n1 +1):
    if n1% c ==0:
        print('\033[33m',end='')
        tot+= 1
    else:
        print('\033[31m',end='')
    print('{}\033[m-'.format(c),end='')
print('\nO número {} foi divisivel {} vezes'.format(n1,tot))
if tot==2:
    print('E por isso ele é PRIMO!!')
else:
    print('E por isso ele não é PRIMO!!')