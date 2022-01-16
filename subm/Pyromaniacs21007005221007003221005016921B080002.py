from random import randint

def roboAttack(robot,sigr):
        position = [0,0,0,0,0,0,0,0]
        a = 1000
        x,y = robot.GetPosition()
                        
        while robot.GetVirus() > a and robot.investigate_up() == "enemy":
                robot.DeployVirus(400)
        up = robot.investigate_up()
        if up == "enemy":        
                position[0] = 1

        while robot.GetVirus() > a and robot.investigate_down() == "enemy":
                robot.DeployVirus(400)
        down =robot.investigate_down()
        if down == "enemy":        
                position[4] = 1

        while robot.GetVirus() > a and robot.investigate_left() == "enemy":
                robot.DeployVirus(400)
        left = robot.investigate_left()
        if left == "enemy":        
                position[6] = 1

        while robot.GetVirus() > a and robot.investigate_right() == "enemy":
                robot.DeployVirus(400)
        right = robot.investigate_right()
        if right == "enemy":        
                position[2] = 1

        while robot.GetVirus() > a and robot.investigate_nw() == "enemy":
                robot.DeployVirus(400)
        nw = robot.investigate_nw()
        if nw == "enemy":        
                position[7] = 1

        while robot.GetVirus() > a and robot.investigate_ne() == "enemy":
                robot.DeployVirus(400)
        ne = robot.investigate_ne()
        if ne == "enemy":        
                position[1] = 1

        while robot.GetVirus() > a and robot.investigate_sw() == "enemy":
                robot.DeployVirus(400)
        sw = robot.investigate_sw() 
        if sw == "enemy":        
                position[5] = 1

        while robot.GetVirus() > a and robot.investigate_se() == "enemy":
                robot.DeployVirus(400)
        se = robot.investigate_se()
        if se == "enemy":        
                position[3] = 1

        d = robot.GetVirus()
        if up == "enemy-base":
                robot.DeployVirus(d)
                position[0] = 1
                if x < 10:
                        msg_x = '0' + str(x)
                else:
                        msg_x = str(x)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg)
                ##print(robot.GetYourSignal())
                
        elif down == "enemy-base":
                robot.DeployVirus(d)
                position[4] = 1
                if x < 10:
                        msg_x = '0' + str(x)
                else:
                        msg_x = str(x)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg)
                ##print(robot.GetYourSignal())

        elif left == "enemy-base":        
                robot.DeployVirus(d)
                position[6] = 1
                if x - 1 < 10:
                        msg_x = '0' + str(x-1)
                else:
                        msg_x = str(x-1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg)
                ##print(robot.GetYourSignal()) 

        elif right == "enemy-base":
                robot.DeployVirus(d)
                position[2] = 1
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else:
                        msg_x = str(x+1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg)
                ##print(robot.GetYourSignal()) 

        elif nw == "enemy-base":
                robot.DeployVirus(d)
                position[7] = 1
                if x-1 < 10:
                        msg_x = '0' + str(x-1)
                else:
                        msg_x = str(x-1)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg) 
                ##print(robot.GetYourSignal())

        elif ne == "enemy-base":
                robot.DeployVirus(d)
                position[1] = 1
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else:
                        msg_x = str(x+1)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg) 
                ##print(robot.GetYourSignal())

        elif sw == "enemy-base":
                robot.DeployVirus(d)
                position[5] = 1
                if x-1 < 10:
                        msg_x = '0' + str(x-1)
                else:
                        msg_x = str(x-1)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg) 
                ##print(robot.GetYourSignal())

        elif se == "enemy-base":
                robot.DeployVirus(d)
                position[3] = 1
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else:
                        msg_x = str(x+1)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg = msg_x + msg_y
                robot.setSignal(sigr + msg) 
                ##print(robot.GetYourSignal())

        if position[0] == 1:
                if position[4] == 0:
                        return 3
                elif position[4] == 1:
                        L=[1,3]
                        return L[randint(0,1)]

        elif position[2] == 1:
                if position[6] == 0:
                        return 4
                elif position[6] == 1:
                        L=[2,4]
                        return L[randint(0,1)]

        elif position[4] == 1:
                if position[0] == 0:
                        return 1
                elif position[0] == 1:
                        L=[1,3]
                        return L[randint(0,1)]

        elif position[6] == 1:
                if position[2] == 0:
                        return 2
                elif position[2] == 1:
                        L=[2,4]
                        return L[randint(0,1)]

        elif position[1] == 1:
                if position[4] == 0 and position[6] == 0:
                        return randint(3,4)
                elif position[4] == 0 and position[6] == 1:
                        return 4
                elif position[4] == 1 and position[6] == 0:
                        return 3
                else:
                        return randint(3,4)
                
        elif position[3] == 1:
                L = (1,4)
                if position[0] == 0 and position[6] == 0:
                        return L[randint(0,1)]
                elif position[0] == 0 and position[6] == 1:
                        return 4
                elif position[0] == 1 and position[6] == 0:
                        return 1
                else:
                        return L[randint(0,1)]

        elif position[5] == 1:
                if position[0] == 0 and position[2] == 0:
                        return randint(1,2)
                elif position[0] == 0 and position[2] == 1:
                        return 2
                elif position[0] == 1 and position[2] == 0:
                        return 1
                else:
                        return randint(1,2)        

        elif position[7] == 1:
                if position[4] == 0 and position[2] == 0:
                        return randint(2,3)
                elif position[4] == 0 and position[2] == 1:
                        return 2
                elif position[4] == 1 and position[2] == 0:
                        return 3
                else:
                        return randint(2,3)
        else:
                return 5

