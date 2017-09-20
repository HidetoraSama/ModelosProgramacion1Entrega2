import pygame, sys
from test1 import *

def my_great_function():
    print("Great! " * 5)

def my_fantastic_function():
    print("Fantastic! " * 5)

pygame.init()

screen = pygame.display.set_mode((120, 100))
RED = (255, 0, 0)
BLUE = (0, 0, 255)

button_01 = Button("Great!", (60, 30), my_great_function)
button_02 = Button("Fantastic!", (60, 70), my_fantastic_function, bg=(50, 200, 20))
buttons = [button_01, button_02]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousebuttondown(buttons)

    for button in buttons:
        button.draw(screen)

    pygame.display.update()
    #pygame.time.wait(40)


