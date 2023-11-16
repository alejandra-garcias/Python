
import bs4
import requests
resultado = requests.get('https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')
sopa = bs4.BeautifulSoup(resultado.text,'lxml')
imagenes = sopa.select('.img-responsive')[0]['src']
print(imagenes)
imagen_curso_1 = requests.get(imagenes)
print(imagen_curso_1.content)
f= open('mi_imagen.jpg','wb') ## write en binario
f.write(imagen_curso_1.content)
f.close()

##imagen guardada, lo puedo poner en un loop y poder rascar todas las que necesite