import bs4
import requests
resultado = requests.get('https://escueladirecta.com/p/excel-aplicado-al-analisis-financiero')
sopa = bs4.BeautifulSoup(resultado.text,'lxml')
tarjeta = sopa.select('.container p')
print(tarjeta)

for p in tarjeta:
    print(p.getText())