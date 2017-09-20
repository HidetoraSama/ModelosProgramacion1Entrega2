import pygame, sys, os
from pygame import *

global name
name = ""

def gnam():
    return name

def tts(screen, text, x, y, size = 50, color = (0, 0, 0), font_type = 'ARCADECLASSIC.TTF'):
    text = str(text)
    font = pygame.font.Font(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
    
def gmp(px=0, py=0):
    x,y = pygame.mouse.get_pos()
    return x+px,y+py

def pause():
    PrPause = input("Press any key to continue...")

WHITE = (255, 255, 255)
GREY = (55, 55, 55)
BLACK = (0, 0, 0)

class Button():
    def __init__(self, txt, location, action, tag="", bg=WHITE, fg=BLACK, size=(80, 30), font_name="ARCADECLASSIC", font_size=16):
        self.color = bg  # the static (normal) color
        self.bg = bg  # actual background color, can change on mouseover
        self.fg = fg  # text color
        self.size = size
        self.tag = tag

        self.font = pygame.font.SysFont(font_name, font_size)
        self.txt = txt
        self.txt_surf = self.font.render(self.txt, 1, self.fg)
        self.txt_rect = self.txt_surf.get_rect(center=[s//2 for s in self.size])

        self.surface = pygame.surface.Surface(size)
        self.rect = self.surface.get_rect(center=location)

        self.call_back_ = action

    def draw(self, screen):
        self.mouseover()

        self.surface.fill(self.bg)
        self.surface.blit(self.txt_surf, self.txt_rect)
        screen.blit(self.surface, self.rect)

    def mouseover(self):
        self.bg = self.color
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            self.bg = GREY  # mouseover color

    def call_back(self):
        self.call_back_()

def mousebuttondown(buttons):
    pos = pygame.mouse.get_pos()
    for button in buttons:
        if button.rect.collidepoint(pos):
            sfxClick = pygame.mixer.Sound('click.wav')
            sfxClick.play()
            global name
            name = str(button.tag)
            button.call_back()