texto="Este es el texto de Federico"
resultado = texto
print(resultado)
#------------------------------------------------------------
## Upper - Pasar a mayusculas
resultado =  texto.upper()
print(resultado)
resultado =  texto[2].upper()
print(resultado) ## aqui solo imprimiria en mayuscula la posicion 2, en este caso T- consola: T

#------------------------------------------------------------
##Lower -  Pasar a minuscula
texto="ESTE ES EL TEXTO DE FEDERICO"
resultado = texto.lower()
print(resultado)

#--------------------------------------------------------------
##Split - Separar en elementos y los guarda en una lista
resultado =  texto.split()
print(resultado) ## ['ESTE', 'ES', 'EL', 'TEXTO', 'DE', 'FEDERICO']
##puedes pasar por el parentesis lo que quieras que identifique como separador. Por defecto usa espacios vacios, pero....
texto = "ESTE ES EL TEXTO DE FEDERICO"
resultado = texto.split('T')
print(resultado) ## ['ES', 'E ES EL ', 'EX', 'O DE FEDERICO']

#----------------------------------------------------------------
##Join - Une
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d])
print(e) ### Aprender Python es genial
e = "-".join([a,b,c,d])
print(e) ##Aprender-Python-es-genial
#------------------------------------------------------------------
##Find - Es como index
resultado = texto.find('F')
##la diferencia con index es que si find no encuentra tu palabra te dara -1 como resultado
#------------------------------------------------------------------
##Replace - reemplazar, necesita parametros
resultado = texto.replace("FEDERICO","todos")
print(resultado)
resultado = texto.replace("E","XX")
print(resultado)



#####################

##Práctica Métodos de String 1Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

##Práctica Métodos de String 2.Une la siguiente lista en un string, separando cada elemento con un espacio. Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
e = " ".join(lista_palabras)
print(e)

##Práctica Métodos de String 3.Reemplaza en la siguiente frase:"Si la implementación es difícil de explicar, puede que sea una mala idea."los siguientes pares de palabras:"difícil" --> "fácil""mala" --> "buena"y muestra en pantalla la frase con ambas palabras modificadas.
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
print(frase.replace("difícil","fácil").replace("mala","buena"))