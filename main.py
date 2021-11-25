import pygame

from pygame.locals import *
from sys import exit
import button
import random

# inicia o pygame
pygame.init()

# dimenções da tela
screen_width = 700
screen_height = 450

# cria a janela
screen = pygame.display.set_mode((screen_width, screen_height))

# set frame rate
clock = pygame.time.Clock()

# cores
white = (255, 255, 255)

# rotas das imagens
monster_image = pygame.image.load('assets/fantasma_1.png').convert_alpha()
player_image = pygame.image.load('assets/PERSONAGEM_1_v2.png').convert_alpha()
bg_image = pygame.image.load('assets/background_startgame.png').convert_alpha()
start_img = pygame.image.load('assets/botao_jogar.png').convert_alpha()
exit_img = pygame.image.load('assets/botao_sair.png').convert_alpha()
tutorial_img = pygame.image.load('assets/botao_TrocaPERSONAGEM.png').convert_alpha()
credit_img = pygame.image.load('assets/botao_TrocaMAPA.png').convert_alpha()
restart_img = pygame.image.load('assets/botao_Restart.png')
menu_img = pygame.image.load('assets/botao_Menu.png')
gameover_img1 = pygame.image.load('assets/gameover.png')
gameover_img = pygame.transform.scale(gameover_img1, (int(250), int(150)))
font = pygame.font.SysFont('Bauhaus 93', 40)

# game variables
y = 0
x = 0

paralaxVert = False
paralaxHorin = False
menu = True
mecanica = False
invtParalaxVert = False
game_over = False
colisao = False

cenario= 1
personagem = 1

monster_frequency = [3000,2500,2000,1800,1500,1100,800,600,400]
last_monster = pygame.time.get_ticks()

velocidade = [3,5,7,8,9,10,11,13,15]

index = 0
level =0

pontos = 0



def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
def reset_game ():
    monster_group.empty()
    jogador.rect.x = screen_width // 8
    jogador.rect.y = screen_height - 90
    jogador.vidas = 3
    return 0

# classe player
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0


        for num in range(1, 6):
            img1 = pygame.image.load(f'assets/PERSONAGEM_1_v{num}.png')
            if number == 1:
                img1= pygame.image.load(f'assets/PERSONAGEM_1_v{num}.png')
            if number == -1:
                img1 = pygame.image.load(f'assets/PERSONAGEM_2_v{num}.png')
            img2 = pygame.transform.scale(img1, (int(70), int(112)))
            img = pygame.transform.flip(img2, True, False)
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.vel = 0
        self.vidas = 3
        pygame.transform.flip(self.image, True, False)
    def update(self):
        self.counter += 1
        pers_cooldown = 5
        if self.counter > pers_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]
        # reseta variaveis
        dx = 0
        dy = 0

        # processa botões
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dy = -4
        else:
            dy = 2

        # bloqueia o player sair da tela
        if self.rect.y >= 330:
            self.rect.y = 330
        if self.rect.y <= 5:
            self.rect.y = 5

        # atualiza a posição
        self.rect.x += dx
        self.rect.y += dy


# monster class
class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y,number):
        pygame.sprite.Sprite.__init__(self)

        if number == 1:
            img1 = pygame.image.load('assets/fantasma_1.png')
        if number == -1:
            img1 = pygame.image.load('assets/fantasma_2.png')

        self.image = pygame.transform.scale(img1, (int(60), int(60)))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

    def update(self):
        self.rect.x -= velocidade[level]

        if self.rect.right < 0:
            self.kill()

            jogador.vidas -= 1
        if colisao == True and self.rect.left < screen_width // 4:
            self.kill()


player_group = pygame.sprite.Group()
jogador = Player(screen_width // 8, screen_height - 90,personagem)
player_group.add(jogador)

monster_group = pygame.sprite.Group()

# instancia dos botoes
start_button = button.Button(205, 140, start_img, 0.1)
exit_button = button.Button(355, 140, exit_img, 0.1)
tutorial_button = button.Button(205, 245, tutorial_img, 0.05)
credit_button = button.Button(355, 245, credit_img, 0.05)
restart_button = button.Button(205,300,restart_img, 0.05)
menu_button = button.Button(355,300,menu_img, 0.05)



back = pygame.transform.scale(bg_image, (int(700), int(900)))
pygame.mixer.music.load('assets/musica.mp3')
pygame.mixer.music.set_volume(0.00)
pygame.mixer.music.play(-1)
while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    colisao = False

    if menu:
        screen.blit(back, (0, 0))
        if credit_button.draw(screen):
            cenario = cenario *-1
            if cenario == 1:
                bg_image = pygame.image.load('assets/background_startgame.png').convert_alpha()
                back = pygame.transform.scale(bg_image, (int(700), int(900)))
            if cenario == -1:
                bg_image = pygame.image.load('assets/background_startgame-2.png').convert_alpha()
                back = pygame.transform.scale(bg_image, (int(700), int(900)))
            #monster_image = pygame.image.load('assets/fantasma_1.png').convert_alpha()
            #player_image = pygame.image.load('assets/PERSONAGEM_1_v2.png').convert_alpha()

        if tutorial_button.draw(screen):

            personagem = personagem *-1

            player_group.empty()
            player_group = pygame.sprite.Group()
            jogador = Player(screen_width // 8, screen_height - 90,personagem)
            player_group.add(jogador)

            monster_group.empty()
            if personagem == 1:
                print('James')
            if personagem == -1:
                print('James universo paralelo')
        if start_button.draw(screen):
            paralaxVert = True
            menu = False
            index = reset_game()
            pontos = index
            level = index
        if exit_button.draw(screen):
            exit()

    if paralaxVert:
        rel_y = y % back.get_rect().height
        if y > -450:
            y -= 5.5
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
        x -= velocidade[level]

    if invtParalaxVert:
        rel_y = y % back.get_rect().height
        if y < 0:
            y += 5.5
        if y >= 0:
            invtParalaxVert = False
            menu = True

        screen.blit(back, (0, rel_y - back.get_rect().height))
    if mecanica:
        if pontos == 0:
            index = 0
        player_group.draw(screen)
        player_group.update()
        monster_group.draw(screen)

        draw_text(str(pontos), font, white, int(screen_width / 2) - 20, 20)
        draw_text("Vidas:" + str(jogador.vidas), font, white, int(screen_width) - 150, 20)
        if pontos == 5:
            level = 1
        if pontos == 10:
            level = 2
        if pontos == 15:
            level = 3
        if pontos == 20:
            level = 4
        if pontos == 25:
            level = 5
        if pontos == 30:
            level = 6
        if pontos == 35:
            level = 7
        if pontos == 40:
            level = 8
        if jogador.vidas == 0:
            game_over = True
            paralaxHorin = False
            mecanica = False
        if pygame.sprite.groupcollide(player_group, monster_group, False, False):
            colisao = True
            pontos += 1


        time_now = pygame.time.get_ticks()
        if time_now - last_monster > monster_frequency[level]:
            btm_monster = Monster(screen_width + 500, random.randint(60, 350),personagem)
            monster_group.add(btm_monster)
            last_monster = time_now
        monster_group.update()
    if game_over:
        screen.blit(gameover_img, ((screen_width/2)-125, 100))
        if menu_button.draw(screen):
            invtParalaxVert = True
            game_over = False
        if restart_button.draw(screen):
            index = reset_game()
            pontos = index
            level = index
            paralaxHorin = True
            mecanica = True
            game_over = False


    pygame.display.update()
    clock.tick(60)
