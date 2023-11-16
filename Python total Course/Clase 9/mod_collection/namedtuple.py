from collections import namedtuple
Persona = namedtuple('Persona',['nombre','altura','peso'])
ariel = Persona('Ariel',1.76,50)
print(ariel)
print(ariel.peso)
print(ariel[2])


