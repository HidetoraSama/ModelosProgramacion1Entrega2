import pygame, sys, time, inspect
from pygame.locals import *
from utilidades import *
from TodosPrueba import *

def selectClass():
    global currentScreen
    currentScreen = 1
    
def goBattlefield():
    global currentScreen
    currentScreen = 2

def goCloningfield(swordsmans):
    global currentScreen, swordsman, swordsman2, swordsman3
    currentScreen = 3
    swordsman=swordsmans[0]
    swordsman2=swordsmans[1]
    swordsman3=swordsmans[2]

def goBack():
    global currentScreen
    currentScreen = 0

def fixClass():
    global currentClass
    currentClass = gnam()

def clonePrSup():
    swordsmanBuilder = SwordsmanBuilder()
    director = Director()
    director.setBuilder(swordsmanBuilder)
    swordsman = director.getCharacter()
    swordsman2 = swordsman.shallowClone()
    swordsman3 = swordsman.shallowClone()
    swordsmans=[swordsman, swordsman2, swordsman3]
    goCloningfield(swordsmans)

def clonePrPro():
    swordsmanBuilder = SwordsmanBuilder()
    director = Director()
    director.setBuilder(swordsmanBuilder)
    swordsman = director.getCharacter()
    swordsman2 = swordsman.deepClone()
    swordsman3 = swordsman.deepClone()
    swordsmans=[swordsman, swordsman2, swordsman3]
    goCloningfield(swordsmans)

def charImgs(charClass = ""):
    x = Singleton()
    x.val = StandardFactory.get_factory(charClass)
    weapon = x.val.get_weapon()
    shield = x.val.get_shield()
    body = x.val.get_body()
    return weapon.show(), shield.show(), body.show()

pygame.init()

x=0
y=0
dur=0
curdur=0

pygame.mixer.music.load('LostWoods.mp3')
pygame.mixer.music.play(0)
sfxGolpe = pygame.mixer.Sound('Golpe.wav')

screen = pygame.display.set_mode((600, 500), 0, 32)

btnclases = Button("Seleccionar clase", (300, 190), selectClass, "", (255, 162, 18), (0, 0, 0), (150, 35), "Segoe UI semibold", 17)
btnbatalla = Button("Campo de batalla", (300, 310), goBattlefield, "", (41, 255, 56), (0, 0, 0), (150, 35), "Segoe UI semibold", 17)
btnback = Button("«", (570, 480), goBack, "", (255, 255, 255), (0, 0, 0), (25, 25), "Press start 2p", 20)
buttons = [btnclases, btnbatalla]

btnswordsman = Button("", (135, 275), fixClass, "Swordsman", (0, 0, 0), (0, 0, 0), (120, 340))
btnsorcerer = Button("", (305, 275), fixClass, "Sorcerer", (0, 0, 0), (0, 0, 0), (120, 340))
btnknight = Button("", (445, 275), fixClass, "Knight", (0, 0, 0), (0, 0, 0), (120, 340))
btnclasses = [btnswordsman, btnsorcerer, btnknight]

btnsuperf = Button("Clonacion superficial", (290, 190), clonePrSup, "superficial", (255, 162, 18), (0, 0, 0), (170, 35), "Segoe UI semibold", 17)
btnprofun = Button("Clonacion profunda", (290, 310), clonePrPro, "profunda", (41, 255, 56), (0, 0, 0), (170, 35), "Segoe UI semibold", 17)
btnclonadores = [btnsuperf, btnprofun]

btnbacks = [btnback]

currentScreen = 0
currentClass = ""

