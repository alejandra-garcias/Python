mi_dic={'c1':'valor1', 'c2':'valor2', 'c3':'valor3'}
##no tienen un orden especifico, solo puedes buscar valores en funcion a su clave
#Hay que usar diccionarios cuando por ejemplo no importa la posicion de algo o no la conoces. Ej, las caracteristicas de una persona
paciente = {
    'nombre':'Pepe',
    'apellido':'Garcia',
    'peso':'52kg'
}
print(paciente['peso'])
print(type(paciente))
print(paciente)
apellido = paciente['apellido']
print(apellido)
#### diccionario de diccionarios
midic={'c1':55, 'c2':[10,20,30], 'c3':{'s1':200,'s2':1}}
print(midic['c2'])##imprime la clave 2, [10,20,30]
print(midic['c2'][1])##imprime el primer elemento de la clave 2, 10
print(midic['c3'])##imprime la clave 3, {'s1':200,'s2':1}
print(midic['c3']['s1'])##imprime la clave 3, {'s1':200,'s2':1}

### imprime la letra e en mayuscula:
dic={'c1':['a','b','c'],'c2':['d','e','f']}
print(dic['c2'][1].upper())
### Agregar elementos a un diccionario;
dic2={1:'a',2:'b'}
print(dic2)
dic2[33]='c'
print(dic2)
##sobreescribir=
dic2[2]=554164154584
print(dic2)

##conocer todas las claver de un diccinarios
print(dic2.keys())
##imprimir los valores
print(dic2.values())
##imprimir todo el diccionario
print(dic2.items())
##Práctica Diccionarios 1.Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:

mi_dic={
'nombre': 'Karen',
'apellido': 'Jurgens',
'edad': 35,
'ocupacion': 'Periodista'
}
##Práctica Diccionarios 2.Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

##Práctica Diccionarios 3Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:nombre: Karen,apellido: Jurgens,edad: 36,ocupacion: Editora,pais: Colombiapara ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad']=36
mi_dic['ocupacion']="Editora"
mi_dic["pais"] = "Colombia"
print(mi_dic)