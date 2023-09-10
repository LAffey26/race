import pygame
import random
from race.config import images_folder
from race.config import WHITE
from race.config import animation_wolf
from race.animation_func import changing_animation_frames



class Wolf(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Wolf, self).__init__()
        self.frame_change = 0
        self.list_with_frames = [pygame.image.load(images_folder+frame+".png") for frame in animation_wolf]
        self.surf = self.list_with_frames[self.frame_change]
        self.surf.set_colorkey(WHITE)
        self.rect = self.surf.get_rect(
            topleft=(random.randint(1940, 2040), 850))

        self.speed = speed
        self.timer = pygame.time.get_ticks()
    def update(self):
        self.speed_animation = 100
        self.List = [
            self.list_with_frames,
            self.frame_change,
            self.timer,
            self.speed_animation
        ]
        self.surf, self.frame_change, self.timer = changing_animation_frames(*self.List)
        self.rect.move_ip(-self.speed, 0)

        if self.rect.left <= 0:
            self.kill()
