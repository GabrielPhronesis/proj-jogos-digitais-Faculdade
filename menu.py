import pygame
from pygame.locals import *
from sys import exit
import button

screen = pygame.display.set_mode((700, 450))
pygame.init()
clock = pygame.time.Clock()
#rotas das imagens
bg_image = pygame.image.load('background_startgame.png').convert_alpha()

start_img = pygame.image.load('botao_jogar.png').convert_alpha()
exit_img = pygame.image.load('botao_sair.png').convert_alpha()
tutorial_img = pygame.image.load('botao_tutorial.png').convert_alpha()
credit_img = pygame.image.load('botao_creditos.png').convert_alpha()


start_button = button.Button(205, 140, start_img,0.1)
exit_button = button.Button(355, 140, exit_img,0.1)
tutorial_button = button.Button(205, 245, tutorial_img,0.1)
credit_button = button.Button(355, 245, credit_img,0.1)


back = pygame.transform.scale(bg_image, (int(700), int(900)))
y=0
x=0






paralaxVert = False
paralaxHorin = False
menu = True
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if menu:
        screen.blit(back, (0, 0))
        if credit_button.draw(screen):
            print('credit')
        if tutorial_button.draw(screen):
            print('tutorial')
        if start_button.draw(screen):
            paralaxVert= True
            menu= False
        if exit_button.draw(screen):
            exit()

    if paralaxVert:
        rel_y = y % back.get_rect().height
        if y > -450:
            y -= 8
        if y <= -450:
            paralaxVert = False
            paralaxHorin = True
        screen.blit(back, (0, rel_y - back.get_rect().height))

    if paralaxHorin:
        rel_x = x % back.get_rect().width
        screen.blit(back, (rel_x - back.get_rect().width, -450))
        if rel_x < 700:
            screen.blit(back, (rel_x, -450))
        x -= 5
    pygame.display.update()
    clock.tick(30)