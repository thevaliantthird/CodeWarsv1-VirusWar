from random import randint

#BeeTechieZ
#Sajal  210070071
#Arnav  210100025
#Shubhranil     210100144
#Soham  210051004



def ActRobot(robot):
        tick =  int(robot.GetCurrentBaseSignal()[:4])

        robotname = robot.GetInitialSignal()[0:2]

        canvas = (int(robot.GetInitialSignal()[6:8]), int(robot.GetInitialSignal()[8:10]))

        base_X=int(robot.GetInitialSignal()[2:4])
        base_Y=int(robot.GetInitialSignal()[4:6])
        EnemyBaseAttackingRobots = int(robot.GetCurrentBaseSignal()[4:6])
        

        base_axial = False
        if abs(canvas[0]/2 - base_X) <= 1 or abs(canvas[1]/2 - base_Y) <= 1:
                base_axial = True
        else:
                base_axial = False
        
        if base_X <= canvas[0]/2:
                side = 'l'
                nside = 'r'
        else:
                side = 'r'
                nside = 'l'

        if tick <=1:
                robot.setSignal(robot.GetInitialSignal()[0:2] + "0"*4 + "xxyy" + robot.GetInitialSignal()[10:20])
        else:
                robot.setSignal(robot.GetYourSignal())

        robotname = robot.GetYourSignal()[0:2]
        Bias=int(robot.GetCurrentBaseSignal()[12])
        
        
        #takes string input of enemy, wall etc... returns (x,y) coords if specified unit is found
        def search(unit):                                                           
                if robot.investigate_right()==unit:
                        return (robot.GetPosition()[0]+1,robot.GetPosition()[1])
                if robot.investigate_left()==unit:
                        return (robot.GetPosition()[0]-1,robot.GetPosition()[1])
                if robot.investigate_up()==unit:
                        return (robot.GetPosition()[0],robot.GetPosition()[1]-1)
                if robot.investigate_down()==unit:
                        return (robot.GetPosition()[0],robot.GetPosition()[1]+1)
                if robot.investigate_ne()==unit:
                        return (robot.GetPosition()[0]+1,robot.GetPosition()[1]-1)
                if robot.investigate_nw()==unit:
                        return (robot.GetPosition()[0]-1,robot.GetPosition()[1]-1)
                if robot.investigate_se()==unit:
                        return (robot.GetPosition()[0]+1,robot.GetPosition()[1]+1)
                if robot.investigate_sw()==unit:
                        return (robot.GetPosition()[0]-1,robot.GetPosition()[1]+1)
                else:
                        return False
        
        def goto(target_x, target_y): #Warning: only use when the target position is not the current position. 
                Cur_x = robot.GetPosition()[0]
                Cur_y = robot.GetPosition()[1]
                if Cur_x > target_x:
                        return 4
                elif Cur_x < target_x:                                
                        return 2
                elif Cur_y > target_y:
                        return 1
                elif Cur_y < target_y:
                        return 3
                else:
                        return 0
                
        
         #sweeps, x2-x1 should be even
        def sweep(y1,y2):
                x1=0
                x2=canvas[0]-1
                x = robot.GetPosition()[0]
                y = robot.GetPosition()[1]
               
                lst = [int(robot.GetCurrentBaseSignal()[-2]),int(robot.GetCurrentBaseSignal()[-1])]
                
                 

                if robot.investigate_right()=="wall" or robot.investigate_left()=="wall":
                        if robot.investigate_right()=="wall":
                                if robotname[1]=='r':
                                        lst[0]=4
                                        robot.setSignal(robot.GetYourSignal()[:19]+"4")
                                elif robotname[1]=='l':
                                        lst[1]=4
                                        robot.setSignal(robot.GetYourSignal()[:19]+"4")
                        elif robot.investigate_left()=="wall":
                                if robotname[1]=='r':
                                        lst[0]=2
                                        robot.setSignal(robot.GetYourSignal()[:19]+"2")
                                elif robotname[1]=='l':
                                        lst[1]=2
                                        robot.setSignal(robot.GetYourSignal()[:19]+"2")
               

                if robotname[1]=='r':     
                        z = lst[0]
                elif robotname[1]=='l':
                        z = lst[1]         
                
            
                if (x-x1)%2==0 and (y!=y2) and (y!=y1):
                        return 1
                elif (x-x1)%2==1 and (y!=y2) and (y!=y1):
                        return 3
                elif (y==y2) and (x-x1)%2==0:
                        return z
                elif (y==y2) and (x-x1)%2==1:
                        return 3
                elif (y==y1) and (x-x1)%2==1:
                        return z
                elif (y==y1) and (x-x1)%2==0:
                        return 1
                else:
                        return z
        
        def patrol(y1,y2,n):
                x1=0
                x2=canvas[0]-1
                x = robot.GetPosition()[0]
                y = robot.GetPosition()[1]
               
                lst = [int(robot.GetCurrentBaseSignal()[-4]),int(robot.GetCurrentBaseSignal()[-3])]
                
                 

                if x==base_X+n or x==base_X-n or x==canvas[0] :
                        if x==base_X+n:
                                if robotname[1]=='r':
                                        lst[0]=4
                                        robot.setSignal(robot.GetYourSignal()[:19]+"4")
                                elif robotname[1]=='l':
                                        lst[1]=4
                                        robot.setSignal(robot.GetYourSignal()[:19]+"4")
                        elif x==base_X-n:
                                if robotname[1]=='r':
                                        lst[0]=2
                                        robot.setSignal(robot.GetYourSignal()[:19]+"2")
                                elif robotname[1]=='l':
                                        lst[1]=2
                                        robot.setSignal(robot.GetYourSignal()[:19]+"2")
               

                if robotname[1]=='r':     
                        z = lst[0]
                elif robotname[1]=='l':
                        z = lst[1]         
                
                if search('enemy')!=False:
                        return 0
            
                if (x-x1)%2==0 and (y!=y2) and (y!=y1) and (y!=0) and (y!=canvas[1]):
                        return 1
                elif (x-x1)%2==1 and (y!=y2) and (y!=y1) and (y!=canvas[1]):
                        return 3
                elif (y==y2 or y==0) and (x-x1)%2==0:
                        return z
                elif (y==y2 or y==0) and (x-x1)%2==1:
                        return 3
                elif (y==y1 or y==canvas[1]) and (x-x1)%2==1:
                        return z
                elif (y==y1 or y==canvas[1]) and (x-x1)%2==0:
                        return 1
                else:
                        return z
                        
           
        def MovementZone(centre_x, centre_y,constraint):
                if int(robot.GetPosition()[0]) <= int(centre_x - canvas[0]*constraint):
                        return 2
                elif int(robot.GetPosition()[0]) >= int(centre_x + canvas[0]*constraint):
                        return 4
                elif int(robot.GetPosition()[1]) <= int(centre_y - canvas[1]*constraint):
                        return 3
                elif int(robot.GetPosition()[1]) >= int(centre_y + canvas[1]*constraint):
                        return 1
                else:
                        return 0
                

        def count(unit):
                count = 0
                if robot.investigate_right()==unit:
                        count += 1
                if robot.investigate_left()==unit:
                        count += 1
                if robot.investigate_up()==unit:
                        count += 1
                if robot.investigate_down()==unit:
                        count += 1
                if robot.investigate_ne()==unit:
                        count += 1
                if robot.investigate_nw()==unit:
                        count += 1
                if robot.investigate_se()==unit:
                        count += 1
                if robot.investigate_sw()==unit:
                        count += 1
                return count

        def Biasedgoto(target_x, target_y):
                Cur_x = robot.GetPosition()[0]
                Cur_y = robot.GetPosition()[1]
                p1 = 25
                p2 = 25
                p3 = 25
                p4 = 25
                if Cur_x > target_x:
                        p2 = 15
                        p4 = 35
                elif Cur_x < target_x:
                        p2 = 35
                        p4 = 15
                if Cur_y > target_y:
                        p1 = 35
                        p3 = 15
                elif Cur_y < target_y:
                        p1 = 15
                        p3 = 35
                n = randint(1,101)
                if n <= p1:
                        return 1
                elif n <= p1 + p3 and n > p1:
                        return 3
                elif n > 50 and n <= 50 + p2:
                        return 2
                else:
                        return 4
        
        def BorderHugger(tarx, tary, dir):
                Cur_x = robot.GetPosition()[0]
                Cur_y = robot.GetPosition()[1]
                CloseToTar = False
                if (tarx - Cur_x)*(tary - Cur_y) == 0 and (abs(tarx - Cur_x) + abs(tary - Cur_y)) - min(tarx, tary, canvas[0] - tarx, canvas[1] - tary) <= 1:
                        CloseToTar = True
                if CloseToTar == False:
                        while search("wall") == False:
                                closest = min(Cur_x, canvas[0] - Cur_x, Cur_y, canvas[1] - Cur_y)
                                if closest == Cur_x:
                                        return 4
                                elif closest == canvas[0] - Cur_x:
                                        return 2
                                elif closest == Cur_y:
                                        return 1
                                elif closest == canvas[1] - Cur_y:
                                        return 3
                        if dir == "c":
                                if robot.investigate_left() == "wall" and robot.investigate_up() != "wall":
                                        return 1
                                elif robot.investigate_up() == "wall" and robot.investigate_right() != "wall":
                                        return 2
                                elif robot.investigate_right() == "wall" and robot.investigate_down() != "wall":
                                        return 3
                                elif robot.investigate_down() == "wall" and robot.investigate_left() != "wall":
                                        return 4
                        elif dir == "a":
                                if robot.investigate_left() == "wall" and robot.investigate_down() != "wall":
                                        return 3
                                elif robot.investigate_down() == "wall" and robot.investigate_right() != "wall":
                                        return 2
                                elif robot.investigate_right() == "wall" and robot.investigate_up() != "wall":
                                        return 1
                                elif robot.investigate_up() == "wall" and robot.investigate_left() != "wall":
                                        return 4
                else:
                        return goto(tarx,tary)

        
        Enemy_coords=robot.GetCurrentBaseSignal()[8:12]
        if Enemy_coords != "xxyy":
                enemy_base_X = int(Enemy_coords[0:2])
                enemy_base_Y = int(Enemy_coords[2:4])
        else:
                enemy_base_X = 0
                enemy_base_Y = 0
        virus = robot.GetVirus()
        elixir = robot.GetElixir()
        target = 50
        if tick == 20:
                target = virus*0.1       
        if elixir >= 500 and (robotname[0]=='1' or robotname[0]=='2'or robotname[0]=='3'):
                robot.setSignal('sa'+robot.GetYourSignal()[2:])

                        
                
              
        if base_axial== False:
                if Enemy_coords != "xxyy" and robotname[0]=='sa' and robot.GetVirus()>=target:
                        if goto(enemy_base_X,enemy_base_Y)!=0:
                                return goto(enemy_base_X,enemy_base_Y)
        else: 
                if Enemy_coords != "xxyy" and robotname[0]=='s' and robot.GetVirus()>=target:
                        if goto(enemy_base_X,enemy_base_Y)!=0:
                                return goto(enemy_base_X,enemy_base_Y)
        
        if Enemy_coords != "xxyy" and (robotname[1]==nside) and tick > 200 and EnemyBaseAttackingRobots <= 2:
                if goto(enemy_base_X,enemy_base_Y)!=0:
                        return goto(enemy_base_X,enemy_base_Y)
                
        if search("enemy-base") != False:
                enemybaseX =  str("00" + str(search("enemy-base")[0]))[-2:]
                enemybaseY = str("00" + str(search("enemy-base")[1]))[-2:]
                updated_signal_with_enemy_base_coords = robot.GetYourSignal()[0:6] + enemybaseX + enemybaseY + robot.GetYourSignal()[10:20]
                robot.setSignal(updated_signal_with_enemy_base_coords)
                robot.DeployVirus(robot.GetVirus()/((EnemyBaseAttackingRobots + 1)))
                robot.setSignal(robot.GetYourSignal()[0:10] + "1" + robot.GetYourSignal()[11:])


      
        
        if robotname == "x1":
                if tick < abs(canvas[0] - 2*base_X) + 5:
                        if (search("enemy") != False or search("enemy-base") != False) and robot.GetYourSignal()[2]!='d':
                                robot.setSignal(robot.GetYourSignal()[0:2]+"d"+robot.GetYourSignal()[3:])
                                return 0
                        if robot.GetPosition() != (canvas[0]-1 - base_X, base_Y):
                                return goto (canvas[0]-1 - base_X, base_Y)
                        #robot.setSignal(robot.GetYourSignal()[0:16] + str("00" + str(robot.GetPosition()[0]))[-2:] + str("00" + str(robot.GetPosition()[1]))[-2:] )
                       
                        
                
        
        if robotname == "x2" :
                if tick < abs(canvas[1] - 2*base_Y) + 5:
                        if (search("enemy") != False or search("enemy-base") != False) and robot.GetYourSignal()[2]!='d':
                                robot.setSignal(robot.GetYourSignal()[0:2]+"d"+robot.GetYourSignal()[3:])
                                return 0
                        if robot.GetPosition() != (base_X, canvas[1]-1 - base_Y):
                                return goto (base_X, canvas[1]-1 - base_Y)
                        #robot.setSignal(robot.GetYourSignal()[0:16] + str("00" + str(robot.GetPosition()[0]))[-2:] + str("00" + str(robot.GetPosition()[1]))[-2:] )
                        
        if search("enemy") != False: 
                if robotname[0]=='c':
                        robot.DeployVirus(robot.GetVirus()/2)

                elif robot.GetVirus() > 400:
                        robot.DeployVirus(400)
        
                if robot.GetElixir() < 100 and robotname[0]=='s' and tick > (canvas[0]+canvas[1])/2:                                                              
                        if robot.investigate_right()== "enemy":
                                return 4
                        if robot.investigate_left()== "enemy":
                                return 2
                        if robot.investigate_up()== "enemy":
                                return 3
                        if robot.investigate_down()== "enemy":
                                return 1
                        if robot.investigate_ne()== "enemy":
                                return randint(3,4)
                        if robot.investigate_nw()== "enemy":
                                return randint(2,3)
                        if robot.investigate_se()== "enemy":
                                return (1 + 3*randint(0,1))                    
                        if robot.investigate_sw()== "enemy":
                                return (1,2)
                        else:
                                return False

   
       
        if robotname[0] == 'a':
                #print(robot.GetYourSignal())
                if base_axial == True:
                        if Bias == 1 or Bias == 3:
                                tar_x = base_X
                                tar_y = canvas[1]-1 - base_Y
                        if Bias == 2 or Bias == 4:
                                tar_x = canvas[0]-1 - base_X
                                tar_y = base_Y
                        if abs(robot.GetPosition()[0] - tar_x) <= 3 and abs(robot.GetPosition()[1] - tar_y) <= 3:
                                if MovementZone(tar_x, tar_y, 3/max(canvas[0], canvas[1])) == 0:
                                        return randint(1,4)
                                else:
                                        return MovementZone(tar_x, tar_y, 3/max(canvas[0], canvas[1]))
                        elif int(robotname[1]) == 1 or (int(robotname[1]) == 2 and tick > 5):
                                return BorderHugger(tar_x, tar_y, "a")
                        elif int(robotname[1]) == 3 or (int(robotname[1]) == 4 and tick > 5):
                                return BorderHugger(tar_x, tar_y, "c")
                elif base_axial == False:
                        if Bias >= 1 and Bias <= 4:
                                robot.setSignal(robot.GetYourSignal()[0:3] + "1" + robot.GetYourSignal()[4:])
                        elif Bias == 5 and robot.GetYourSignal()[3] == "1":
                                robot.setSignal('sa' + robot.GetYourSignal()[2:])
                                robotname=robot.GetYourSignal()[0:2]
                                
                        if robotname[0]=='a':
                                if base_X < canvas[0]/2:
                                        tar_x = canvas[0]-1 - base_X
                                else:
                                        tar_x = 0
                                if base_Y < canvas[1]/2:
                                        tar_y = canvas[1]-1 - base_Y
                                else:
                                        tar_y = 1
                                startingtick = (abs(canvas[0] - 2*base_X) + abs(canvas[1] - 2*base_Y))/2
                                if tick <= startingtick and Bias == 0:
                                        if int(robotname[1]) == 1 or (int(robotname[1]) == 2 and tick > 5):
                                                return BorderHugger(tar_x, tar_y, "a")
                                        elif int(robotname[1]) == 3 or (int(robotname[1]) == 4 and tick > 5):
                                                return BorderHugger(tar_x, tar_y, "c")
                                elif Bias == 5:
                                        tar_x = canvas[0]-1 - base_X
                                        tar_y = canvas[1]-1 - base_Y
                                        if abs(robot.GetPosition()[0] - tar_x) <= 3 and abs(robot.GetPosition()[1] - tar_y) <= 3:
                                                if MovementZone(tar_x, tar_y, 3/max(canvas[0], canvas[1])) == 0:
                                                        return randint(1,4)
                                                else:
                                                        return MovementZone(tar_x, tar_y, 3/max(canvas[0], canvas[1]))
                                        
                                        elif int(robotname[1]) <=2:
                                                return BorderHugger(tar_x, tar_y, "a")
                                        elif int(robotname[1]) > 2:
                                                return BorderHugger(tar_x, tar_y, "c")
                                else:
                                        if Bias == 1 or Bias == 3:
                                                tar_x = base_X
                                                tar_y = canvas[1]-1 - base_Y
                                        if Bias == 2 or Bias == 4:
                                                tar_x = canvas[0]-1 - base_X
                                                tar_y = base_Y
                                        if abs(robot.GetPosition()[0] - tar_x) <= 1 and abs(robot.GetPosition()[1] - tar_y) <= 1:
                                                if MovementZone(tar_x, tar_y, 2/max(canvas[0], canvas[1])) == 0:
                                                        if Enemy_coords == "xxyy":
                                                                robot.setSignal(robot.GetYourSignal()[0:2] + str("00" + str(int(robot.GetYourSignal()[2]) + 1))[-1:] + robot.GetYourSignal()[3:])
                                                        return randint(1,4)
                                                else:
                                                        return MovementZone(tar_x, tar_y, 3/max(canvas[0], canvas[1]))
                                        elif int(robotname[1]) <= 2:
                                                return BorderHugger(tar_x, tar_y, "a")
                                        elif int(robotname[1]) > 2:
                                                return BorderHugger(tar_x, tar_y, "c")               
                                        else:
                                                return 0
                                        
                                
        
        if robotname[0]=='s' or (robotname[0] == "x" and tick>=(canvas[0] + canvas[1])/2):

                if base_axial==True:
                        if tick<=int((canvas[0]+canvas[1])/4):
                        
                                k = MovementZone(int(canvas[0]/2), int(canvas[1]/2), 0.3)
                                if k != False:
                                        return k
                                else :
                                        
                                        n = randint(1,4)
                                        if Bias != 0:
                                                if n == Bias:
                                                        return n
                                                else:
                                                        return randint(1,4)
                                                

                                        else:
                                                return randint(1,4)
                        else:
                                if MovementZone(canvas[0]-1-base_X,canvas[1]-1-base_Y,0.08)==0:
                                        return randint(1,4)
                                else: 
                                        return MovementZone(canvas[0]-1-base_X,canvas[1]-1-base_Y,0.08)

                else: #Improve this!!
                        n = randint(1,4)
                        if Bias != 0 and Bias !=5:
                                if n == Bias:
                                        return n
                                else:
                                        return randint(1,4)
                                        
                        elif Bias==5:
                                if robotname!='sb':
                                        return MovementZone(canvas[0]-1-base_X, canvas[1]-1-base_Y,0.05)
                                else :
                                        return randint(1,4)
                        else:
                                return randint(1,4)
                                
        #sweeper robots
        y1=canvas[1]-1
        y2=canvas[1]//2     
        y3=y2-1
        y4=0   

        if robotname[0:2]=="2r":
                return sweep(y1,y2) 
        if robotname[0:2]=="1r":
                return sweep(y3,y4)
        if robotname[0:2]=="2l":
                return sweep(y1,y2) 
        if robotname[0:2]=="1l":
                return sweep(y3,y4)
        if robotname[0:2]=="3"+side:
                return sweep(int(canvas[1]*0.75),int(canvas[1]*0.25))
        if robotname[0:2]=="3"+nside:
                return sweep(int(canvas[1]*0.75),int(canvas[1]*0.25))  
        
        
        #patrol robots
        if robotname[0]=='p':
                return patrol(base_Y+2,base_Y-2,2)
        
        if robotname[0]=='q' and tick > 4:
                return patrol(base_Y+2,base_Y-2,2)            

        if robotname[0]=='r' and tick > 8:
                return patrol(base_Y+2,base_Y-2,2)       

        if robotname[0]=='t' and tick>12:
                return patrol(base_Y+2,base_Y-2,2)  
        
        if robotname[0]=='c':
                num = int(robotname[1])
                ###discord disconnected rejoining k
                ###janky
                if tick>=2*num:
                    if search('enemy')!=False:
                            return 0
                    else:

                        return Bias
                '''if tick == 1:
                        if num==1:     
                                return 1
                        elif num==2:
                                return 3
                        

                elif tick==2:
                        if num!=0:
                                return Bias 
                else:
                        if search('enemy')!=False:
                            return goto(search('enemy')[0],search('enemy')[1])
                        else:
                            return Bias'''
                        

