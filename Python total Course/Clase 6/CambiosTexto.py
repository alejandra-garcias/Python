##r=modo lectura
##w=modo escritura
##a=solo escritura al final del archivo
archivo = open('prueba.txt','w')
archivo.write('Soy el nuevo texto')
archivo.write('si no pongo la n de salto de linea no la hace')
archivo.write('\n aqui si la va a hacer')
archivo.write('''o
              ascii
              tambien 
              hace 
              saltitos
              de
              linea''')
archivo.close()
############

mi_archivo = open('prueba.txt','w')
mi_archivo.writelines(['hola','mundo'])
archivo.close()
########

mi_archivo = open('prueba.txt','w')
lista = ['hola','mundo']
for p in lista:
    mi_archivo.writelines(p)
archivo.close()

##########
mi_archivo = open('prueba.txt','w')
mi_archivo.write('i')
mi_archivo.close()
######Práctica Crear y Escribir Archivos 1-Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".Imprime el contenido completo de "mi_archivo.txt" al finalizar.Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
mi_archivo = open('mi_archivo.txt','w')
mi_archivo.write('Nuevo texto')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt','r')
print(mi_archivo.read())
mi_archivo.close()

##Práctica Crear y Escribir Archivos 2-Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".Imprime el contenido completo de "mi_archivo.txt" al finalizar.Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.
mi_archivo = open('mi_archivo.txt','a')
mi_archivo.write('Nuevo inicio de sesion')
mi_archivo.close()
mi_archivo = open('mi_archivo.txt','r')
print(mi_archivo.read())
mi_archivo.close()

###Práctica Crear y Escribir Archivos 3Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]Imprime el contenido completo de "registro.txt" al finalizar.Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.

mi_archivo = open('registro.txt','w')
mi_archivo.writelines('registro_ultima_sesion = ["Federico",\t."20/12/2021",\t. "08:17:32 hs",\t. "Sin errores de carga"]')
mi_archivo.close()
mi_archivo = open('registro.txt','r')
print(mi_archivo.read())