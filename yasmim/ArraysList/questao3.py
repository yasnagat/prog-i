from random import randint

lista1 = []
lista2 = []

for i in range(3):
    lista1.append(randint(0, 10))
    lista2.append(randint(0, 10))

lista3 = []
somatotal = 0
for i in range(3):
    soma = lista1[i] + lista2[i]
    lista3.append(soma)
    somatotal += lista3[i]

print(lista1, lista2, lista3, somatotal)