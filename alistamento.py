idade = int(input('em que ano você nasceu?'))

alistar = 2024 - idade

f = alistar - 18
f2 = 18 - alistar

if alistar < 18:
    print('ainda falta {} anos para você se alistar'.format(f2))
elif alistar> 18:
    print('já passou {}anos do prazo de alistamento'.format(f))
else:
    print('Você está no ano certo para se alistar')