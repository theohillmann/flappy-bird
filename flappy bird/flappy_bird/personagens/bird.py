import pygame

class Bird(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('data/yellowbird.png')
        self.image = pygame.transform.scale(self.image, (35, 35))
        self.rect = pygame.rect.Rect(50, 315, 50, 50)

