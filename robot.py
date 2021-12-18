import pygame
from pygame.sprite import Sprite
from random import randint
class Robot(Sprite):
    def __init__(self, screen, x, y, type, signal, base):
        super().__init__()
        self.screen = screen
        self.type = type
        self.__myBase = base
        self.selfElixir = 50
        self.__Signal = 0
        # Integer less than 2^31 -1
        self.__Initialsignal = signal
        if type == "red":
            self.image = pygame.image.load("red_robot.png")
        else:
            self.image = pygame.image.load("blue_robot.png")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

    

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        if self.rect.y >0:
            self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 0
            del self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self]
            self.rect.y -= 20
            if (self.rect.x//20, self.rect.y//20) in self.__myBase._Base__myGame.PositionToRobot:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            else:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)] = {}
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            if self.type == 'red': 
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 1
            else:
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 2

    def addResource(self, v):
        if v < 0:
            self.__myBase.TotalVirus -= v
        else:
            self.selfElixir += v
            self.__myBase.TotalTeamElixir += v

    def move_down(self):
        if self.rect.y < 780:
            self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 0
            del self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self]
            self.rect.y += 20
            if (self.rect.x//20, self.rect.y//20) in self.__myBase._Base__myGame.PositionToRobot:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            else:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)] = {}
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            if self.type == 'red': 
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 1
            else:
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 2

    def move_left(self):
        if self.rect.x > 0:
            self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 0
            del self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self]
            self.rect.x -= 20
            if (self.rect.x//20, self.rect.y//20) in self.__myBase._Base__myGame.PositionToRobot:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            else:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)] = {}
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            if self.type == 'red': 
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 1
            else:
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 2

    def move_right(self):
        if self.rect.x < 780:
            self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 0
            del self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self]
            self.rect.x += 20
            if (self.rect.x//20, self.rect.y//20) in self.__myBase._Base__myGame.PositionToRobot:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            else:
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)] = {}
                self.__myBase._Base__myGame.PositionToRobot[(self.rect.x//20, self.rect.y//20)][self] = True
            if self.type == 'red': 
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 1
            else:
                self.__myBase.robot_map[self.rect.y//20][self.rect.x//20] = 2

    def investigate_up(self):
        if self.rect.y == 0:
            return "wall"
        elif self.robot_map[self.rect.y//20  - 1][self.rect.x//20] == 1 or self.__myBase.robot_map[self.rect.y//20  - 1][self.rect.x//20] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20  - 1][self.rect.x//20] == 2 or self.__myBase.robot_map[self.rect.y//20  - 1][self.rect.x//20] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"
    

    def investigate_down(self):
        if self.rect.y == 780:
            return "wall"
        elif self.robot_map[self.rect.y//20  + 1][self.rect.x//20] == 1 or self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20  + 1][self.rect.x//20] == 2 or self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"
    
    def investigate_left(self):
        if self.rect.x == 0:
            return "wall"
        elif self.robot_map[self.rect.y//20][self.rect.x//20  - 1] == 1 or self.__myBase.robot_map[self.rect.y//20][self.rect.x//20 - 1] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20][self.rect.x//20 - 1] == 2 or self.__myBase.robot_map[self.rect.y//20][self.rect.x//20 - 1] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"

    
    def investigate_right(self):
        if self.rect.x == 780:
            return "wall"
        elif self.robot_map[self.rect.y//20][self.rect.x//20 + 1] == 1 or self.__myBase.robot_map[self.rect.y//20][self.rect.x//20 + 1] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20][self.rect.x//20 + 1] == 2 or self.__myBase.robot_map[self.rect.y//20][self.rect.x//20 + 1] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"

    
    def investigate_nw(self):
        if self.rect.x == 780 or self.rect.y == 0:
            return "wall"
        elif self.robot_map[self.rect.y//20  - 1][self.rect.x//20 + 1] == 1 or self.__myBase.robot_map[self.rect.y//20  - 1][self.rect.x//20 + 1] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20  - 1][self.rect.x//20 + 1] == 2 or self.__myBase.robot_map[self.rect.y//20  - 1][self.rect.x//20 + 1] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"

    def investigate_ne(self):
        if self.rect.x == 0 or self.rect.y == 0:
            return "wall"
        elif self.robot_map[self.rect.y//20  - 1][self.rect.x// - 1] == 1 or self.__myBase.robot_map[self.rect.y//20  - 1][self.rect.x//20 - 1] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20  - 1][self.rect.x//20 - 1] == 2 or self.__myBase.robot_map[self.rect.y//20  - 1][self.rect.x//20 - 1] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"

    def investigate_sw(self):
        if self.rect.x == 780 or self.rect.y == 780:
            return "wall"
        elif self.robot_map[self.rect.y//20  + 1][self.rect.x//20 + 1] == 1 or self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20 + 1] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.robot_map[self.rect.y//20  + 1][self.rect.x//20 + 1] == 2 or self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20 + 1] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"
    def DeployVirus(self, v):
        if v < self.__myBase.TotalVirus:
            return
        self.__myBase.actVirus(v/8,(self.rect.x//20-1,self.rect.y//20))
        self.__myBase.actVirus(v/8,(self.rect.x//20+1,self.rect.y//20))
        self.__myBase.actVirus(v/8,(self.rect.x//20-1,self.rect.y//20+1))
        self.__myBase.actVirus(v/8,(self.rect.x//20-1,self.rect.y//20-1))
        self.__myBase.actVirus(v/8,(self.rect.x//20+1,self.rect.y//20+1))
        self.__myBase.actVirus(v/8,(self.rect.x//20+1,self.rect.y//20-1))
        self.__myBase.actVirus(v/8,(self.rect.x//20,self.rect.y//20+1))
        self.__myBase.actVirus(v/8,(self.rect.x//20,self.rect.y//20-1))
    def setSignal(self, sig):
        self.__Signal = sig
    
    def GetInitialSignal(self):
        return self.__Initialsignal

    def GetYourSignal(self):
        return self.__Signal
    
    def GetCurrentBaseSignal(self):
        return self.__myBase.__Signal
    
    def GetTotalElixir(self):
        return self.__myBase.TotalTeamElixir
    
    def GetVirus(self):
        return self.TotalVirus

    def GetElixir(self):
        return self.selfElixir
    
    def GetPosition(self):
        return (self.rect.x//20, self.rect.y//20)
    
    def GetDimensionX(self):
        return self.__myBase._Base__myGame.dim[0]

    def GetDimensionY(self):
        return self.__myBase._Base__myGame.dim[1]

    #def __hash__(self):
     #   return self.ID

    def investigate_se(self):
        if self.rect.x == 0:
            return "wall"
        elif self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20 - 1] == 1 or self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20 - 1] == 3:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        elif self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20 - 1] == 2 or self.__myBase.robot_map[self.rect.y//20  + 1][self.rect.x//20 - 1] == 4:
            if self.type == "red":
                return "friend"
            else:
                return "enemy"
        else:
            return "blank"