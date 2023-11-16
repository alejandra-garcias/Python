#Calculadora de comisiones
nombre = input ("Cual es tu nombre?")
vendido = float(input("Cuanto has venido este mes"))
comision =round((vendido * 0.13),2)
print(f"Hola {nombre}, tus ventas han sido {vendido} por lo que has generado una comision de {comision} $")
#####
nombre = input ("Cual es tu nombre?")
comision = round(float(input("Cuanto has venido este mes"))*0.13,2)
print(f"Hola {nombre},has generado una comision de {comision} $")
