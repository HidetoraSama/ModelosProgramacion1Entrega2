import pygame, sys, time
from pygame.locals import *
from utilidades import *

def slclase():
    print("seleccion de clases! " * 5)
    
def campo():
    print("campo de batalla! " * 5)

def initi():
    pygame.mixer.music.play(0)

pygame.init()

x=0
y=0
dur=0
curdur=0
pygame.mixer.music.load('LostWoods.mp3')
pygame.mixer.music.play(0)

sfxGolpe = pygame.mixer.Sound('Golpe.wav')

menu = pygame.display.set_mode((600, 500), 0, 32)

btnclases = Button("Seleccionar clase", (200, 100), slclase, (41, 255, 56), (0, 0, 0), (150, 35))
btnbatalla = Button("Campo de batalla", (200, 190), campo, (41, 255, 56), (0, 0, 0), (150, 35))
buttons = [btnclases, btnbatalla]

while True:
    menu.fill((0, 0, 0))

    pygame.mouse.set_visible(0)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_r:
                initi()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown(buttons)
            if event.button == 1:
                if prect.collidepoint(pygame.mouse.get_pos()):
                    sfxGolpe.play()
                    dur=35
                    curdur=10
                    player = pygame.image.load("humano-golpe.png").convert_alpha()
                    cursor = pygame.image.load("ataque2.png").convert_alpha()

    #Controla movimiento del jugador
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        y -= 5
    if pressed[pygame.K_a]:
        x -= 5
    if pressed[pygame.K_s]:
        y += 5
    if pressed[pygame.K_d]:
        x += 5

    #Controla duracion de cambio de imagen
    if dur <= 0:
        player = pygame.image.load("humano.png").convert_alpha()
    else:
        dur -= 1

    menu.blit(player, (x,y))

    if curdur <= 0:
        cursor = pygame.image.load("ataque1.png").convert_alpha()
        menu.blit(cursor, gmp())
    else:
        curdur-=1
        menu.blit(cursor, gmp(0,-20))

    #Dibuja botones en la pantalla               
    for button in buttons:
        button.draw(menu)

    
    
    prect=player.get_rect(topleft=(x,y))
    
    tts(menu, str(dur), 5, 5, 20, (255, 0, 0))

    pygame.time.Clock().tick(60)
    pygame.display.update()
                
