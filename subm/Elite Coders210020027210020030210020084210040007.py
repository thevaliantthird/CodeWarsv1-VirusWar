from random import randint


def ActRobot(robot):
        init_signal = robot.GetInitialSignal()
        if init_signal.find('defender') != -1:
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
                if x==base_x and y==base_y:
                        return randint(1,4)
                        
        up = robot.investigate_up()                 
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        nw = robot.investigate_nw()
        ne = robot. investigate_ne()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        if up == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
        elif up == "enemy-base":
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
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        if down == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
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
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        if left == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
        elif left == "enemy-base":
                x,y = robot.GetPosition()
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
        if right == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
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
        if nw == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
        elif nw == "enemy-base":
                x,y = robot.GetPosition()
                if x-1 < 10:
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
        if ne == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
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
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        if se == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
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
        if sw == "enemy" and robot.GetVirus() > 500:
                robot.DeployVirus(500)
        elif sw == "enemy-base":
                x,y = robot.GetPosition()
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
        if len(robot.GetCurrentBaseSignal()) > 0:
                s = robot.GetCurrentBaseSignal()[4:]
                sx = int(s[0:2])
                sy = int(s[2:4])
                dist = abs(sx-x) + abs(sy-y)
                if dist <= 1:
                        robot.DeployVirus(robot.GetVirus()*0.8)
                        return 0
                if x < sx:
                        return 2
                if x > sx:
                        return 4
                if y < sy:
                        return 3
                if y < sy:
                        return 1 
        else:
                return randint(1,4)

def ActBase(base):
    '''
    Add your code here
    
    '''
    if base.GetElixir()>500:
        p = randint(0,9)
        if p!=0:
                base.create_robot('attacker')
        else:
                x,y = base.GetPosition()
                msg_x = str(x)
                msg_y = str(y)
                if x < 10:
                        msg_x = '0' + msg_x
                if y < 10:
                        msg_y = '0' + msg_y
                base.create_robot('defender' + msg_x + msg_y)

        up1 = base.investigate_up()
        down1 = base.investigate_down()
        left1 = base.investigate_left()
        right1 = base.investigate_right()
        nw1 = base.investigate_nw()
        ne1 = base.investigate_ne()
        se1 = base.investigate_se()                 
        sw1 = base.investigate_sw()
        if up1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        if down1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75) 
        if left1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        if right1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        if nw1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        if ne1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        if se1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        if sw1 == "enemy" and base.GetVirus() > 75:
                base.DeployVirus(base.GetVirus()*0.75)
        return