from random import randint

def ActRobot(robot):
        up=robot.investigate_up();
        down=robot.investigate_down();
        left=robot.investigate_left();
        right=robot.investigate_right();
        x,y=robot.GetPosition();
        
        if(up=='enemy_base'):
                if(robot.GetVirus()>=2000):
                        robot.DeployVirus(1500)
                return 2
        elif(down=='enemy_base'):
                if(robot.GetVirus()>=2000):
                        robot.DeployVirus(1500)
                return 2
        elif(left=='enemy_base'):
                if(robot.GetVirus()>=2000):
                        robot.DeployVirus(1500)
                return 2
        elif(right=='enemy_base'):
                if(robot.GetVirus()>=2000):
                        robot.DeployVirus(1500)
                return 1
        elif(up=='enemy'):
                if(robot.GetVirus()>=1000):
                        robot.DeployVirus(800)
                return 3
        elif(down=='enemy'):
                if(robot.GetVirus()>=1000):
                        robot.DeployVirus(800)
                return 1
        elif(left=='enemy'):
                if(robot.GetVirus()>=1000):
                        robot.DeployVirus(800)
                return randint(1,3)
        elif(right=='enemy'):
                if(robot.GetVirus()>=1000):
                        robot.DeployVirus(800)
                return 4
        else:
                if(x>35):
                        return 4
                if(robot.GetTotalElixir()<=5000 and robot.GetVirus()<=3000):
                        return randint(1,4)
                else:
                        
                        if(y<17):
                                return 3
                        elif(y>23):
                                return 1
                        elif(x>34):
                                return 4
                        else:
                                return randint(1,4)
                          #we would after say that the robots should concentrate on the base rather than random movements



def ActBase(base):
        up = base.investigate_up()
        down=base.investigate_down()
        left = base.investigate_left()
        right = base.investigate_right()
        ne = base.investigate_ne()
        nw = base.investigate_nw()
        se = base.investigate_se()
        sw = base.investigate_sw()
        if(base.GetElixir()>650):
                base.create_robot('')
        if(up=='enemy'):
                if(base.GetVirus()>=1000):
                        base.DeployVirus(800)
        elif(down=='enemy'):
                if(base.GetVirus()>=1000):
                        base.DeployVirus(800)
        elif(left=='enemy'):
                if(base.GetVirus()>=1000):
                        base.DeployVirus(800)
        elif(right=='enemy'):
                if(base.GetVirus()>=1000):
                        base.DeployVirus(800)
        elif(nw=='enemy'):
                if(base.GetVirus()>=1000):
                        base.DeployVirus(800)
                
        elif(se=='enemy'):
                if(base.GetVirus()>=1000):
                        base.DeployVirus(800)
        return
        if(base.GetElixir()>650):
                base.create_robot('')
        return
