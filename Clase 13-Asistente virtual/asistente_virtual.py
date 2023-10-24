import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

#opciones de vox:
español='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0'
ingles='HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'  

#transformar voz en texto(escuchar nuestro microfono y devolver el audio como texto)
def transformar_audio_en_texto():
    #almacenar recogniser en variable
    r=sr.Recognizer()

    #configurar el microfono
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8
        #informar que comenzo la grabacion
        print('Grabando')
        #guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            #buscar en google lo que ha escuchado
            pedido = r.recognize_google(audio, language='es-es')
            #prueba de que pudo transformar voz en texto
            print(f'Dijiste: {pedido}')
            #devolver pedido
            return pedido
        #si no funciona:
        except sr.UnknownValueError:
            print('ups, no entendid')
            return "sigo esperando"
        except sr.RequestError:
            return('sigo esperando')
        except:
            print('Algo ha salido mal')
            return('sigo esperando')

#funcion para que el asistente pueda ser escuchado:
def hablar(mensaje):
    #encender el motor de puttsx3 ( a la variable se le pone engine por defecto)
    engine = pyttsx3.init()
    engine.setProperty('voice',español)
    #pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()

#informar del dia de la semana:
def pedir_dia():
    #crear variable con los datos de hoy
    dia=datetime.date.today()
    print(dia)
    #crear una variable para el dia de la semana
    dia_semana=dia.weekday()
    print(dia_semana)#esto me da el indice del dia por lo que creo un diccionario
    #diccionario con nombres de dias
    calendario = {0:'Lunes',
                  1:'Martes',
                  2:"Miercoles",
                  3:'Jueves',
                  4:'Viernes',
                  5:'Sabado',
                  6:'Domingo'}
    #decir dia de la semana
    hablar(f'Hoy es {calendario[dia_semana]}')

#informar hora
def pedir_hora():
    #crear variable con los datos hora:
    hora = datetime.datetime.now()
    hora = f'Son las {hora.hour} y {hora.minute}'
    print(hora)
    #decir la hora
    hablar(hora)

#saludo inicia:
def saludo_inicial():
    #crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour >21:
        momento = '¡Buenas noches!'
    elif  6<= hora.hour < 13:
        momento = '¡Buenos dias!'
    else:
        momento = '¡Buenas tardes!'
    #saludar
    hablar(f'{momento}¡Muchas gracias por configurarme Alejandra! Mi nombre es Coco. En compensación, voy a hacer tu vida mucho más fácil. Me convertiré en tu asistente personal. ¡Dime qué necesitas y te asistiré!')

#funcion central del asistente
def pedir_cosas():
#activar saludo inicial
    saludo_inicial()
#variable que finaliza el asistente
    comenzar = True
#loop central para que el programa siempre funcione
    while comenzar:
        #activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()
        if 'abrir youtube' in pedido:
            hablar('Por supuesto, estoy abriendo Youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'buscar en google' in pedido:
            hablar('Claro, ahora mismo lo hago.')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es'in pedido:
            pedir_hora()
            continue

        elif 'busca en wikipedia' in pedido:
            hablar('Vale, ahora mismo te lo busco y lo muestro')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences = 1)
            hablar(f'Wikipedia dice lo siguiente: {resultado}')
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Vale, ahora mismo te lo busco y lo muestro')
            pedido = pedido.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido,sentences = 1)
            hablar(f'Wikipedia dice lo siguiente: {resultado}')
            continue
        elif 'busca en internet' in pedido:
            hablar('Vale, ahora mismo te lo busco y lo muestro')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que he encontrado')
            continue
        elif 'reproducir'in pedido:
            hablar('Yo tambien estoy deseando esto!.Lo busco ahora mismito')
            pedido =pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma'in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones de ' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'Apple':'APPL',
                       'Amazon':'AMZN',
                       'Google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Tickers(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre,el precio de {accion} es {precio_actual} dolares')
                continue
            except:
                hablar('Perdon, pero no tengo informacion actual sobre esa accion')
        elif 'adiós' in pedido:
            hablar('Muchas gracias, si necesitas cualquier cosa avisame')
            break


        
pedir_cosas()