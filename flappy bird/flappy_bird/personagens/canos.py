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