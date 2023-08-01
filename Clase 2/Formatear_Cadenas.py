x=10
y=5
#Manera antigua no practica:
print("Mis numeros son{}y{}".format(x,y)) #Consola: Mis numeros son 5y10
print("Mis numeros son{}y{} y suman{}".format(x,y, x+y))

######FORMA ACTUAL CORRECTA Y VISIBLE
color = "rojo"
matricula = 151132
print(f"El auto es {color} y la matricula es {matricula}")

#Práctica Formatear Cadenas 1.Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")
print("Estimado/a {}, su número de asociado es: {}".format(nombre_asociado,numero_asociado))
#Práctica Formatear Cadenas 2.Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos.
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_totales))

#Práctica Formatear Cadenas 3.Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntosEn esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.

puntos_anteriores = 875
puntos_nuevos = 350
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos")
print("Has ganado {} puntos! En total, acumulas {} puntos".format(puntos_nuevos,puntos_nuevos+puntos_anteriores))