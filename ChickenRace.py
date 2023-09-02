import pygame
import random
import sys
from pygame.locals import (
    K_SPACE,
    QUIT,
    K_ESCAPE,
    RLEACCEL,
    KEYDOWN)

HEIGHT = 1080
WIDTH = 1920
background_image = pygame.image.load('background.png')

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.correct_anim = 0 
        self.walking_on_ticks = [
            pygame.image.load("chicken.png"),
            pygame.image.load("chicken_going_1.png"),
            pygame.image.load("chicken_going_2.png"),
            pygame.image.load("chicken_sit.png")
        ]
        self.surf_jump = pygame.image.load("chicken_jump.png")
        self.surf = self.walking_on_ticks[self.correct_anim]
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(topleft=(300, 675))
        self.jumping = False
        self.jump_time = 0
        self.walk_animation_timer = pygame.time.get_ticks()

    def update(self, pressed_keys):
        walk_animation_speed = 100        

        if pygame.time.get_ticks() - self.walk_animation_timer > walk_animation_speed:
            self.walk_animation_timer = pygame.time.get_ticks()
            self.correct_anim = (self.correct_anim + 1) % len(self.walking_on_ticks)


        if pressed_keys[K_SPACE] and not self.jumping:
            self.jumping = True
            self.jump_time = 60

        if self.jump_time != 0:
            self.rect.move_ip(0, -5)
            self.jump_time -= 1
            self.surf = self.surf_jump

        if self.jump_time == 0:
            self.rect.move_ip(0, 5)
            self.surf = self.walking_on_ticks[self.correct_anim]
        if self.rect.bottom == 675:
            self.jumping = False

    def limit(self):
        if self.rect.bottom > 675:
            self.rect.bottom = 675


class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed = 5):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("Enemy.png")
        self.surf.set_colorkey((255,255,255))
        self.rect = self.surf.get_rect(topleft=(random.randint(WIDTH+20, WIDTH+120), 605))
        self.speed = speed 

    def update(self):

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()


class Objects(pygame.sprite.Sprite):
    def __init__(self,speed = 5):
        super(Objects,self).__init__()
        self.correct_anim = 0
        self.walking_on_ticks = [
            pygame.image.load("bird_1.png"),
            pygame.image.load("bird_2.png"),
            pygame.image.load("bird_3.png"),
            pygame.image.load("bird_4.png"),      
            pygame.image.load("bird_5.png"),
            pygame.image.load("bird_4.png"),
            pygame.image.load("bird_3.png"),
            pygame.image.load("bird_2.png") 
        ]
        self.surf = self.walking_on_ticks[self.correct_anim]
        self.rect = self.surf.get_rect(
        topleft=(random.randint(WIDTH+20,WIDTH+100), random.randint(425,475)))
        self.speed = speed
        self.walk_animation_timer = pygame.time.get_ticks()

    def update(self):
        walk_animation_speed = 500        

        if pygame.time.get_ticks() - self.walk_animation_timer > walk_animation_speed:
            self.walk_animation_timer = pygame.time.get_ticks()
            self.correct_anim = (self.correct_anim + 1) % len(self.walking_on_ticks)
            self

        self.rect.move_ip(-self.speed, 0)
        if self.rect.left <= 0:
            self.kill()


pygame.init()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
name = pygame.display.set_caption("ChickenRace")

player = Player()
enemy = Enemy()
objects = Objects()
ADDENEMY = pygame.USEREVENT + 0
pygame.time.set_timer(ADDENEMY, random.randint(2000,3000))

all_sprites = pygame.sprite.Group()
all_sprites.add(player)
enemies = pygame.sprite.Group()

Clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)
score = 0
enemy_speed_timer = 0
time = 60
speed = 3
running = True


while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        if event.type == QUIT:
            running = False
        if event.type == ADDENEMY:
            new_enemy = random.choice((Enemy(speed),Objects(speed)))
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    enemy_speed_timer += 1
    time -= 1

    if enemy_speed_timer == 1200:
        enemy_speed_timer = 0
        speed += 1
    if speed == 6:
        speed = 6

    if time == 0:
        time = 60
        score += 1

    pressed_keys = pygame.key.get_pressed()

    player.update(pressed_keys)
    player.limit()
    objects.update()
    enemies.update()

    screen.blit(background_image, (0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player,enemies):
        player.kill()
        running = False

    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (1750, 10))

    pygame.display.flip()
    Clock.tick(144)

pygame.quit()
