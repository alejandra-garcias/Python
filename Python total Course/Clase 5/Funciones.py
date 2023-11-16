##def = function
def mi_funcion(parametro):
    '''Buena practica poner aqui para que sirve la funcion'''
    print('Hola' + parametro)


mi_funcion ("parametroLuis")

##Práctica Crear Funciones 1Declara una función llamada saludar, que cada vez que sea llamada imprima en pantalla "¡Hola mundo!"

def saludar():
    '''saludar'''
    print("¡Hola mundo!")

##Práctica Crear Funciones 2.Declara una función llamada bienvenida, que tome como argumento el nombre de una persona, y que cada vez que sea llamada imprima en pantalla "¡Bienvenido {nombre_persona}!"Crea la variable nombre_persona, y almacena dentro de la misma el nombre que prefieras.Debes definir la función y crear la variable, no debes invocar la función luego.
def bienvenida(nombre_persona):
    '''Saluda a personas por su nombre'''
    print(f"¡Bienvenido {nombre_persona}!") #### nombre de persona es una 
bienvenida('Josefina')

##Práctica Crear Funciones 3.Declara una función llamada cuadrado, que tome como argumento un número cualquiera, y que cada vez que sea llamada, imprima en pantalla el cuadrado de dicho número (es decir, la potencia 2 del valor).El nombre del argumento que debe tomar dicha función es un_numero. Crea dicha variable y asígnale un número cualquiera.Solo debes definir la función y crear la variable, no debes invocar la función luego.
def cuadrado(un_numero):
    '''imprime el cuadrado del numero'''
    print(un_numero ** 2)

cuadrado(8)
