## **kwargs, seria un arg tipo diccionario
##nums, args ,kwargs
def prueba(**kwargs):
    total = 0
    for clave, valor in kwargs.items():
        print(f'{clave} ={valor}')
        total+=valor
    return total
kwargs = {'x':1,'y':2}
print(prueba(z=3,k=5, **kwargs))

def pruebas(num1,num2,*args,**kwargs):
    print(f"el valor primero es {num1}")
    print(f"el valor segundo es {num2}")

    for arg in args:
        print(f"arg = {arg}")
    
    for clave, valor in kwargs.items():
        print(f'{clave} ={valor}')
args = [1,2,3,4,5,6]
kwargs = {'x':1,'y':21}

###Práctica sobre Argumentos Indefinidos (**kwargs) 1.Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros que se entregan, y devuelva esa cantidad como resultado.
def cantidad_atributos(**kwargs):
    suma = 0
    for clave in kwargs:
        suma = suma + 1
    return suma

###Práctica sobre Argumentos Indefinidos (**kwargs) 2Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
def lista_atributos (**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista

###Práctica sobre Argumentos Indefinidos (**kwargs) 3Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad indetermida de argumentos. Esta función deberá mostrar en pantalla:Características de {nombrenombre_argumento}: {valor_argumento}{nombre_argumento}: {valor_argumento}etc...Por ejemplo:describir_persona("María", , )Mostrará en pantalla:Características de María:color_ojos: azulescolor_pelo: rubio
def describir_persona (nombre,**kwargs):
    print(f"Caracteristicas de {nombre}:")
    for clave, valor in kwargs.items():
        print(f'{clave}:{valor}')
print(describir_persona("María", color_ojos="azules",color_pelo="rubio"))
