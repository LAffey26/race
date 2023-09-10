import pygame
import random
from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    K_r)
from race.wolf import Wolf
from race.player import Player
from race.bird import Bird
from race.game_over_sence import GameOverSence
from race.config import HEIGHT
from race.config import WIDTH
from race.config import BLACK
from race.config import images_folder
pygame.init()


background_image = pygame.image.load(images_folder+'background.png')
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

boot_screen = pygame.image.load(images_folder+"start.png")
boot_screen = pygame.transform.scale(boot_screen, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
name = pygame.display.set_caption("ChickenRace")

screen.blit(boot_screen,(0,0))
pygame.display.flip()
pygame.time.delay(2000)


player = Player()
wolf = Wolf()
bird = Bird()
game_over_sence = GameOverSence()
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
speed = 5
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
            new_enemy = random.choice((Wolf(speed), Bird(speed)))
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    enemy_speed_timer += 1
    time -= 1

    if enemy_speed_timer == 1200:
        enemy_speed_timer = 0
        speed += 1
    if speed == 13:
        speed = 13 

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
        if game_over_sence.restart_game_func(score,screen) :
            reset_game()
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (1750, 10))

    pygame.display.flip()
    Clock.tick(144)

pygame.quit()
