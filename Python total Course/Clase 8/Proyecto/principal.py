import numeros


def elegir_categoria():

    print('Farmacia Alejandra')
    print('*'*25)
    while True:
        print('''
              [C] - Cosmetica
              [F] - Farmacia
              [P] - Perfumeria
              
                     ''')
        try:
            eleccion = input('Para que area desea sacar un tiket?').upper()
        except ValueError:
            print('Esa no es una accion valida')
        else:
            break
    numeros.dar_numero(eleccion)

        
def inicio():
    while True:
        elegir_categoria()
        try:
            otro_turno = input('Quieres sacar otro numero? [S] -[N]').upper()
            ['S','N'].index(otro_turno)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break

inicio()
