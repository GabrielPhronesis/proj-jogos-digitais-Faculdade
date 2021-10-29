import pygame
from pygame.locals import *
from sys import exit
import button

screen = pygame.display.set_mode((700, 450))
pygame.init()
clock = pygame.time.Clock()
#rotas das imagens
ghost_image = pygame.image.load('assets/sprite_0.png').convert_alpha()
bg_image = pygame.image.load('assets/background_startgame.png').convert_alpha()
start_img = pygame.image.load('assets/botao_jogar.png').convert_alpha()
exit_img = pygame.image.load('assets/botao_sair.png').convert_alpha()
tutorial_img = pygame.image.load('assets/botao_tutorial.png').convert_alpha()
credit_img = pygame.image.load('assets/botao_creditos.png').convert_alpha()
som_img = pygame.image.load('assets/botao_som_off.png.png').convert_alpha()


start_button = button.Button(205, 140, start_img,0.1)
exit_button = button.Button(355, 140, exit_img,0.1)
tutorial_button = button.Button(205, 245, tutorial_img,0.1)
credit_button = button.Button(355, 245, credit_img,0.1)
som_button = button.Button(200,200, som_img,0.1)

ghost = pygame.transform.scale(ghost_image, (int(100), int(70)))
back = pygame.transform.scale(bg_image, (int(700), int(900)))
y=0
x=0

velocidade = 1

paralaxVert = False
paralaxHorin = False
menu = True
mecanica = False


personX = 100
personY = 350
up = 1

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
            mecanica = True
        screen.blit(back, (0, rel_y - back.get_rect().height))


    if paralaxHorin:
        rel_x = x % back.get_rect().width
        screen.blit(back, (rel_x - back.get_rect().width, -450))
        if rel_x < 700:
            screen.blit(back, (rel_x, -450))
        x -= 5 * velocidade
        velocidade += 0.001
    if mecanica:
        if event.type == KEYDOWN:
            if event.key==K_LEFT:
                personY -= 5
        if event.type == KEYUP:
            if event.key == K_LEFT:
                personY += 5
        if personY >= 350:
            personY = 350
        if  personY <= -20:
            personY = -20
        screen.blit(ghost,(personX,personY))
        


    pygame.display.update()
    clock.tick(30)