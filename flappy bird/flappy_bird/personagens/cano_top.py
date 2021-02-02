import pygame


class Cano_top(pygame.sprite.Sprite):
    def __init__(self, *groups, x=0):
        super().__init__(*groups)


        self.image = pygame.image.load('data/pipe-green.png')
        self.image = pygame.transform.scale(self.image, (70, 400))
        self.image = pygame.transform.flip(self.image, False, True)
        self.rect = pygame.rect.Rect(570, x, 70, 300)

    def update(self, *args):
        self.rect.x -= 5