import pygame
from pygame.locals import *
from sys import exit
import button

screen = pygame.display.set_mode((600, 400), 0, 32)
pygame.init()

#rotas das imagens
start_img = pygame.image.load('start_button.png').convert_alpha()
exit_img = pygame.image.load('exit_button.png').convert_alpha()



start_button = button.Button(100, 200, start_img,1)
exit_button = button.Button(450, 200, exit_img,1)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))

    if start_button.draw(screen):
        print("start")
    if exit_button.draw(screen):
        exit()

    pygame.display.update()
