import os
archivo = open('curso.txt','w')
archivo.write('texto de prueba')
archivo.close()
##mover archivos
import shutil ## shutil.move(+ruta relativa)
import send2trash
send2trash.send2trash('curso.txt')
ruta = 'C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Apuntes'
for carpeta, subcarpeta,archivo in os.walk(ruta):
    print(f'en la carpeta: {carpeta}')
    print(f'las subcarpetas son')
    for sub in subcarpeta:
        print(f'{sub}')
    print('los archivos son')
    for arch in archivo:
        if arch.startswith('2014'):
            print(f'{arch}')
