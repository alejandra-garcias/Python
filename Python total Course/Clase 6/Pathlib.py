###crear rutas interpretadas por todos los sistemas operativos
from pathlib import Path
base = Path.home()
guia = Path('Barcelona','Sagrada')
guia2=Path(base,'Barcelona','Sagrada')
print(guia) ###Barcelona\Sagrada
print(base)##C:\Users\algas
print(guia2)###C:\Users\algas\Barcelona\Sagrada
guia3=guia.with_name('LA.txt')##elimina el ultimo y anade el que hay en te parentesis
print(guia3)
print(guia2.parent.parent)##puedes añadir todos los parent que quieras
####buscar archivos:
guia =  Path(Path.home(),'Europa')
for txt in Path(guia).glob('*.txt'):
    print(txt)## los que esten solo en ese directorio


### para incluir subdirectorios: 
for txt in Path(guia).glob('*.txt'):
    print(txt)

###buscar desde algun punto = 
guia = Path('Europa','España','Barcelona','SagradaFamilia.txt')
en_europa = guia.relative_to(Path('Europa'))
print(en_europa)### España','Barcelona','SagradaFamilia.txt'
en_europa = guia.relative_to(Path('Europa'))
en_espania = guia.relative_to(Path('Europa','España')) ### Barcelona','SagradaFamilia.txt')



carpeta = Path('C:/Users/algas/OneDrive/Escritorio/Python/Pruebas')
archivos = carpeta/'prueba.txt'
mi_archivo = open(archivos)
print(mi_archivo.read())

##Práctica Path 1.Almacena en la variable ruta_base, un objeto Path que señale el directorio base del usuario.Recuerda importar Path del módulo pathlib, y utilizar el método home()
ruta_base = Path.home()
print(ruta_base)

###Práctica Path 2.Implementa y crea una ruta relativa que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:Almacena el directorio obtenido en la variable ruta. No olvides importar Path.
guia = Path('Curso Python','Dia 6','practicas_path.py')
ruta = guia.relative_to(Path())
print(ruta) ##Curso Python\Dia 6\practicas_path.py

###Práctica Path 3Implementa y crea una ruta absoluta que nos permita llegar al archivo "practicas_path.py" a partir de la siguiente estructura de carpetas:Almacena el directorio obtenido en la variable ruta. No olvides importar Path, y de concatenar el objeto Path que refiere a la carpeta base del usuario.
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")