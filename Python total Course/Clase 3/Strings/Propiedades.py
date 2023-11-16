## son inmutibales
## se pueden multiplicar string
n1="Alejandra"
print(n1 *10) ##AlejandraAlejandraAlejandraAlejandraAlejandraAlejandraAlejandraAlejandraAlejandraAlejandra

poema = """Mil pequeños peces blancos
como si hirviera
el color del agua
"""
print(poema)
print("agua" in poema)
print ("agua" not in poema)
print ("ghf" not in poema)
print (len(poema))

##Práctica Propiedades de Strings 1 .Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla. Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad de forma simple y elegante.
print("Repetición" * 15)

##Práctica Propiedades de Strings 2-Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
print("agua" not in("""Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""))

##Práctica Propiedades de Strings 3.Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
print(len("electroencefalografista"))
