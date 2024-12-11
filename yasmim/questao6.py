def linha(linhas):
    for j in range(1, linhas+1):
        print(j, end=" ")
    print("")

n = int(input("Numero de linhas: "))
for i in range(n+1):
    linha(i)
