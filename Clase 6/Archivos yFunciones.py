###Práctica Archivos y Funciones 1Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).
def abrir_leer(archivo):
    aux = open(archivo)
    return (aux.read())

##Práctica Archivos y Funciones 2Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobrescribir(archivo):
    aux = open(archivo,'w')
    aux.write("contenido eliminado")
    aux.close()
    return aux

##Práctica Archivos y Funciones 3.Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.


def registro_error(archivo):
    aux = open(archivo,'a')
    aux.write("se ha registrado un error de ejecución")
    aux.close()