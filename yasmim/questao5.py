def vetor(num):
    lista = []
    for i in range(num):
        lista.append(int(input("- ")))

    a = int(input("Digite o valor que você está procurando: "))

    for i in range(len(lista)):
        if a == lista[i]:
            print(i)
        else:
            print(-1)

# programa principal
tam = int(input("Digite o tamanho do vetor: "))

vetor(tam)

