import random

tam = int(input("ingrese cantidad: "))
vec = []
c1 = 0
c2 = 0
s1 = 0
s2 = 0
p1 = 0
p2 = 0

for i in range(tam):
    vec.insert(i, round(random.random()*100))

print(vec)

for i in range(len(vec)):
    if vec[i]%2==0:
        c1 += 1
        s1 += vec[i]
        p1 = s1 // c1
        print(vec[i], "par",)
    else:
        c2 += 1
        s2 += vec[i]
        p2 = s2 // c2
        print(vec[i], "impar")
        
print("cantidad par:", c1, "\nsuma de los pares:",s1 ,"\ncantidad impar:", c2, "\nsuma de los impares", s2 )
print("el promedio de los numeros pares es: ", p1, "\nel promedio de los numeros impares es: ", p2)