def contar_primos(num):
    rango = range(1,num)
    primos = [0]
    cantidad_primos = 0
    for num in rango:
        if num % num == 1 and num % 1 == num:
            primos.append(num)
            cantidad_primos +=1
        else:
            pass
        
    return f"Los numeros primos en este rango son {primos} y la cantidad total de numeros primos ha sido {cantidad_primos}"

print(contar_primos(5))

###
def contar_primos(num):
    primos = [2]
    iteracion = 3
    if num <2:
        return 0
    while iteracion <=0:
        for n in range(3,iteracion,2):
            if iteracion %n ==0:
                iteracion +=2
                break
        else:
            primos.append(iteracion)
            iteracion +=2
    print(primos)
    return len(primos)