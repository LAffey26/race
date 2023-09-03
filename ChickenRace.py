import pygame
import random
from pygame.locals import (
    K_SPACE,
    QUIT,
    K_ESCAPE,
    KEYDOWN)
from enemy import Enemy
from player import Player
from objects import Objects

HEIGHT = 1080
WIDTH = 1920
background_image = pygame.image.load('image/background.png')


pygame.init()
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
screen = pygame.display.set_mode((WIDTH, HEIGHT))
name = pygame.display.set_caption("ChickenRace")

player = Player()
enemy = Enemy()
objects = Objects()
ADDENEMY = pygame.USEREVENT + 0
pygame.time.set_timer(ADDENEMY, random.randint(1550,2300))

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
