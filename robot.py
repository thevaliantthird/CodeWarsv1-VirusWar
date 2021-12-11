import pygame
from pygame.sprite import Sprite

class Robot(Sprite):
    def __init__(self, screen, x, y, type):
        super().__init__()
        self.screen = screen
        self.type = type
        self.__myBase
        self.Signal
        if type == "red":
            self.image = pygame.image.load(" red robot image")
        else:
            self.image = pygame.image.load(" blue robot image")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update_pos(self, dir):
        #whatever