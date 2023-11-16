### Path
##os
import os
##getcurrentworkdirectory
ruta = os.getcwd()
print(ruta)
rut = os.chdir("C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Codigo Python\\Clase 5") ##cambia de directorio
print(rut)
archivo = open('registro.txt')
print(archivo.read())

##rutas= os.makedirs("C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Codigo Python\\Clase 7") ###crea uno nuevo
rutita = "C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Codigo Python\\Clase 6\\registro.txt"
elemento = os.path.basename(rutita)
print(elemento)###registro.txt
elemento2 =os.path.dirname(rutita)
print(elemento2)####C:\Users\algas\OneDrive\Escritorio\Python\Codigo Python\Clase 6
#######si queremos ambos separados en una tuola
elemento3 = os.path.split(rutita)
print(elemento3)

###########eliminar carpeta. Tiene que estar vacia
##os.rmdir("C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Codigo Python\\Clase 6\\otra")

##########
###otro_archivo = open('C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Apuntes')
##print(otro_archivo.read())

