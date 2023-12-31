import pygame
import random
from pygame.locals import (
    K_SPACE,
    KEYDOWN
)
from race.config import images_folder
from race.config import animation_bird
from race.config import WIDTH
from race.config import WHITE
from race.animation_func import changing_animation_frames
class Bird(pygame.sprite.Sprite):
    def __init__(self, speed=5):
        super(Bird, self).__init__()
        self.frame_change = 0
        self.list_with_frames = [pygame.image.load(images_folder+frame+".png") for frame in animation_bird]
        self.surf = self.list_with_frames[self.frame_change]
        self.surf.set_colorkey(WHITE)
        self.rect = self.surf.get_rect(
            topleft=(random.randint(WIDTH+20, WIDTH+100), random.randint(660,720)))
        self.speed = speed
        self.timer = pygame.time.get_ticks()
    def update(self):
        self.speed_animation = 100
        self.List =[
            self.list_with_frames,
            self.frame_change,
            self.timer,
            self.speed_animation
            ]
        self.surf,self.frame_change,self.timer = changing_animation_frames(*self.List) 

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()
