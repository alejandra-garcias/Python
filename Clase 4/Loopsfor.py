## loop for = se repiten una cantidad definida
lista = ['a','b','c']
for element in lista:
    numero_letra = lista.index(element)
    print(f"Las letras es {element}")
    print(f"Letra {numero_letra}:{element}")

lista2 = ['pablo','laura','pepe','jose']
for element in lista: 
    if element.startswith('l'):
        print(f'Tu nombre es {element}')
    else:
        print(f'No sabemos tu {element}') 

numeros = [1,2,3,4,5,6]   
mi_valor = 0
for element in numeros:
    mi_valor = mi_valor + element
    print(mi_valor)


palabras = 'python'
for element in palabras:
    print(element)

for element in [[1,2],[3,4],[5,6]]:
    print(element) ###[1,2]
                   ###[3,4]
                   ###[5,6]
for element1,element2 in [[1,2],[3,4],[5,6]]:
    print(element1)
    print(element2)

dic = {'clave1':'a','clave2':'b','clave3':'c' }

for element in dic:
    print(element) ###esto imprime solo las claves

for element in dic.items():
    print (element) ###('clave1', 'a')
                ###('clave2', 'b')
            ###('clave3', 'c')

for a,b in dic.items():
    print (a,b) ###clave1 a
            ###clave2 b
            ###clave3 c

####Práctica Loop For 1 - Utilizando loops For, saluda a todos los miembros de una clase, imprimiendo "Hola" + su nombre.Por ejemplo: "Hola María" 
alumnos_clase = ["María", "José", "Carlos", "Martina", "Isabel", "Tomás", "Daniela"]
for element in alumnos_clase:
    print(f"Hola {element}")

####Práctica Loop For 2 Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado de la suma en una variable llamada suma_numeros:

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for element in lista_numeros:
    suma_numeros = suma_numeros + element
    print(suma_numeros)


###Práctica Loop For 3 - Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables suma_pares y suma_impares respectivamente:lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es imparnum % 2 == 0 (valores pares)num % 2 == 1 (valores impares)
lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for element in lista_numeros:
    if element % 2 == 0:
        suma_pares = suma_pares + element
        print(suma_pares)
    else:
        suma_impares = suma_impares + element
        print(suma_impares)


