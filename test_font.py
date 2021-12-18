import pygame

pygame.init()
screen = pygame.display.set_mode((1200,800))

font = pygame.font.SysFont(None, 48)
title = font.render("Score Board", True, (255,255,255), (0,0,0))
titlerect = title.get_rect()
titlerect.x = 500
titlerect.y = 500
screen.blit(title, titlerect)