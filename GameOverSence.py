import pygame
from pygame.locals import (
    K_SPACE,
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    )
WIDTH = 1920
HEIGHT = 1080


class GameOverSence(pygame.sprite.Sprite):
    def __init__(self):
        super(GameOverSence, self).__init__()
        self.font = pygame.font.Font(None, 72)
        self.background = pygame.image.load("image/end.png").convert()
        self.high_score = 0

    def load_score(self):
        try:
            with open("score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            pass

    def download_score(self,):
        with open("score.txt", "w") as file:
            file.write(str(self.high_score))

    def run_file(self, score, screen):
        if score > self.high_score:
            self.high_score = score
            self.load_score()
        self.text_record = self.font.render(str(self.high_score), True, (0, 0, 0))
        self.text_score = self.font.render(str(score), True, (0, 0, 0))
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == pygame.K_r:
                        return True
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        return False

            screen.blit(self.background, (0, 0))
            screen.blit(self.text_score, (WIDTH // 3 - 290, HEIGHT // 2 - 120))
            screen.blit(self.text_record, (WIDTH//3 - 280, HEIGHT - 275))
            pygame.display.flip()
