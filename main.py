import sys
import pygame
from pygame.sprite import Group
import numpy as np

from base import Base
from collectible import Collectible
import script
#resources library

class Game():

        
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,800))
        pygame.display.set_caption("Code Wars")
        self.fps_controller = pygame.time.Clock()
        self.dim = (40,40)
        self.resources = np.random.randint(-50, high=50, size = self.dim)
        self.resources[19][9] = 0
        self.resources[19][29] = 0
        self.GlobalRobotCount = 0
        

        self.collectibles = []
        
        self.PositionToRobot = {}
        for i in range(self.dim[0]):
            Z = []
            for j in range(self.dim[1]):
                Z.append(Collectible(self.screen, i*20, j*20, self.resources[j][i]))
            self.collectibles.append(Z)
        
        

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
        self.PositionToRobot[(9,19)] = {self.__redbase:True}
        self.PositionToRobot[(29,19)] = {self.__bluebase:True}

        for j in range(3):
            self.__redbase.create_robot('')
            self.__bluebase.create_robot('')

    def run_game(self):
        iter = 0
        while True:
            iter+=1
            self.screen.fill((60,60,60))
            self.collect()
            script.ActOperator(self.__bluebase)
            script.ActOperator(self.__redbase)
            for robo in self.__redbots:
                n = script.ActRobot(robo)
                if n == 1:
                    robo.move_up()
                elif n == 2:
                    robo.move_right()
                elif n == 3:
                    robo.move_down()
                elif n == 4:
                    robo.move_right()
            for robo in self.__bluebots:
                n = script.ActRobot(robo)
                if n == 1:
                    robo.move_up()
                elif n == 2:
                    robo.move_left()
                elif n == 3:
                    robo.move_left()
                elif n == 4:
                    robo.move_down()
            for i in range(0,self.dim[0]):
                for j in range(0,self.dim[1]):
                    self.collectibles[i][j].blitme()
                
            self.__bluebase.blitme()
            self.__redbase.blitme()
            self.check_collisions()
            self.updateRoboMap()
            self.__bluebots.draw(self.screen)
            self.__redbots.draw(self.screen)
            #print(self.PositionToRobot)
            pygame.display.flip()
            self.check_events()
            self.update_score()
            if iter % 10 == 0:
                self.replenish()
            self.fps_controller.tick(2)
    def updateRoboMap(self):
        self.robots = np.zeros((self.dim[1],self.dim[0])).astype(int)
        for key in self.PositionToRobot.keys():
            value = self.PositionToRobot[key]
            entr = 0
            for v in value:
                if v==self.__redbase:
                    entr = 3
                    break
                if v==self.__bluebase:
                    entr = 4
                    break
                if v.type=="red":
                    entr = 1
                else:
                    entr = 2
            self.robots[key[1]][key[0]] = entr
    
    def check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
    
    def check_collisions(self):
       removals = pygame.sprite.groupcollide(self.__bluebots, self.__redbots, False, False)
       #print(removals)
       to_kill = set()
       for b, r_list in removals.items():
           #print(id(b))
           for r in r_list:
            #print(id(r))
            if b.selfElixir > r.selfElixir:
               b.selfElixir -= r.selfElixir
               self.robots[r.rect.y//20][r.rect.x//20] = 2
               to_kill.add(r)
               self.__redbase.TotalTeamElixir -= r.selfElixir
               self.__bluebase.TotalTeamElixir -= r.selfElixir
               r.selfElixir = 0
            elif b.selfElixir < r.selfElixir:
                self.robots[r.rect.y//20][r.rect.x//20] = 1
                r.selfElixir -= b.selfElixir
                to_kill.add(b)
                self.__bluebase.TotalTeamElixir -= b.selfElixir
                self.__bluebase.TotalTeamElixir -= b.selfElixir
                b.selfElixir = 0
            else:
                self.robots[r.rect.y//20][r.rect.x//20] = 0
                to_kill.add(r)
                to_kill.add(b)
                self.__redbase.TotalTeamElixir -= r.selfElixir
                self.__bluebase.TotalTeamElixir -= b.selfElixir
                r.selfElixir = 0
                b.selfElixir = 0
       for a in to_kill:
            del self.PositionToRobot[(a.rect.x//20, a.rect.y//20)][a]
            a.kill()


    def create_map(self):
        """Take info about collectibles and create the map"""

    def replenish(self):
        for i in range(0,self.dim[0]):
            for j in range(0,self.dim[1]):
                # if self.collectibles[i][j].initPoints > 1e-5:
                #     self.collectibles[i][j].points = min(self.collectibles[i][j].initPoints, self.collectibles[i][j].points*1.3)
                if self.collectibles[i][j].initPoints < -1e-5:
                    self.collectibles[i][j].points = max(self.collectibles[i][j].initPoints, self.collectibles[i][j].points*1.3)
                self.resources[j][i] = self.collectibles[i][j].points
                self.collectibles[i][j].setColor()


    def collect(self):
        """Take positions of robots and collectibles and check collisions"""
        
        for key in self.PositionToRobot.keys():
            value = self.PositionToRobot[key]
            if self.robots[key[1]][key[0]] == 1 or self.robots[key[1]][key[0]] == 2:
                V = self.resources[key[1]][key[0]]/(2*len(value))
                for v in value:
                    v.addResource(V)
                self.resources[key[1]][key[0]] /= 2
                self.collectibles[key[0]][key[1]].points = self.resources[key[1]][key[0]]
                self.collectibles[key[0]][key[1]].setColor()


                


    def update_score(self):
        """Update scores in the scoreboard"""
        print("Blue Team")
        print("Total Elixir :" + str(self.__bluebase.TotalTeamElixir))
        print("Self Elixir : " + str(self.__bluebase.SelfElixir))
        print("No. of Robots: " +str(len(self.__bluebots)))

        print("Red Team: ")
        print("Total Elixir: "+ str(self.__redbase.TotalTeamElixir))
        print("Self ELixir: " + str(self.__redbase.SelfElixir))
        print("No. of Robots: " + str(len(self.__redbots)))
        

    def game_over(self):
        """Check conditions of game over"""
        if self.__redbase.SelfElixir <= 0:
            print( "Blue Wins")
            sys.exit(0)
        elif self.__bluebase.SelfElixir <= 0:
            print("Red Wins")
            sys.exit(0)
            
    

game = Game()
game.run_game()