def moveDefault(xmin,xmax,ymin,ymax,robot,sigr):
    r = randint(1,4)
    
    if (r == 2 or r == 4):
        if (xmin >= robot.GetPosition()[0]):
                return 2,sigr
        elif (xmax <= robot.GetPosition()[0]):
                return 4,sigr
        else:
                s = sigr[:4] + '1' + sigr[5:]
                if sigr[0] == 'e':
                        r = 0
                return (r,s)
    else:
            if (ymax <= robot.GetPosition()[1]):
                    return 1,sigr
            elif (ymin >= robot.GetPosition()[1]):
                    return 3,sigr
            else:
                    s = sigr[:5] + '1' + sigr[6]
                    if sigr[0] == 'e':
                        r = 0
                    return (r,s)    

def ActRobot(robot):
        if robot.GetYourSignal() == '':
                robot.setSignal(robot.GetInitialSignal()+'000')
        sig = robot.GetCurrentBaseSignal()
        sigr = robot.GetYourSignal()
        
        #robot no. is in the first two chars of sigr

        n = roboAttack(robot,sigr)
        if (n != 5):
                return n
        
        if(sigr[0] == 'b'):
                n,s = moveDefault(int(sigr[1:3]),int(sigr[3:5]),int(sigr[5:7]),int(sigr[7:9]),robot,sigr)
                return n
        
        n = int(robot.GetInitialSignal()[:2]) 
        groupn = n//5

        ##print(sig)
        if(sig[0] =='e'):
                x = int(sig[1:3]);y = int(sig[3:5])
                n,s = moveDefault(x,x,y,y,robot,sigr)
                return n


        else :
                T = sig[3*groupn+2]           
                        
                x = int(sig[3*groupn])
                y = int(sig[3*groupn+1])
                xmin = 10*x
                ymin = 10*y
                xmax = 10*x +9
                ymax = 10*y +9
                n,s = moveDefault(xmin,xmax,ymin,ymax,robot,sigr)
                ###print(xmax,xmin)
                
                if(T != sigr[6]):
                        robot.setSignal(sigr[:4] + '00' + T)
                else:
                        robot.setSignal(s)
                return n
                
def baseSense(base):
        up = base.investigate_up()
        down = base.investigate_down()
        left = base.investigate_left()
        right = base.investigate_right()
        nw = base.investigate_nw()
        ne = base.investigate_ne()
        sw = base.investigate_sw()
        se = base.investigate_se()
        a = 100
        f = 1
        
        while base.GetVirus() > a and up == "enemy":
                base.DeployVirus(100)
                up = base.investigate_up()
                #print(base.GetVirus())
                f = 0

        while base.GetVirus() > a and down == "enemy":
                base.DeployVirus(100)
                down = base.investigate_down()
                #print(base.GetVirus())
                f = 0

        while base.GetVirus() > a and left == "enemy":
                base.DeployVirus(100)
                left = base.investigate_left()
                #print(base.GetVirus())
                f = 0
        
        while base.GetVirus() > a and right == "enemy":
                base.DeployVirus(100)
                right = base.investigate_right()
                #print(base.GetVirus())
                f = 0

        while base.GetVirus() > a and nw == "enemy":
                base.DeployVirus(100)
                nw = base.investigate_nw()
                #print(base.GetVirus())
                f = 0

        while base.GetVirus() > a and ne == "enemy":
                base.DeployVirus(100)
                ne = base.investigate_ne()
                #print(base.GetVirus())
                f = 0

        while base.GetVirus() > a and sw == "enemy":
                base.DeployVirus(100)
                sw = base.investigate_sw()
                #print(base.GetVirus())
                f = 0

        while base.GetVirus() > a and se == "enemy":
                base.DeployVirus(100)
                se = base.investigate_se()
                #print(base.GetVirus())
                f = 0

        return f

