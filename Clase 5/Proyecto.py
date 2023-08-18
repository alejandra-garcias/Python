from random import *

##choice
palabras = ["casa", "perro", "gato", "auto"]

letras_correctas = []
letras_incorrectas = []
intentos = 6
aciertos = 0
juego_terminado =  False

def elegir_palabra(lista_palabras):
    palabra_aleatoria = choice(lista_palabras)
    letras_unicas = len(set(palabra_aleatoria))
    return palabra_aleatoria,letras_unicas

def pedir_letra():
    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'

    while not es_valida:
        letra_elegida = input('Elige una letra: ').lower()
        if letra_elegida in abecedario and len(letra_elegida)==1:
            es_valida =  True
        else:
            print('Esa letra no es valida')
    return letra_elegida

def guiones(palabra_aleatoria):
    lista_guiones = []
    for letra in palabra_aleatoria:
        if letra in letras_correctas:
            lista_guiones.append(letra)
        else: 
            lista_guiones.append('-')
    print(' '.join(lista_guiones))

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencia):
    fin = False
    if letra_elegida in palabra_oculta:
        letras_correctas.append(letra_elegida)
        coincidencia +=1
    else: 
        letras_incorrectas.append(letra_elegida)
        vidas -=1
    if vidas == 0:
        fin =  perder()
    elif coincidencia == letras_unicas:
        fin =  ganar(palabra_oculta)
    return vidas,fin,coincidencia

def perder():
    print('Te has quedado sin vidas')
    print(f'La palabra oculata era {palabra}')

    return True

def ganar (palabra_descubierta):
    guiones(palabra_descubierta)
    print("Enhorabuena has ganado!")

    return True


palabra,letras_unicas = elegir_palabra(palabras)
while not juego_terminado:
    print('\n' + '*'* 20 + '\n')
    guiones(palabra)
    print('\n')
    print ('Letas incorrectas: ' + '-'.join (letras_incorrectas))
    print(f'Vidas = {intentos}')
    print('\n' + '*'* 20 + '\n')
    letra = pedir_letra()

    intentos ,terminados,aciertos = chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminados
    