def suma ():
    n1 = int(input('numero 1 '))
    n2 = int(input('numero 2 '))
    print(n1 +n2)
    print('Gracias pro sumar')


'''
try:
    #codigo a probar
except:
    #codigo a ejecutar si el primero da error
else:
    #codigo que se ejecuta si no hay un error
finally:
    #codigo que se va a ejecutar de todos modos
'''
try:
    suma()
except TypeError:
    print('Algo no ha ido bien')
except ValueError:
    print('otro erro diferente')
else:
    print('Hiciste todo bien')
finally:
    print('Eso fue todo')



def pedir_numero():
    while True:
        try:
            numero = int(input('dame un numero'))
        except:
            print('ese no es un numero')
        else:
            print(f'ingresaste el numero {numero}')
            break
    print('Gracias')


pedir_numero()   


##Práctica Manejo de Errores 1Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.
def sumar(num1,num2):
    while True:
        try:
            num1 = int(num1)
            num2= int(num2)
        except:
            print('ese no es un numero')
            break
        else:
            print(f'ingresaste el numero {num1} y el numero {num2}')
            print(f'resultado = {num1+num2}')
            break
    print('Gracias')


###Práctica Manejo de Errores 2Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.Implementa para la siguiente función cociente(), un manejador de errores:Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"En caso que no se produzca un error, deberá limitarse a imprimir el resultado del cociente (división) entre los dos números entregados como argumento.sumar(2,'fede') 

def cociente(num1,num2):
    try:
        print(num1/num2)
       
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print('El segundo argumento no debe ser cero')



cociente(2,'fede')

####Práctica Manejo de Errores 3Hemos visto en la lección de qué manera se implementa el manejo de errores habitualmente en Python. En el caso de este ejercicio, sin embargo, necesitaré que lo hagamos de una forma ligeramente distinta para que pueda ser evaluado: deberás implementarlo DENTRO de la función. En forma de comentario, verás un ejemplo de resolución. Ten presente, sin embargo, que la forma preferida es la que hemos visto en clase.Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"En todos los casos, al finalizar, imprimir: "Finalizando ejecución"
def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print('Error desconocido')
    else:
        print("Abriendo exitosamente")
    finally:
        print('Finalizando ejecucion')

abrir_archivo('a.txt')