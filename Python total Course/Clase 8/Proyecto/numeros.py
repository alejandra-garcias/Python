def generadorCosmetica():
    for num in range (1,10000):
        yield (f'Ticket = [C - {num}]')
        
def generadorFarmacia():
    for num in range (1,10000):
        yield(f'Ticket = [F - {num}]')
def generadorPerfumeria():
    for num in range (1,10000):
        yield (f'Ticket = [P - {num}]')

c= generadorCosmetica()
f=generadorFarmacia()
p=generadorPerfumeria()

def dar_numero(eleccion):
    print('Ticket numero:')

    if eleccion =='C':
        print(next(c))
    elif eleccion == 'F':
        print(next(f))
    elif eleccion == 'P':
        print(next(p))
    print('Gracias por su visita')