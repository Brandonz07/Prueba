#prueba atletica con diferentes rondas (salto largo), promedio, puntaje mas alto y mas bajo

school_class = {}

while True:
    name = input("Ingresa el nombre del atleta: ")
    if name == '':
        break
    
    score = int(input("Ingresa la calificación del salto (0-10): "))
    if score not in range(0, 16):
	    break
    
    if name in school_class:
        school_class[name] += (score,)
    else:
        school_class[name] = (score,)
        
for name in sorted(school_class.keys()):
    adding = 0
    counter = 0
    for score in school_class[name]:
        adding += score
        counter += 1
    print(name, ":", adding / counter)
    
    print("promedio", name, ":", adding/counter)
        
        


