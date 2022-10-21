"""
Este módulo contiene 3 funciones:

* generarTableroLogico --> No recibe nada, 
                           Retorna una lista de None's

* insertarCaracterEnTablero --> Recibe lista, posicion y caracter
                                Retorna una lista actualizada con el nuevo caracter

* determinarGanador --> Recibe una lista (tablero)
                        Retorna un Ganador ("x", "o", None)

* mostrarGanador --> Recibe un Ganador
                     Retorna un mensaje de victoria al ganador
"""

def generarTableroLogico():
    tableroLogico=[None]*9

    return tableroLogico


def insertarCaracterEnTablero(tableroLogico:list, posicion:int, caracter:str):
    tableroLogico[posicion] = caracter

    return tableroLogico


def determinarGanador(tableroLogico:list):
    posicionesAComparar = [(0,1,2),
                           (3,4,5),
                           (6,7,8),
                           (0,3,6),
                           (1,4,7),
                           (2,5,8),
                           (0,4,8),
                           (2,4,6)]

    ganador=None
    for pos1, pos2, pos3 in posicionesAComparar:
        if tableroLogico[pos1] == tableroLogico[pos2] == tableroLogico[pos3] and tableroLogico[pos1] != None:
            ganador = tableroLogico[pos1]
            break
    
    return ganador

if __name__=="__main__":
    tablero = generarTableroLogico()
    print(tablero)
    
    tableroNuevo = insertarCaracterEnTablero(tablero, 2, "x")
    tableroNuevo = insertarCaracterEnTablero(tablero, 3, "x")
    tableroNuevo = insertarCaracterEnTablero(tablero, 6, "x")
    print(tablero)

    print(determinarGanador(tablero))