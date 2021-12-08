import pygame

class Base():
    def __init__(self, screen, x, y, type, robot_list):
        self.screen = screen
        self.type = type
        
        self.robot_list = robot_list
        
        self.SelfElixir
        self.TotalTeamElixir
        self.TotalVirus

        self.Signal
        
        if type == "red":
            self.image = pygame.image.load(" red base image")
        else:
            self.image = pygame.image.load(" blue base image")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def blitme(self):
        self.screen.blit(self.image, self.rect)