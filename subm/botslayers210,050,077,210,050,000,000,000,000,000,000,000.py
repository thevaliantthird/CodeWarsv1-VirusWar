from random import randint


def ActRobot(robot):
        up = robot.investigate_up()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        x,y = robot.GetPosition() 
        b = robot.GetInitialSignal()[4:]
        bx = int(b[0:2])
        by = int(b[2:4])
        distBase = abs(bx-x) + abs(by-y)
        
        if up == "enemy-base":        
                if x < 10:
                        msg_x = '0' + str(x)
                else:
                        msg_x = str(x) 
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)                       
                msg = "enemy" + msg_x + msg_y
                robot.setSignal(msg)
                
                robot.DeployVirus(robot.GetVirus()) 
                
          

        
        if down == "enemy-base":       
                if x < 10:
                        msg_x = '0' + str(x)
                else:
                        msg_x = str(x) 
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg = "enemy" + msg_x +msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
       
        if left == "enemy-base":       
                if x-1 < 10:
                        msg_x = '0' + str(x-1)
                else:
                        msg_x = str(x-1) 
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg = "enemy" + msg_x +msg_y

                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(robot.GetVirus())
        
        if right == "enemy-base":       
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else:
                        msg_x = str(x+1) 
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg = "enemy" + msg_x +msg_y

                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(robot.GetVirus())     
        
        



        if robot.GetCurrentBaseSignal().startswith("enemy"):                
                s = robot.GetCurrentBaseSignal()[5:]
                sx = int(s[0:2]) 
                sy = int(s[2:4])                               
                if x < sx:
                        return 2
                if x > sx:
                        return 4
                if y  < sy:
                        return 3
                if y > sy:
                        return 1
        if (( up=='enemy' and down=='enemy' ) or  (up=='enemy' and left=='enemy') or (up=='enemy' and right=='enemy') or (up=='enemy'and ne=='enemy') or (up=='enemy' and nw=='enemy') or ( up=='enemy' and se=='enemy') or ( up=='enemy' and sw=='enemy') or ( down=='enemy' and left=='enemy') or (down=='enemy'and  right =='enemy') or (down=='enemy' and ne=='enemy') or (down=='enemy'and nw=='enemy') or (down=='enemy'and se=='enemy') or (down=='enemy'and sw=='enemy') or (left=='enemy'and right=='enemy') or (left=='enemy'and ne=='enemy') or (left=='enemy'and nw=='enemy') or (left=='enemy' and se=='enemy') or (left=='enemy'and  sw=='enemy') or (right == 'enemy' and ne=='enemy') or (right=='enemy' and nw=='enemy') or (right=='enemy' and se=='enemy') or (right=='enemy' and sw=='enemy')or (ne=='enemy' and nw=='enemy')or (ne=='enemy' and se=='enemy')or (ne=='enemy'and sw=='enemy')or (nw=='enemy'and se=='enemy')or (nw=='enemy'and sw=='enemy')or (se=='enemy'and sw=='enemy')) and robot.GetVirus() > 3800 :               
                robot.DeployVirus(800)  
        
        return randint(1,4)  

        
        

        


def ActBase(base):

        x1,y1=base.GetPosition()
        if x1 < 10:
                msg_x1 = "0"+ str(x1)
        else:
                msg_x1 = str(x1)
        if y1 < 10:
                msg_y1 = "0" + str(y1)
        else:
                msg_y1 = str(y1)
        msg1 = "base" + msg_x1 + msg_y1
        if base.GetElixir()>800:
            base.create_robot(msg1)

        baseup = base.investigate_up()
        basedown = base.investigate_down()
        baseleft = base.investigate_left()
        baseright = base.investigate_right()
        basene = base.investigate_ne
        basenw = base.investigate_nw
        basese = base.investigate_se
        basesw = base.investigate_sw
        if baseup == 'enemy' or basedown == 'enemy' or baseleft == 'enemy' or baseright == 'enemy' or basene == 'enemy' or basenw == 'enemy' or basese == 'enemy' or basesw == 'enemy' :
                if base.GetVirus() > 800:
                        base.DeployVirus(800)
                else:
                        base.DeployVirus(base.GetVirus())


        
        L = base.GetListOfSignals()
        for l in L:
            if len(l) > 0:
                    base.SetYourSignal(l)
        return
        