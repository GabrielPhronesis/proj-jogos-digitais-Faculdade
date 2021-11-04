import pygame

from pygame.locals import *
from sys import exit
import button
import random
#inicia o pygame
pygame.init()

#dimenções da tela
screen_width = 700
screen_height = 450

#cria a janela
screen = pygame.display.set_mode((screen_width, screen_height))

#set frame rate
clock = pygame.time.Clock()

#cores
white = (255,255,255)

#rotas das imagens
monster_image = pygame.image.load('assets/monstro.png').convert_alpha()
ghost_image = pygame.image.load('assets/sprite_0.png').convert_alpha()
bg_image = pygame.image.load('assets/background_startgame.png').convert_alpha()
start_img = pygame.image.load('assets/botao_jogar.png').convert_alpha()
exit_img = pygame.image.load('assets/botao_sair.png').convert_alpha()
tutorial_img = pygame.image.load('assets/botao_tutorial.png').convert_alpha()
credit_img = pygame.image.load('assets/botao_creditos.png').convert_alpha()
som_img = pygame.image.load('assets/botao_som_off.png.png').convert_alpha()

#game variables
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

monster_frequency = 1500
last_monster = pygame.time.get_ticks() - monster_frequency
#classe player
class Player():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(ghost_image,(int(90), int(90)))
        self.width = 50
        self.height = 80
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = (x,y)
    def move(self):
        #reseta variaveis
        dx = 0
        dy = 0

        #processa botões
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dy = -4
        else :
            dy = 2

        #bloqueia o player sair da tela
        if self.rect.y >= 330:
            self.rect.y = 330
        if self.rect.y <= 5:
            self.rect.y = 5

        #atualiza a posição do retangulo
        self.rect.x += dx
        self.rect.y += dy
    def draw (self):
        screen.blit(pygame.transform.flip(self.image, True , False), (self.rect.x - 24 , self.rect.y-10))
        pygame.draw.rect(screen, white, self.rect, 2)



#monster class
class Monster(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = monster_image
        self.rect = self.image.get_rect()
        self.rect.topleft = [x,y]

    def update(self):
        self.rect.x -= 3


#instacia do jogador
ghost = Player(screen_width//6, screen_height -90 )

monster_group = pygame.sprite.Group()



start_button = button.Button(205, 140, start_img,0.1)
exit_button = button.Button(355, 140, exit_img,0.1)
tutorial_button = button.Button(205, 245, tutorial_img,0.1)
credit_button = button.Button(355, 245, credit_img,0.1)
som_button = button.Button(200,200, som_img,0.1)


back = pygame.transform.scale(bg_image, (int(700), int(900)))



while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    color = (255, 0, 0)

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
            y -= 4.5
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
        x -= 3
        velocidade += 0.0001

    if mecanica:
        monster_group.draw(screen)
        monster_group.update()
        time_now = pygame.time.get_ticks()
        if time_now - last_monster > monster_frequency:
            btm_monster = Monster(screen_width+500, random.randint(50,250))
            monster_group.add(btm_monster)
            last_monster = time_now

        ghost.draw()
        ghost.move()





    pygame.draw.rect(screen, color, pygame.Rect(20, -20, 60, 60))

        


    pygame.display.update()
    clock.tick(60)