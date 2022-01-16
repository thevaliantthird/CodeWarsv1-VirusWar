from random import randint


def ActRobot(robot):
    u = robot.investigate_up() 
    d = robot.investigate_down()
    r = robot.investigate_right()
    l = robot.investigate_left()
    nw = robot.investigate_nw()
    ne = robot.investigate_ne()
    se = robot.investigate_se()
    sw = robot.investigate_sw()
    x,y = robot.GetPosition()
    if u=="blank":
       return randint(0,4)
    if d=="blank":
       return randint(0,4)
    if r=="blank":
       return randint(0,4)
    if l=="blank":
       return randint(0,4)
    if u=="enemy" and robot.GetVirus()>10000 :
       robot.DeployVirus(0.1*robot.GetVirus())
       return 3
    elif u=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 3 
    if d=="enemy" and robot.GetVirus()>10000:
       robot.DeployVirus(0.1*robot.GetVirus())
       return 1
    elif d=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 1 
    if l=="enemy" and robot.GetVirus()>10000:
        robot.DeployVirus(0.1*robot.GetVirus())
        return 2
    elif l=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 2 
    if r=="enemy" and robot.GetVirus()>10000:
        robot.DeployVirus(0.1*robot.GetVirus())
        return 4
    elif r=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 4 
    if nw=="enemy" and robot.GetVirus()>10000:
        robot.DeployVirus(0.1*robot.GetVirus())
        return 3
    elif nw=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 3 
    if ne=="enemy" and robot.GetVirus()>10000:
        robot.DeployVirus(0.1*robot.GetVirus()) 
        return 4
    elif ne=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 4 
    if sw=="enemy" and robot.GetVirus()>10000:
        robot.DeployVirus(0.1*robot.GetVirus())
        return 1
    elif sw=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 1
    if u=="enemy" and d=="enemy" and robot.GetVirus()>10000 :
       robot.DeployVirus(0.15*robot.GetVirus())
       return 2
    elif u=="enemy" and d=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.03*robot.GetVirus())
       return 3 
    if u !="friend" or d!="friend" or l !="friend" or r!="friend":
       robot.DeployVirus(0.1*robot.GetVirus())
       return 0
    if se=="enemy" and robot.GetVirus()>10000:
       robot.DeployVirus(0.1*robot.GetVirus())
       return 1 
    elif se=="enemy" and robot.GetVirus()<=10000:
       robot.DeployVirus(0.02*robot.GetVirus())
       return 1
    if nw=="enemy-base" or u =="enemy-base" or d=="enemy-base" or l =="enemy-base" or r=="enemy-base" or ne =="enemy-base" or se =="enemy-base" or sw=="enemy-base":
       signal="enemybasefound"
       robot.setSignal(signal)
    if u == "enemy-base":
                if x < 10:
                        pos_x = '0' + str(x)
                else: 
                        pos_x = str(x)
                if y-1 < 10:
                        pos_y = '0' + str(y-1)
                else:
                        pos_y = str(y-1)
                pos = "base" + pos_x + pos_y
                robot.setSignal(pos)
                if robot.GetVirus() > 35:
                        robot.DeployVirus(25)
    elif d == "enemy-base":
                
                if x < 10:
                        pos_x = '0' + str(x)
                else: 
                        pos_x = str(x)
                if y+1 < 10:
                        pos_y = '0' + str(y+1)
                else:
                        pos_y = str(y+1)
                pos = "base" + pos_x + pos_y
                robot.setSignal(pos)
                if robot.GetVirus() > 35:
                        robot.DeployVirus(25)
    elif r == "enemy-base":
                if x - 1 < 10:
                        pos_x = '0' + str(x-1)
                else: 
                        pos_x = str(x-1)
                if y < 10:
                        pos_y = '0' + str(y)
                else:
                        pos_y = str(y)
                pos = "base" + pos_x + pos_y
                robot.setSignal(pos)
                if robot.GetVirus() > 35:
                        robot.DeployVirus(25)
    elif l== "enemy-base":
                x,y = robot.GetPosition()
                if x+1 < 10:
                        pos_x = '0' + str(x+1)
                else: 
                        pos_x = str(x+1)
                if y < 10:
                        pos_y = '0' + str(y)
                else:
                        pos_y = str(y)
                pos = "base" + pos_x + pos_y
                robot.setSignal(pos)
                if robot.GetVirus() > 35:
                        robot.DeployVirus(25)
        
        

    


    if robot.GetElixir() < 5:
       signal="die"
       robot.setSignal(signal)


def ActBase(base):
    
    
     for i in base.GetListOfSignals() :
        if i=="die":
          signal ="new"
          base.create_robot(signal)
     
     if base.investigate_up()=="enemy" or base.investigate_down() =="enemy" or base.investigate_left()=="enemy" or base.investigate_right()=="enemy" or base.investigate_nw()=="enemy" or base.investigate_ne() =="enemy" or base.investigate_se()=="enemy" or base.investigate_sw()=="enemy":
          base.DeployVirus(0.2*base.GetVirus())  


     if base.GetElixir() > 1000 :
        for i in range (0,12):
           signal ="new"
           base.create_robot(signal)
