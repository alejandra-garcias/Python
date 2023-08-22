class Persona:
    triste = False

class Horacio(Persona):
    @classmethod
    def rechazado_trabajo(cls):
        cls.triste = True
        print('Horacio esta triste porque no ha conseguido el trabajo')
    
    @classmethod
    def estudiandopython(cls):
        cls.triste = False
        print('Horacio vuelve a estar feliz porque esta estudiando Python y conseguira algo mejor')
    

Horacio.rechazado_trabajo()
Horacio.estudiandopython()