import pygame
from dino_runner.utils.constants import SCREEN_WIDTH
from dino_runner.utils.constants import DEAD


class Obstacle:
    def __init__(self, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.death_sfx = pygame.mixer.Sound("dino_runner/assets/sfx/lose.mp3")


    def update(self, game_speed, player):
        self.rect.x -= game_speed
        if self.rect.colliderect(player.dino_rect):
            if not player.shield:
              player.image = DEAD
              pygame.time.delay(200)
              player.dino_dead = True
              self.death_sfx.play()


    def draw(self, screen):
        screen.blit(self.image, self.rect)
