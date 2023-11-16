import os 
from os import system
from pathlib import Path 
import shutil

ruta_global = Path('C:/Users/algas/OneDrive/Escritorio/Recetas')

rutas = [
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Carne'),
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Ensaladas'),
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Pasta'),
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Postres')

]
cantidad_categorias = len(rutas)

def bienvenida(ruta):
    cantidad_recetas = list(ruta.glob('**/*.txt'))
    cantidad_recetas = len(cantidad_recetas)

    print(f'Bienvenido a el recetario, esta carpeta se encuentra en {ruta_global} y tiene {cantidad_recetas} recetas  ')
def mostrarcategorias(ruta):
    elementos = ruta.iterdir()
    # Filtrar la lista para obtener solo los subdirectorios
    subdirectorios = [elemento for elemento in elementos if elemento.is_dir()]
    # Obtener los nombres de las carpetas
    nombres_carpetas = [subdir.name for subdir in subdirectorios]
    print("Nombres de las carpetas:", nombres_carpetas)
    return nombres_carpetas
def mostrararchivos(ruta):
    elementos = ruta.iterdir()
    # Filtrar la lista para obtener solo los subdirectorios
    archivos = [elemento for elemento in elementos if elemento.is_file()]
    # Obtener los nombres de las carpetas
    nombres_archivos = [archivo.name for archivo in archivos]
    print("Elige la receta:", nombres_archivos)
    return nombres_archivos
def elegirparacrear(categorias):
    receta = 0
    posicion = 0
    aux = input(f'Quieres crear una receta en {categorias[receta]} Presiona S para acceder a ella o enter para pasar a la siguiente')
    while aux != 'S' and aux != 's':
        posicion+=1
        aux = input(f'Quieres crear una receta en {categorias[receta +posicion]} Presiona S para acceder a ella o enter para pasar a la siguiente')
        if aux == 'S'or  aux=='s':
            break

    print(f'De acuerdo, crearemos una receta en  {categorias[receta +posicion]}')
    return posicion

def elegir(categorias):
    receta = 0
    posicion = 0
    aux = input(f'Quieres una receta de {categorias[receta]} Presiona S para acceder a ella o enter para pasar a la siguiente')
    while aux != 'S' and aux != 's':
        posicion+=1
        aux = input(f'Quieres una receta de {categorias[receta +posicion]} Presiona S para acceder a ella o enter para pasar a la siguiente')
        if aux == 'S'or  aux=='s':
            break

    print(f'De acuerdo, pasare a mostrarte la receta de {categorias[receta +posicion]}')
    return posicion
def elegirparaeliminar(categorias):
    receta = 0
    posicion = 0
    aux = input(f'Quieres eliminar una receta en {categorias[receta]} Presiona S para acceder a ella o enter para pasar a la siguiente')
    while aux != 'S' and aux != 's':
        posicion+=1  
        aux = input(f'Quieres eliminar una receta en {categorias[receta +posicion]} Presiona S para acceder a ella o enter para pasar a la siguiente')
        if aux == 'S'or  aux=='s':
            break

    print(f'De acuerdo, eliminaremos una receta en  {categorias[receta +posicion]}')
    return posicion


def opciones(categorias):
    eleccion = ''
    while eleccion != 6:
        if eleccion == '':
            print('''Elige una de las siguientes opciones:
          [1]-leer receta
          [2]-crear receta
          [3]-crear categoria
          [4]-eliminar receta
          [5]-eliminar categoria
          [6]-finalizar programa''')
            eleccion = int(input('Qué acción quieres realizar? '))
            system('cls')
        elif eleccion == 1:
            categorias = mostrarcategorias(ruta_global)
            posicion = elegir(categorias)
            ruta_elegida = rutas[posicion]
            nombres_archivos = mostrararchivos(ruta_elegida)
            posicion_archivo = elegir(nombres_archivos)
            elegida = nombres_archivos[posicion_archivo]
            with open(ruta_elegida / elegida) as archivo:
                contenido = archivo.read()
                print(contenido)
            eleccion = ''
            
        elif eleccion == 2:
            categorias = mostrarcategorias(ruta_global)
            posicion = elegirparacrear(categorias)
            ruta_elegida = rutas[posicion]
            nueva_receta = input('Cómo se llama tu receta: ')
            nueva_receta = f'{nueva_receta}.txt'
            creando_archivo = ruta_elegida / nueva_receta
            os.makedirs(os.path.dirname(creando_archivo), exist_ok=True)
            with open(creando_archivo, 'w') as editor:
                receta_poruser = input('Describe aquí la receta: ')
                editor.write(receta_poruser)
            print('Tu receta se ha guardado correctamente')
            eleccion = ''
        elif eleccion == 3:
            categoria_a_crear = input('Cómo quieres que se llame la categoria? ')
            nueva_categoria = os.path.join(ruta_global, categoria_a_crear)
            os.makedirs(nueva_categoria)
            print(f'La nueva categoria {categoria_a_crear} ha sido creada')
            eleccion = ''
        elif eleccion == 4:
            print('De acuerdo, eliminaremos una receta')
            posicion = elegirparaeliminar(mostrarcategorias(ruta_global))
            ruta_elegida = rutas[posicion]
            nombres_archivos = mostrararchivos(ruta_elegida)
            posicion_archivo = elegir(nombres_archivos)
            archivo_a_borrar = nombres_archivos[posicion_archivo]
            os.remove(ruta_elegida / archivo_a_borrar)
            print(f'La receta {archivo_a_borrar} ha sido borrada')
            eleccion = ''
        elif eleccion == 5:
            print('De acuerdo, eliminaremos una categoría')
            posicion = elegirparaeliminar(mostrarcategorias(ruta_global))
            ruta_a_borrar = rutas[posicion]
            shutil.rmtree(ruta_a_borrar,ignore_errors=True)
            
            print(f'La categoría {ruta_a_borrar} ha sido borrada')
            eleccion = ''
        
        elif eleccion == 6:
            print('Gracias por usar nuestro recetario')
            break
        

bienvenida(ruta_global)
opciones(rutas)