###Práctica Loop While 1 - Crea un Loop While que se imprima en pantalla los números del 10 al 0, uno a la vez.
numero = 10
while numero >= 0:
    print(numero)
    numero = numero -1 ## esto lo pongo despues del print porque si lo hiciera antes, ya empezaria numero siendo 9
else:
    print('Game over')

###Práctica Loop While 2.Crea un Loop While que reste de uno en uno los números desde el 50 al 0 (ambos números incluídos) con las siguientes condiciones adicionales:- Si el número es divisible por 5, mostrar dicho número en pantalla (¡recuerda que aquí puedes utilizar la operación módulo dividiendo por 5 y verificando el resto!)- Si el número no es divisible por 5, continuar ejecutando el loop sin mostrar el valor en pantalla (no te olvides de seguir restando para que el programa no corra infinitamente).

numeros = 50
while numeros >=0:
    numeros = numeros -1 ### en este caso va aqui porque el loop tiene que ir dentro del while 
    if numeros % 5==0:
        print(numeros)
    else:
        continue
##Práctica Interrupción de Flujo-Crea un loop For a lo largo de la siguiente lista de números, imprimiendo en pantalla cada uno de sus elementos, e interrumpe el flujo en el momento que encuentres un valor negativo:No debes cambiar el orden de la lista.
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]

for element in lista_numeros:
    if element >=0:
        print(element)
    else:
        break
