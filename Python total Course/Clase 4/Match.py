cliente = {'nombre':'Federico',
           'edad': 45,
           'ocupacion':'instructor'}
pelicula = {'titulo':'Matrix',
            'ficha_tecnica':{'protagonista':'Keanu reeves',
                             'director' : 'Lana y Lilly Wachoswski'}}

elementos = [cliente,pelicula,'libro']
for element in elementos:
    match elementos:
        case{'nombre':nombre,
             'edad' :edad,
             'ocupacion': ocupacion}:
            print("es un cliente")
            print(nombre,edad,ocupacion)
        case{'titulo':titulo,
             'ficha_tecnica':{'protagonista':protagonista,
                              'director':director}}:
             print('Es una pelicula')
             print(titulo,protagonista,director)   
        case _:
            print("No se que es esto")