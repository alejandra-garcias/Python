##Práctica Métodos y Ayuda 1.Remueve los caracteres a la izquierda de nuestro texto principal:,,:%_#Utiliza el método lstrip(). Imprime el resultado en pantalla:",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa. Puedes utilizar variables intermedias si las necesitas.
cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
nueva_cadena = cadena.lstrip(",,:,%,_#")
print(nueva_cadena)

##Práctica Métodos y Ayuda 2.Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando el método insert():Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)
####Práctica Métodos y Ayuda 3Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común), utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = (marcas_smartphones.isdisjoint(marcas_tv))
print(conjuntos_aislados)