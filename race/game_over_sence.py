import pygame
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    )

from race.config import branch
from race.config import BLACK
class GameOverSence(pygame.sprite.Sprite):
    def __init__(self):
        super(GameOverSence, self).__init__()
        self.font = pygame.font.Font(None, 72)
        self.background = pygame.image.load(branch+"end.png").convert()
        self.high_score = 0

    def read_in_txt(self):
        try:
            with open("score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            pass

    def push_in_txt(self,):
        with open("score.txt", "w") as file:
            file.write(str(self.high_score))

    def run_file(self, score, screen):
        if score > self.high_score:
            self.high_score = score
            self.read_in_txt()
        self.text_record = self.font.render(str(self.high_score), True, BLACK)
        self.text_score = self.font.render(str(score), True, BLACK)
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
            screen.blit(self.text_score, (350, 420))
            screen.blit(self.text_record, (360, 805))
            pygame.display.flip()
