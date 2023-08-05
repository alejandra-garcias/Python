##listas inutables. Puedes encerrarlos en las () o sin nada. Ocupan menos que las listas
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
t=(5,'jajaja',[1,2,3],2.03,(1,2,3,5,66666666))
print(t[4][4])##6666666666


#Casting= formar mi tupple en lista
t=list(t)
print(type(t))
t=tuple(t)
print(type(t))
###Se puede asignar el contenido de un tupple a diferentes varibales
t=(1,2,3)
x,y,z=t
print(x,y,z)

#METODOS

print(t.count(1)) ##saber cuantas veces aparece el parametro que hay dentro de los parentesis
print(t.index(2))##saber que hay en el indice que esta en el parentesis

##Práctica Tuples 1.Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))
##Práctica Tuples 2.Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

##Práctica Tuples 3.Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
mi_tupla = (1, 2, 3, 4)
a,b,c,d=mi_tupla
