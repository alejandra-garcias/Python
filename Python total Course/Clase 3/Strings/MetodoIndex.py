#conocer el indice de un caracter
mi_texto = "hola"
resultado = mi_texto.index("o")
print(resultado) ##consola->>>1 (o esta en la posicion 1)
##saber que caracter hay en un indice
resultado = mi_texto[3] 
print(resultado) ##consola->>>a
##pruebas:
resultado = mi_texto[-1] 
print(resultado)
print(mi_texto.index("hol"))#aqui me indicaria donde empieza esto
print(mi_texto.index("hola"))#aqui me indicaria donde empieza esto
resultado = mi_texto.index("hola")
print(resultado)#aqui me indicaria donde empieza esto

### si hay una variable que repite letras python pararia la ejecicion al encontrar la primera. DISTINGUE ENTRE MAYUSCULAS Y MINUSCULAS. ejemplo:
mi_nombre = "alejandra"
print(mi_nombre.index("a"))## Daria 0
print(mi_nombre.index("a",3)) #aqui empieza a buscar desde la posicion 3 por lo que la primera a es la 4.
print(mi_nombre.index("a",3,5)) #la tercera coma indica hasta donde quiero que busque.No es inclusivo el 4, en este caso me daria error


### tambien tenemos el metodo rindex, que es reverse index. Es decir, busca de izquierda a derecha
print(mi_nombre.rindex("a"))
#Práctica Método Index() 1Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"
palabra = "ordenador"
print(palabra[5])

#Práctica Método Index() 2Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
print(frase.index("práctica"))
##Práctica Método Index() 3Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:
print(frase.rindex("práctica"))
