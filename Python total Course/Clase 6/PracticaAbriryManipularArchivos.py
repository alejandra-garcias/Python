##Práctica Abrir y Manipular Archivos 1Abre el archivo texto.txt e imprime su contenido.Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
mi_archivo = open('texto.txt')
print(mi_archivo.read())

##Práctica Abrir y Manipular Archivos 2Imprime la primera línea del archivo texto.txtNo olvides abrir el archivo y cerrarlo luego de ejecutar tu código.Nota: el archivo se encuentra guardado en la misma carpeta donde se aloja tu código
mi_archivo = open('texto.txt')
una_linea = mi_archivo.readline()
print(una_linea)

mi_archivo.close()

##Práctica Abrir y Manipular Archivos 3Abre el archivo texto.txt e imprime únicamente la segunda línea.
mi_archivo = open('texto.txt')
linea_dos = mi_archivo.readline()
linea_dos = mi_archivo.readline()
print(linea_dos)
mi_archivo.close()
###################
