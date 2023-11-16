mi_archivo = open('prueba.txt')
print(mi_archivo.read())
print('-------------------------------')
mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea.upper()) ##puedo usar upper para

print('-------------------------------')
mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea.rstrip()) ## puedo usar rstrip para quitar salto de linea

print('-------------------------------')
mi_archivo = open('prueba.txt')
una_linea = mi_archivo.readline()
print(una_linea)
print('-------------------------------')
mi_archivo = open('prueba.txt')
for linea in mi_archivo:
    print(f'Aqui pone: {linea}')








mi_archivo.close()

