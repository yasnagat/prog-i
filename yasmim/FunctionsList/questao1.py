def baixo(numero):
    print(int(n))
def cima(numero):
    print(int(n + 1))
def convencional(num):
    if (n - int(n)) < 0.5:
        baixo(n)
    else:
        cima(n)

n = float(input("Insira um número: "))

if n < 0:
    print("Por favor, digite um número positivo.")
else:
    baixo(n)
    cima(n)
    convencional(n)
    