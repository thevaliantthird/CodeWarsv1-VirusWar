from random import randint

def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        x,y = robot.GetPosition()

        def goNear_xy(nrx,nry): #Function to send bot to one of the 8 places around that place
                dist = abs(nrx-x) + abs(nry-y)
                while True:
                        if dist==1:

                                return 0
                        else:
                                if x < nrx:
                                        return 2
                                if x > nrx:
                                        return 4
                                if y < nry :
                                        return 3
                                if y > nry:
                                        return 1


        if up == "enemy" and robot.GetVirus() > 1000:
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
                robot.DeployVirus(robot.GetVirus() * 0.9)

        if down == "enemy" and robot.GetVirus() > 1000:
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
                robot.DeployVirus(robot.GetVirus() * 0.9)
        
        if left == "enemy" and robot.GetVirus() > 1000:
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
                robot.DeployVirus(robot.GetVirus() * 0.9)
                
        if right == "enemy" and robot.GetVirus() > 1000:
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
                robot.DeployVirus(robot.GetVirus() * 0.9)
             
        if robot.GetCurrentBaseSignal()[0:4] == "base":
                if robot.GetInitialSignal()[0:9] == "find_base":
                        robot.setSignal("attack_base")
                        sx = int(robot.GetCurrentBaseSignal()[4:6])
                        sy = int(robot.GetCurrentBaseSignal()[6:8])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist == 1:
                                robot.DeployVirus(robot.GetVirus() * 0.9)
                        return goNear_xy(sx,sy)
                elif robot.GetInitialSignal() == "go_random":
                        return randint(1,4)
        elif robot.GetInitialSignal()[0:9] == "find_base":
                if int(robot.GetInitialSignal()[9:11]) <= 14:
                        u = randint(1,100)
                        if u <= 80: return 2
                        elif u <= 90: return 1
                        else: return 3
                elif int(robot.GetInitialSignal()[9:11]) <= 18:
                        u = randint(1,100)
                        if u <= 80: return 1
                        elif u <= 90: return 2
                        else: return 4
                elif int(robot.GetInitialSignal()[9:11]) <= 22:
                        u = randint(1,100)
                        if u <= 80: return 4
                        elif u <=90: return 1
                        else: return 3
                elif int(robot.GetInitialSignal()[9:11]) <= 26:
                        u = randint(1,100)
                        if u <= 80: return 3
                        elif u <=90: return 4
                        else: return 2
                elif int(robot.GetInitialSignal()[9:11]) <= 28:
                        u = randint(1,100)
                        if u <= 50: return 2
                        else: return 1
                elif int(robot.GetInitialSignal()[9:11]) <= 30:
                        u = randint(1,100)
                        if u <= 50: return 2
                        else: return 3
                elif int(robot.GetInitialSignal()[9:11]) <= 32:
                        u = randint(1,100)
                        if u <= 50: return 4
                        else: return 1
                else:
                        u = randint(1,100)
                        if u <= 50: return 4
                        else: return 3
                                          

def ActBase(base):
        if base.GetElixir() > 100: #Create Initial Robots to find base
                base.create_robot("find_base"+str(randint(11,34)))
        if base.GetYourSignal()[0:4] == "base" and base.GetElixir() > 50:#if base is found then create bots to collect virus
                base.create_robot('go_random')
        L = base.GetListOfSignals()
        for l in L:
                if l[0:4] == "base":
                        base.SetYourSignal(l)
                        return
