##Valor minimo:
menor = min(58,52,6,2,1,4,555,3,-1)
print(menor)
##valor maximo
maximo = max(58,52,6,2,1,4,555,3,-1)

lista = [58,96,72,64,3,45]
print(f'El menor es {min(lista)} y el mayor es {max(lista)}')

## min con string busca primero en las mayusculas y despues las minusculas
nombre = 'Alejandra'
print(min(nombre.lower()))
##dicionadios
dic = {'c1':45,'c2':11}
print(min(dic))## te devuelve la clave primera, c1
print(min(dic.values))###22


##Práctica Min y Max 1 Obtén el valor máximo entre los valores de la siguiente lista, y almacénalo en una variable llamada valor_maximo:
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5] 
valor_maximo = max(lista_numeros)

##Práctica Min y Max 2.Calcula la diferencia entre el valor máximo y el mínimo en la siguiente lista de números, y almacénalo en una variable llamada rango:

lista_numeros = [44542247, 21310, 2134747, 44556475, 121676, 6654067, 353254, 123134, 552512, 611665]
rango = (max(lista_numeros) - (min(lista_numeros)))


##Práctica Min y Max 3.Utilizando max(), min() y métodos de diccionarios, obtén el mínimo valor a partir del siguiente diccionario:diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}Almacena dicho valor en una variable llamada edad_minima.También, obtén el nombre que se ubica último en orden alfabético, y almacénalo en una variable llamada ultimo_nombre. #### la letra de menor valor es la A
diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)