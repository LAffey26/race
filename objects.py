import pygame
import random
from pygame.locals import (
    K_SPACE,
    KEYDOWN
)
HEIGHT = 1080
WIDTH = 1920
class Objects(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Objects, self).__init__()
        self.correct_anim = 0
        self.walking_on_ticks = [
            pygame.image.load("image/bird_1.png"),
            pygame.image.load("image/bird_2.png"),
            pygame.image.load("image/bird_3.png"),
            pygame.image.load("image/bird_4.png"),
            pygame.image.load("image/bird_5.png"),

        ]
        self.surf = self.walking_on_ticks[self.correct_anim]
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            topleft=(random.randint(WIDTH+20, WIDTH+100), random.randint(425, 475)))
        self.speed = speed
        self.walk_animation_timer = pygame.time.get_ticks()

    def update(self):
        walk_animation_speed = 500

        if pygame.time.get_ticks() - self.walk_animation_timer > walk_animation_speed:
            self.walk_animation_timer = pygame.time.get_ticks()
            self.correct_anim = (self.correct_anim +
                                 1) % len(self.walking_on_ticks)

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()
