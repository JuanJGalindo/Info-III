import math as m
"""
Imprimir las variables Pi y Euler, ejecutar al menos una función del módulo
"""

#print('Pi => %f'%(m.pi))
#print('Euler => %f'%(m.e))
#print('seno(pi/2) => %f'%(m.sin(m.pi/2)))



import random as rd

"""
Imprimir diez números aleatorios. Opciones: flotante del 0 al 1
Imprimir un número aleatorio. Opciones: 1,2,3,4,5
Imprimir un caracter aleatorio: Opciones: "a", "b", "c"
"""

#for i in range(11):
#    numeroAleatorio = rd.random()
#    print(numeroAleatorio)
#
#print(rd.choice([1,2,3,4,5]))
#
#print(rd.choice(["a", "b", "c"]))



import tqdm
from tqdm import trange

#for i in trange(100000000):
#    10*5
#print('Proceso Terminado')



import calendar

#print(calendar.calendar(2022))



"""
Utilizar la estructura básica de Numpy: Un arreglo
Luego, graficar usando matplotlib la función x**2 + 1
"""

import numpy as np
import matplotlib.pyplot as plt

arreglo1=np.array([1,2,3,4,5])
arreglo2=np.linspace(1,50,100)
arreglo3 = arreglo2**2

plt.figure()
plt.plot(arreglo2, arreglo3)
plt.show()


#x = np.linspace(0, 10, 10)
#plt.plot(x, x**2 + 1)

#plt.show()


#print(dir(m))
#print(help(rd.random()))


