import pygame
from pygame.locals import (
    K_SPACE,
    KEYDOWN)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.correct_anim = 0
        self.walking_on_ticks = [
            pygame.image.load("image/chicken.png"),
            pygame.image.load("image/chicken_going_1.png"),
            pygame.image.load("image/chicken_going_2.png"),
            pygame.image.load("image/chicken_sit.png")]
        self.surf_jump = pygame.image.load("image/chicken_jump.png")
        self.surf = self.walking_on_ticks[self.correct_anim]
        self.surf.set_colorkey((255, 255, 255))
        self.rect = self.surf.get_rect(topleft=(300, 810))
        self.jumping = False
        self.jump_time = 0
        self.walk_animation_timer = pygame.time.get_ticks()

    def update(self, pressed_keys):
        walk_animation_speed = 100

        if pygame.time.get_ticks() - self.walk_animation_timer > walk_animation_speed:
            self.walk_animation_timer = pygame.time.get_ticks()
            self.correct_anim = (self.correct_anim +
                                 1) % len(self.walking_on_ticks)
            self.surf = self.walking_on_ticks[self.correct_anim]
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
            self.surf = self.walking_on_ticks[self.correct_anim]
        if self.rect.bottom == 810:
            self.jumping = False

    def limit(self):
        if self.rect.bottom > 810:
            self.rect.bottom = 810
