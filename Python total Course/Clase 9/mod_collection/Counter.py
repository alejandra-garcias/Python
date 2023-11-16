from collections import Counter
##sirve para hacer cuentas
numeros = [8,2,4,14,5,8,7,1,4,5,7,8]
print(Counter(numeros))
serie = Counter[1,2,5,47,8,4,6,8,7,4,5,2,4,5,7]
print(serie.most_common()) ## busca la cantidad de veces que se repiten los numeros en la serie y los ordena de mas veces a menos
print(serie.most_common(1)) ## busca la cantidad de veces que se repiten los numeros y muestra el que mas aparece, si pongo dos salen los dos primero
