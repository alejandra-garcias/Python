import zipfile
'''comprimir
mi_zip = zipfile.ZipFile('archivo_comprimido.zip','w')
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')

mi_zip.close()
'''

'''descomprimir
'''
zip_abierto = zipfile.ZipFile('archivo_comprimido.zip','w')
zip_abierto.extractall()
