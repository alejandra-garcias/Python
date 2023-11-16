## de clase - aplica a todos los objetos
## de instancia- distinto para cada pajaro ej color



class Pajaro :
    ## de clase: Aplica a todos los objetos de la clase igual
    alas = True

    ### de instancia: Cada objeto tiene uno diferente
    def __init__(self, color, especie): ##parametro
        self.color = color ##atributo, parametro
        self.especie = especie

mi_Pajaro = Pajaro('negro','tucan') ## ahora tengo que pasarle un atributo
print(mi_Pajaro.color) ##negro
print(mi_Pajaro.especie)##
print(f'Mi pajaro es un {mi_Pajaro.especie} y es de color {mi_Pajaro.color}') ##Mi pajaro es un tucan y es de color negro
print(Pajaro.alas)##True
print(mi_Pajaro.alas)


###Práctica Atributos 1Crea una clase llamada Casa, y asígnale atributos: color, cantidad_pisos.Crea una instancia de Casa, llamada casa_blanca, de color "blanco" y cantidad de pisos igual a 4.

class Casa:
    def __init__(self, color,cantidad_pisos):
        self.color = color
        self.cantidad_pisos=cantidad_pisos

casa_blanca = Casa('blanco',4)

###Práctica Atributos 2Crea una clase llamada Cubo, y asígnale el atributo de clase:caras = 6 y el atributo de instancia: color Crea una instancia cubo_rojo, de dicho color.
class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color
    
cubo_rojo = Cubo('rojo')

##Práctica Atributos 3Crea una clase llamada Personaje, y asígnale el siguiente atributo de clase:real = FalseCrea una instancia llamada harry_potter con los siguientes atributos de instancia:especie = "Humano"magico = Trueedad = 17

class Personaje: 
    real = False
    
    def __init__(self,especie,magico,edad):
        self.especie =especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano',True, 17)