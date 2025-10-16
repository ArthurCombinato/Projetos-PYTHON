def caonversao_k(a):
    k = a + 273.15
    print(k)

def conversao_F(b):
    F = b *(9/5)+32
    print(F)

n1 = float(input("Digite o valor da temperatura: "))
converter = input("Dese converter em Farenheit [F] ou Kelvin [K]").upper()
if converter =="F":
    conversao_F(n1)
elif converter == "K":
    caonversao_k(n1)