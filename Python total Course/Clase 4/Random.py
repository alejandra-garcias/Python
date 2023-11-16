from random import *
###radint=>valor aleatorio entre 2 numeros
aleatorio = randint (5,555555555)
print(aleatorio)
##uniform->valor aleatorio con decimal
aleatorio  = uniform(1,5)
print(aleatorio)#### da muchos decimales, si quiero menos:

aleatorio  = round(uniform(1,5),1)##ultimo numero igual a cantidad de decimales
print(aleatorio)

###random
aleatorio = random()
##da un aleatorio entre 0 y 1

###choice ->trabaja con una seleccion aleatoria dentro de los elementos de una lista
colores = ['azul','amarillo','verde']
aleatorio = choice(colores)
####suffle->mezclar
numeros = list(range(5,50,5))##lista del 5 al 50 que avanza de 5 en 5
print(numeros)####[5, 10, 15, 20, 25, 30, 35, 40, 45]
##en cambio si en el medio usara el metodo shuffle:

numeros = list(range(5,50,5))
shuffle(numeros)### hace una mezcla aleatoria de dichos numeros
print(numeros)

###Práctica Random 1.Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10, y almacena dicho valor en una variable llamada aleatorio

aleatorio = randint(1,10)

###Práctica Random 2.Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1, y almacena dicho valor en una variable llamada aleatorio

aleatorio = random()

##Práctica Random 3Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación, y almacena el nombre escogido en una variable llamada sorteo.

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)