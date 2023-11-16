import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"
palabra =  'ayuda' in texto

patron = "ayuda"
busqueda =  re.search(patron,texto)
print(busqueda.span())##ubicacion de la palabra encontrada
print(busqueda.start())##ubicacion de la palabra encontrada de inicio
print(busqueda.end())##ubicacion de la palabra encontrada, el final

busqueda =  re.findall(patron,texto)
for hallazgo in re.finditer(patron,texto):
    print (hallazgo.span()) ## daria las dos hubicaciones
