import pygame
import random
from pygame.locals import (
    K_SPACE,
    KEYDOWN
)
import config
class Bird(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Bird, self).__init__()
        self.bird_animation_frame = 0
        self.animation_sheet = [pygame.image.load(frame+".png") for frame in config.animation_bird]
        self.surf = self.animation_sheet[self.bird_animation_frame]
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(
            topleft=(random.randint(config.WIDTH+20, config.WIDTH+100), random.randint(550,610)))
        self.speed = speed
        self.animation_sheet_timer = pygame.time.get_ticks()

    def update(self):
        animation_frame_speed = 100

        if pygame.time.get_ticks() - self.animation_sheet_timer > animation_frame_speed:
            self.animation_sheet_timer= pygame.time.get_ticks()
            self.bird_animation_frame = (self.bird_animation_frame +1) % len(self.animation_sheet)
            self.surf = self.animation_sheet[self.bird_animation_frame]
            self.surf.set_colorkey((255,255,255))

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()
