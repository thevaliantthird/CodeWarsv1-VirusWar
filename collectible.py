import pygame
from pygame.sprite import Sprite

class Collectible(Sprite):
    def __init__(self, screen, x, y, points):
        self.screen = screen
        self.points = points
        if points <-40:
            self.image = pygame.load("dark virus image")
        elif points<-20:
            self.image = pygame.load("moderate virus image")
        elif points<0:
            self.image = pygame.load("ligth virus image")
        elif points == 0:
            self.image = pygame.load("blank image")
        elif points < 20:
            self.image = pygame.load("light elixir image")
        elif points<40:
            self.image = pygame.load("moderate elixir image")
        else:
            self.image = pygame.load("strong elixir image")

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)