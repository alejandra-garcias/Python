class Animal:
    def __init__(self,edad,color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print(f"este animal ha nacido")

class Pajaro(Animal):
    pass
###__bases__ te dice de quien hereda 
##__subclasses__() te dice a quien transmite su herencia
piolin = Pajaro(2,'amarillo')
piolin.nacer()
######
###Práctica Herencia 1Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, Alumno, que herede de la primera estos atributos.
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

###Práctica Herencia 2Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.
class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

##Práctica Herencia 3Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() (puedes dejar el código de los métodos en blanco con pass). Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
class Vehiculo:
    @classmethod
    def acelerar(cls):
        pass
    @classmethod
    def frenar(cls):
        pass
class Automovil(Vehiculo):
    pass