import re
texto =  'llama al 546-524-58988 ya mismo'

patron = r'\d\d\d-\d\d\d-\d\d\d\d'
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group()) ### da el resultado

## patron podria cuantificarse
patron = r'\d{3}-\d{3}-\d{4}'

### compilarlo:
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
mi_resultado = re.search(patron,texto)
print(mi_resultado.group(2)) ## aqui solo me saldria el segundo d{3}

###ejemplo uso = VERIFICAR SI UNA CONTRASEñA ES VAlida
clave =  input('Clave')
patron = r'\D{1}\w{7}'
chequear = re.search(patron,clave)

###
texto = 'no abrimos los lunes por la tarde'
buscar = re.search(r'lunes|martes', texto)
buscar2 = re.search(r'.imos', texto) ##rimos
buscar2 = re.search(r'..imos', texto) ##brimos
buscar2 = re.search(r'..imos', texto) ##arimos
buscar2 = re.search(r'.imos..', texto) ##rimos l
buscar2 = re.search(r'^\d', texto) ## indica si se encuentra al comienzo. En este caso daria none porqe empieza el texto por no digito
buscar2 = re.search(r'\D$', texto) ## indica si se encuentra al final. En este caso daria none porqe empieza el texto por no digito
buscar2 = re.findall(r'[^\s]', texto) ## todos los caracteres que no sean espacios vacios entonces me da letra una por una
buscar2 = re.findall(r'[^\s]+', texto) ## todos los caracteres que no sean espacios vacios una o mas veces entonces los construye en una lista de palabras y cada vez que se encuentre un espacio vacio corta el grupo
print(''.join(buscar2)) ## texto sin espacios vacios/
