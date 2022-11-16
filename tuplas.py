#llenar una tupla con numeros aleatoreos entre 0 y 100 de 10 a 25 de tamaño y decir cuales son primos


import random

# p = []

# tupla = tuple(round(random.random()*100)for i in range(random.randint(10, 25)))

# print(tupla)

# for i in range (len(tupla)):
#     d = 0
#     for j in range(1, 101):
#         if tupla[i] % j == 0:
#             d += 1
#     if d == 2:
#         p.append(tupla[i])
        
# print("los numeros primos son: ", p ,"\nen total son: ", len(p))

tam = round(random.randint (5, 10))
tup = tuple(round(random.random()*100) for i in range (tam))
print(tup)
for i in tup:
    cont = 0
    for j in range (1,i):
        if i % j ==0:
            cont += 1
    if cont == 1:
        print("primo", i)