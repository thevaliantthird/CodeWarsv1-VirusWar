from random import randint


def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        northwest = robot.investigate_nw()
        southwest = robot.investigate_sw()
        southeast = robot.investigate_se()
        northeast = robot.investigate_ne()
        x,y = robot.GetPosition()
        if up == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 1
        elif up == "enemy-base":
                if x < 10:
                        x = '0' + str(x)
                else: 
                        x = str(x)
                if y-1 < 10:
                        y = '0' + str(y-1)
                else:
                        y = str(y-1)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  up == "friend" or  up == "friend-base":
             if randint (1,4)==1:
                        return 3
             else:
                        return randint(1,4)
        if down == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 3
        elif down == "enemy-base":
                if x < 10:
                        x = '0' + str(x)
                else: 
                        x = str(x)
                if y+1 < 10:
                        y = '0' + str(y+1)
                else:
                        y = str(y+1)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  down == "friend" or  down == "friend-base":
                if randint (1,4)==3:
                        return 1
                else:
                        return randint(1,4)
        if left == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 4
        elif left == "enemy-base":
                if x-1 < 10:
                        x = '0' + str(x-1)
                else: 
                        x = str(x-1)
                if y < 10:
                        y = '0' + str(y)
                else:
                        y = str(y)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  left == "friend" or  left == "friend-base":
                if randint (1,4)==4:
                        return 4
                else:
                        return randint(1,4)
        if right == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 2
        elif right == "enemy-base":
                if x+1 < 10:
                        x = '0' + str(x+1)
                else: 
                        x = str(x+1)
                if y < 10:
                        y = '0' + str(y)
                else:
                        y = str(y)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  right == "friend" or  right == "friend-base":
                if randint (1,4)==2:
                        return 4
                else:
                        return randint(1,4)
              
        if northwest == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 3
        elif northwest == "enemy-base":
                if x-1 < 10:
                        x = '0' + str(x-1)
                else: 
                        x = str(x-1)
                if y-1 < 10:
                        y = '0' + str(y-1)
                else:
                        y = str(y-1)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  northwest == "friend" or  northwest == "friend-base":
                if randint (1,4)==1 or randint (1,4)==4:
                        return 3
                else:
                        return randint(1,4)
        if northeast == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 3
        elif northeast == "enemy-base":
                if x+1 < 10:
                        x = '0' + str(x+1)
                else: 
                        x = str(x+1)
                if y-1 < 10:
                        y = '0' + str(y-1)
                else:
                        y = str(y-1)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  northeast == "friend" or  northeast == "friend-base":
                if randint (1,4)==1 or randint (1,4)==2:
                        return 3
                else:
                        return randint(1,4)
              
        if southeast == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 1
        elif southeast == "enemy-base":
                if x+1 < 10:
                        x = '0' + str(x+1)
                else: 
                        x = str(x+1)
                if y+1 < 10:
                        y = '0' + str(y+1)
                else:
                        y = str(y+1)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0 
        elif  southeast == "friend" or  southeast == "friend-base":
                if randint (1,4)==3 or randint (1,4)==2:
                        return 1
                else:
                        return randint(1,4)
        if southwest == "enemy" and robot.GetVirus() > 2000:
                robot.DeployVirus(400)
                return 1
        elif southwest == "enemy-base":
                if x-1 < 10:
                        x = '0' + str(x-1)
                else: 
                        x = str(x-1)
                if y+1 < 10:
                        y = '0' + str(y+1)
                else:
                        y = str(y+1)
                baselocation =  x + y
                robot.setSignal(baselocation)
                robot.DeployVirus(robot.GetVirus())
                return 0
        elif  southwest == "friend" or  southwest == "friend-base":
                if randint (1,4)==3 or randint (1,4)==4:
                        return 1
                else:
                        return randint(1,4)
        if len(robot.GetCurrentBaseSignal())>0:
            bx = robot.GetCurrentBaseSignal()[-4:-2]
            by = robot.GetCurrentBaseSignal()[-2:]
            if robot.GetYourSignal().find("Attacker") != -1:
             if (abs(x-bx) + abs(y-by))==1:
                   robot.DeployVirus(robot.GetVirus())
                   return 0
             if x>bx:
                return 4
             if x<bx:
                return 2
             if y>by:
                return 1
             if y<by:
               return 3
        return randint(1,4)
def ActBase(base):
   u = base.investigate_up()
   d = base.investigate_down() 
   l = base.investigate_left() 
   r = base.investigate_right()
   nw = base.investigate_nw() 
   ne = base.investigate_ne() 
   se = base.investigate_se() 
   sw = base.investigate_sw() 
   if base.GetElixir()>1950:
      base.create_robot('Collector')
   elif base.GetElixir()>600:
        base.create_robot('Attacker')
   for i in base.GetListOfSignals():
          if len(i)>0:
             base.SetYourSignal(i)
             return
   if u == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if d == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if l == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if r == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if se == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if sw == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if ne == "enemy":
           base.DeployVirus(base.GetVirus()*.7)
   if nw == "enemy":
           base.DeployVirus(base.GetVirus()*.7)