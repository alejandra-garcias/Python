mi_numero = 1 
print(mi_numero)
#type permite saber el tipo de dato de mi variable
print(type(mi_numero))

mi_numero2 = 1+3
print(mi_numero2 + mi_numero2) #resultado = 8


mi_numero = 5.8
print(mi_numero)
print(type(mi_numero))

mi_numero = mi_numero + mi_numero
print(mi_numero) 

edad = input("Dime tu edad: ")
print("Tu edad es " + edad)

#Práctica con Integers. Declara una variable numérica llamada num_entero que contenga un valor de tipo integer de tu elección.Imprime el tipo de dato de dicha variable.
num_entero = 2
print(type(num_entero))
 
#Práctica con Floats.Declara una variable numérica llamada num_decimal que contenga un valor de tipo float de tu elección.Imprime el tipo de dato de dicha variable.
num_decimal=1.5
print(type(num_decimal))


#Práctica con Tipos de Datos Numéricos¿De qué tipo es el resultado de la suma de 7.5 + 2.5? Genera el código para verificarlo.Para ello, crea dos variables:num1 = 7.5 y num2 = 2.5.A continuación, muestra en pantalla el tipo de dato que resulta de la suma de ambos números.
num1 = 7.5 
num2 = 2.5
print((num1+num2)) # la suma de esto da 10.0 por lo que el tipo sigue siendo "float"
print(type(num1+num2))
num3 = int(num1+num2)
print(type(num3))

# Práctica con Conversiones 1.Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:
num1 = 7.5
#opcion en dos lineas:
num1 = int(num1)
print(type(num1))

#opcion en una linea:
print(type(int(num1)))

#Práctica con Conversiones 2 .Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:
num2 = 10

print(type(float(num2)))
print(float(num2)) #10.0
num2 = num2+0.0 #10.0
print(num2)

#Práctica con Conversiones 3.Suma los valores de num1 y num2.No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().
num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))

