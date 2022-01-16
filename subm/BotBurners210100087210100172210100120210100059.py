from random import choice, randint

def to_str(pos):
        x,y=pos
        msgx=str(x)
        msgy=str(y)
        if x<10:
                msgx="0"+msgx
        if y<10:
                msgy="0"+msgy  
        return msgx+msgy

def go_to_rand(robot,pos):
        x,y=pos
        x0,y0=robot.GetPosition()
        reached_y=False
        reached_x=False

        if x0<x-1:
                dx=2
        elif x0>x+1:
                dx=4
        elif x0==x:
                dx=int(choice([2,4]))
        else:
                reached_x=True
                dx=int(choice([2,4]))
        if y0<y-1:
                dy=3
        elif y0>y+1:
                dy=1
        elif y0==y:
                dy=int(choice([1,3]))
        else:
                reached_y = True
                dy=int(choice([1,3]))
        if reached_x and reached_y:
                return randint(1,4)
        else:
                return int(choice([dx,dy]))

def investigate_all(robot):
        if "enemy-base" in [robot.investigate_up(),robot.investigate_down(),robot.investigate_left(),robot.investigate_right(),robot.investigate_ne(),robot.investigate_nw(),robot.investigate_se(),robot.investigate_sw()]:
                return True
        else:
                return False

# S1 - USING SYMMERTY TO OUR ADVANTAGE

def ActRobot(robot):
        
        xb=int(robot.GetInitialSignal()[4:6])
        yb=int(robot.GetInitialSignal()[6:8])

        if len(robot.GetCurrentBaseSignal())>0:
                xeb=int(robot.GetCurrentBaseSignal()[2:4])
                yeb=int(robot.GetCurrentBaseSignal()[4:6])
                move= go_to_rand(robot,(xeb,yeb))
                if move == 0:
                        robot.DeployVirus(robot.GetVirus())
                        return 0
                else:
                        return move
        if robot.GetInitialSignal()[:2] == "fr":
                return randint(1,4)
        else:
                
                if not investigate_all(robot):
                        if robot.GetInitialSignal()[3]=="H":
                                return go_to_rand(robot,(robot.GetDimensionX()-xb-2,yb-1))
                        elif robot.GetInitialSignal()[3]=="D":
                                return go_to_rand(robot,(robot.GetDimensionX()-xb-2,robot.GetDimensionY()-yb-1))
                        else:
                                return go_to_rand(robot,(xb-2,robot.GetDimensionY()-yb-1))
                else:
                        x,y = robot.GetPosition()
                        if robot.investigate_right()=='enemy-base':
                                robot.setSignal("fd"+to_str((x+1,y)))
                        elif robot.investigate_left()=='enemy-base':
                                robot.setSignal("fd"+to_str((x-1,y)))
                        elif robot.investigate_up()=='enemy-base':
                                robot.setSignal("fd"+to_str((x,y-1)))
                        elif robot.investigate_down()=='enemy-base':
                                robot.setSignal("fd"+to_str((x,y+1)))
                        elif robot.investigate_se()=='enemy-base':
                                robot.setSignal("fd"+to_str((x+1,y+1)))
                        elif robot.investigate_ne()=='enemy-base':
                                robot.setSignal("fd"+to_str((x+1,y-1)))
                        elif robot.investigate_nw()=='enemy-base':
                                robot.setSignal("fd"+to_str((x-1,y-1)))
                        elif robot.investigate_sw()=='enemy-base':
                                robot.setSignal("fd"+to_str((x-1,y+1)))
                        
                        return 0

def ActBase(base):
        
        pos=to_str(base.GetPosition())
        if len(base.GetListOfSignals())<9:
                
                for _ in range(3):
                        base.create_robot("ScoH"+pos)  # scouting in horizontal direction
                        base.create_robot("ScoV"+pos)  # scounting in vertical direction
                        base.create_robot("ScoD"+pos)  # scouting in diagonal direction
                
        for l in base.GetListOfSignals():
                if len(l)>0:
                        if l[1] == "d":
                                base.SetYourSignal(l)

        if base.GetElixir() > 500:
                
                base.create_robot('frm0'+pos)

        