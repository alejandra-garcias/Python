mi_variable = "esta palabra sera extraida"
mi_variable[5:12] ## El primer numero mestra desde donde y el segundo hasta donde extraeremos sin incluirlo.
mi_variable[5:12] ## El primer numero mestra desde donde y el segundo hasta donde extraeremos sin incluirlo.
seleccion = mi_variable[2]
print(seleccion) ## t
seleccion = mi_variable[2:5]
print(seleccion) ## ta (incluye espacio pero no incluye la p que seria el 5)
seleccion = mi_variable[2:10:2]
print(seleccion) ## t aa. el ultimo 2 significa que va cogiendo de dos en dos, es decir se coge uno si uno no. si fuera de tres es decir el 1,2 no y el 3 si:
seleccion = mi_variable[2:10:3]
print(seleccion) ## tpa


###Práctica Sub-Strings 1Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:"Controlar la complejidad es la esencia de la programación"Pista: "Controlar" tiene un largo de 9 caracteres.
frase = "Controlar la complejidad es la esencia de la programación"
seleccion = frase[0:9]
print(seleccion)

##Práctica Sub-Strings 2Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
print(frase.rindex("a"))
seleccion = frase[8:66:3] ## seleccion = frase[8::3]
print(seleccion)
##Práctica Sub-Strings 3Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])