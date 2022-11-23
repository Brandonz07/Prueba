def crear_artista(play, arti, gene, canc, dura):
    play.update ({
        arti:{
            "genero":gene,
            "canciones":{canc:dura}
        }
    })
    return play

crear_artista(1)