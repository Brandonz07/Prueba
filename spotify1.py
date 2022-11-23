#spotify

print ("""

🥵🥵🥵Welcome to spotify🥵🥵🥵

""")


print("""
1 - crear playlist
2 - abrir playlist 

    """)

lista = {}


def crear_playlist(lista):
    playlis = input("insertar nombre de la playlist: ")
    lista.update({"playlist":playlis})
    return new_artist

def new_artist(lista):
    artista =input("insertar nombre del artista: ")
    lista.update({crear_playlist(lista):{"artista":artista}})
    return lista

def seleccionar_pl():
    o = input("elige una opcion: ")

    if o == "1":
        crear_playlist(lista)
        new_artist(lista)
    elif o == "2":
        pass
    else:
        print("Escribe opcion valida")
        return seleccionar_pl

seleccionar_pl()
print(lista)
    




    
    


