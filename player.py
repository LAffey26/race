import pygame
from pygame.locals import (
    K_SPACE,
    KEYDOWN)
import config

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.chicken_animation_frame = 0
        self.animation_sheet = [pygame.image.load(frame +".png") for frame in config.animation_chicken ]
        self.surf_jump = pygame.image.load("images/chicken_jump.png")
        self.surf = self.animation_sheet[self.chicken_animation_frame]
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=(300, 810))
        self.jumping = False
        self.jump_time = 0
        self.animation_sheet_timer = pygame.time.get_ticks()

    def update(self, pressed_keys):
        walk_animation_frame_speed = 100

        if pygame.time.get_ticks() - self.animation_sheet_timer > walk_animation_frame_speed:
            self.animation_sheet_timer = pygame.time.get_ticks()
            self.chicken_animation_frame = (self.chicken_animation_frame +
                                 1) % len(self.animation_sheet)
            self.surf = self.animation_sheet[self.chicken_animation_frame]
            self.surf.set_colorkey((255, 255, 255))
        if pressed_keys[K_SPACE] and not self.jumping:
            self.jumping = True
            self.jump_time = 60

        if self.jump_time != 0:
            self.rect.move_ip(0, -5)
            self.jump_time -= 1
            self.surf = self.surf_jump
            self.surf.set_colorkey((255, 255, 255))

        if self.jump_time == 0:
            self.rect.move_ip(0, 5)
            self.surf = self.animation_sheet[self.chicken_animation_frame]
        if self.rect.bottom == 810:
            self.jumping = False

    def limit(self):
        if self.rect.bottom > 810:
            self.rect.bottom = 810
