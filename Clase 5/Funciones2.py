def cifras(numero):
    '''Checkear 3 cifras'''
    return numero in range(100,1000)

resultado = cifras(65) ##falso
resultado = cifras(650) ##verdadero
suma = 155+444
resultado = suma ##falso

def cifras3(lista):
    '''Checkear 3 cifras'''
    for numero in lista:
        if numero in range (100,1000):
            return True
        else:
            pass
    return False ##lo pongo aqui para que me devuelva false una vex haya hecho todas las comprobaciones. Si lo pongo en el else daria false siempre

resultado = cifras3([55,14,122])##true

##si quiero que esta funcion me devuelva QUE cifras cumplen la condicion:
def cifras33(lista):
    '''Checkear 3 cifras'''
    lista3cifras= []
    for numero in lista:
        if numero in range (100,1000):
            lista3cifras.append(numero)
        else:
            pass
    return lista3cifras

resultado = cifras33([55,14,122])##122
print(resultado)

###Práctica Funciones Dinámicas 1Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.No invoques la función, solo es necesario definirla.
def todos_positivos (lista_numeros):
    '''devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo'''
    for numeros in lista_numeros:
        if numeros <0:
            return False
        else:
            pass
    return True

    
lista = todos_positivos([1,15,14,-5,4,7])
print(lista)

##Práctica Funciones Dinámicas 2-Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if (numero>0) and (numero<1000):
            suma+=(numero) ##con esto le sumo a suma cada numero que cumple la condicion de arriba
        else:
            pass
    return suma
resultado= suma_menores([1,1,1,1])
print(resultado)

##Práctica Funciones Dinámicas 3Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
def cantidad_pares(lista_numeros):
    pares = []
    for numero in lista_numeros:
        if numero % 2 ==0:
            pares.append(numero)
        else:
            pass
    return pares
print(cantidad_pares([4,8,6,5,7,4,6]))
