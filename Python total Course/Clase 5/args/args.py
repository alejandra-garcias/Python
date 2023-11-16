## args= funciones genericas que se adapten al numero de argumentos que quiera pasar el usuario
####almacenamos el total en una variable que se inicializa en 0  y diriamos que por cada argumento en args, total sera la suma de si mismo mas el argumento de cada iteracion,
def suma (*args):
    total = 0
    for arg in args:
        total +=arg
    return total

def suma (*args):
    return sum(args)

###Práctica sobre Argumentos Indefinidos (*args) 1Crea una función llamada suma_cuadrados que tome una cantidad indeterminada de argumentos numéricos, y que retorne la suma de sus valores al cuadrado.Por ejemplo para los argumentos suma_cuadrados(1,2,3) deberá retornar 14 (1+4+9).


def suma_cuadrados(*args):
    total = 0
    for n in args:
        total += n**2
    return total
print(suma_cuadrados(1,2,3))

###Práctica sobre Argumentos Indefinidos (*args) 2Crea una función llamada suma_absolutos, que tome un conjunto de argumentos de cualquier extensión, y retorne la suma de sus valores absolutos (es decir, que tome los valores sin signo y los sume, o lo que es lo mismo, los considere a todos -negativos y positivos- como positivos).
def suma_absolutos(*args):
    total = 0
    for n in args:
        total +=abs(n)
    return total


##Práctica sobre Argumentos Indefinidos (*args) 3Crea una función llamada numeros_persona que reciba, como primer argumento, un nombre, y a continuación, una cantidad indefinida de números.La función debe devolver el siguiente mensaje:"{nombre}, la suma de tus números es {suma_numeros}"

def numeros_persona(nombre,*args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus numeros es {suma_numeros}"
print((numeros_persona("Alejandra",1,2,3,4,5,6)))