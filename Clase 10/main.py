import pygame
import random
import math
from pygame import mixer

#Inicializar Pygame
pygame.init()

#Crear la pantalla
pantalla = pygame.display.set_mode((800,600))

# Titulo e Icono
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load('meteorito.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('Fondo.jpg')

##agregar musica
mixer.music.load('MusicaFondo.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)
#Jugador
img_jugador = pygame.image.load("astronave.png")
jugador_x = 368
jugador_y = 500
jugador_x_cambio = 0
jugador_y_cambio = 0

#enemigo
img_enemigo = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 10

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("ovni.png"))
    enemigo_x.append(random.randint(0,736))
    enemigo_y.append(random.randint(50,200))
    enemigo_x_cambio.append( 0.2)
    enemigo_y_cambio.append( 50)

#bala
img_bala = pygame.image.load("balas.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = 0.5
bala_visible = False

#puntajes
puntos = 0
fuente = pygame.font.Font('Trepang_free.ttf',32)
texto_x =10
texto_y = 10

##texto final del juego
fuente_final = pygame.font.Font('Trepang_free.ttf', 40)

def texto_final():
    mi_fuente_final = fuente_final.render("GAME OVER", True, (255, 255, 255))
    pantalla.blit(mi_fuente_final, (60, 200))



##mostrar puntaje:
def mostrar_puntaje(x,y):
    texto = fuente.render(f'Puntos: {puntos}', True, (255,255,255))
    pantalla.blit(texto,(x,y))
#Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador,(x, y))

#Funcion enemigo
def enemigo(x, y,ene):
    pantalla.blit(img_enemigo[ene],(x, y))

#Funcion disparar
def disparar(x,y):
    global bala_visible
    bala_visible = True
    pantalla.blit(img_bala,(x + 16, y + 10))

##funcion detectar colisiones
def hay_colision(x_1,y_1,x_2,y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2,2) + math.pow(y_1 - y_2,2))
    if distancia <27:
        return True
    else:
        False


#Loop del juego
se_ejecuta = True

while se_ejecuta:
    #imagen fondo:
    pantalla.blit(fondo,(0,0))
    
    #iterar eventos
    for evento in pygame.event.get():
        #evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        #evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_bala = mixer.Sound('disparo.mp3')
                sonido_bala.set_volume(0.1)
                sonido_bala.play()
                if not bala_visible:
                    bala_x = jugador_x
                    disparar(bala_x,bala_y)
        #evento soltar flechas
        if evento.type ==pygame.KEYUP:
            if evento.key==pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    #modificar ubicacion jugador       
    jugador_x +=jugador_x_cambio
   

    #mantener dentro de bordes jugador
    if jugador_x <=0:
        jugador_x = 0
    elif jugador_x >=736: ## ya que la pantalla tiene 800 pixeles y mi nave 64
        jugador_x = 736


    #modificar ubicacion enemigo
    for e in range(cantidad_enemigos):
        #fin de juego
        if enemigo_y[e]>500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break
        enemigo_x[e] +=enemigo_x_cambio[e]
    #mantener dentro de bordes enemigo
        if enemigo_x[e] <=0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] +=enemigo_y_cambio[e]
        elif enemigo_x[e] >=736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] +=enemigo_y_cambio[e]
          #colision
        colision = hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            sonido_colision = mixer.Sound('golpe.mp3')
            sonido_colision.set_volume(0.1)
            sonido_colision.play()
            bala_y = 500
            bala_visible = False
            puntos+=1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)

        enemigo(enemigo_x[e], enemigo_y[e],e)
    
    ##Movimiento balas
    if bala_y <=-64:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar(bala_x,bala_y)
        bala_y -=bala_y_cambio

    #colision
        colision = hay_colision(enemigo_x[e],enemigo_y[e],bala_x,bala_y)
        if colision:
            bala_y = 500
            bala_visible = False
            puntos+=1
            enemigo_x[e] = random.randint(0,736)
            enemigo_y[e] = random.randint(50,200)
        enemigo(enemigo_x[e], enemigo_y[e],e)



    jugador(jugador_x, jugador_y)
    mostrar_puntaje(texto_x,texto_y)
    
    #actualizar
    pygame.display.update()

