import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Block, self).__init__()
        self.surf = pygame.image.load("images/block.png")
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            topleft=(random.randint(1940, 2040), 750))
        self.speed = speed

    def update(self):

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()
