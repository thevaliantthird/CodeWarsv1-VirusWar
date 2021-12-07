import sys
import pygame
from pygame.sprite import Group

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Code Wars")

    def run_game(self):
        while True:
            pygame.display.flip()
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)

    def create_robots(self):
        """Will take total info from both bases and create robots"""


    def create_map(self):
        """Take info about collectibles and create the map"""


    def collect(self):
        """Take positions of robots and collectibles and check collisions"""


    def update_score(self):
        """Update scores in the scoreboard"""


    def game_over(self):
        """Check conditions of game over"""


game = Game()
game.run_game()