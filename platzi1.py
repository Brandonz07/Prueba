#conversor de monedas

"""cop = 4801.87

e = int(input("introduzca dolares: "))

print(cop*e)"""


def conversor (tipopesos, cop):
    pesos = int(input("introduzca pesos " + tipopesos + ": "))

    
    d = pesos / cop
    d = round(d, 2)

    print(d, "dolares")


m = """
conversor de monedas rata

1 - peso colombiano
2 - peso argentino
3 - peso mexicano

elige opcion: """

o = input(m)


if o == "1":
    conversor("colombianos", 4805.99) 

elif o == "2":
    conversor("argentinos", 160.31)
elif o == "3":
 conversor("mexicanos", 19.32)
else:
    print("introduzca opcion valida")




