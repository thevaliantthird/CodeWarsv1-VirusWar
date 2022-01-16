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
        x,y = robot.GetPosition()
        robot.setSignal('')
        if up == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif up == "enemy-base" :
                robot.DeployVirus(robot.GetVirus())
                if x < 10 :
                       msg_x = '0'+ str (x)
                else: 
                       msg_x = str(x)
                if y-1 < 10 :
                       msg_y = '0'+ str(y-1)
                else:
                       msg_y =str(y-1)

                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
        if down == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif down == "enemy-base" :
               robot.DeployVirus(robot.GetVirus())
               if x < 10 :
                       msg_x = '0'+ str (x)
               else: 
                       msg_x = str(x)
               if y+1 < 10 :
                       msg_y = '0'+ str(y+1)
               else:
                       msg_y =str(y+1)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)
        if left == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif left == "enemy-base" :
               robot.DeployVirus(robot.GetVirus())
               if x-1 < 10 :
                       msg_x = '0'+ str (x-1)
               else: 
                       msg_x = str(x-1)
               if y < 10 :
                       msg_y = '0'+ str(y)
               else:
                       msg_y =str(y)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)
        if right == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif right == "enemy-base" :
               robot.DeployVirus(robot.GetVirus())
               if x+1 < 10 :
                       msg_x = '0'+ str (x+1)
               else: 
                       msg_x = str(x+1)
               if y < 10 :
                       msg_y = '0'+ str(y)
               else:
                       msg_y =str(y)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)
        if ne == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif ne == "enemy-base" :
               robot.DeployVirus(robot.GetVirus()) 
               if x+1 < 10 :
                       msg_x = '0'+ str (x+1)
               else: 
                       msg_x = str(x+1)
               if y-1 < 10 :
                       msg_y = '0'+ str(y-1)
               else:
                       msg_y =str(y-1)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)
        if nw == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif nw == "enemy-base" :
               robot.DeployVirus(robot.GetVirus())
               if x-1 < 10 :
                       msg_x = '0'+ str (x-1)
               else: 
                       msg_x = str(x-1)
               if y-1 < 10 :
                       msg_y = '0'+ str(y-1)
               else:
                       msg_y =str(y-1)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)
        if se == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif se == "enemy-base" :
               robot.DeployVirus(robot.GetVirus())
               if x+1 < 10 :
                       msg_x = '0'+ str (x+1)
               else: 
                       msg_x = str(x+1)
               if y+1 < 10 :
                       msg_y = '0'+ str(y+1)
               else:
                       msg_y =str(y+1)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)
        if sw == "enemy" and robot.GetVirus() > 500 :
               robot.DeployVirus(300)
        elif sw == "enemy-base" :
               robot.DeployVirus(robot.GetVirus())
               if x-1 < 10 :
                       msg_x = '0'+ str (x-1)
               else: 
                       msg_x = str(x-1)
               if y+1 < 10 :
                       msg_y = '0'+ str(y+1)
               else:
                       msg_y =str(y+1)

               msg = "base" + msg_x + msg_y
               robot.setSignal(msg)


        if len(robot.GetCurrentBaseSignal()) > 0 :
                s = robot.GetCurrentBaseSignal()[4:] 
                sx = int(s[0:2])
                sy = int(s[2:4])
                dist = abs(sx-x) + abs(sy-y)
                if dist == 1:
                        robot.DeployVirus(robot.GetVirus())
                        return 0
                if x < sx :
                        return 2
                if x > sx:
                        return 4
                if y < sy :
                        return 3
                if y > sy:
                        return 1   
        else:
                return randint(1,4)     



        l = robot.GetInitialSignal()
        data = l.split(',') 
        basex = int(data[0])
        basey = int(data[1])
        basewidth = 2
        basex = int(basex)
        basey = int(basey)                            
        p =  randint (1,4)
        if robot.GetDimensionX() + 1 > basewidth + basex:
                while p == 2:
                        p = 4
                return p
        if robot.GetDimensionY() + 1 > basewidth + basey:
                while p == 3:
                        p = 1
                return p
        if robot.GetDimensionX() - 1 <  basex:
                while p == 4:
                        p = 2
                return p   
        if robot.GetDimensionY() -1 <  basewidth + basey:
                while p == 1:
                        p = 3
                return p

def ActBase(base):
         if base.GetElixir() > 1800:
                  base.create_robot(str(base.GetPosition()[0]) +','+ str(base.GetPosition()[1])+','+'def')
                 
         if base.GetElixir() > 300: 
                 base.create_robot('')
         L=base.GetListOfSignals()
         for l in L:
                 if len(l) > 0 :
                         base.SetYourSignal(l)
                         return
