from random import randint
def ActRobot(robot):
        enemy_positions = ["enemy", "enemy-base"] 
        up = robot.investigate_up() 
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        robot.setSignal('')

        my_signal = robot.GetInitialSignal()
        if my_signal.find('basebots')!=-1:
                x,y = robot.GetPosition()
                sig_x = int(my_signal[8:10])
                sig_y = int(my_signal[10:])
                if x > sig_x:
                        return 4
                if x < sig_x:
                        return 2
                if y > sig_y:
                        return 1
                if y < sig_y:
                        return 3
                if x == sig_x or y == sig_y:
                        return randint(1,4)

        if up in enemy_positions:
                if up == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if up == "enemy-base":
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_x = 0 + x
                        else:
                                msg_x = x
                        if y-1 < 10:
                                msg_y = 0 + (y-1)
                        else:
                                msg_y = (y-1)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)       

        if down in enemy_positions:
                if down == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if down == "enemy-base":
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_x = 0 + (x)
                        else:
                                msg_x = (x)
                        if y+1 < 10:
                                msg_y = 0 + (y+1)
                        else:
                                msg_y = (y+1)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)

        if left in enemy_positions:
                if left == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if left == "enemy-base":
                        x,y = robot.GetPosition()
                        if x-1 < 10:
                                msg_x = 0 + (x-1)
                        else:
                                msg_x = (x-1)
                        if y < 10:
                                msg_y = 0 + (y)
                        else:
                                msg_y = (y)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)

        if right in enemy_positions:
                if right == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if right == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = 0 + (x+1)
                        else:
                                msg_x = (x+1)
                        if y < 10:
                                msg_y = 0 + (y)
                        else:
                                msg_y = (y)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)                 

        if ne in enemy_positions:
                if ne == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if ne == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = 0 + (x+1)
                        else:
                                msg_x = (x+1)
                        if y-1 < 10:
                                msg_y = 0 + (y-1)
                        else:
                                msg_y = (y-1)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)

        if nw in enemy_positions:
                if nw == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if nw == "enemy-base":
                        x,y = robot.GetPosition()
                        if x-1< 10:
                                msg_x = 0 + (x-1)
                        else:
                                msg_x = (x-1)
                        if y-1 < 10:
                                msg_y = 0 + (y-1)
                        else:
                                msg_y = (y-1)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)

        if se in enemy_positions:
                if se == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if se == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 < 10:
                                msg_x = 0 + (x+1)
                        else:
                                msg_x = (x+1)
                        if y+1 < 10:
                                msg_y = 0 + (y+1)
                        else:
                                msg_y = (y+1)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)

        if sw in enemy_positions:
                if sw == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.75)
                if sw == "enemy-base":
                        x,y = robot.GetPosition()
                        if x-1 < 10:
                                msg_x = 0 + (x-1)
                        else:
                                msg_x = (x-1)
                        if y+1 < 10:
                                msg_y = 0 + (y+1)
                        else:
                                msg_y = (y+1)
                        message = "base" + str(msg_x) + str(msg_y)
                        robot.setSignal(message)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus()*0.85)
        else:
                return randint(1,4)

        if len(robot.GetCurrentBaseSignal()) >0:
                s = robot.GetCurrentBaseSignal()[4:]
                sx = int(s[0:2])
                sy = int(s[2:4])
                dist = abs(sx-x) + abs(sy-y)
                if dist==1:
                        robot.DeployVirus(500)
                        return randint(1,4)
                if x < sx:
                        return 2
                if x > sx:
                        return 4
                if y < sy:
                        return 3
                if y > sy:
                        return 1
        else:
                return randint(1,4)
        
def ActBase(base):

        while(base.GetElixir() >= 1800 and base.GetElixir()<=2000):
                x,y = base.GetPosition()
                if x < 10:
                        MSG_x = str(0) + str(x)
                if y < 10:
                        MSG_y = str(0) + str(y)
                if x >= 10:
                        MSG_x = str(x)
                if y >=10:
                        MSG_y = str(y)
                base.create_robot('basebots' + MSG_x + MSG_y)
        while(base.GetElixir() > 500 and base.GetElixir()< 1800):
                base.create_robot('')
        L = base.GetListOfSignals()
        for l in L:
                if len(l) > 0:
                        base.SetYourSignal(l)
                return  