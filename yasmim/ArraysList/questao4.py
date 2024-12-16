# desafio
from random import randint

lista = []
cont = 0

for i in range(10):
    lista.append(randint(1,10))
print(lista)

while 1 in lista:
    for i in range(10):
        lista[i] = lista[i] - 1
        if lista[i] == 0:
            cont += 1
print(lista, cont)