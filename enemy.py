import pygame
import random
from pygame.locals import (
    K_SPACE,
    KEYDOWN
    )
HEIGHT = 1080
WIDTH = 1920
class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("image/Enemy.png")
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            topleft=(random.randint(WIDTH+20, WIDTH+120), 750))
        self.speed = speed

    def update(self):

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()