def ActBase(base):
        base_pos = base.GetPosition()
        base_X=int(base_pos[0])
        base_Y=int(base_pos[1])
        canvas = (base.GetDimensionX(),base.GetDimensionY())
        list = base.GetListOfSignals()
        EnemyBaseRobotCounter = 0

        if base_X <= canvas[0]/2:
                side = 'l'
                nside = 'r' 
                dir = '4'
                ndir = '2'
        else:
                side = 'r'
                nside = 'l'
                dir = '2'
                ndir = '4'

        #timer
        if base.GetYourSignal() == '':                          
                tick = '0000'
        else:
                tick = base.GetYourSignal()[:4]
        
        if base.GetYourSignal() == '':     
                base.SetYourSignal(('0000' + str(int(('000'+tick)[-4:])+1))[-4:] +  "0"*4 + "xxyy" + "0"*4 +"2424")
        else:
                base.SetYourSignal(('0000' + str(int(('000'+tick)[-4:])+1))[-4:] +"0"*4+ base.GetYourSignal()[8:])            ##########

        if abs(canvas[0]/2 - base_X) <= 1:
                if base_Y < canvas[1]/2:
                        base.SetYourSignal(base.GetYourSignal()[0:12]+"3"+ base.GetYourSignal()[13:])
                if base_Y > canvas[1]/2: 
                        base.SetYourSignal(base.GetYourSignal()[0:12]+"1"+ base.GetYourSignal()[13:])
                base_axial = True
        elif abs(canvas[1]/2 - base_Y) <= 1:
                if base_X < canvas[0]/2:
                        base.SetYourSignal(base.GetYourSignal()[0:12]+"2"+ base.GetYourSignal()[13:])
                if base_X > canvas[0]/2:
                        base.SetYourSignal(base.GetYourSignal()[0:12]+"4"+ base.GetYourSignal()[13:])
                base_axial = True
        else:
                base_axial = False
        
        Bias = int(base.GetYourSignal()[12])

        if tick=='0000':
                if base_axial==False:
                        for i in range(1,5):
                                base.create_robot('a' + str(i) +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*10)
                

                base.create_robot('1l' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")
                base.create_robot('2l' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")
                base.create_robot('1r' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"2")                        
                base.create_robot('2r' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"2")
                base.create_robot('3'+side +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+dir) 
                if base_axial==False:
                        base.create_robot('3'+nside +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+ndir) 
                #Patrol robot
                
                base.create_robot('pr' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"2")                       
                base.create_robot('qr' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"2")  
                base.create_robot('rr' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"2")  
                base.create_robot('pl' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")  
                base.create_robot('ql' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")  
                base.create_robot('rl' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")
                #base.create_robot('tl' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")
                #base.create_robot('tr' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")      

                if base_axial==True:
                        for i in range(0,3):
                                base.create_robot('c'+ str(i) +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*9+"4")   
                
                if base_axial == False:
                        base.create_robot('x1' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*10)
                        base.create_robot('x2' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*10)
                
                k = int((base.GetElixir() - 300)/50)
                if k%2==0:
                        a=int(k/2)+4
                        b=int(k/2)-4
                else:
                        a=int(k/2)+5
                        b=int(k/2)-4
                for i in range(0,a):
                        base.create_robot('sa' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*10)
                for i in range(0,b):
                        base.create_robot('sb' +("00"+str(base_X))[-2:]+("00"+str(base_Y))[-2:]+("00"+str(canvas[0]))[-2:]+("00"+str(canvas[1]))[-2:]+"0"*10)
               
        for i in list:
                if len(i)>0 and i[6:10] != "xxyy":
                        enemy_base_coords = i[6:10]
                        base_signal = base.GetYourSignal()[0:8] + enemy_base_coords+base.GetYourSignal()[12:20]
                        base.SetYourSignal(base_signal)
       

        for i in list:
                if i[0] in ['p','q','r','t']:
                        if len(i) > 0 and i[1]=='r':
                                base.SetYourSignal(base.GetYourSignal()[0:16] + i[-1] + base.GetYourSignal()[-3:])
                        if len(i) > 0 and i[1]=='l':
                                base.SetYourSignal(base.GetYourSignal()[0:17] + i[-1]+ base.GetYourSignal()[-2:])
                        if len(i) > 0 and i[10] == "1":
                                EnemyBaseRobotCounter += 1

                else:
                        if len(i) > 0 and i[1]=='r':
                                base.SetYourSignal(base.GetYourSignal()[0:18] + i[-1] + base.GetYourSignal()[-1])
                        if len(i) > 0 and i[1]=='l':
                                base.SetYourSignal(base.GetYourSignal()[0:19] + i[-1])
                        if len(i) > 0 and i[10] == "1":
                                EnemyBaseRobotCounter += 1
        
        
        if base_axial == False and Bias == 0:
                x1_detect='0'
                x2_detect='0'
                for i in list:
                        if len(i) > 0 and i[0]=='x':
                                if i[0:2]=='x1':
                                        x1_detect = i[2]        
                                if i[0:2]=='x2':
                                        x2_detect = i[2]
                
                #print(x1_detect,x2_detect)
                #Bias Condition
                if x1_detect=='d' and x2_detect!='d': #Enemy base is symmetric along y-axis
                        if base_X < canvas[0]/2:
                                base.SetYourSignal(base.GetYourSignal()[0:12]+"2" + base.GetYourSignal()[13:])
                        if base_X > canvas[0]/2:
                                base.SetYourSignal(base.GetYourSignal()[0:12]+"4" + base.GetYourSignal()[13:])
                                        
                elif x1_detect!='d' and x2_detect=='d': #Enemy base is symmetric along x-axis
                        if base_Y < canvas[1]/2:
                                base.SetYourSignal(base.GetYourSignal()[0:12]+"3" + base.GetYourSignal()[13:])
                        if base_Y > canvas[1]/2:
                                base.SetYourSignal(base.GetYourSignal()[0:12]+"1" + base.GetYourSignal()[13:])   
                else:
                        if int(tick) > max(abs(canvas[0] - 2*base_X),abs(canvas[1] - 2*base_Y)):
                        #Diagonal Bias
                                base.SetYourSignal(base.GetYourSignal()[0:12] + '5' + base.GetYourSignal()[13:])
                        
        
        for i in list:
                if i[0]=='a':
                        if i[2] =='2':
                                base.SetYourSignal(base.GetYourSignal()[0:12] + '5' + base.GetYourSignal()[13:])
        
        #print(base.GetYourSignal()[12])

        if base.investigate_up()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_down()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_right()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_left()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_nw()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_ne()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_se()=='enemy':
                base.DeployVirus(base.GetVirus()/2)
        elif base.investigate_sw()=='enemy':
                base.DeployVirus(base.GetVirus()/2)

        base.SetYourSignal(base.GetYourSignal()[0:4] + ("00" + str(EnemyBaseRobotCounter))[-2:] + base.GetYourSignal()[6:])
