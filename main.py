import sys
import pygame
from pygame.sprite import Group
import numpy as np
from base import Base
from collectible import Collectible
#resources library

class Game():

        
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Code Wars")
        self.dim = (40,40)
        self.resources = np.random.randint(-50, high=50, size = self.dim)
        self.resources[19][9] = 0
        self.resources[19][29] = 0
        self.GlobalRobotCount = 0
        self.collectibles = Group()
        self.PositionToRobot = {}
        for i in range(self.dim[0]):
            for j in range(self.dim[1]):
                collectible = Collectible(self.screen, j*20, i*20, self.resources[i][j])
                self.collectibles.add(collectible) 
        
        self.__bluebots = Group()
        self.__redbots = Group()
        self.robots = np.zeros(self.dim)
        # 0 in self.robots means no robots
        # 1 means one robot of red team
        # 2 means one robot of blue team
        # 3 means base for team red
        # 4 means base for team blue

        self.__redbase = Base(self.screen, 180, 380, 'red', self.__redbots, self.robots,self)
        self.__bluebase = Base(self.screen, 580, 380, 'blue', self.__bluebots, self.robots,self)


    def run_game(self):
        while True:
            self.screen.fill((60,60,60))
            for robo in self.__bluebots:
                n = self.next_move(robo)
                if n == 1:
                    robo.move_up()
                elif n == 2:
                    robo.move_down()
                elif n == 3:
                    robo.move_left()
                elif n == 4:
                    robo.move_right()
            for robo in self.__redbots:
                n = self.next_move(robo)
                if n == 1:
                    robo.move_up()
                elif n == 2:
                    robo.move_down()
                elif n == 3:
                    robo.move_left()
                elif n == 4:
                    robo.move_right()
            for collectible in self.collectibles:
                collectible.blitme()
            self.__bluebase.blitme()
            self.__redbase.blitme()
            self.check_collisions()
            self.__bluebots.draw(self.screen)
            self.__redbots.draw(self.screen)
            pygame.display.flip()
            self.check_events()

    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
    
    def check_collisions(self):
        for b_robo in self.__bluebots:
            for r_robo in self.__redbots:
                if b_robo.rect == r_robo.rect:
                    if b_robo.selfElixir > r_robo.selfElixir:
                        b_robo.selfElixir -= r_robo.selfElixir
                        r_robo.kill()
                    elif b_robo.selfElixir < r_robo.selfElixir:
                        r_robo.selfElixir -= b_robo.selfElixir
                        b_robo.kill()
                    else:
                        r_robo.kill()
                        b_robo.kill()
            for b_robo2 in self.__bluebots:
                if b_robo != b_robo2 and b_robo.rect == b_robo2.rect and b_robo.rect != self.__bluebase:
                    b_robo.selfElixir += b_robo2.selfElixir
                    b_robo2.kill()
        for r_robo in self.__redbots:
            for r_robo2 in self.__redbots:
                if r_robo != r_robo2 and  r_robo.rect == r_robo2.rect and r_robo.rect != self.__redbase:
                    b_robo.selfElixir += b_robo2.selfElixir
                    b_robo2.kill()


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