from random import randint, choice
base_def = 0
line_robo_alive = [True]*13
robo_count = 0

i = 16
j = 32
k = 9

#########################################

# f-values for different squads

ld = 1200
fd = 0.4

la = 1000
fa = 0.4

lm = 1000
fm = 0.7

ls = 1000
fs = 0.4

#########################################

baseX = None
baseY = None
attackersPosAssumed = False
originMirrorPosAssumed = False
xMirrorPosAssumed = False
yMirrorPosAssumed = False
diagonal1PosAssumed = False
diagonal2PosAssumed = False

# lineRobotsPosAssumed = [False]*13

#########################################

# signal for the newly created robot
def cr_robo_sig():
        global robo_count
        robo_count += 1
        signal = 'id=' + str(robo_count).zfill(2)
        return signal

#################################################

def ActRobot(robot):
        robotX, robotY = robot.GetPosition()
        X, Y = robot.GetDimensionX(), robot.GetDimensionY()
        global ld
        global fd
        global la
        global fa
        global lm
        global fm
        global ls
        global fs

        # getting the robot signal        
        sig=robot.GetInitialSignal()
        # ofc this function is only called by'alive' robots
        # so signal being blank can only mean a new robot popped up
        
        # scanning the neighbourhood
        p_n = robot.investigate_up()
        p_ne = robot.investigate_ne()
        p_e = robot.investigate_right()
        p_se = robot.investigate_se()
        p_s = robot.investigate_down()
        p_sw = robot.investigate_sw()
        p_w = robot.investigate_left()
        p_nw = robot.investigate_nw()
        p_list = [p_n, p_ne, p_e, p_se, p_s, p_sw, p_w, p_nw]

        # tracking multiple enemies
        count = 0
        for l in p_list:
            if l == 'enemy':
                count+=1
        if count > 1:
            robot.setSignal("db" + str(robotX) + str(robotY)) #Abhijit : replaced double with db to avoid conflict
        else:
            robot.setSignal(robot.GetInitialSignal())    


        roboid = int(sig[3:5]) #Abhijit : I changed this
        

        # gang up codes
        if roboid > 16 and roboid < 32:
                base_signal = robot.GetCurrentBaseSignal()
                if len(base_signal) == 6 :
                        if base_signal[:2] == 'eb' :
                                enemy_baseX = int(base_signal[2:4])
                                enemy_baseY = int(base_signal[4:])
                                diffX = abs(enemy_baseX - robotX)
                                diffY = abs(enemy_baseY - robotY)
                                if diffX + diffY == 1:
                                        robot.DeployVirus(robot.GetVirus())
                                        return 0
                                else:
                                        if robotX < enemy_baseX:
                                                return 2
                                        elif robotX > enemy_baseX:
                                                return 4
                                        elif robotY < enemy_baseY:
                                                return 3
                                        else:
                                                return 1
                        else :
                                if roboid > 16 and roboid < 22 :
                                        double_robotX = int(base_signal[2:4])
                                        double_robotY = int(base_signal[4:])
                                        diffX = abs(double_robotX - robotX)
                                        diffY = abs(double_robotY - robotY)
                                        if diffX + diffY == 1:
                                                robot.DeployVirus(robot.GetVirus()*0.4)
                                                return 0
                                        else:
                                                if robotX < double_robotX:
                                                        return 2
                                                elif robotX > double_robotX:
                                                        return 4
                                                elif robotY < double_robotY:
                                                        return 3
                                                else:
                                                        return 1
                
        #defenceRobots
        elif roboid > 0 and roboid < 9:
                global i
                if "enemy" in p_list:
                        #if robot.GetVirus() > 1200:
                        #        robot.DeployVirus(1000)
                        #elif robot.GetVirus() > 800:
                        #        robot.DeployVirus(600)
                        #elif robot.GetVirus() > 300:
                        #        robot.DeployVirus(200)
                        robot.DeployVirus(min(ld,fd*robot.GetVirus()))

                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())                
                if i > 0:                
                        if roboid == 1:  #nw
                                robotX, robotY = robot.GetPosition()
                                posX=baseX-1
                                posY=baseY-1
                                if(robotX>posX):
                                        i-=1 
                                        return 4
                                if(robotY>posY):
                                        i-=1  
                                        return 1
                        elif roboid == 2:  #ne
                                robotX, robotY = robot.GetPosition()
                                posX=baseX+1
                                posY=baseY-1
                                if(robotX<posX):
                                        i-=1  
                                        return 2
                                if(robotY>posY):
                                        i-=1  
                                        return 1
                        elif roboid == 3:  #sw
                                robotX, robotY = robot.GetPosition()
                                posX=baseX-1
                                posY=baseY+1
                                if(robotX>posX):
                                        i-=1  
                                        return 4
                                if(robotY<posY):
                                        i-=1  
                                        return 3
                        elif roboid == 4:  #se
                                robotX, robotY = robot.GetPosition()
                                posX=baseX+1
                                posY=baseY+1
                                if(robotX<posX):
                                        i-=1  
                                        return 2
                                if(robotY<posY):
                                        i-=1  
                                        return 3
                        elif roboid == 5:  #n
                                robotX, robotY = robot.GetPosition()
                                posX=baseX
                                posY=baseY-1
                                if(robotX>posX):
                                        i-=1  
                                        return 4
                                if(robotY>posY):
                                        i-=1  
                                        return 1
                        elif roboid == 6:  #s
                                robotX, robotY = robot.GetPosition()
                                posX=baseX
                                posY=baseY+1
                                if(robotX<posX):
                                        i-=1  
                                        return 2
                                if(robotY>posY):
                                        i-=1  
                                        return 1
                        elif roboid == 7:  #w
                                robotX, robotY = robot.GetPosition()
                                posX=baseX-1
                                posY=baseY
                                if(robotX>posX):
                                        i-=1  
                                        return 4
                                if(robotY<posY):
                                        i-=1  
                                        return 3
                        elif roboid == 8:  #e
                                robotX, robotY = robot.GetPosition()
                                posX=baseX+1
                                posY=baseY
                                if(robotX<posX):
                                        i-=1  
                                        return 2
                                if(robotY<posY):
                                        i-=1  
                                        return 3
                        i-=1
                        return 0
                        
                else:
                        #Rotation
                        deltaX = robotX - baseX
                        deltaY = robotY - baseY
                        delta = (deltaX, deltaY)

                        if delta == (0, -1):
                                return 2
                        elif delta == (1, -1):
                                return 3
                        elif delta == (1, 0):
                                return 3
                        elif delta == (1, 1):
                                return 4
                        elif delta == (0, 1):
                                return 4
                        elif delta == (-1, 1):
                                return 1
                        elif delta == (-1, 0):
                                return 1
                        elif delta == (-1, -1):
                                return 2


        #OriginMirror
        elif roboid > 19 and roboid < 24:
                posX = X - baseX
                posY = Y - baseY
                global originMirrorPosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm)) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not originMirrorPosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        originMirrorPosAssumed = True                          
                else:            
                    return randint(1,4)

        #XMirror
        elif (roboid > 23 and roboid < 26) or (10 <= roboid and roboid <= 12) :
                posX = baseX
                posY = Y - baseY
                global xMirrorPosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm)) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not xMirrorPosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        xMirrorPosAssumed = True                          
                else:            
                    return randint(1,4)

        #YMirror
        elif (roboid > 25 and roboid < 28) or (13 <= roboid and roboid <= 15):
                posX = X - baseX
                posY = baseY
                global yMirrorPosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm)) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not yMirrorPosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        yMirrorPosAssumed = True                          
                else:            
                    return randint(1,4)
        
        #diagonal1mirror
        elif (roboid > 27 and roboid < 30) or roboid in [16, 17]:
                posY = (2*X*Y*baseX + Y*Y*baseY - X*X*baseY) // (X*X + Y*Y)
                posX = (2*X*Y*baseY + X*X*baseX - Y*Y*baseX) // (X*X + Y*Y)
                global diagonal1PosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm)) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not diagonal1PosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        diagonal1PosAssumed = True                          
                else:            
                    return randint(1,4)
        
        #diagonal2mirror
        elif (roboid > 29 and roboid < 32) or roboid in [18, 19]:
                posX = (baseX*X*X + 2*X*Y*Y - baseX*Y*Y - 2*baseY*X*Y) // (X*X + Y*Y)
                posY = (baseY*Y*Y + 2*Y*X*X - baseY*X*X - 2*baseX*X*Y) // (X*X + Y*Y)
                global diagonal2PosAssumed
                
                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))           
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm)) 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':  
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw
                if p_nw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        robot.DeployVirus(min(lm , robot.GetVirus()*fm))
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0

                if not diagonal2PosAssumed:
                    if robotX > posX:
                        return 4
                    elif robotX < posX:
                        return 2
                    elif robotY > posY:
                        return 1
                    elif robotY < posY:
                        return 3
                    else:
                        diagonal2PosAssumed = True                          
                else:            
                    return randint(1,4)
        

        #scouters
        elif roboid == 32:
                if baseX < X//2:
                        if(robotX >= baseX):
                                return 4
                else:
                        if(robotX <= baseX):
                                return 2

                if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

                # scan n
                if p_n == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3     
                elif p_n == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)
                        robot.setSignal('eb' + x + y)
                        return 0        
                        
                # scan s
                if p_s == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3 
                elif p_s == 'enemy-base':
                        x = str(robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                  
                        robot.setSignal('eb' + x + y)
                        return 0         

                # scan e
                if p_e == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3
                elif p_e == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan w
                if p_w == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3
                elif p_w == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(robotY).zfill(2)                
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan ne
                if p_ne == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3
                elif p_ne == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan se
                if p_se == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3
                elif p_se == 'enemy-base':
                        x = str(1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan nw #
                if p_nw == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3
                elif p_nw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(-1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                
                # scan sw
                if p_sw == 'enemy':
                        robot.DeployVirus(min(ls, robot.GetVirus()*fs))       
                        return 3
                elif p_sw == 'enemy-base':
                        x = str(-1 + robotX).zfill(2)
                        y = str(1 + robotY).zfill(2)                 
                        robot.setSignal('eb' + x + y)
                        return 0
                        
                return randint(1,4)
        else:
            global k
            scout2X, scout3X, scout4X = None, None, None
            if baseX < X//2:
                scout2X = baseX - 1
                scout3X = baseX - 2
                scout4X = baseX - 3
            else:
                scout2X = baseX + 1
                scout3X = baseX + 2
                scout4X = baseX + 3
                
            if "enemy-base" in p_list:
                        robot.DeployVirus(robot.GetVirus())

            # scan n
            if p_n == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                            robot.DeployVirus(500)           
            elif p_n == 'enemy-base':
                    x = str(robotX).zfill(2)
                    y = str(-1 + robotY).zfill(2)
                    robot.setSignal('eb' + x + y)
                    return 0        
                        
            # scan s
            if p_s == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500) 
            elif p_s == 'enemy-base':
                    x = str(robotX).zfill(2)
                    y = str(1 + robotY).zfill(2)                  
                    robot.setSignal('eb' + x + y)
                    return 0         

            # scan e
            if p_e == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_e == 'enemy-base':
                    x = str(1 + robotX).zfill(2)
                    y = str(robotY).zfill(2)                
                    robot.setSignal('eb' + x + y)
                    return 0
                
            # scan w
            if p_w == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_w == 'enemy-base':
                    x = str(-1 + robotX).zfill(2)
                    y = str(robotY).zfill(2)                
                    robot.setSignal('eb' + x + y)
                    return 0
                
            # scan ne
            if p_ne == 'enemy':  
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_ne == 'enemy-base':
                    x = str(1 + robotX).zfill(2)
                    y = str(-1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
            
            # scan se
            if p_se == 'enemy':
                    if(robot.GetVirus()>800):
                        robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_se == 'enemy-base':
                    x = str(1 + robotX).zfill(2)
                    y = str(1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
                
            # scan nw
            if p_nw == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_nw == 'enemy-base':
                    x = str(-1 + robotX).zfill(2)
                    y = str(-1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
            
            # scan sw
            if p_sw == 'enemy':
                    if(robot.GetVirus()>800):
                         robot.DeployVirus(800)
                    else:
                        robot.DeployVirus(500)
            elif p_sw == 'enemy-base':
                    x = str(-1 + robotX).zfill(2)
                    y = str(1 + robotY).zfill(2)                 
                    robot.setSignal('eb' + x + y)
                    return 0
            if baseX < X//2:
                if k > 0:
                        if roboid == 33:
                                if(robotX > scout2X):
                                        k-=1
                                        return 4
                                else:
                                        k-=1
                                        return 0
                        elif roboid == 34:
                                if(robotX > scout3X):
                                        k-=1
                                        return 4
                                else:
                                        k-=1
                                        return 0
                        elif roboid == 9:
                                if(robotX > scout4X):
                                        k-=1
                                        return 4
                                else:
                                        k-=1
                                        return 0
                else:
                        if roboid == 33:
                                if robotX == scout2X and not robotY == 2 :
                                        return 1
                                elif robotY == 2 and not robotX == 2 :
                                        return 4
                                elif robotX == 2 and not robotY == Y-2 :
                                        return 3
                                elif robotY == Y-2 and not robotX == scout2X :
                                        return 2
                        elif roboid == 34:
                                if robotX == scout3X and not robotY == 3 :
                                        return 1
                                elif robotY == 3 and not robotX == 3 :
                                        return 4
                                elif robotX == 3 and not robotY == Y-3 :
                                        return 3
                                elif robotY == Y-3 and not robotX == scout3X :
                                        return 2
                        elif roboid == 9:
                                if robotX == scout4X and not robotY == 4 :
                                        return 1
                                elif robotY == 4 and not robotX == 4 :
                                        return 4
                                elif robotX == 4 and not robotY == Y-4 :
                                        return 3
                                elif robotY == Y-4 and not robotX == scout4X :
                                        return 2
            else:
                if k > 0:
                        if roboid == 33:
                                if(robotX < scout2X):
                                        k-=1
                                        return 2
                                else:
                                        k-=1
                                        return 0
                        elif roboid == 34:
                                if(robotX < scout3X):
                                        k-=1
                                        return 2
                                else:
                                        k-=1
                                        return 0
                        elif roboid == 9:
                                if(robotX < scout4X):
                                        k-=1
                                        return 2
                                else:
                                        k-=1
                                        return 0
                else:
                        if roboid == 33:
                                if robotX == scout2X and not robotY == 2 :
                                        return 1
                                elif robotY == 2 and not robotX == X-2 :
                                        return 2
                                elif robotX == X-2 and not robotY == Y-2 :
                                        return 3
                                elif robotY == Y-2 and not robotX == scout2X :
                                        return 4
                        elif roboid == 34:
                                if robotX == scout3X and not robotY == 3 :
                                        return 1
                                elif robotY == 3 and not robotX == X-3 :
                                        return 2
                                elif robotX == X-3 and not robotY == Y-3 :
                                        return 3
                                elif robotY == Y-3 and not robotX == scout3X :
                                        return 4
                        elif roboid == 9:
                                if robotX == scout4X and not robotY == 4 :
                                        return 1
                                elif robotY == 4 and not robotX == X-4 :
                                        return 2
                                elif robotX == X-4 and not robotY == Y-4 :
                                        return 3
                                elif robotY == Y-4 and not robotX == scout4X :
                                        return 4       

        
        return randint(1,4)

def ActBase(base):
        
        global baseX
        global baseY
        global robo_list
        baseX, baseY = base.GetPosition()

        los = base.GetListOfSignals()
        for id in range(1, 14):
                if ("id=" + str(id).zfill(2)) not in los:
                        line_robo_alive[id-1] = False
        
        for l in los:
                if not base.GetYourSignal()[:2] == 'eb':
                        if len(l) == 6:
                                base.SetYourSignal(l)
                                break
                        elif len(l) == 10:
                                base.SetYourSignal(l)
                                break
                        else:
                                base.SetYourSignal('')    
        
        # create robots with unique IDs
        
        #scan nbh
        p_n = base.investigate_up()
        p_ne = base.investigate_ne()
        p_e = base.investigate_right()
        p_se = base.investigate_se()
        p_s = base.investigate_down()
        p_sw = base.investigate_sw()
        p_w = base.investigate_left()
        p_nw = base.investigate_nw()
        p_list = [p_n, p_ne, p_e, p_se, p_s, p_sw, p_w, p_nw]
                                      
        
        while base.GetElixir() > 300:
                new_sig = cr_robo_sig()  
                base.create_robot(new_sig)

        return
