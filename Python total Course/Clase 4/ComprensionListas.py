###manera dinamica de construir listas
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)

print(lista) ####manera de convertir la palabra python en una lista letra por letra
##otra opcion mas corta=

lista = [letra for letra in palabra]
print(lista)

lista = [element for element in 'Python']
print(lista)

#############con numeros
lista = [n for n in range(0,21,2)] ## lista a igual todos los numeros pares que van del 0 al 21
print(lista)

#############con numeros
lista = [n/2 for n in range(0,21,2)] ## podemos alterar el numero
print(lista)

####
#############añadiendo un if
lista = [n for n in range(0,21,2) if n*2>10] ## se hace siempre que se cumpla una condicion
print(lista)

###si queremos añadir una condicion else seria:
lista = [n if n*2>10 else 'no' for n in range(0,21,2)] ### Incorporaremos a N siempre y cuando N por 2 sea mayor que 10 y sino pondremos la palabra no por cada n en el rango de 0 a 21

pies = [10,20,30,40,50]
metros = [p/3.281 for p in pies]
print(metros)

###Práctica Comprensión de Listas 1Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.

valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [numero ** 2 for numero in valores]
print(valores_cuadrado)

###Práctica Comprensión de Listas 2.Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [numero for numero in valores if numero % 2 == 0]
print(valores_pares)

##Práctica Comprensión de Listas 3.Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:°C = (°F - 32) * (5/9) expresado de otro modo:(grados_fahrenheit-32)*(5/9)La lista de temperaturas es la siguiente:temperatura_fahrenheit = [32, 212, 275] Almacena esta nueva lista en una variable llamada grados_celsius
temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(element - 32)*(5/9) for element in temperatura_fahrenheit ]
print(grados_celsius)