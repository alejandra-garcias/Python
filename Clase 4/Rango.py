##permite establecer un rango de numero sin necesitar una lista o una variable
## los rangos comienzan en 0 y no incluye el ultimo numero
## puedes poner desde que numero quieres empezar (primer parametro, parametro hasta donde, parametro de cada cuanto es el salto)


### hacer una lista = 
lista = list(range(1,8))
print(lista)

##Práctica Rango 1-Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(2500,2586))
print(mi_lista)

##Práctica Rango 3.Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive). Almacena el resultado en una variable llamada suma_cuadrados.Para ello:Crea un rango de valores que puedas recorrer en un loopPara cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.
lista = list(range(1,16))
suma_cuadrados = 0

for element in lista:
        suma_cuadrados = element **2 + suma_cuadrados ## suma_cuadrados +=element **2

print(suma_cuadrados)
