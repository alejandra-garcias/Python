def cuadrado(un_numero):
    '''imprime el cuadrado del numero'''
    return (un_numero ** 2) ##esta devuelve un valor

sesentaycuatro = cuadrado(8)
print(sesentaycuatro)

def sumar (gasto1,gasto2):
    '''Suma los gastos de dos personas'''
    return (gasto1+gasto2)
gastos = sumar(4,8)
print(gastos)

##alternativa:
def sumar2(gasto1,gasto2):
    gastoss = gasto1 + gasto2
    print(gastoss)
    return(gastoss)

sumar2(1,1)

####Práctica Return 1Crea una función llamada potencia que tome dos valores numéricos como argumentos. Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
def potencia (base,exponente):
    '''calcula la potencia de un numero por otro'''
    return (base**exponente)
print(potencia(2,2))
### o 
def potencia1 (base,exponente):
    '''calcula la potencia de un numero por otro'''
    total = (base**exponente)
    return total
print(potencia(2,2))
print(potencia1(3,3))

####Práctica Return 2Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función y evaluar su resultado.Pista: para realizar la conversión, la función internamente debe multiplicar este valor en dólares por 0.90 para obtener el monto equivalente en euros.
def usd_a_eur(dolar):
    '''pasa de dolar a euro una cantidad'''
    euros = dolar * 0.9
    return euros

def usd_a_eur2(dolar):
    '''hace lo mismo que la de arriba'''
    return (dolar *0.9)
euros = usd_a_eur2(1)

###Práctica Return 3Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, para sumisitrarle como argumento a la función creada.Pista: dentro de la función creada, deberás utilizar métodos de strings ya vistos.

def invertir_palabra(palabra):
    ''''invierte palabra'''
    palabra_invertida = palabra[::-1]
    return(palabra_invertida)
invertir_palabra("Python")

print(invertir_palabra("Python"))