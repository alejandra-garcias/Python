###metodos de instancia= def
##metodos de clase= @classmethod
##metodos estaticos = @staticmethods
class Pajaro :
    alas = True
    def __init__(self, color, especie): 
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}')
    
    def volar(self,metros):
        print(f'El pajaro ha volado {metros} metros')
        self.piar()## ahora cada vez que llamemos al metodo volar tambien llamaremos al metodo piar

    def pintar_nefro(self): ##modifica caracteristica de los metros

        self.color = 'negro'

    @classmethod
    def poner_huevos(cls,cantidad):
        print(f'Puso {cantidad} huevos')
        ##desde aqui podria modifocar atributos de clase, es decir alas en este caso, lo demas no, esx decir, todo lo que tenga el metodo self no

    @staticmethod
    def mirar():
        print('El pajaro mira')

piolin = Pajaro('amarillo', 'canario')
piolin.alas =False

##los metodos de clase no necesitan instancia para poder ejecutarse, pero no pueden acceder a los atributos de instancia

######METODOS DE CLASE != INSTANCIA DE CLASE

####Práctica Tipos de Métodos 1Crea un método estático respirar() para la clase Mascota. Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"

class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")

##Práctica Tipos de Métodos 2Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase Jugador, estableciéndolo en True cada vez que es invocado. El valor predeterminado del atributo vivo, debe ser False.
class Jugador:
    vivo = False
    
    @classmethod
    def revivir(cls):
        cls.vivo = True

###Práctica Tipos de Métodos 3Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
class Personaje:
    def __init__(self, cantidad_flechas): 
        self.cantidad_flechas = cantidad_flechas
    
    def lanzar_flecha(self):
        self.cantidad_flechas -=1
