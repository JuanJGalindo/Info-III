"""Desarrolle las siguientes funciones: 
PARAMETRO DE ENTRADA     VALOR DE RETORNO       PROBLEMA
 * edad                     * booleano            * Función que determine si una persona es mayor de edad
 * nombre y salario         * string              * Función que reciba el nombre y salario de trabajador, y luego retorne una cadena con el mensaje: "hola <nombre>, su salario es <salario>"
 * numero                   * entero              * Función que calcule la suma de los digitos de un numero 
 * mensaje                  * booleano            * Función que determine si un mensaje tiene vocales o no
 * numero                   * lista               * Función que devuelva todos los divisores de un numero
 * numero                   * booleano            * Función para determinar si un número es primo
"""

def MayorEdad(edad):
    if edad<18:
        return False

    if edad>=18:
        return True


def Saludo(nombre, salario):
    return ('hola %s, su salario es %i'%(nombre, salario))


def SumaDigitos(numero):
    suma=0
    for i in range(len(numero)):
        suma+=int(numero[i])

    return suma


print(MayorEdad(18))
print(Saludo('Juan',7500000))
print(SumaDigitos('765'))
