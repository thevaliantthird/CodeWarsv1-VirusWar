from random import randint


def ActRobot(robot):
        xr,yr=robot.GetPosition()
        xc= robot.GetDimensionX()/2-1
        yc= robot.GetDimensionX()/2-1    
        if xr==2*xc+1 or xr==0 or yr==2*yc+1 or yr==0 :
            return randint(1,4)
        L= robot.investigate_up()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
        L= robot.investigate_down()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
        L= robot.investigate_nw()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
        L= robot.investigate_ne()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
        
        L= robot.investigate_sw()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
       
        L= robot.investigate_se()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
        
        L= robot.investigate_left()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())
        L= robot.investigate_right()
        if L=='enemy':
            if(robot.GetVirus()>10000):
                robot.DeployVirus(robot.GetVirus()*0.2)
            elif(robot.GetVirus()>5000):
                robot.DeployVirus(500)
            elif(robot.GetVirus()>1000):
                robot.DeployVirus(100)
        if L=='enemy-base':
            if(robot.GetVirus()<1000):
                robot.DeployVirus(robot.GetVirus()*0.9)
            elif(robot.GetVirus()>=1000):
                robot.DeployVirus(robot.GetVirus())      
        if len(robot.GetInitialSignal())==8:
           s=robot.GetInitialSignal()[4:]
           xb=int(s[0:2])
           yb=int(s[2:4])
           if xb-xc<0 and yb-yc==0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
               L= robot.investigate_right()
               if L=='enemy-base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                        robot.DeployVirus(robot.GetVirus())
               return 2
           elif xb-xc>0 and yb-yc==0 and xr!=2*xc+1 and xr!= 0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_left()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                elif(robot.GetVirus()>=1000):
                    robot.DeployVirus(robot.GetVirus())
                return 4 
           elif xb-xc<0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_se()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                        robot.DeployVirus(robot.GetVirus())
                return 2
           elif xb-xc>0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_sw()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 4
           elif xb-xc>0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_nw()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return (4,1)
           elif xb-xc<0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0 :
                L= robot.investigate_ne() 
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return (2,1)
           elif xb-xc == 0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_up()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 1
           elif xb-xc ==0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_down()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 3
           elif xr==2*xc+1 or xr==0 or yr==2*yc+1 or yr==0 :
                 return randint(1,4)
        elif len(robot.GetInitialSignal())==9:
            s=robot.GetInitialSignal()[5:]
            xb=int(s[0:2])
            yb=int(s[2:4])   
            if xb-xc<0 and yb-yc==0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_right()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 2
            elif xb-xc>0 and yb-yc==0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_left()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 4
            elif xb-xc == 0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_up()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 1
            elif xb-xc ==0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_down()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 3
            elif xb-xc<0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0 :
                L= robot.investigate_right()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 2
            elif xb-xc>0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_left()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 4
            elif xb-xc>0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_left()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 4
            elif xb-xc<0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0 :
                L= robot.investigate_right()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 2
            elif xr==2*xc+1 or xr==0 or yr==2*yc+1 or yr==0 :
                 return randint(1,4)
        elif len(robot.GetInitialSignal())==10 :
            s=robot.GetInitialSignal()[6:]
            xb=int(s[0:2])
            yb=int(s[2:4])
            if xb-xc<0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0: 
                L= robot.investigate_down()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 3
            elif xb-xc>0 and yb-yc<0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0 :
                L= robot.investigate_down()
                if L=='enemy_base' :
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 3

            elif xb-xc>0 and yb-yc>0  and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0:
                L= robot.investigate_up()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 1
            elif xb-xc<0 and yb-yc>0 and xr!=2*xc+1 and xr!=0 and yr!=2*yc+1 and yr!=0 :
                L= robot.investigate_up()
                if L=='enemy_base':
                    if(robot.GetVirus()<1000):
                        robot.DeployVirus(robot.GetVirus()*0.9)
                    elif(robot.GetVirus()>=1000):
                         robot.DeployVirus(robot.GetVirus())
                return 1
            elif xr==(2*xc+1 or 0) or yr==(2*yc+1 or 0) :
                 return randint(1,4)
        if len(robot.GetCurrentBaseSignal()) > 0:
            s = robot.GetCurrentBaseSignal()[4:]
            sx = int(s[0:2])
            sy = int(s[2:4])
            dist = abs(sx-xr) + abs(sy-yr)
            if dist==1:
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
            if xr < sx:
                return 2
            if xr > sx:
                return 4
            if yr < sy :
                return 3
            if yr > sy:
                return 1
        else :   
            return randint(1,4)
           


def ActBase(base):
        x,y= base.GetPosition()
        if x < 10:
            msg_x = '0' + str(x)
        else: 
            msg_x = str(x)
        if y< 10:
            msg_y = '0' + str(y)
        else:
            msg_y = str(y)
        msg = "base" + msg_x + msg_y
        msg1= "basea"+ msg_x+msg_y
        msg2="baseaa"+ msg_x+msg_y
        if base.GetElixir() > 500:
            if base.GetElixir() > 800:
                 base.create_robot('')
            if  base.GetVirus()>=800:
                 base.create_robot(msg)
            if base.GetVirus()>=800 :
                 base.create_robot(msg1)       
                 base.create_robot(msg2)
        L= base.investigate_up()
        if L=='enemy':
           if(base.GetVirus()>5000):
                base.DeployVirus(2000)
           else:
                base.DeployVirus(base.GetVirus()*0.8)
        L= base.investigate_down()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.8)
        L= base.investigate_nw()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.75)
        L= base.investigate_ne()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.75)
        L= base.investigate_sw()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.75)
        L= base.investigate_se()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.75)
        L= base.investigate_left()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.8)
        L= base.investigate_right()
        if L=='enemy':
            if(base.GetVirus()>5000):
                base.DeployVirus(2000)
            else:
                base.DeployVirus(base.GetVirus()*0.8)