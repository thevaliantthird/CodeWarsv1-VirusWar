from random import randint


def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne=robot.investigate_ne()
        nw=robot.investigate_nw()
        sw=robot.investigate_sw()
        se=robot.investigate_se()
        x,y = robot.GetPosition()
        robot.setSignal('')
        b=robot.GetInitialSignal()
        
        
        if len(robot.GetInitialSignal())>4:
                xb=int(b[0:2])
                yb=int(b[2:4])
                #defense
                
                while robot.GetVirus()>500:
                        if(up=="enemy" or down=="enemy" or left=="enemy" or right=="enemy" or ne=="enemy" or nw=="enemy" or se=="enemy" or sw=="enemy" ):
                                robot.DeployVirus(120)
                        else:
                                break
                
                
                if up == "wall":
                        return 3
                
                if down == "wall":
                        return 1

                if right == "wall":
                        return 4

                if left == "wall":
                        return 2

                
                #movement
                if x>xb+4:
                        return 4
                elif x<xb-4:
                        return 2
                elif y>yb+4:
                        return 1
                elif y<yb-4:
                        return 3
                else:
                        return randint(1,5)
                
                
        #for others
        else:
                xb=int(b[0:2])
                yb=int(b[2:4])
                if up == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif up == "enemy-base":
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
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)
                elif up == "wall":
                        return 3
                
                if down == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif down == "enemy-base":
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
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)
                elif down == "wall":
                        return 1

                if left == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif left == "enemy-base":
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
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)
                elif left == "wall":
                        return 2
        
                if right == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
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
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)
                elif right == "wall":
                        return 4

                if ne == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif ne == "enemy-base":
                        if x + 1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)

                if nw == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif nw == "enemy-base":
                        if x-1< 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)

                
                if sw == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif sw == "enemy-base":
                        if x-1 < 10:
                                msg_x = '0' + str(x-1)
                        else: 
                                msg_x = str(x-1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)


                if se == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(100)
                elif se == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = '0' + str(x+1)
                        else: 
                                msg_x = str(x+1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                                robot.DeployVirus(500)

                
                if len(robot.GetCurrentBaseSignal()) > 0:
                        s = robot.GetCurrentBaseSignal()[4:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                        dist = (abs(x-sx) + abs(y-sy))
                        if dist==1:
                                robot.DeployVirus(robot.GetVirus()*0.75)
                                return 0
                        if x<sx:
                                return 2
                        if x>sx:
                                return 4
                        if y<sy:
                                return 3
                        if y>sy:
                                return 1
                
                xc,yc=robot.GetDimensionX(),robot.GetDimensionY()
                
                u=randint(1,11)
                num=0
                #1st quad bias
                if xb>6*xc/10 and yb<4*yc/10:
                        if u<=4:
                                num=3
                        elif u<=8:
                                num=4
                        elif u==9:
                                num=2
                        elif u==10:
                                num=1
                        return num
                #2nd quad bias
                elif xb<4*xc/10 and yb<4*yc/10:
                        if u<=4:
                                num=3
                        elif u<=8:
                                num=2
                        elif u==9:
                                num=4
                        elif u==10:
                                num=1
                        return num
                #3rd quad bias
                elif xb<4*xc/10 and yb>6*yc/10:
                        if u<=4:
                                num=1
                        elif u<=8:
                                num=2
                        elif u==9:
                                num=3
                        elif u==10:
                                num=4
                        return num
                #4th quad bias
                elif xb>6*xc/10 and yb>6*yc/10:
                        if u<=4:
                                num=1
                        elif u<=8:
                                num=4
                        elif u==9:
                                num=3
                        elif u==10:
                                num=2
                        return num
                #central area
                elif xb>=4*xc/10 and xb<=6*xc/10 and yb>=4*xc/10 and yb<=6*xc/10:
                        return randint(1,5)
                #intersection of 1,2
                elif xb>=4*xc/10 and xb<=6*xc/10 and yb<=4*yc/10:
                        if u<=5:
                                num=3
                        elif u<=7:
                                num=2
                        elif u<=9:
                                num=4
                        elif u==10:
                                num=1
                        return num
                #intersection of 2,3
                elif xb<=4*xc/10 and yb>=4*yc/10 and yb<=6*yc/10:
                        if u<=5:
                                num=2
                        elif u<=7:
                                num=3
                        elif u<=9:
                                num=1
                        elif u==10:
                                num=4
                        return num
                #intersection of 3,4
                elif xb<=6*xc/10 and xb>=4*xc/10 and yb>=6*yc/10:
                        if u<=5:
                                num=1
                        elif u<=7:
                                num=2
                        elif u<=9:
                                num=4
                        elif u==10:
                                num=3
                        return num
                #intersection of 4,1
                elif xb>=6*xc/10 and yb>=4*yc/10 and yb<=6*yc/10:
                        if u<=5:
                                num=4
                        elif u<=7:
                                num=1
                        elif u<=9:
                                num=3
                        elif u==10:
                                num=2
                        return num
                
#to get initial amount of elixir
l=[]
def check(h):
        elixir =h
        l.append(elixir)
        if len(l)>=2:
                l.pop(1)
        return l[0]

def ActBase(base):
    '''
    Add your code here
    
    '''
    xb,yb=base.GetPosition()
    basex=""
    basey=""
    if xb<10:
            basex="0"+str(xb)
    else:
            basex=str(xb)
    if yb<10:
            basey="0"+str(yb)
    else:
            basey=str(yb)
    elixir=check(base.GetElixir())
    if base.GetElixir() > elixir*1/2:
        base.create_robot(basex+basey)
    elif base.GetElixir()>elixir*1/4:
        base.create_robot(basex+basey+"def")
    
    
    #base defense
    up = base.investigate_up()
    down = base.investigate_down()
    left = base.investigate_left()
    right = base.investigate_right()
    ne=base.investigate_ne()
    nw=base.investigate_nw()
    sw=base.investigate_sw()
    se=base.investigate_se()
    
    while base.GetVirus()>500:
        if(up=="enemy" or down=="enemy" or left=="enemy" or right=="enemy" or ne=="enemy" or nw=="enemy" or se=="enemy" or sw=="enemy" and base.GetVirus()>500):
                base.DeployVirus(120)
        else:
                break
    

    L = base.GetListOfSignals()
    for l in L:
        if len(l) > 0:
                base.SetYourSignal(l)
                return