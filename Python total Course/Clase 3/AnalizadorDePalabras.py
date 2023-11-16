mi_texto = input( "Dame un texto a comparar" )
text_min = mi_texto.lower()
aux1 = input( "Dime una letra" ) 
aux2 = input( "Dime una otra" )
aux3 = input( "Dime una otra" )
letras = aux1 + " " + aux2+ " " + aux3
letras_min = letras.lower()
lista_letras = letras_min.split()
print(lista_letras)

print("La letra " + aux1 +" aparece " + str(text_min.count(lista_letras[0]))+ " veces")
print("La letra " +  aux2 +" aparece " + str(text_min.count(lista_letras[1]))+ " veces")
print("La letra " + aux3 +" aparece " + str(text_min.count(lista_letras[2]))+ " veces")

texto_lista = mi_texto.split()
longitud_texto = len(texto_lista)
print("La longitud de tu texto es de " + str(longitud_texto) + " palabras")

print ("La primera palabra de tu texto es " + (texto_lista[0]))
print ("La primera palabra de tu texto es " + (texto_lista[-1]))

texto_lista.reverse()
print(texto_lista)

buscadorPython = " ".join(texto_lista)
resultado = "Python" in buscadorPython
AparecePython={'AparecePython':resultado}
print(AparecePython)