import random

vec = []
c = 0
s = 0
p = 0
moda = 0
mediana = 0
d = 0

for i in range(10, 26):
    vec.insert(i,round(random.random()*100))
    
    
for i in range(len(vec)):
    c += 1
    s += vec[i]
    p = s // c
    
            




print(vec)
print("la suma de todos los numeros es: ",s)
print("el promedio de todos los numeros es: ",p)
print("la moda de todos los numeros es: ",moda)
print("la mediana de todos los numeros es: ",mediana)
print("la desviacion estandar de todos los numeros es: ",d)
print("vec[",i,"]= ", vec[i], "se repite", c, "veces")