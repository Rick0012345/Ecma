import pygame
from pygame.locals import *
from sys import exit


pygame.init()
altura = 800
largura = 600
x = altura/2
y = largura/2
red = 225
pygame.display.set_caption('MATH GAME')
tela = pygame.display.set_mode((altura, largura), 0, 32)
relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.fill(000)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                x -= 50
            if event.key == K_RIGHT:
                x += 50
            if event.key == K_UP:
                y -= 50
            if event.key == K_DOWN:
                y += 50
    pygame.draw.rect(tela, (red, 255, 255), (x, y, 40, 50))
   
   
    pygame.display.update()