saldo = 0
result = 0
def reg_venda():
    print("~~"*15)
    print("Venda Registrada")
    print("~~"*15)

def total(valor1):
    global saldo
    saldo += valor1
    return saldo
def zerar_caixa():
    print("~~"*15)
    print("Caixa zerado")
    print("~~"*15)

while True:
    n1 = int(input('''Escolha uma opção
finalizar programa [0]
Registrar venda [1]
Mostrar saldo [2]
Zerar caixa [3]
'''))
    if n1 == 0:
        break
    elif n1 ==1:
        venda = float(input("Digite o valor da venda: "))
        reg_venda()
        result = total(venda)
    elif n1 ==2:
        print("~~"*15)
        print(f"Seu saldo é de {result}")
        print("~~"*15)
    elif n1 == 3:
        ler = input("tem certezar que quer zerar o caixa S/N").upper()
        if ler =="S":
            result = 0
            zerar_caixa()
        elif ler == "N":
            continue
        else:
            print("~~"*15)
            print("opção inválida")
            print("~~"*15)
    else:
        print("~~"*15)
        print("Opção inválida")
        print("~~"*15)