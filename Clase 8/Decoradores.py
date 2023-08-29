'''
def mayusculas(texto):
    print(texto.upper())

def minuscula(texto):
    print(texto.lower())

def una_funcion(funcion):
    return funcion


mi_funcion = mayusculas
mi_funcion('python')

una_funcion(mayusculas('probando'))

'''


def cambiar_letras(tipo):
    def mayuscula(texto):
        print(texto.upper())
    
    def minuscula(texto):
        print(texto.lower())
    
    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula


operacion = cambiar_letras('min')

operacion ('HOLA LO ENTENDI')


def decorar_saludo(funcion):
    def otra_funcion(palabra):
        print('hola')
        funcion(palabra)
        print('adios')
    return otra_funcion

def mayusculas(palabra):
    print(palabra.upper())
def minusculas(palabra):
    print(palabra.lower())

impresion = decorar_saludo(mayusculas)
impresion('creo que si me ha salido lo que queria hacer')