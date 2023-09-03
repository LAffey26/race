import pygame
import random
from pygame.locals import (
    K_SPACE,
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    K_r)
from enemy import Enemy
from player import Player
from objects import Objects
from GameOverSence import GameOverSence
HEIGHT = 1080
WIDTH = 1920


pygame.init()

background_image = pygame.image.load('image/background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

start_3sec = pygame.image.load("image/start.png")
start_3sec = pygame.transform.scale(start_3sec, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
name = pygame.display.set_caption("ChickenRace")

screen.blit(start_3sec,(0,0))
pygame.display.flip()
pygame.time.delay(2000)


player = Player()
enemy = Enemy()
objects = Objects()
gameoversence = GameOverSence()
ADDENEMY = pygame.USEREVENT + 0
pygame.time.set_timer(ADDENEMY, random.randint(1550, 2300))

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

def reset_game():
    global player, enemies, score,all_sprites
    player = Player()
    all_sprites.empty()
    enemies = pygame.sprite.Group()
    score = 0
    all_sprites = pygame.sprite.Group() 
    all_sprites.add(player)
    speed = 3

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
            if event.key == K_r:
                pass
        if event.type == QUIT:
            running = False
        if event.type == ADDENEMY:
            new_enemy = random.choice((Enemy(speed), Objects(speed)))
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
    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        if gameoversence.run_file(score,screen) :
            reset_game()
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (1750, 10))

    pygame.display.flip()
    Clock.tick(144)

pygame.quit()
