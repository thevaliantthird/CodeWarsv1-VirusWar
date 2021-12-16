import pygame
from pygame.sprite import Sprite

class Collectible(Sprite):
    def __init__(self, screen, x, y, points):
        super().__init__()
        self.screen = screen
        self.initPoints = points
        self.points = points
        self.rect = (x, y, 20, 20)
        self.color = (60,60,60)
        
    def blitme(self):
        pygame.draw.rect(self.screen, self.color,  self.rect)

    def setColor(self):
        if self.points <-40:
            self.color = (240,240,250)
        elif self.points<-20:
            self.color = (220,220,250)
        elif self.points<0:
            self.color = (200,200,240)
        elif self.points == 0:
            self.color = (200,200,200)
        elif self.points < 20:
            self.color = (10,230, 10)
        elif self.points<40:
            self.color = (20, 230, 20)
        else:
            self.color = (50,200,50)