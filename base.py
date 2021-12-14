import pygame
from robot import Robot

class Base():
    def __init__(self, screen, x, y, type, robot_list, robot_map, game):
        self.screen = screen
        self.type = type
        self.robot_map = robot_map
        self.robot_list = robot_list
        self.__myGame = game
        self.SelfElixir = 200
        self.TotalTeamElixir = 200
        self.TotalVirus = 0

        self.__Signal = ''
        
        if type == "red":
            self.image = pygame.image.load("redbase.png")
        else:
            self.image = pygame.image.load("bluebase.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    def actVirus(self, v, pos):
        g = self.__myGame
        if pos[0] < 0 or pos[0] >= g.dim[0]:
            return
        if pos[1] < 0 or pos[1] >= g.dim[1]:
            return
        if self.robots[pos[0],pos[1]]==0:
            self.resource[pos[0,pos[1]]]+=v
            return
        if self.robots[pos[0],pos[1]]==1 and self==g.__redbase:
            self.TotalVirus += v
            return
        if self.robots[pos[0],pos[1]]==1 and self==g.__bluebase:
            g.__bluebase(pos, v)
            return
        if self.robots[pos[0],pos[1]]==2 and self==g.__bluebase:
            self.TotalVirus += v
            return
        if self.robots[pos[0],pos[1]]==2 and self==g.__redbase:
            g.__redbase.VirusOnRobot(pos, v)
            return
        if self.robots[pos[0],pos[1]]==3 and self==g.__bluebase:
            self.__myGame.__redbase.SelfElixir -= v
            self.__myGame.__redbase.TotalTeamElixir -= v
            return
        if self.robots[pos[0],pos[1]]==3 and self==g.__redbase:
            self.TotalVirus += v
            return
        if self.robots[pos[0],pos[1]]==4 and self==g.__redbase:
            self.__myGame.__bluebase.SelfElixir -= v
            self.__myGame.__bluebase.TotalTeamElixir -= v
            return
        if self.robots[pos[0],pos[1]]==4 and self==g.__bluebase:
            self.TotalVirus += v
            return

    def GetListOfSignals(self):
        res = []
        for x in self.robot_list:
            res.append(x.__Signal)
        return res

    
        
    def VirusOnRobot(self, pos,virus):
        robot = self.PositionToRobot[pos]
        if robot.__Elixir <= virus:
            e = virus - robot.__Elixir
            self.TotalTeamElixir -= robot.__Elixir
            del self.__myGame.PositionToRobot[pos]
            robot.kill()
            self.__myGame.resource[pos[0],pos[1]]+=e
        else:
            self.TotalTeamElixir -= virus
            robot.__Elixir-=virus
            
    def create_robot(self, signal):
        if self.SelfElixir >= 50:
            self.SelfElixir -= 50
            self.GlobalRobotCount += 1
            robo = Robot(self.screen, self.rect.x, self.rect.y, self.type, signal, self,self.GlobalRobotCount)
            self.robot_list.add(robo)
          #  self.__myGame[(self.rect.x, self.rect.y)].append(robo)
            if self.type == 'red':
                self.robot_map[self.rect.y/20][self.rect.x/20] = 3
            else:
                self.robot_map[self.rect.y/20][self.rect.x/20] = 4

    def GetYourSignal(self):
        return self.__Signal
    
    def SetYoutSignal(self, s):
        self.__Signal = s
    def GetTotalElixir(self):
        return self.TotalTeamElixir
    def GetElixir(self):
        return self.SelfElixir
    def GetVirus(self):
        return self.TotalVirus
    
    def GetPosition(self):
        return (self.rect.x/20,self.rect.y/20)
    
    def GetDimensionX(self):
        return self.__myGame.dim[0]

    def GetDimensionY(self):
        return self.__myGame.dim[1]

    def DeployVirus(self, v):
        if v < self.TotalVirus:
            return
        self.actVirus(v/8,(self.rect.x-1,self.rect.y))
        self.actVirus(v/8,(self.rect.x+1,self.rect.y))
        self.actVirus(v/8,(self.rect.x-1,self.rect.y+1))
        self.actVirus(v/8,(self.rect.x-1,self.rect.y-1))
        self.actVirus(v/8,(self.rect.x+1,self.rect.y+1))
        self.actVirus(v/8,(self.rect.x+1,self.rect.y-1))
        self.actVirus(v/8,(self.rect.x,self.rect.y+1))
        self.actVirus(v/8,(self.rect.x,self.rect.y-1))

    def blitme(self):
        self.screen.blit(self.image, self.rect)