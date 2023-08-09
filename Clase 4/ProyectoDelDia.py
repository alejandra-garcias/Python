from random import randint
premio = randint(1,100)
intentos = 8
intentos_usados = 0

nombre = input("Cual es tu nombre?")
print(f"Hola {nombre}, te propongo un juego, voy a pensar un numero del 1 al 100 y te doy 8 intentos para que adivines que numero es")

while (intentos > 0) :
        intentos = intentos - 1 
        intentos_usados = intentos_usados + 1
        guess = int(input(f"Elige un numero "))

        if (guess == premio):
            print(f'Enhorabuena has acertado y lo has hecho en {intentos_usados} intentos')
            break

        elif(guess> 100) or (guess <= 0) :
            print(f"Tu numero esta fuera de rango no es valido , te quedan {intentos} intentos")

        elif(guess < premio):
            print(f"Tu numero es menor al que he pensado, prueba otro , te quedan {intentos} intentos") 

        elif(guess> premio):
            print(f"Tu numero es mayor al que he pensado, tienes {intentos} mas, prueba otro") 

else:
     print(f'te has quedado sin intentos el numero secreto era: {premio}')
