def fatorial(num):
    contador = num
    fat = 1
    for i in range(num):
        fat *= contador
        contador -= 1
    return fat

def soma(a, b):
    print(a+b)

def subtracao(a, b):
    print(a-b)

def multiplicacao(a, b):
    print(a * b)

def divisao(a, b):
    print(a/b)

n1 = fatorial(int(input("Digite o primeiro numero: ")))
n2 = fatorial(int(input("Digite o segundo numero: ")))

choice = input("Qual operacao você quer realizar? ")

if choice == "+":
    soma(n1, n2)
elif choice == "-":
    subtracao(n1, n2)
elif choice == "*":
    multiplicacao(n1, n2)
elif choice == "/":
    divisao(n1, n2)
else:
    print("Digite uma operacao valida!")
