total = 0
totalpar = 0 
totalimpar = 0
resultpar = 0
resultimpar = 0
def somatotal(a):
    global total
    total += a
    return total

def somapar(b ):
    global totalpar
    totalpar += b
    return totalpar

def somaimpar(c ):
    global totalimpar
    totalimpar += c
    return totalimpar

while True:
    n1 = float(input("Digite um número: "))
    if n1 == 0:
        break
    elif n1 % 2 == 0:
        resultpar = somapar(n1)
        result = somatotal(n1)
        
    else:
        resultimpar = somaimpar(n1)
        result = somatotal(n1)
print(f" A soma total é : {result}")
print(f"A soma dos números pares é: {resultpar}")
print(f"A soma dos númerps ímpares é {resultimpar}")
