def divisor(vet1, vet2):
    return vet1 % vet2 == 0

lista1 = []
lista2 = []
for i in range(5):
    n = int(input("- "))
    if i < 3:
        lista1.append(n)
    else:
        lista2.append(n)


for i in range(min(len(lista1), len(lista2))):
    if divisor(lista1[i], lista2[i]):
        print(lista1[i], lista2[i])