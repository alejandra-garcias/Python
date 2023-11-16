import os
from os import system
from pathlib import Path

ruta_global = Path('C:/Users/algas/OneDrive/Escritorio/Recetas')
rutas = [
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Carne'),
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Ensaladas'),
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Pasta'),
    Path('C:/Users/algas/OneDrive/Escritorio/Recetas/Postres')
]

def bienvenida(ruta):
    cantidad_recetas = list(ruta.glob('**/*.txt'))
    cantidad_recetas = len(cantidad_recetas)

    print(f'Bienvenido al recetario, esta carpeta se encuentra en {ruta_global} y tiene {cantidad_recetas} recetas')

def mostrarcategorias(ruta):
    elementos = ruta.iterdir()
    subdirectorios = [elemento for elemento in elementos if elemento.is_dir()]
    nombres_carpetas = [subdir.name for subdir in subdirectorios]
    print("Nombres de las carpetas:", nombres_carpetas)
    return nombres_carpetas

def mostrararchivos(ruta):
    elementos = ruta.iterdir()
    archivos = [elemento for elemento in elementos if elemento.is_file()]
    nombres_archivos = [archivo.name for archivo in archivos]
    print("Elige la receta:", nombres_archivos)
    return nombres_archivos

def elegir(categorias):
    receta = 0
    posicion = 0
    aux = input(f'Quieres una receta de {categorias[receta]} Presiona S para acceder a ella o enter para pasar a la siguiente')
    while aux != 'S' and aux != 's':
        posicion += 1
        aux = input(f'Quieres una receta de {categorias[receta + posicion]} Presiona S para acceder a ella o enter para pasar a la siguiente')

        if aux == 'S' or aux == 's':
            break

    print(f'De acuerdo, pasare a mostrarte la receta de {categorias[receta + posicion]}')
    return posicion

def elegirparacrear(categorias):
    receta = 0
    posicion = 0
    aux = input(f'Quieres crear una receta en {categorias[receta]} Presiona S para acceder a ella o enter para pasar a la siguiente')
    while aux != 'S' and aux != 's':
        posicion += 1
        aux = input(f'Quieres crear una receta en {categorias[receta + posicion]} Presiona S para acceder a ella o enter para pasar a la siguiente')
        if posicion>categorias:
            print('No hay mas recetas')
            continue
        if aux == 'S' or aux == 's':
            break

    print(f'De acuerdo, crearemos una receta en  {categorias[receta + posicion]}')
    return posicion

def elegirparaeliminar(categorias):
    receta = 0
    posicion = 0
    aux = input(f'Quieres eliminar una receta en {categorias[receta]} Presiona S para acceder a ella o enter para pasar a la siguiente')
    while aux != 'S' and aux != 's':
        posicion += 1
        aux = input(f'Quieres eliminar una receta en {categorias[receta + posicion]} Presiona S para acceder a ella o enter para pasar a la siguiente')

        if aux == 'S' or aux == 's':
            break

    print(f'De acuerdo, eliminaremos una receta en  {categorias[receta + posicion]}')
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
        if eleccion == 1:
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
        if eleccion == 2:
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
        if eleccion == 3:
            categoria_a_crear = input('Cómo quieres que se llame la categoria? ')
            nueva_categoria = os.path.join(ruta_global, categoria_a_crear)
            os.makedirs(nueva_categoria)
            print(f'La nueva categoria {categoria_a_crear} ha sido creada')
            eleccion = ''
        if eleccion == 4:
            print('De acuerdo, eliminaremos una receta')
            posicion = elegirparaeliminar(mostrarcategorias(ruta_global))
            ruta_elegida = rutas[posicion]
            nombres_archivos = mostrararchivos(ruta_elegida)
            posicion_archivo = elegir(nombres_archivos)
            archivo_a_borrar = nombres_archivos[posicion_archivo]
            os.remove(ruta_elegida / archivo_a_borrar)
            print(f'La receta {archivo_a_borrar} ha sido borrada')
            eleccion = ''
        if eleccion == 5:
            print('De acuerdo, eliminaremos una categoría')
            posicion = elegirparaeliminar(mostrarcategorias(ruta_global))
            ruta_a_borrar = rutas[posicion]
            os.rmdir(ruta_a_borrar)
            print(f'La categoría {ruta_a_borrar} ha sido borrada')
            eleccion = ''
        if eleccion == 6:
            print('Gracias por usar nuestro recetario')
            break
            
bienvenida(ruta_global)
opciones(rutas)
