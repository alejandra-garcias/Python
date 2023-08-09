##Zip junta 2 listas y las convierte en un tuple que mezcla ambas listas
nombre = ['Ana','Hugo',"Valeria"]
edad = [36,54,15]
ciudad = ["Lima", "Peru","Sevilla"]

combinados = list(zip(nombre,edad,ciudad)) ##tenemos que ponerle list delante para poder verlo, sino nos da un objeto que parece un link. lega hasta el largo de la lista mas corta,puedes hacer todos los que quieras
print(combinados)

for nombre,edad,ciudad, in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}")

###Práctica Zip 1 Muestra en pantalla frases como la del siguiente ejemplo:La capital de Alemania es Berlín.Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinado = list(zip(capitales,paises))

for capital,pais in combinado:
    print(f"La capital de {pais} es {capital}")

###Práctica Zip 2-Crea un objeto zip formado a partir de listas, de un conjunto de marcas y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ["Sony", "Adidas", "Microsoft", "Pepsi", "Toyota"]
productos =[    "PlayStation 5","Zapatillas Ultraboost","Surface Laptop 4","Pepsi Cola","Corolla"]
mi_zip = list(zip(marcas,productos))


###Práctica Zip 3.Crea el zip con las traducciones los números del 1 al 5 en español, portugués e inglés (en el mismo orden), y convierte el objeto generado en una lista almacenada en la variable numeros:

esp = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
port = ['um', 'dois', 'três', 'quatro', 'cinco']
ing = ['one', 'two', 'three', 'four', 'five']

numeros = list(zip(esp,port,ing))
print(numeros)