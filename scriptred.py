from random import randint


def ActRobot(robot):
                up = robot.investigate_up()
                down = robot.investigate_down()
                left = robot.investigate_left()
                right =robot.investigate_right()
                if up == "enemy" and robot.GetVirus() > 1000:
                        robot.DeployVirus(100)        
                elif up == "enemy-base":
                        x,y = robot.GetPosition()
                        


                        msg = "base" + str(x) + str(y-1) 
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                            robot.DeployVirus(500)
                if down == "enemy" and robot.GetVirus() > 1000:
                        robot.DeployVirus(100)        
                elif down == "enemy-base":
                        x,y = robot.GetPosition()
                        if x < 10:
                                msg_X = '0' + str(x)
                        else:
                                msg_x = str(x)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)        
                        msg = "base" + str(x) + str(y+1) 
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                            robot.DeployVirus(500)  
                if right == "enemy" and robot.GetVirus() > 1000:
                        robot.DeployVirus(100)        
                elif up == "enemy-base":
                        x,y = robot.GetPosition()
                        msg = "base" + str(x) + str(y-1) 
                        robot.setSignal(msg)
                        if robot.GetVirus() > 500:
                            robot.DeployVirus(500)                     



                if len(robot.GetCurrentBaseSignal())  >0:


        return randint(1,4)


def ActBase(base):
    '''
    Add your code here
    
    '''
    if base.GetElixir() > 500:
            base.create_robot('')

    return
