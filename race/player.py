import pygame
from pygame.locals import (
    K_SPACE,
    KEYDOWN)
from race.animation_func import  changing_animation_frames
import race.animation_func
from race.config import images_folder
from race.config import WHITE
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.frame_change = 0
        self.list_with_frames = [pygame.image.load(images_folder + frame +".png") for frame in race.config.animation_chicken ]
        self.surf_jump = pygame.image.load(images_folder+"chicken_jump.png")
        self.surf = self.list_with_frames[self.frame_change]
        self.surf.set_colorkey((WHITE))
        self.rect = self.surf.get_rect(topleft=(300, 930))

        self.jumping = False
        self.jump_time = 0
        self.timer = pygame.time.get_ticks()
        

    def update(self, pressed_keys):
        self.speed_animation = 100
        self.List =[
            self.list_with_frames,
            self.frame_change,
            self.timer,
            self.speed_animation
        ]
        self.surf,self.frame_change,self.timer = changing_animation_frames(*self.List)        
        if pressed_keys[K_SPACE] and not self.jumping:
            self.jumping = True
            self.jump_time = 60

        if self.jump_time != 0:
            self.rect.move_ip(0, -5)
            self.jump_time -= 1
            self.surf = self.surf_jump
            self.surf.set_colorkey((WHITE))

        if self.jump_time == 0:
            self.rect.move_ip(0, 5)
            self.surf = self.list_with_frames[self.frame_change]
        if self.rect.bottom == 930:
            self.jumping = False

    def limit(self):
        if self.rect.bottom > 930:
            self.rect.bottom = 930
