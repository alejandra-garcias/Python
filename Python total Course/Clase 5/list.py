from random import *

##choice
palabras = ["casa", "perro", "gato", "auto", "agua", "pied", "sol", "luna", "rojo", "azul", "niño", "niña", "arte", "bien", "calor", "día", "frio", "idea", "juez", "kilo", "leer", "mesa", "noche", "olla", "paso", "queso", "ruin", "sano", "tren", "uvas", "vino", "yoga", "zona"]

vidas = 6
def elegir_palabra():
    palabra_aleatoria = choice(palabras)
    return palabra_aleatoria
###esto da una palabra

def guiones(palabra):
    letras = len(palabra)
    guiones = '-'
    guiones = letras * guiones
    lista_guiones = []
    for guion in guiones:
        lista_guiones.append(guion)
    return lista_guiones
##esto una lista de guiones


def pedir_letra (palabra,guiones):
    vidas = 6
    palabra = palabra
    lista = []
    validacionnum= str(range (1,9))
    for letra in palabra:
        lista.append(letra)
    while vidas >0:
        intento = input("Dime una letra")
        vidas -=1
        for element in lista:
            
            if intento == element in validacionnum:
                vidas+=1
                print('Esa letra no es valida')

            elif lista [0] == intento:
                guiones [0] == lista[0]
                print(guiones)
            elif lista [1] == intento:
                guiones [1] == lista[1]
                print(guiones)
            elif lista [2] == intento:
                guiones [2] == lista[2]
                print(guiones)
            elif lista [3] == intento:
                guiones [3] == lista[3]
                print(guiones)

        else:
            return intento
    else:  print('no tienes mas intentos')




palabra = elegir_palabra()
guion=guiones
print(guiones(palabra))
###esto convierte la palabra e lista y pide una letra
pedir_letra(palabra,guion)