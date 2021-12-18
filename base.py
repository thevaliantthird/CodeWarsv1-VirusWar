import pygame
from robot import Robot

class Base():
    def __init__(self, screen, x, y, type, robot_list, robot_map, game):
        self.screen = screen
        self.type = type
        self.robot_map = robot_map
        self.robot_list = robot_list
        self.__myGame = game
        self.SelfElixir = 2000
        self.TotalTeamElixir = 2000
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
        self.screen.blit(g.virus, pos)
        if pos[0] < 0 or pos[0] >= g.dim[0]:
            return
        if pos[1] < 0 or pos[1] >= g.dim[1]:
            return
        if self.robot_map[pos[1]][pos[0]]==0:
            g.resources[pos[1]][pos[0]]-= v
            return
        if self.robot_map[pos[1]][pos[0]]==1 and self ==g._Game__redbase:
            self.TotalVirus += v
            return
        if self.robot_map[pos[1]][pos[0]]==1 and self==g._Game__bluebase:
            g._Game__redbase.VirusOnRobot(pos, v)
            return
        if self.robot_map[pos[1]][pos[0]]==2 and self==g._Game__bluebase:
            self.TotalVirus += v
            return
        if self.robot_map[pos[1]][pos[0]]==2 and self==g._Game__redbase:
            g._Game__redbase.VirusOnRobot(pos, v)
            return
        if self.robot_map[pos[1]][pos[0]]==3 and self==g._Game__bluebase:
            g._Game__redbase.SelfElixir -= v
            g._Game__redbase.TotalTeamElixir -= v
            return
        if self.robot_map[pos[1]][pos[0]]==3 and self==g._Game__redbase:
            self.TotalVirus += v
            return
        if self.robot_map[pos[1]][pos[0]]==4 and self==g._Game__redbase:
            g._Game__bluebase.SelfElixir -= v
            g._Game__bluebase.TotalTeamElixir -= v
            return
        if self.robot_map[pos[1]][pos[0]]==4 and self==g._Game__bluebase:
            self.TotalVirus += v
            return

    def GetListOfSignals(self):
        res = []
        for x in self.robot_list:
            res.append(x.__Signal)
        return res

    def addResource(self, v):
        if v < 0:
            self.TotalVirus -= v
        else:
            self.SelfElixir += v
            self.TotalTeamElixir += v
        
    def VirusOnRobot(self, pos,virus):
        robots = self.__myGame.PositionToRobot[pos]
        virus /= len(robots)
        for robot in robots:
            if robot.selfElixir <= virus:
                e = virus - robot.selfElixir
                self.TotalTeamElixir -= robot.selfElixir
                del self.__myGame.PositionToRobot[pos][robot]
                robot.kill()
                self.robot_map[pos[1]][pos[0]] = 0
                self.__myGame.resource[pos[1]][pos[0]]+=e
            else:
                self.TotalTeamElixir -= virus
                robot.selfElixir-=virus
            
    def create_robot(self, signal):
        if self.SelfElixir >= 50:
            self.SelfElixir -= 50
            #self.GlobalRobotCount += 1
            robo = Robot(self.screen, self.rect.x, self.rect.y, self.type, signal, self)
            self.robot_list.add(robo)
            if (self.rect.x//20, self.rect.y//20) in self.__myGame.PositionToRobot:
                self.__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][robo] = True
            else:
                self.__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)] = {}
                self.__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][robo] = True
            if self.type == 'red':
                self.robot_map[self.rect.y//20][self.rect.x//20] = 3
            else:
                self.robot_map[self.rect.y//20][self.rect.x//20] = 4

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
        return (self.rect.x//20,self.rect.y//20)
    
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