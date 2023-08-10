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
