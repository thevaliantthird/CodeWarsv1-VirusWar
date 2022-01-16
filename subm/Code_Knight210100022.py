from random import randint


def ActRobot(robot):
    up = robot.investigate_up()
    down = robot.investigate_down()
    left = robot.investigate_left()
    right = robot.investigate_right()
    ne = robot.investigate_ne()
    nw = robot.investigate_nw()
    se = robot.investigate_se()
    sw = robot.investigate_sw()
    if up == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if down == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if left == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if right == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if ne == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if nw == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if se == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    if sw == "enemy" and robot.GetVirus() > 700:
        robot.DeployVirus(100)
    init_signal = robot.GetInitialSignal()
    if init_signal.find('defender')!=-1:
        base_x = int(init_signal[8:10])
        base_y = int(init_signal[10:])
        x,y = robot.GetPosition()
        if x > base_x:
            return 4        
        if x < base_x:
            return 2
        if y > base_y:
            return 1        
        if y < base_y:
            return 3                                
        if x == base_x and y == base_y:
            return randint(1,4) 
    elif init_signal.find('attacker')!=-1:
        base_x = int(init_signal[8:10])
        base_y = int(init_signal[10:])
        x,y = robot.GetPosition()
        if up == "enemy-base":
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
            return 0
        if down == "enemy-base":
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
            return 0
        if left == "enemy-base":
            if x-1 < 10:
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
            return 0
        if right == "enemy-base":
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
            return 0
        if ne == "enemy-base":
            if robot.GetVirus() > 500:
                robot.DeployVirus(500)
            return 0
        if nw == "enemy-base":
            if robot.GetVirus() > 500:
                robot.DeployVirus(500)
            return 0
        if se == "enemy-base":
            if robot.GetVirus() > 500:
                robot.DeployVirus(500)
            return 0
        if sw == "enemy-base":
            if robot.GetVirus() > 500:
                robot.DeployVirus(500)
            return 0
        if init_signal.find('attacker')==-1 and init_signal.find('defender')==-1:
            s = robot.GetCurrentBaseSignal()[4:]
            sx = int(s[0:2])
            sy = int(s[2:4])
            dist = abs(sx-x) + abs(sy-y)
            if dist==1:
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
            if x < sx:
                return 2
            if x > sx:
                return 4
            if y < sy :
                return 3
            if y > sy:
                return 1
        else:
            return randint(1,4)
    else:
        return randint(1,4)


def ActBase(base):
    if base.GetElixir() > 500:
        p = randint(0,5)
        if p != 0:
            x,y = base.GetPosition()    
            msg_x = str(x)
            msg_y = str(y)
            if x < 10:
                msg_x = '0' + msg_x
            if y < 10:
                msg_y = '0' + msg_y 
            base.create_robot('attacker'+msg_x+msg_y)
        else :
            x,y = base.GetPosition()    
            msg_x = str(x)
            msg_y = str(y)
            if x < 10:
                msg_x = '0' + msg_x
            if y < 10:
                msg_y = '0' + msg_y        
            base.create_robot('defender' + msg_x + msg_y)   
    L = base.GetListOfSignals()
    for l in L:
        if l.find('attacker')==-1 and l.find('defender')==-1:
            base.SetYourSignal(l)        
    return