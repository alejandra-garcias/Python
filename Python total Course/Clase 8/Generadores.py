## en lugar de return - yield - mejora memoria ram

def generador():
    for num in range(1,5):
        yield num *10

g = generador()

print(next(g))
print(next(g))
print(next(g))

#####################################
def mi_generadoor():
    x = 1
    yield x
    x+=1
    yield x
    x+=1
    yield x

gg = mi_generadoor()
print(next(gg))
print('hola, esto no interrumpe nada')
print(next(gg))

###Práctica Generadores 1Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.
def mi_generador():
    num = 0
    while True:
        num+=1
        yield num

generador = mi_generador()
print (next(generador))
print (next(generador))
print (next(generador))

###Práctica Generadores 2Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def generador_multiplos():
    num = 0
    while True:
        num +=7
        yield num

generador = generador_multiplos()
print(next(generador))
print(next(generador))

##Práctica Generadores 3Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:"Te quedan 3 vidas""Te quedan 2 vidas""Te queda 1 vida""Game Over"Almacena el generador en la variable perder_vida
def vidas():
    vidas = 4
    while True:
        vidas -=1
        if vidas > 1:
            yield(f'Te quedan {vidas} vidas')
        elif vidas == 1:
            yield(f'Te queda {vidas} vida')
        
        else:
            yield('Game over')

perder_vida = vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))