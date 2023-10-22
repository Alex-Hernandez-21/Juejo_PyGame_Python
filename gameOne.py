import random
import math
import sys
import pygame 
import os

#iniciamos pygame

pygame.init()

#Seguimos a establecer la pantalla (tamaño)

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height)) #aplica los parámetros y establece las medidas de la pantalla

#Establecemos el titulo de la ventana

pygame.display.set_caption("Pygame - Fire Game")

#Creamos una función para rutear los archivos

def resource_routes(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")   #devuelve al ruta absoluta de los recursos
        return os.path.join(base_path, relative_path)

# cargar imagenes fondo
background = pygame.image.load(resource_routes('assets/images/fondofire2.jpg'))

# upload_found = resource_routes("assets/images/fondofire2.jpg")  de esta forma tambien se pueden realizar 
# upload = pygame.image.load(upload_found)

# cargar icono
icon = pygame.image.load(resource_routes('assets/images/icon1.png'))

# upload_icon = resource_routes("assets/images/icon1.png")
# icon = pygame.image.load(upload_icon)

# cargar sonido
upload_sound = pygame.mixer.music.load(resource_routes('assets/audios/music1.mp3'))

#imagen del jugador
playerImg = pygame.image.load(resource_routes('assets/images/player1.png'))

#imagen de bala
bulletImg = pygame.image.load(resource_routes('assets/images/bullet.png'))

#cargar fuente para game over
font = pygame.font.Font(resource_routes('assets/fuentes/RAVIE.TTF'))

#cargar fuente de puntaje
score_font = pygame.font.Font(resource_routes('assets/fuentes/score.ttf'))

#icono de la ventana y reproducir sonido
pygame.display.set_icon(icon)
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()

#posición del jugador
x = 370
y = 470
x_change = 0
y_change = 0

#velocidad del jugador
speed = [1, 1]

#posiciones de los enemigos
enemyimg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 8
for i in range(num_of_enemies):
    enemyimg.append(pygame.image.load(resource_routes('assets/images/enemi1.png')))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 150))  # posición aleatoria del enemigo

    #velocidad del enemigo x y
    enemyX_change.append(4)
    enemyY_change.append(20)

    #guardar la posición de la bala
    bulletx = 0
    bullety = 480
    bulletx_change = 0
    bullety_change = 10
    bullet_state = "ready"

    score = 0

    #función que muetsra puntuación en la pantalla
    def show_score():
        score_value = font.render("Score "+ str(score), True, (255, 255, 255))
        screen.blit(score_value, (10, 10))


    #Funciones que me perimite dibujar  al jugador, al enemigo y disparar 
    def player(x, y):
        screen.blit(playerImg, (x, y))

    def enemy(x, y, i):
        screen.blit(enemyimg[i], (x, y))
        
    def fire_bullet(x, y):
        global bullet_state

        bullet_state = "fire"
        screen.blit(bulletImg, (x + 16, y + 10))

    #función para revisar el disparo bala-enemigo
    def isCollision(enemyX, enemyY, bulletx, bullety):
        distance = math.sqrt((math.pow(enemyX - bulletx, 2)) + (math.pow(enemyY - bullety, 2)))
        if distance < 27:
            return True
        else:
            return False
        
    #función de game over en pantalla
    def game_over():
        large_text = font.render("Game Over", True, (255, 255, 255))
        text_rect = large_text.get_rect(center=(int(screen_width/2),int(screen_height/2)))
        screen.blit(large_text, text_rect)

    #Función principal del juego
    def gamepy():
        global score
        global x
        global x_change
        global bulletx
        global bullety
        global bullet_state
        global collision

        in_game = True
        while in_game:
            screen.fill((0,0,0))     #limpia la pantalla
            screen.blit(background, (0,0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    in_game = False
                    pygame.quit()
                    sys.exit()
                
                if event.type == pygame.KEYDOWN:      #deja que el teclado desarrolle los movimientos
                    if event.key == pygame.K_LEFT:
                        x_change = -5

                    if event.key == pygame.K_RIGHT:
                        x_change = 5

                    if event.key == pygame.K_SPACE:
                        if bullet_state == "ready":
                            bulletx = x
                            fire_bullet(bulletx, bullety)
                    
                if event.type == pygame.KEYUP:       #detiene el movimiento al soltar las flechas
                    x_change = 0

                #podemos crear un condicional para actualizar al jugador
            x += x_change

            if x <= 0:
                x = 0
            elif x >= 736:
                x = 736

            
            for i in range(num_of_enemies):     #para cada enemigo realice el ciclo
                if enemyY[i] > 440:
                    for j in range(num_of_enemies):
                        enemyY[j] = 2000
                    game_over()

                enemyX[i] += enemyX_change[i]
                if enemyX[i] <= 0:
                    enemyX_change[i] = 5
                    enemyY[i] += enemyY_change[i]
                elif enemyX[i] >= 736:
                    enemyX_change[i] = -5
                    enemyY[i] += enemyY_change[i]


                collision = isCollision(enemyX[i], enemyY[i], bulletx, bullety)
                if collision:
                    # explosionSound = pygame.mixer.Sound('explosion.wav')
                    # explosionSound.play()
                    bullety = 454
                    bullet_state = "ready"
                    score += 1
                    enemyX[i] = random.randint(0, 735)
                    enemyY[i] = random.randint(0, 150)
                enemy(enemyX[i], enemyY[i], i)

            if bullety < 0:
                bullety = 454
                bullet_state = "ready"

            if bullet_state == "fire":
                fire_bullet(bulletx, bullety)
                bullety -= bullety_change

            player(x,y)
            show_score()

            pygame.display.update()

            clock.tick(120)

gamepy()
            
