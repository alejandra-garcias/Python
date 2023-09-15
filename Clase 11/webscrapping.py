import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')
print(resultado.text)
sopa =  bs4.BeautifulSoup(resultado.text,'lxml')
print(sopa.select('title')[0]) ##con select elijo que etiqueta quiero leer
print(sopa.select('title')[0].getText())##con este ya solo veo el texto, no veo las etiquetas
parrafo_especial = sopa.select('h1')[0].getText()
print(parrafo_especial)
