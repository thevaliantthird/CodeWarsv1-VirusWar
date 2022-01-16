from random import randint
import random

def to_str(x):
        if x>9:
                return str(x)
        else:
                return ('0'+str(x)) 

def ActRobot(robot):

        x = robot.GetPosition()[0]
        y = robot.GetPosition()[1]
        Lx = robot.GetDimensionX()
        Ly = robot.GetDimensionY()
        
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()

        nw = robot.investigate_nw()
        ne = robot.investigate_ne()
        sw = robot.investigate_sw()
        se = robot.investigate_ne()

        I = robot.GetInitialSignal()
        B = robot.GetCurrentBaseSignal()
        Y = robot.GetYourSignal()

        #For All bots
        #SELF DEFENDING
        if (right=='enemy' or left=='enemy' or up=='enemy' or down=='enemy' or nw=='enemy' or ne=='enemy' or sw=='enemy' or se=='enemy'): 
                if I[0]=='p':
                        if robot.GetVirus()>10000:
                                robot.DeployVirus(4500)
                        elif robot.GetVirus()>5000:
                                robot.DeployVirus(4500)
                        elif robot.GetVirus()>3000:
                                robot.DeployVirus(2700)
                        elif robot.GetVirus()>2000:
                                robot.DeployVirus(1800)
                        else:
                                robot.DeployVirus(robot.GetVirus())

                else:
                        if robot.GetVirus()>10000:
                                robot.DeployVirus(3600)
                        elif robot.GetVirus()>5000:
                                robot.DeployVirus(2700)
                        elif robot.GetVirus()>2000:
                                robot.DeployVirus(1800)
                        elif robot.GetVirus()>1000:
                                robot.DeployVirus(900)
                        else:
                                robot.DeployVirus(robot.GetVirus())
                                

        #For Rnd bots        
        #FINIDING ENEMY BASE
        if up=='enemy-base' or down=='enemy-base' or left=='enemy-base' or right=='enemy-base' or nw=='enemy-base' or ne=='enemy-base' or sw=='enemy-base' or se=='enemy-base':  
                robot.setSignal('foundbase'+ to_str(x) + to_str(y))
                robot.DeployVirus(robot.GetVirus())

                
        #Emeny Base Location Conformation Bots
        if I[0]=='C':

                Ex = int(I[2:4])
                Ey = int(I[4:6])
                
                if I[1]=='x':
                        if  x - Ex > 0:
                                return 4
                        elif x -Ex < 0:
                                return 2
                        elif x==Ex:
                                if y - Ey > 0:
                                        return 1
                                elif y - Ey < 0:
                                        return 3

                elif I[1]=='y':
                        if  y - Ey > 0:
                                return 1
                        elif y -Ey < 0:
                                return 3
                        elif y==Ey:
                                if x - Ex > 0:
                                        return 4
                                elif x - Ex < 0:
                                        return 2
                        
                        
        #For Protecting bots
        #PROTECTING MY BASE
        if I[0]=='p':
                if (robot.GetYourSignal()[0:2] != 'pp'):
                        robot.setSignal('pp' + I[1])
                        return int(I[1]);           
                else:
                        return 0
                
        #For Rnd Attacking bots
        #ATTACKING ENEMY BASE
        if B[0:6]=='attack' and I[0:10]=='rnd_attack':

                enemy_base_x = int(B[6:8])
                enemy_base_y = int(B[8:10])
                
                dist = abs(enemy_base_x - x) + abs(enemy_base_y - y)

                if dist==1:
                        robot.DeployVirus(10)
                        return 0
                if x>enemy_base_x:
                        return 4
                elif x<enemy_base_x:
                        return 2
                elif y>enemy_base_y:
                        return 1
                elif y<enemy_base_y:
                        return 3
              
        return randint(1,4)


def ActBase(base):
        L = base.GetListOfSignals()
        
        x = base.GetPosition()[0]
        y = base.GetPosition()[1]
        Lx = base.GetDimensionX()
        Ly = base.GetDimensionY()
        #Enemy base location guess
        Ex = Lx - x - 1
        Ey = Ly - y - 1
        #
        
        up = base.investigate_up()
        down = base.investigate_down()
        left = base.investigate_left()
        right = base.investigate_right()
        nw = base.investigate_nw()
        ne = base.investigate_ne()
        sw = base.investigate_sw()
        se = base.investigate_ne()

        ### 
        #Base Protecting itself
        if (right=='enemy' or left=='enemy' or up=='enemy' or down=='enemy' or nw=='enemy' or ne=='enemy' or sw=='enemy' or se=='enemy'):
                base.DeployVirus(2700)


        ###   
        #Creating Robots
        #Farming Only Robots
        if base.GetElixir() > 1600:
                base.create_robot('rnd_farm')
        #Farming+attacking bots
        elif base.GetElixir() > 800:
                base.create_robot('rnd_attack')
            
        #Base Protecting Robots
        elif base.GetElixir() > 600:
                base.create_robot('p1')
                base.create_robot('p2')
                base.create_robot('p3')
                base.create_robot('p4')

        #Enemy Base Location Conformation Robots
        elif base.GetElixir()>500 and base.GetTotalElixir() > 4000 and len(L)<25 and base.GetYourSignal()[0:6] != 'attack':
                base.create_robot('Cx'+to_str(Ex)+to_str(Ey))
                base.create_robot('Cy'+to_str(Ex)+to_str(Ey))
        

        if base.GetElixir() > 100 and base.GetElixir() < 600:
                if 'pp1' not in L:
                        base.create_robot('p1')
                if 'pp2' not in L:
                        base.create_robot('p2')
                if 'pp3' not in L:
                        base.create_robot('p3')
                if 'pp4' not in L:
                        base.create_robot('p4')

        #If I lose                
        if base.GetElixir() == 0:
                print('gg, well played')
                
        ###
        #Setting Signal to attack enemy base               
        for l in L:
                if l[0:9]=='foundbase':
                        base.SetYourSignal('attack'+l[9:13])
                        
                        
        return 
