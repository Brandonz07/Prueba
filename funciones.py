# def tdm(n):                               #tablas de multiplicar
#     for i in range(1, 11):
#         print(n, "*", i, "=", i*n) 
# tdm(5)


# def c():                                 #me regresa el texto
#     return "cursos de python"
# print(c())

# n = 5                                   #formas de mostrar una variable
# def f():
#     z = 15
#     print(n, m, z)
# m = 10
# f()

# def d():                               #que pasa si un parametro se llama igual que la variable
#     n = 2                              #R/ 2 \n2 \n4
#     print(n)
# d()
# n = 4
# d()
# print(n)

# def s(a, b):                          #una suma pero con return
#     return a+b
# r = s(4, 8)
# print(r)

import random                                       #creo una lista, luego la funcion
                                                    #con sort se ordena la lista
n = []                                              #creo la lista de pares e impares
                                                    #con el for determino si es o no par
for i in range(random.randint(10, 25)):             #con append se agregan
    n.insert(0, int(random.random()*100))           #con return para que vuelva los valores de la lista
                                                    #llamo a la funcion con la lista
def sl(l):
    l.sort()
    p = []
    im = []
    for i in l:
        if i % 2 == 0:
            p.append(i)
        else:
            im.append(i)
    return p, im

p, im = sl(n)

print("numeros pares: ",p,"\nnumeros impares: ",im)