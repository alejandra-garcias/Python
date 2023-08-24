class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
class Cliente(Persona):
    def __init__(self, nombre, apellido,numero_cuenta,balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance
    
    def __str__(self):
        return(f'''
                Nombre : {self.nombre}
                Apellido : {self.apellido}
                Numero de cuenta : {self.numero_cuenta}
                Balance : {self.balance} euros ''')
    
    def depositar(self):
        deposito = input('Cuanto quieres depositar?')
        deposito = int(deposito)
        self.balance += deposito
        print (f' Tu deposito de {deposito} ha sido ingresado correctamente, tu balance es de {self.balance}')
    
    def retirar(self):
        retiro = input('Cuanto dinero desea retirar?')
        retiro = int(retiro)
        if self.balance > retiro:
            self.balance = self.balance - retiro
            print(f'{retiro} euros han sido retirados correctamente de su cuenta. Su nuevo balance es de {self.balance}')
        else:
            print('Lo siento pero tu saldo es insuficiente.')
        return self.balance
    

def crear_cliente():
    print('Bienvenido al Banco Money, antes de empezar necesitamos algunos datos para poder crear tu perfil')
    nombre = input('Cual es tu nombre ')
    apellido = input('Cual es tu apellido ')
    numero_cuenta = input('Cual es tu numero de cuenta ')
    balance = input('Cuanto dinero te gustaria ingresar? ')
    balance = float(balance)
    return Cliente(nombre, apellido,numero_cuenta,balance)



def inicio(cliente):
    salir = False
    eleccion = 'x'
    cliente = crear_cliente()
    balance = cliente.balance
    while not eleccion.isnumeric() or int(eleccion) not in range(1,4) or not salir:
        print(cliente.__str__())
        print('Elige una opcion:')
        print('''
          [1]-Depositar
          [2]-Retirar
          [3]-Salir''')
        eleccion =input()
        eleccion_int =int(eleccion)
        if eleccion_int ==  1:
            cliente.depositar()
            eleccion = 'x'
        elif eleccion_int == 2:
            cliente.retirar()
            eleccion = 'x'
        elif eleccion_int == 3:
            salir = True
            print('Gracias por utilizar nuestros servicios. Esperamos que vuelvas pronto')    



inicio(crear_cliente)