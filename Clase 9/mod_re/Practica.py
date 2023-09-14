###Práctica Módulo RE 1Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el mensaje.
import re

def verificar_email():
    email =  input('Email:')
    patron = r"\w+@\w+\.com\w*" 
    buscar = re.search(patron,email)
    if buscar == None:
        print('La direccion de email es incorrecta')
    else:
        print('Ok')

####En esta versión del patrón, utilizamos \w+ para hacer coincidir uno o más caracteres de palabra antes y después del carácter de arroba, y \. para hacer coincidir el carácter de punto literal en la extensión ".com".
verificar_email()



###Práctica Módulo RE 2Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra "Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.

def verificar_saludo(frase):
    buscar = re.search(r'Hola', frase)
    if buscar:
        print("Ok")
    else:
        print("No has saludado")


###Práctica Módulo RE 3El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: "El código postal ingresado no es correcto".
def verificar_cp(cp):
    patron = r'\D{2}\d{4}'
    buscar = re.search(patron, cp)
    if buscar:
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

verificar_cp('XX5241')