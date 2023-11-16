##siempre argumento obligatorio self

class Pajaro :
    alas = True
    def __init__(self, color, especie): 
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}')
    
    def volar(sef,metros):
        print(f'El pajaro ha volado {metros} metros')

piolin = Pajaro('amarillo','canario')
piolin.volar(50)
piolin.piar()

###Práctica Métodos 1Crea una clase Perro. Dicho perro debe poder ladrar.Crea el método ladrar() y ejecútalo en una instancia de Perro. Cada vez que ladre, debe mostrarse en pantalla "Guau!".
class Perro:
    def ladrar(self):
        print('Guau!')

Nina = Perro()
Nina.ladrar()

###Práctica Métodos 2Crea una clase llamada Mago, y crea un método llamado lanzar_hechizo() (deberá imprimir "¡Abracadabra!").Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.

class Mago:
    def lanzar_hechizo(self):
        print('¡Abracadabra!')
    
merlin =  Mago()
merlin.lanzar_hechizo()

###Práctica Métodos 3Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). El método debe imprimir en pantalla el mensaje"La alarma ha sido pospuesta {cantidad_minutos} minutos"

class Alarma:
    def postergar(self,cantidad_minutos):
        print(f'La alarma ha sido postpuesta {cantidad_minutos} minutos')

mi_alarma = Alarma()
mi_alarma.postergar(5)