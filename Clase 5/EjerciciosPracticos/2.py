def ordenar(palabra):
    palabra = palabra.lower()
    palabra.split()
    nuevalista = []

    for valor in palabra:

        if valor not in nuevalista:
            nuevalista.append(valor)
        else:
           pass
    nuevalista.sort()
    return nuevalista

    
 

print(ordenar('entretenido'))

####con sets:
def letras_unicas(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)
    
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista
print(letras_unicas('entretenido'))

