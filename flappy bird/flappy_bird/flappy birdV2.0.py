import pygame
from random import randint


class Cano(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        tamanho = randint(270, 480)

        self.image = pygame.image.load('data/pipe-green.png')
        self.image = pygame.transform.scale(self.image, (70, 300))
        self.rect = pygame.rect.Rect(570, tamanho, 70, 300)

    def update(self, *args):

        self.rect.x -= 5


class Cano_top(pygame.sprite.Sprite):
    def __init__(self, *groups, x=0):
        super().__init__(*groups)


        self.image = pygame.image.load('data/pipe-green.png')
        self.image = pygame.transform.scale(self.image, (70, 400))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = pygame.rect.Rect(570, x, 70, 300)

    def update(self, *args):
        self.rect.x -= 5


class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/yellowbird.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = pygame.rect.Rect(50, 315, 50, 50)

    def update(self, *args):
        key = pygame.key.get_pressed()

        if key == pygame.K_a:
            print('apertou 1')


class Conf(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/conf_bot.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = pygame.rect.Rect(460, 590, 50, 50)

class Back(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/back.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = pygame.rect.Rect(10, 590, 50, 50)


class Mouse(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/mouse.png')
        self.image = pygame.transform.scale(self.image, (15, 20))
        self.rect = pygame.rect.Rect(10, 590, 15, 20)

    def update(self, *args):

        self.rect = pygame.mouse.get_pos()
#tela
pygame.init()
altura = 630
largura = 500
gameloop = True
clock = pygame.time.Clock()
time = 0
gameover = False
gamestart = False

screen = pygame.display.set_mode((largura, altura))

icon = pygame.image.load('data/yellowbird.png')

pygame.display.set_icon(icon)
pygame.display.set_caption('flappy bird')


#fundo
fundo = pygame.image.load('data/background-day.png')
fundo = pygame.transform.scale(fundo, (largura, altura))

gameover_png = pygame.image.load('data/gameover.png')
gameover_png = pygame.transform.scale(gameover_png, (300, 100))

start_png = pygame.image.load('data/start.png')
start_png = pygame.transform.scale(start_png, (300, 500))

#chao
chao1 = pygame.image.load('data/base.png')
chao1 = pygame.transform.scale(chao1, (500, 100))
chao1_x = -250
chao1_y = altura - 100

chao2 = pygame.image.load('data/base.png')
chao2 = pygame.transform.scale(chao2, (500, 100))
chao2_x = 250
chao2_y = altura - 100


#personagens
bird_group = pygame.sprite.Group()
bird = Bird(bird_group)

movement =0
gravity = 0.25

#cano
canoGroup = pygame.sprite.Group()

#placar
placar_time = 0
placar = 0


base_font = pygame.font.Font(None, 70)

base_font_regame = pygame.font.Font(None, 40)

base_font_placar_gameover = pygame.font.Font(None, 200)


#conf
confGroup = pygame.sprite.Group()
conf = Conf(confGroup)
conf_tela = False

backGroup = pygame.sprite.Group()
back = Back(backGroup)

fundo_conf = pygame.image.load('data/fundo_conf.png')
fundo_conf = pygame.transform.scale(fundo_conf, (largura, altura))

base_font_conf = pygame.font.Font(None, 30)



#mouse
mouseGroup = pygame.sprite.Group()
mouse = Mouse(mouseGroup)

pygame.mouse.set_visible(False)


#musicas

coxa = 'music/Hino do Coritiba - MEGA FUNK 2019.mp3'
ribamar = 'music/HOJE TEM GOL DO RIBAMAR -  MC NANDINHO by Pitter Correa ((Audio Oficial)).mp3'
azeitona = 'music/dj azeitona.mp3'
pressao = 'music/PRESSÃO NENÉM (completo).mp3'
vale = 'music/VALE NADA VALE TUDO.mp3'


while gameloop:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameloop = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            movement = 0
            movement -= 7
            gameover = False
            gamestart = True

            if pygame.sprite.collide_mask(mouse, conf):
                conf_tela = True

            if pygame.sprite.collide_mask(mouse, back):
                conf_tela = False
                gamestart = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.mixer.music.load(coxa)
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_2:
                pygame.mixer.music.load(pressao)
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_3:
                pygame.mixer.music.load(vale)
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_4:
                pygame.mixer.music.load(ribamar)
                pygame.mixer.music.play(-1)

            if event.key == pygame.K_5:
                pygame.mixer.music.load(azeitona)
                pygame.mixer.music.play(-1)





    screen.blit(fundo, (0, 0))

    if conf_tela:

        screen.blit(fundo_conf, (0, 0))

        backGroup.draw(screen)
    else:


        if not gamestart:
            screen.blit(start_png, (100,100))
            confGroup.draw(screen)
            mouseGroup.draw(screen)
            mouseGroup.update()

        if gamestart:

            if not gameover:


                #draw
                canoGroup.draw(screen)
                canoGroup.update()

                screen.blit(chao1, (chao1_x, chao1_y))
                screen.blit(chao2, (chao2_x, chao2_y))

                bird_group.draw(screen)
                bird_group.update()


                movement += gravity
                bird.rect.y += movement


                #move chao

                chao1_x += -2
                chao2_x += -2

                if chao1_x <= -500:
                    chao1_x = 494
                if chao2_x <= -500:
                    chao2_x = 494


                #cano

                time +=1
                if time == 65:
                    novo_cano = Cano(canoGroup)
                    tamanho = 500 - novo_cano.rect.top
                    novo_cano_top = Cano_top(canoGroup, x=-520 + novo_cano.rect.top)
                    time = 0



                #placar
                for cano in canoGroup.spritedict:
                    if cano.rect.x == 50:
                        placar += 0.5

                placar_txt = str(placar).replace('.0', '')
                text_surface = base_font.render(placar_txt, True, (255, 255, 255))
                screen.blit(text_surface, (200, 0))

                placar_final = placar



                #colisao

                if pygame.sprite.spritecollide(bird, canoGroup, False, pygame.sprite.collide_mask):
                    print('bateu')
                    gameover = True

                if bird.rect.bottom >= altura - 70:
                    gameover = True

                if bird.rect.top <= 0:
                    gameover = True

            if gameover:
                screen.blit(gameover_png, (largura//2 - 150, altura//2 - 50))
                regame_txt = 'tap to play again'
                text_regame_surface = base_font_regame.render(regame_txt, True, (0, 0, 0))
                screen.blit(text_regame_surface, (130, 390))

                placar_final_txt = str(placar_final).replace('.0', '')
                text_surface = base_font_placar_gameover.render(placar_final_txt, True, (255, 255, 255))
                screen.blit(text_surface, (220, 100))


                bird.rect.center = (50, 315)
                canoGroup.empty()

                placar_time = 0
                placar = 0

                backGroup.draw(screen)

            #fim game screen
            pygame.display.update()


    #mouse


    mouseGroup.draw(screen)
    mouseGroup.update()


    #fim start screen
    pygame.display.update()



