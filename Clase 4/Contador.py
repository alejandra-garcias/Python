lista = ['a','b','c']
indice = 0

for item in lista:
    print (indice, item)
    indice +=1 ##aqui indice se suma de uno en uno para que vaya cambiando


##con el enumerador seri :
for item in enumerate(lista):
    print(item) ## crea un tupple que pone al indice y luego el contenido

## si queremos que lo haga de la misma forma que antes seria
for indice,item in enumerate(lista):
    print (indice,item)

for indice,item in enumerate(range(50,55)):
    print (indice,item)


mis_tuples = list(enumerate(lista))
print(mis_tuples)
print(mis_tuples[1])

###Práctica Enumerador 1.Imprime en pantalla frases como la siguiente:'{nombre} se encuentra en el índice {indice}'Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.Tip: utiliza loops!

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')


##Práctica Enumerador 2.Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener mediante enumerate() los índices de cada caracter del string "Python".Llama a la lista obtenida con el nombre de variable lista_indices .

lista_indices = list(enumerate("Python"))
print(lista_indices)

##Práctica Enumerador 3.Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M: lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:LoopsCondicionales ifEl método enumerate()Métodos de strings o indexado
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for nombres in lista_nombres:
    if nombres[0] == "M":
        print(nombres)