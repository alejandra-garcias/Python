def devolver_distintos(num1,num2,num3):
    comparador  = [num1,num2,num3]
    total = num1+num2+num3
    comparador.sort()
    listaordenada = comparador
    if total >15:
        return max(listaordenada)
    elif total<10:
        return min(listaordenada)
    elif total>=10 and total <=15:
        return listaordenada[2]
        
    return listaordenada
print(devolver_distintos(5,10,4))