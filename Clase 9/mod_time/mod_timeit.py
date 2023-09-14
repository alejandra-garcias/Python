import timeit

###$ la diferencia con time es que timeit lo que hace es repetir el codigo muchas veces para que en codigos pequenos podamos apreciar el tiempo que tardaria en ejecutarse la funcion 

def prueba_for(numero):
    lista = []
    for num in range(1,numero + 1):
        lista.append(num)
    return lista

def prueba_while(numero):
    lista =[]
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador+=1
    return lista

declaracion = '''
prueba_for(10)
'''

setup = '''

def prueba_for(numero):
    lista = []
    for num in range(1,numero + 1):
        lista.append(num)
    return lista
'''


duracion = timeit.timeit(declaracion, setup, number = 100000)
print(duracion)