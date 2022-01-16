import random
from random import randint,choice

        # almost final
        
def ActRobot(robot):
                
                p,q = robot.GetPosition()
                
                up = robot.investigate_up()
                down = robot.investigate_down()
                left = robot.investigate_left()
                right = robot.investigate_right()
                ne = robot.investigate_ne()
                nw = robot.investigate_nw()
                se = robot.investigate_se()
                sw = robot.investigate_sw()
                x,y = robot.GetPosition()
                robot.setSignal('')

                if up == "enemy-base":
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_x = '0' + str(x)
                        else: 
                                msg_x = str(x)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                        
                elif down == "enemy-base":
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_x = '0' + str(x)
                        else: 
                                msg_x = str(x)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                elif left == "enemy-base":
                        x,y = robot.GetPosition()
                        if x - 1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                
                elif right == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())

                elif ne == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())

                elif nw == "enemy-base":
                        x,y = robot.GetPosition()
                        if x-1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y-1< 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())

                elif se == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y+1< 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())

                elif sw == "enemy-base" :
                        x,y = robot.GetPosition()
                        if x - 1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                                msg = "base" + msg_x + msg_y
                                robot.setSignal(msg)
                                robot.DeployVirus(robot.GetVirus())

                elif up == "enemy" :
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_x = '0' + str(x)
                        else: 
                                msg_x = str(x)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)
                
                elif down == "enemy" :
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_x = '0' + str(x)
                        else: 
                                msg_x = str(x)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)
                
                elif left == "enemy" :
                        x,y = robot.GetPosition()
                        if x - 1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)
                elif right == "enemy" :
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)
                elif ne == "enemy" :
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)

                elif nw == "enemy" :
                        x,y = robot.GetPosition()
                        if x-1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y-1< 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)

                elif se == "enemy" :
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y+1< 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "robo" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 6000:                               
                            robot.DeployVirus(3000)
                        

                elif sw == "enemy" :
                        x,y = robot.GetPosition()
                        if x - 1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                                msg = "robo" + msg_x + msg_y
                                robot.setSignal(msg)
                                if robot.GetVirus() > 6000:                               
                                    robot.DeployVirus(3000)
                        
                if len(robot.GetCurrentBaseSignal()) > 0 :
                        signal = robot.GetCurrentBaseSignal()

                        if signal[0:4] == "base":
                            s = robot.GetCurrentBaseSignal()[4:]
                            sx = int(s[0:2])
                            sy = int(s[2:4])
                            dist = abs(sx-x) + abs(sy-y)
                        if dist==1:
                                robot.DeployVirus(robot.GetVirus()*1.00)
                                return 0
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy :
                                return 3
                        if y > sy:
                                return 1
                        else :
                            move_bias = signal[4:6]
                        if move_bias == "up" :
                                return(choice([1,2,4]))
                        if move_bias == "rt":
                                return(choice([1,2,3]))
                        if move_bias == "dn":
                                return(choice([2,3,4]))
                        if move_bias == "lt":
                                return(choice([1,3,4]))    



                else:
                        
                        
                        return randint(1,4)

def ActBase(base):
            numberofright = 0   
            numberofleft = 0
            numberofup = 0
            numberofdown = 0
            
                                                                            
            r,s = base.GetPosition()

            if base.GetElixir() > 50:
                    base.create_robot('')
            L = base.GetListOfSignals()
            for l in L:
                    if len(l) > 0:

                            if l[0:4] == "base":
                                base.SetYourSignal(l)

                            elif l[0:4] == "enem":
                                xe = int(l[4:6])
                                ye = int(l[6:8])

                                if abs(xe - r) < 4 and ye > s:
                                        numberofdown += 1
                                elif abs(xe - r) < 4 and ye < s:
                                        numberofup += 1
                                elif abs(ye - s) < 4 and xe < r:
                                        numberofleft += 1
                                elif abs(ye - s) < 4 and xe > r:
                                        numberofright += 1
                                elif xe>r and ye>s: 
                                        numberofright += 0.5
                                        numberofdown += 0.5
                                elif xe>r and ye<s:
                                        numberofright +=0.5
                                        numberofup+=0.5
                                elif xe<r and ye>s:
                                        numberofleft+=0.5
                                        numberofdown+=0.5
                                elif xe<r and ye<s:
                                        numberofleft+=0.5
                                        numberofup+=0.5
                            

                    

            bias_exec = [1,2,3,4]
            if numberofup>=5 and 1 in bias_exec:
                    base.SetYourSignal("biasup")
                    bias_exec[1]=0
                    bias_exec[2]=0
                    bias_exec[3]=0
                    
            if numberofright>=5 and 2 in bias_exec:
                    base.SetYourSignal("bias" + "rt")
                    bias_exec[0]=0
                    bias_exec[2]=0
                    bias_exec[3]=0
            if numberofdown>=5 and 3 in bias_exec:
                    base.SetYourSignal("biasdn")
                    bias_exec[1]=0
                    bias_exec[0]=0
                    bias_exec[3]=0
            if numberofleft>=5 and 4 in bias_exec:
                    base.SetYourSignal("biaslt")
                    bias_exec[1]=0
                    bias_exec[2]=0
                    bias_exec[0]=0
                                   



        
                        
                

        