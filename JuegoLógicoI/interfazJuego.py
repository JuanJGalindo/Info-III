"""
Aquí contenemos la parte visual del Triki. Este módulo contiene dos funciones:

    * explicarJuego: retornar mensaje explicativo
    * imprimirTablero: retornar string con el tablero
"""

def explicarJuego():
    explicacion="""
    =========================================================
    Bienvenido, eso es Triki.

    Para ganar, debe completar una línea recta (Vertical, Horizontal o Diagonal),
    compuesta por un mismo carácter: "x" ó "o"

    Debe ingresar la posición 0-8, para ingresar la opción en el lugar requerido durante su turno.
    Las posiciones son las siguientes:
      

    tablero  =>   0 | 1 | 2  
                -------------
                  3 | 4 | 5  
                -------------
                  6 | 7 | 8  

 ============================================
    """

    print(explicacion)
 

def ImprimirTablero(tableroLogico:list):
    tableroVisual="""
                  %s | %s | %s  
                -------------
                  %s | %s | %s  
                -------------
                  %s | %s | %s  """%(tableroLogico[0],tableroLogico[1],tableroLogico[2],
                                           tableroLogico[3],tableroLogico[4],tableroLogico[5],
                                           tableroLogico[6],tableroLogico[7],tableroLogico[8])

    tableroVisual = tableroVisual.replace("None"," ")
    print(tableroVisual)

if __name__== "__main__":
    explicarJuego()
    tableroLogico=["x","o","x",None,None,"o",None,"x",None]
    ImprimirTablero(tableroLogico)

    

