import pygame, sys
from pygame.locals import *
from utilidades import *

pygame.init()

skn = pygame.display.set_mode((400, 400), 0, 32)
rc = pygame.image.load("circulo-1.png").convert_alpha()

score=0
xco=0
yco=0

while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEMOTION:
            xco, yco = pygame.mouse.get_pos()
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                score+=1
    
    skn.fill((90, 90, 90))
    
    x, y = gmp()
    x-= rc.get_width()/2
    x-= rc.get_height()/2
    
    skn.blit(rc, (x, y))
    
    tts(skn, "x:"+str(xco)+ " y:" +str(yco), 1, 380, 15, (225, 0, 0), 'Arcade.ttf')
    tts(skn, "Score: " + str(score), 260, 5, 15, (225, 0, 0), 'Arcade.ttf')
    
    pygame.display.update()
    pygame.time.Clock().tick(60)
