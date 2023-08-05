#puede haber listas hechas de listas.pueden estar formadas por diferentes tipos de datos
mi_lista = ['a','b','c']
otra_lista = ['a',5,6.52]
print(len(mi_lista))
print(mi_lista[0])
print(mi_lista[0:2])
print(mi_lista[0:])
print(mi_lista+otra_lista) ## da una sola lista
mi_lista3=mi_lista+otra_lista

## si son alterables
mi_lista3[1]='alfa'
print(mi_lista3) ##['a', 'alfa', 'c', 'a', 5, 6.52]

##append
mi_lista3.append('g') ## añade al final el elemento que pongas en el parentesis
print(mi_lista3)
mi_lista3.pop()## eliminas un elemento de la lista. Por defecto es el ultimo, sino puedes poner dentro del parentesesis que elemento quieres eliminar.
## se puede almacenar lo eliminado en otra variable. Ej:
eliminado = mi_lista3.pop(0)
print(eliminado)##a


### sort
lista = ['g','o','b','m','c']
lista.sort()
print(lista)

## reverse
lista.reverse()

## tanto sort como reverse no devuelven nada, es decir un objeto none


##Práctica Listas 1-Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.
mi_lista = ['hola', 23, 0.5,True,['5',5]]

##Práctica Listas 2 Agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

##Práctica Listas 3.Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(frutas)
print(eliminado)