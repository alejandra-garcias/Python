mi_lista = [1,1,1,1,1,1]
print(len(mi_lista))

class CD:
   def __init__(self,autor,titulo,canciones):
      self.autor = autor
      self.titulo = titulo
      self.canciones = canciones
      
      
   def __len__(self): ## establezco como quiero que se comporte mi metodo len, que en este caso sera dandome el largo de el cd, es decir el numero de canciones.
     return self.canciones
   
   def __str__(self): ## establece la forma en la que yo quiero que se impirima el metodo string
     return (f'Album:{self.titulo} de {self.autor}')
   
   def __del__(self):
      print('Se ha eliminado el cd')

mi_cd = CD('Pink Floyd','The Wall', 24)

del mi_cd


###Práctica Métodos Especiales 1Dada la clase Libro, implementa el método especial __str__ para que cada vez que se imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: el título debe estar encerrado entre comillas dobles).

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas
        
    def __str__(self):
       return(f'"{self.titulo}", de {self.autor}')
    

##Práctica Métodos Especiales 2 Dada la clase Libro, implementa el método especial __len__ para que cada vez que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
       return int(self.cantidad_paginas)
    

##Práctica Métodos Especiales 3Dada la clase Libro, implementa el método especial __del__ para que el usuario sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que el libro se elimine.

class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print('Libro eliminado')