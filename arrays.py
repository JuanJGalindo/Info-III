"""
Ejemplos: crear los siguientes vectores, matrices y tensores

vector1 = 1,2,3,4,5,6,100

vector2 = 10,20,30,40,50


matriz1 = [1 1 1
           1 1 1
           1 1 1]

matriz2 = [1 2 3
           4 5 6
           7 8 9]


tensor1=[[0 0 0
          0 0 0
          0 0 0]
         [2 2 2
          2 2 2
          2 2 2]] 

tensor2= [[1  2  3
           4  5  6
           7  8  9]
          [10 11 12
           13 14 15
           16 17 18]] 
"""
import numpy as np

#Cómo Crear Vectores
vector1 = np.array([1,2,3,4,5,6,100])
vector2 = np.array([10,20,30,40,50])


#Cómo Crear Matrices
matriz1 = np.array([[1, 1, 1],
                    [1, 1, 1],
                    [1, 1, 1]])

matriz2 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])


#Cómo Crear Temsores
tensor1=np.array([ [[0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]],

                    [[2, 2, 2],
                     [2, 2, 2],
                     [2, 2, 2]]
                ]) 

tensor2=np.array([ [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]],

                   [[10, 11, 12],
                    [13, 14, 15],
                    [16, 17, 18]]
                ]) 


"""
Ejemplo 2: Cómo crear los elementos anteriores de forma rápida
"""
vector1 = np.arange(1, 6, 1) #Inicio, Fin y Salto
vector2 = np.arange(10, 51, 10) 
#print(vector1, vector2) 

matriz1 = np.ones([3, 3])
matriz2 = np.arange(1, 10).reshape([3, 3]) #reshape(filas, columnas) = redimensiona el arreglo
#print(matriz1, matriz2)

tensor1 = np.zeros(18)
for i in range(10,19): tensor1[i-1]=2
tensor1=np.reshape(tensor1,[2,3,3])

tensor2 = np.arange(1, 19).reshape(2,3,3)
#print(tensor1)

"""
Ejemplo 3:
    a) Apilar los vectores para hacer uno más grande
    b) Apilar los vectores para crear una matriz
    c) Apilar las matrices horizontalmente
    d) Apilar las matrices verticalmente
    e) Apilar las matrices para crear un tensor
"""

vectorResultante = np.hstack((vector1, vector2))
#print(vectorResultante)

matrizResultante = np.vstack((vector1, vector2))
#print(matrizResultante)

matrizResultante2 = np.hstack((matriz1, matriz2))
#print(matrizResultante2) 

matrizResultante3 = np.vstack((matriz1, matriz2))
#print(matrizResultante3) 

tensorResultante = np.stack((matriz1, matriz2))
#print(tensorResultante)


vectorNuevo=np.array([1,2,3])
matrizNueva=np.arange(1,10).reshape((3, 3))

matrizNuevo1=np.vstack((matrizNueva, vectorNuevo))
#print(matrizNuevo1)

matrizNuevo2=np.hstack((matrizNueva, vectorNuevo.reshape((3,1))))
print(matrizNuevo2)