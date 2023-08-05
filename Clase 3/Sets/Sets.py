##no se puede repetir un mismo elemento
#no tienen indice
##son inmutable, no puedes escribir ni listas ni diccionarios dentro de un set
## piede escribirse tanto
set([1,2,3,4,5,6]) ## Aqui el set solo va a admitir un unico argumento
##como
{1,2,3,4,5,6}

mi_set=set([1,2,3,4,5,6])
print(type(mi_set))
print(mi_set)

otro_set={1,2,3}
## SI ADMITE TUPLES PORQUE ESTOS SI SON INMUTABLES  
print(len(mi_set))##ver tamaño
print(2 in mi_set)##ver si mi set contiene un 2


########## si tengo 2 sets que quiero juntar:
s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1.union(s2)
print(s3)## Devolvera {1,2,3,4,5,6}. El valor 3 que se repetia lo omite 

### añadir:
s1.add(4)
print(s1)
### eliminar:
##s2.remove(2)## si no existe el numero no lo eliminara y dara error
s2.discard(2)##En este caso si no lo hay no hara nada pero no tira error

##pop
s2.pop() # si no ponemos cual es se eliminara un valor aleatorio
##clear
s2.clear() # vacia el set entero

##Práctica Sets 1.Une los siguientes sets en uno solo, llamado mi_set_3:{1, 2, "tres", "cuatro"}{"tres", 4, 5}
mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5} 
mi_set_3=mi_set_1.union(mi_set_2)
print(mi_set_3)

##Práctica Sets 2Elimina un elemento al azar del siguiente set, utilizando métodos de sets.
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.pop())
##Práctica Sets 3.Agrega el nombre Damián al siguiente set, utilizando métodos de sets:
sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
print(sorteo.add("Damián"))
