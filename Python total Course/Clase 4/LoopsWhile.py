##loop con while, sucede mientras se de una determinada condicion
monedas = 5
while monedas>0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas -1 ## monedas- = 1
else:
    print(f"Te has quedado sin monedas")


respuesta = 's'
while respuesta == 's':
    respuesta = input("quieres seguir? s/n")
    
else:
    print("Gracias")

#####
respuesta = 's'
while respuesta == 's':
    pass ##guarda espacio para seguir en otro momento y no tener que terminar este codigo
    
print("Gracias")

nombre = input ("tu nombre : ")
for element in nombre:
    if element ==  'ñ':
        break ### interrumpe la iteracion actual y no se imprime nada mas
    print(element)

nombre = input ("tu nombre : ")
for element in nombre:
    if element ==  'ñ':
        continue ### interrumpe la iteracion actual 1 vez y continua
    print(element)


