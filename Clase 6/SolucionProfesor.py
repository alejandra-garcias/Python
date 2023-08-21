import os
from pathlib import Path
from os import system
finalizar =  False

mi_ruta = Path(Path.home(),"recetas" )
def contar_recetas(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador +=1
    return contador

def inicio():
    system('cls')
    print('*'*50)
    print('*'* 5 + 'Bienvenido al administrador de recetas' + '*'* 5 )
    print('*'*50)
    print('\n')
    print(f'Las recetas se encuentran en {mi_ruta}')
    print(f'Las recetas disponibles son {contar_recetas(mi_ruta)}')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion:')
        print('''
          [1]-leer receta
          [2]-crear receta
          [3]-crear categoria
          [4]-eliminar receta
          [5]-eliminar categoria
          [6]-finalizar programa''')
        eleccion_menu = input()
    return int(eleccion_menu)

def mostrar_categorias(ruta):
    print('Categorias')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1

    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}]-{carpeta_str}')
        lista_categorias.append(carpeta)
        contador+=1
    return lista_categorias    

def elegir_categorias(lista):
    eleccion_correcta ='x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta)not in range(1,len(lista)+1): ## un valor mas porque el ultimo numero del rango no va incluido
        eleccion_correcta = input("\nElige una categoria:")
    return lista[int(eleccion_correcta)-1]##porque los indices van desde 0

def mostrar_recetas(ruta):
    print('Recetas:')
    ruta_recetas = Path(ruta)
    lista_recetas=[]
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}]-{receta_str}')
        lista_recetas.append(receta)
        contador +=1
    return lista_recetas

def elegir_recetas(lista):
    eleccion_receta = 'x'
    while not eleccion_receta.isnumeric() or int(eleccion_receta)not in range (1,len(lista)+1):
        eleccion_receta = input('Elige una receta')
    return lista[int(eleccion_receta)-1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False
    while not existe:
        print('Escribe el nombre de tu receta:')
        nombre_receta=input() +'.txt'
        print('Escribe tu nueva receta: ')
        contenido_receta = input()
        ruta_nueva  =Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta{nombre_receta} ha sido creada')
            existe = True
        else:
            print('lo siento esa receta ya existe')

def crear_categoria(ruta):
    existe = False
    while not existe:
        print('Escribe el nombre de la nueva:')
        nombre_categoria=input() 
        print('Escribe tu nueva categoria: ')
        ruta_nueva  =Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu carpeta{nombre_categoria} ha sido creada')
            existe = True
        else:
            print('lo siento esa categoria ya existe')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')

def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'la categoria{categoria.name} ha sido eliminada')

def volver_inicio():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\n Presione v para volver al inicio')

while not finalizar:
    menu =inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mis_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mis_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
    if menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mis_categoria = elegir_categorias(mis_categorias)
        crear_receta(mis_categoria)
        volver_inicio()
        
    if menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()

        
    if menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mis_categoria = elegir_categorias(mis_categorias)
        mis_recetas = mostrar_recetas(mis_categoria)
        if len(mis_recetas) < 1:
            print("no hay recetas en esta categoría.")
        else:
            mi_receta = elegir_recetas(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
        
    if menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mis_categoria = elegir_categorias(mis_categorias)
        eliminar_categoria(mis_categoria)
        volver_inicio()
        
    if menu == 6:
        finalizar =  True
