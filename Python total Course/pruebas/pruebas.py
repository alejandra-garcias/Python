def descending_order(num):
    num = list(str(num))
    num=sorted(num,reverse=True)
    num = "".join(num)
    num = int(num)
    return(num)


def square_digits(num):
    num = list(str(num))
    lista_cuadrado = []
    for numero in num:
          numero = int(numero) **2
          numero = str(numero)
          lista_cuadrado.append(numero)
    lista_cuadrado = "".join(lista_cuadrado)
    lista_cuadrado = int(lista_cuadrado)
    return (lista_cuadrado)
          
def solution(number):
    suma_numeros = 0
    if number <0:
        return 0
    else:
        number-=1
        while number > 0:
            number -=1
            if number % 3 or number % 5 == 0:
                suma_numeros +=number

    print(suma_numeros)


def sum_two_smallest_numbers(numbers):
    numbers = sorted(numbers)
    return numbers[0]+numbers[1]

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "0dd"
    
##return 'Odd' if number % 2 else 'Even'
