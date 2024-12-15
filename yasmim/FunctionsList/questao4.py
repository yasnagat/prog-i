

def celsius(f):
    print((f - 32) / 1.8)
def fahrenheit(c):
    print((c * 1.8) + 32)

temp = float(input("Temperatura para converter: "))
unid = input("Converter para qual medida? ")

if unid == "celsius":
    celsius(temp)
elif unid == "fahrenheit":
    fahrenheit(temp)
else:
    print("ERRO")
