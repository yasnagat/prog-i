lista = []
positivos = negativos = 0
for i in range(5):
    n = int(input("Nº: "))
    lista.append(n)
    if n > 0:
        positivos += 1
    else:
        negativos += n

print(positivos, negativos)
for i in range(len(lista) - 1, -1, -1):
    print(lista[i], end=" ")