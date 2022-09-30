"""
Crear las siguientes listas:

lista1 = [1,2,3,4,5,6,7,8]
lista2 = list(range(20)) + ["a", "b", "c", 100]
lista3 = ["cruel", "mundo", "hola", 1, 100, 200, 500]

Realice lo siguiente:

- Agregar a lista1, los elementos => 1,2,3,4
- Agregar al comienzo de la lista1, los elementos => 0,0,2,4
- Eliminar los 3 últimos elementos de la lista1
- Eliminar los 2 primeros elementos de lista1


- Sume todos los elementos de la lista2 que pueden operarse algebraicamente
- Organice lista2 de forma ascendente
- Elimine todos los elementos de la lista2 original que son enteros


- Sume todos los elementos de la lista3 que pueden operarse algebraicamente
  sin afectar ni cambiar lista3 original
- Haga una copia de lista3 de la siguiente manera:
    lista3copia = lista3
  Y agregue 3 nuevos elementos sobre esta nueva lista.
  ¿Qué sucede con la lista3 original?
- Encuentre una manera de alterar la copia sin afectar la lista original


INDEXADO ==> Extraer el elemento inicial de lista1 (de dos maneras)
             Extraer el elemento final de lista1 (de dos maneras)
             Extraer el elemento del medio de lista2 (de dos maneras)

SLICING  ==> Extraer los 3 primeros elementos de lista1, lista2 y lista3 y colocarlos en una nuevaLista
             Extraer cada dos elementos de lista2
             Extraer todos los elementos de lista3 al revés
             Extraer los elementos de lista3 ubicados en índices impares
"""

lista1 = [1,2,3,4,5,6,7,8]
lista2 = list(range(20)) + ["a", "b", "c", 100]
lista3 = ["cruel", "mundo", "hola", 1, 100, 200, 500]

#Agregar a lista1, los elementos => 1,2,3,4
lista1.append(0)
lista1[8:]=[1,2,3,4]

#Agregar al comienzo de la lista1, los elementos => 0,0,2,4
lista1_1=[0,0,2,4]
lista1_1.extend(lista1)
lista1=lista1_1

#Eliminar los 3 últimos elementos de la lista1
for i in range(3):
    lista1.pop()

#Eliminar los 2 primeros elementos de lista1
for i in range(2):
    lista1.pop(0)


print(lista1)



#Sume todos los elementos de la lista2 que pueden operarse algebraicamente
suma=0
for i in range(len(lista2)):
    if type(lista2[i]) == int:
        suma+=lista2[i]

#Organice lista2 de forma ascendente
lista2_1=lista2
lista2_1.remove("a")
lista2_1.remove("b")
lista2_1.remove("c")
lista2=lista2_1
lista2.extend(["a","b","c"])

#Elimine todos los elementos de la lista2 original que son enteros
listaApoyo=[]
for elemento in lista2:
    if type(elemento)==str:
        listaApoyo.append(elemento)

lista2=listaApoyo
    

print(lista2)



#Código lista3


