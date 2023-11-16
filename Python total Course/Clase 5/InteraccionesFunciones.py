from random import *

##lista inicial 
palitos = ['-','--','---','----']

##mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return(lista)

##pedirle intento
def suerte():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Elige un numero del 1 y el 4: ')
    return int(intento)


##comprobar intentos
def chequearintento(lista,intento):
    if lista[intento -1 ] == '-':
        print('Has perdido')
    else:
        print('Esta vez te has salvado')
    
    print(f"te ha tocado {lista[intento-1]}")


palitos_mezclados=mezclar(palitos)
seleccion = suerte()
chequearintento(palitos_mezclados,seleccion)

###El hecho de que uses intento - 1 en tu código se debe a que las listas en Python están indexadas desde cero. Esto significa que el primer elemento de la lista tiene un índice de 0, el segundo elemento tiene un índice de 1, y así sucesivamente.

##En tu código, estás pidiendo al usuario que elija un número del 1 al 4 (esto corresponde a las opciones 1, 2, 3 y 4). Sin embargo, para acceder a los elementos en la lista, necesitas restar 1 al valor del intento del usuario para obtener el índice correcto.

##Por ejemplo:

##Si el usuario elige 1, en realidad se debe acceder al elemento en el índice 0 de la lista.
##Si el usuario elige 2, se debe acceder al elemento en el índice 1 de la lista.
##Y así sucesivamente.
##De ahí la necesidad de usar intento - 1 para ajustar el valor ingresado por el usuario al índice adecuado en la lista. Sin este ajuste, estarías tratando de acceder a elementos que no son los que deseas verificar en función de la elección del usuario.

###Práctica sobre Interacción entre Funciones 1.Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:Si la suma es menor o igual a 6:"La suma de tus dados es {suma_dados}. Lamentable"Si la suma es mayor a 6 y menor a 10:"La suma de tus dados es {suma_dados}. Tienes buenas chances"Si la suma es mayor o igual a 10:"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"Pistas: utiliza el método choice o randint de la biblioteca random para elegir un valor al azar entre 1 y 6.+

def lanzar_dados ():
    '''Lanza dados y genera dos nuemeros aleatorios'''
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return (dado1,dado2)


def evaluar_jugada (dado1,dado2):
    '''evalua los resultados posibles'''
    sumadados = dado1 + dado2
    if sumadados <= 6:
        return(f'La suma de tus dados es {sumadados}. Lamentable')
    elif (sumadados >6) and (sumadados<10):
        return(f"La suma de tus dados es {sumadados}.Tienes buenas chances")
    else:
        return{f"La suma de tus dados es{sumadados}.Parece una jugada ganadora"}


##tengo que declarar dado1 y dado2 y como quiero obtenerlos de lanzar dados, especifico que dado1 y 2= funcionlanzardados(que retornaba 2 valores numericos)
dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1,dado2))
########


####Práctica sobre Interacción entre Funciones 2Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.
lista_numeros = [1,2,15,7,2]
def reducir_lista(lista_numeros):
    '''Elimina duplicados y numero mas alto'''
    nueva_lista = []
    for element in lista_numeros:
        if element in nueva_lista:
            nueva_lista.remove(element)
        else:
            nueva_lista.append(element)
    nueva_lista.sort()
    nueva_lista.pop(-1)
    return nueva_lista

print(reducir_lista(lista_numeros))


##Práctica sobre Interacción entre Funciones 3Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.Pistas: utiliza el método choice de la biblioteca random para elegir un elemento al azar de una secuencia.
lista_numeros=[1,2,3,4,5,6,7,8,9]
def lanzar_moneda():
    moneda = ["Cara","Cruz"]
    resultado = choice(moneda)
    return resultado

def probada_suerta(lanzamiento,lista):
    if lanzamiento =="Cara":
        lista = []
        return (f'La {lista} se autodestruira')
    else:
        return (f"La {lista} lista fue salvada")
lanzamiento = lanzar_moneda()
print(probada_suerta(lanzamiento,lista_numeros))