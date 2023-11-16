import shutil

carpeta_origen = 'C:\\Users\\algas\\OneDrive\\Escritorio\\Python\\Codigo Python\\Clase 9\\pruebas'
archivo_destino = 'Todo_comprimido'
shutil.make_archive(archivo_destino,'zip','carpeta origen') ##construyendo archivo comprimido con shutil

##descomprimiendo:
shutil.unpack_archive('Todo_Comrimido.zip','Extraccion terminada')