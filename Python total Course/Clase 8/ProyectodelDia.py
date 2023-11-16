def elegir_categoria():
    eleccion = input('''Para que area desea sacar un tiket?
                     [C] - Cosmetica
                     [F] - Farmacia
                     [P] - Perfumeria
                     ''')
    eleccion = eleccion.upper()
    return eleccion

eleccion = elegir_categoria

def dar_numero(funcion):
    def otra_funcion(eleccion):
        print('Ticket numero:')
        funcion(eleccion)
        print('Gracias por su visita')
    return otra_funcion

def elegir_generador(letra):
    def generadorCosmetica():
        num = 0
        while True:
            num += 1
            yield num
            print(f'Ticket = [C - {next(num)}]')
        
    def generadorFarmacia():
        num = 0
        while True:
            num += 1
            yield num
            print(f'Ticket = [F - {next(num)}]')
    def generadorPerfumeria():
        num = 0
        while True:
            num += 1
            yield num
            print(f'Ticket = [P - {next(num)}]')

    if letra =='C':
        return generadorCosmetica
    elif letra == 'F':
        return generadorFarmacia
    elif letra == 'P':
        return generadorPerfumeria
    

dar_numero(elegir_generador(eleccion))