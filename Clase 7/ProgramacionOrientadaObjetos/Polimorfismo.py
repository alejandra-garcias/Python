'''
mi_gato.hablar()
mi_pájaro.hablar()
mi_caballo.hablar()
mi_pez.hablar()
mi_hámster.hablar()
mi_conejo.hablar()
mi_tortuga.hablar()
mi_cobra.hablar()
mi_rana.hablar()
mi_delfín.hablar()

for animal in lista:
animal.hablar()
'''

###################################################################################
class Vaca:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(f'{self.nombre} dice muuuuu')   

class Oveja:
    def __init__(self,nombre):
        self.nombre = nombre
    def hablar(self):
        print(f'{self.nombre} dice beeeeee')   

vaca1 =Vaca('Aurora')
oveja1 = Oveja('Nube')

#vaca1.hablar()
#oveja1.hablar()

#####dos objetos diferentes puede usar el mismo metodo que haga cosas diferentes
animales = [vaca1,oveja1]
for animal in animales:
    animal.hablar() #Aurora dice muuuuu
                    #Nube dice beeeeee



def animal_habla(animal):
    animal.hablar()

animal_habla(vaca1)#Aurora dice muuuuu
animal_habla(oveja1) #Nube dice beeeeee

####Práctica Polimorfismo 1La función incorporada en Python len() tiene un comportamiento polimórfico, ya que calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), devolviendo la cantidad de items o caracteres que lo componen.Crea un iterador que recorra los siguientes objetos: palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud con la función len().Puedes recordar cómo implementar la función len() siguiente enlace: https://docs.aws.amazon.com/es_es/redshift/latest/dg/r_LEN.html

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
nuevo = [palabra,lista,tupla]
for n in nuevo:
    print(len(n)) 

###Práctica Polimorfismo 2Cuentas con tres clases de personajes en un juego, los cuales cuentan con sus métodos de ataque específicos.Crea un iterador que logre un ataque conjugado en el siguiente orden: Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. Deberás crear instancias de cada una de las clases anteriores para construir un iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")
        

mi_mago = Mago()
mi_arquero =Arquero()
mi_samurai = Samurai()

personajes = [mi_arquero,mi_mago,mi_samurai]
for personaje in personajes:
    personaje.atacar()


###Práctica Polimorfismo 3Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de defensa específicos.Crea una función llamada personaje_defender(), que pueda recibir un objeto (una instancia de las clases de tus personajes), y ejecutar su método defender() independientemente de qué tipo de personaje se trate.

class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")
def personaje_defender(personaje):
    return personaje.defender()
    