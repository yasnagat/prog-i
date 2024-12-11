def primo(num):
    contador = 1
    soma = 0
    while num >= contador:
        if num % contador == 0:
            soma += 1
        contador += 1
    return soma == 2


# programa principal

lista = []
for i in range(3):
    lista.append(int(input("Digite um número: ")))

for i in range(len(lista)):
    if primo(lista[i]):
        print(lista[i], i)

