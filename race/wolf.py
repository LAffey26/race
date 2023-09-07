import pygame
import random
import race.config
WHITE = race.config.WHITE
branch = race.config.branch
from race.animation_func import change



class Wolf(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Wolf, self).__init__()
        self.frame_change = 0
        self.tuple_with_png = [pygame.image.load(branch+frame+".png") for frame in race.config.animation_wolf]
        self.surf = self.tuple_with_png[self.frame_change]
        self.surf.set_colorkey(WHITE)
        self.rect = self.surf.get_rect(
            topleft=(random.randint(1940, 2040), 850))

        self.speed = speed
        self.timer = pygame.time.get_ticks()
    def update(self):
        self.speed_animation = 100
        self.List = [
            self.tuple_with_png,
            self.frame_change,
            self.timer,
            self.speed_animation
        ]
        self.surf, self.frame_change, self.timer = change(*self.List)
        self.rect.move_ip(-self.speed, 0)

        if self.rect.left <= 0:
            self.kill()
