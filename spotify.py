#spotify

print ("""

🥵🥵🥵Welcome to spotify🥵🥵🥵

""")


print("""
1 - crear playlist
2 - abrir playlist 

    Elige una opcion
    """)


lista = {}


def crear_playlist(lista):
    playlis = input("insertar nombre de la playlist: ")
    lista.update({playlis})
    return lista
    
    
crear_playlist(1)

