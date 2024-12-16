n = int(input("Digite um número inteiro, maior ou igual a 0: "))
maior = menor = n
if n >= 0:
    while n >= 0:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
        n = int(input(" "))
    print(maior, menor)
else:
    print("Número inválido!")