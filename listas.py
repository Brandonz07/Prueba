#laboratorio 3.4.1.6}

"""hat_list = [1, 2, 3, 4, 5]  # Esta es una lista existente de números ocultos en el sombrero.

n = int(input("introduzca un numero: "))
hat_list[2] = n 

del hat_list[4]

print("longitud de la lista: ", len(hat_list))

print(hat_list)"""

"""numbers = [111, 7, 2, 1]
print(len(numbers))
print(numbers)

###

numbers.append(4)

print(len(numbers))
print(numbers)

###

numbers.insert(0, 222)
print(len(numbers))
print(numbers)

#
numbers.insert(1, 333)
print(len(numbers))
print(numbers)"""

"""my_list = [10, 1, 8, 3, 5]
total = 0

for i in range(len(my_list)):
    total += my_list[i]

print(total)"""

"""my_list = [10, 1, 8, 3, 5]

my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]

print(my_list)"""


"""my_list = [10, 1, 8, 3, 5]
length = len(my_list)

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)"""


Beatles = []
print("Paso 1:", Beatles)

Beatles.append("john lennon")
Beatles.append("paul mccartney")
Beatles.append("george harrison")
print("Paso 2:", Beatles)

for i in range(2):
    Beatles.append (input("agregue a stu sutcliffe y pete best: "))
print("Paso 3:", Beatles)

del Beatles[3]
del Beatles[3]
print("Paso 4:", Beatles)

Beatles.insert(0, "ringo starr")
print("Paso 5:", Beatles)


print(len(Beatles))# probando la longitud de la lista
print("Los Fav", len(Beatles))

#lista = [] #se puede modificar y hacer de todo
#coleccion tupla = () #solo se puede buscar
#coleccion conjunto = set() y despues {} # no puden haber duplicados(porque solo muestra 1) ni listas
#coleccion diccionario = {} # tiene clave y valor
#diccionario = {"azul":"blue","rojo":"red"}
#print(diccionario["azul"]) # me muestra el valor = blue
# diccionario["amarillo"] = "yellow" # agrega nuevo elemento
# del(diccionario[#]) #se borra la calve
# conjunto = fronzenset(#) # vuelvo el conjunto inmutable(tupla)
#conjunto.add(#) #agrega el dato pero sin un orden especifico
#conjunto.discard(#) #eliminda el dato segun el nombre
#lista.clear # borra toda la lista
#lista.pop #borra un dato depende del indice
#lista.remove #borra un dato depende del nombre
#lista.index # buscar indice del dato
#lista.reverse # cambia el orden de la lista
#lista.sort #ordenar lista, (reverse=true) ordenar en orden decendente
#lista append # agregar un dato al final
#lista.insert # agregar un dato donde quiera (#, #) primero va el indice y luego el dato
#lista.extend # agregar lista
#lista.count # cuantas veces aparece el dato en la lista
#print(# in lista) # buscar ese dato en la lista
#len(lista) # cuantos datos hay en la lista
#lista = list(tuple) # pasar de lista a coleccion tupla y viceversa
#(elem) in (lista) # para saber si un elemento esta dentro de la lista
#(elem) not in (lista) # para saber si un elemento no esta dentro de la lista


# my_list = [8, 10, 6, 2, 4]  # lista a ordenar
# swapped = True  # Lo necesitamos verdadero (True) para ingresar al bucle while.

# while swapped:
#     swapped = False  # no hay intercambios hasta ahora
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True  # ¡ocurrió el intercambio!
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print(my_list)


# my_list = []
# swapped = True
# num =int(input("¿Cuántos elementos deseas ordenar?: "))

# for i in range(num):
#     val = float(input("Ingresa un elemento de la lista: "))
#     my_list.append(val)

# while swapped:
#     swapped = False
#     for i in range(len(my_list) - 1):
#         if my_list[i] > my_list[i + 1]:
#             swapped = True
#             my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]

# print("\nOrdenada:")
# print(my_list) 


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5
# found = False

# for i in range(len(my_list)):
#     found = my_list[i] == to_find
#     if found:
#         break

# if found:
#     print("Elemento encontrado en el índice", i)
# else:
#     print("ausente")