while True:

    screen.fill((0, 0, 0))
    btnback.draw(screen)
    pygame.mouse.set_visible(1)

    if currentScreen == 0:
        for button in buttons:
            button.draw(screen)
    elif currentScreen == 1:
        for button in btnclasses:
            button.draw(screen)

        tts(screen, "Seleccion de clases", 190, 30, 25, (247, 247, 247), "seguisb.ttf")
        tts(screen, "Armas", 273, 80, 18, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Escudos", 265, 190, 18, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Cuerpos", 265, 300, 18, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Swordsman", 80, 445, 20, (135, 210, 108), "seguisb.ttf")
        tts(screen, "Sorcerer", 260, 445, 20, (210, 108, 145), "seguisb.ttf")
        tts(screen, "Knight", 420, 445, 20, (247, 247, 247), "seguisb.ttf")

        a1, b1, c1 = charImgs("swordsman") 
        a1i = pygame.image.load(a1+".png").convert_alpha()
        b1i = pygame.image.load(b1+".png").convert_alpha()
        c1i = pygame.image.load(c1+".png").convert_alpha()

        screen.blit(a1i, (130, 130))
        screen.blit(b1i, (125, 250))
        screen.blit(c1i, (120, 360))

        a2, b2, c2 = charImgs("sorcerer")
        a2i = pygame.image.load(a2+".png").convert_alpha()
        b2i = pygame.image.load(b2+".png").convert_alpha()
        c2i = pygame.image.load(c2+".png").convert_alpha()

        screen.blit(a2i, (295, 130))
        screen.blit(b2i, (290, 250))
        screen.blit(c2i, (285, 360))

        a3, b3, c3 = charImgs("knight")
        a3i = pygame.image.load(a3+".png").convert_alpha()
        b3i = pygame.image.load(b3+".png").convert_alpha()
        c3i = pygame.image.load(c3+".png").convert_alpha()

        screen.blit(a3i, (440, 140))
        screen.blit(b3i, (435, 250))
        screen.blit(c3i, (430, 360))

    elif currentScreen == 2:
        for button in btnclonadores:
            button.draw(screen)

    elif currentScreen == 3:
        pygame.mouse.set_visible(0)
        tts(screen, "Modo de ataque", 190, 30, 25, (183, 0, 24), "seguisb.ttf")

        bod1 = pygame.image.load(currentClass+"-body.png").convert_alpha()
        screen.blit(bod1, (130, 190))
        b1hp, b1dps, b1pps = swordsman.stats()
        tts(screen, "Swordsman stats", 80, 120, 15, (255, 211, 74), "seguisb.ttf")
        tts(screen, "HP"+str(b1hp), 80, 140, 13, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Dps"+str(b1dps), 125, 140, 13, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Pps"+str(b1pps), 170, 140, 13, (255, 211, 74), "seguisb.ttf")

        bod2 = pygame.image.load(currentClass+"-body.png").convert_alpha()
        screen.blit(bod1, (285, 190))
        b2hp, b2dps, b2pps = swordsman2.stats()
        tts(screen, "Swordsman2 stats", 230, 120, 15, (255, 211, 74), "seguisb.ttf")
        tts(screen, "HP"+str(b2hp), 230, 140, 13, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Dps"+str(b2dps), 275, 140, 13, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Pps"+str(b2pps), 325, 140, 13, (255, 211, 74), "seguisb.ttf")

        bod3 = pygame.image.load(currentClass+"-body.png").convert_alpha()
        screen.blit(bod3, (440, 190))
        b3hp, b3dps, b3pps = swordsman3.stats()
        tts(screen, "Swordsman3 stats", 390, 120, 15, (255, 211, 74), "seguisb.ttf")
        tts(screen, "HP"+str(b3hp), 390, 140, 13, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Dps"+str(b3dps), 435, 140, 13, (255, 211, 74), "seguisb.ttf")
        tts(screen, "Pps"+str(b3pps), 480, 140, 13, (255, 211, 74), "seguisb.ttf")


        if curdur <= 0:
            cursor = pygame.image.load("ataque1.png").convert_alpha()
            screen.blit(cursor, gmp())
        else:
            curdur-=1
            screen.blit(cursor, gmp(0,-20))

        prect=bod1.get_rect(topleft=(130,190))
        prect2=bod2.get_rect(topleft=(285,190))
        prect3=bod3.get_rect(topleft=(440,190))


    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mousebuttondown(btnbacks)
                if currentScreen == 0:
                    mousebuttondown(buttons)
                elif currentScreen == 1:
                    mousebuttondown(btnclasses)
                elif currentScreen == 2:
                    mousebuttondown(btnclonadores)
                elif currentScreen == 3:
                    if prect.collidepoint(pygame.mouse.get_pos()):
                        sfxGolpe.play()
                        dur=35
                        curdur=10
                        swordsman.health-=10
                        cursor = pygame.image.load("ataque2.png").convert_alpha()
                    elif prect2.collidepoint(pygame.mouse.get_pos()):
                        sfxGolpe.play()
                        dur=35
                        curdur=10
                        swordsman2.health-=10
                        cursor = pygame.image.load("ataque2.png").convert_alpha()
                    elif prect3.collidepoint(pygame.mouse.get_pos()):
                        sfxGolpe.play()
                        dur=35
                        curdur=10
                        swordsman3.health-=10
                        cursor = pygame.image.load("ataque2.png").convert_alpha()


    tts(screen, str(gmp()), 5, 487, 8, (255, 0, 0), "Arcade.ttf")
    tts(screen, "Current class: " + currentClass, 5, 8, 8, (250, 222, 129), "Arcade.ttf")

#    pygame.time.Clock().tick(60)
    pygame.display.update()