def ActBase(base):
        basesig = base.GetYourSignal()

        a = baseSense(base)
        if(a==0):
               basesig = basesig[:15] + 'b' + basesig[16:]
        
        x = base.GetDimensionX()
        if x%10 ==0 or x%10 ==1:
                x = base.GetDimensionX()//10
        else :
                x = -(base.GetDimensionX()//-10)
        x-=1

        y = base.GetDimensionY()
        if y%10 ==0 or y%10 ==1:
                y = base.GetDimensionY()//10
        else :
                y = -(base.GetDimensionX()//-10)
        y-=1

        if basesig == '':
                baseX,baseY = base.GetPosition()      
                basex = baseX//10; basey = baseY//10
                
                for i in range(0,10):
                        s = 'b'
                        L = [0,0,0,0]
                        if (baseX<3):
                                s += '0003'
                        else:
                                L[0] = int(baseX) - 1; L[1] = int(baseX) + 1                          
                        if (baseY<3):
                                s += '0005'
                        else:
                                L[2] = int(baseY) - 1; L[3] = int(baseY) + 1  

                        for i in L:
                                if i < 10:
                                        k = '0' + str(i)
                                else:
                                        k = str(i)
                                s = s + k
                        base.create_robot(s) 

                basesig = str(basey) + str(basex) + '0'
                for i in range(0,5):
                        base.create_robot('0'+ str(i)+basesig[0:2])        
                basesig = basesig + str(x - basex) + str(y - basey) + '0'
                for i in range(5,10):
                        base.create_robot('0' + str(i)+basesig[3:5])
                basesig = basesig + str(x-basex) + str(basey) + '0'
                for i in range(10,15):
                        base.create_robot(str(i)+basesig[6:8])
                basesig = basesig + str(basex) + str(y-basey) + '0'
                for i in range(15,20):
                        base.create_robot(str(i)+basesig[9:11])        
                basesig = basesig + str(x-basey) + str(y-basex) + '0'
                for i in range(20,25):
                        base.create_robot(str(i)+basesig[12:14])           
                 
                if baseX < 10:
                        BaseX = '0' + str(baseX)
                else:
                        BaseX = str(baseX)         
                if baseY < 10:
                        BaseY = '0' + str(baseY)
                else:
                        BaseY = str(baseY)

                base.SetYourSignal(basesig + '0' + BaseX + BaseY)

        else:
                List = base.GetListOfSignals()
                check = [0,0,0,0,0]
                for Str in List:
                        if(Str[0] != 'b'):
                                groupn = int(Str[:2])//5
                                if(Str[4:6] != '11' ):
                                        check[groupn] = 1
                        if(basesig[0] != 'e' and len(Str) == 11):
                                base.SetYourSignal('e'+Str[7:11]+basesig[5:])
                                basesig = base.GetYourSignal()
                
                if(basesig[0] == 'e'):
                        check[0] = 1;check[1] = 1; check[2] = 1

                if (basesig[15] == 'b'):
                        check[3] = 1; check[4] = 1

                for i in range(0,5):
                        if check[i] == 0:
                                T = basesig[3*i+2]
                                basesig = basesig[0:3*i+2]+str((int(T)+1)%2) +basesig[3*i +3:]
                                dir = randint(1,4)
                                while True:
                                        if(dir == 1):
                                                T = basesig[3*i+1]
                                                if(T == '0'):
                                                        dir = 3
                                                else:
                                                        basesig = basesig[0:3*i+1]+str(int(T)-1) +basesig[3*i +2:]
                                                        break
                                        if(dir == 2):
                                                S = basesig[3*i]
                                                if(S == str(x)):
                                                        dir = 4
                                                else:
                                                        basesig = basesig[0:3*i]+str(int(S)+1) +basesig[3*i +1:]                                                        
                                                        break
                                        if(dir == 3):
                                                T = basesig[3*i+1]
                                                if(T == str(y)):
                                                        dir = 1
                                                else:
                                                        basesig = basesig[0:3*i+1]+str(int(T)+1) +basesig[3*i +2:]
                                                        break
                                        if(dir == 4):
                                                T = basesig[3*i]
                                                if(T == '0'):
                                                        dir = 2
                                                else:
                                                        basesig = basesig[0:3*i]+str(int(T)-1) +basesig[3*i +1:]
                                                        break
                base.SetYourSignal(basesig)
        return