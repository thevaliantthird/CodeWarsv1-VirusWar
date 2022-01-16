from random import randint


def ActRobot(robot):
        if robot.GetVirus() > 1000:
                robot.DeployVirus(100)
        if robot.investigate_up()=='enemy':
                if robot.GetVirus() > 200:
                   robot.DeployVirus(100)
                return 2 
        if robot.investigate_down()=='enemy':
                if robot.GetVirus() > 200:
                   robot.DeployVirus(100)
                return 1
        if robot.investigate_left()=='enemy':
                if robot.GetVirus() > 200:
                   robot.DeployVirus(100)
                return 3
        if robot.investigate_right()=='enemy':
                if robot.GetVirus() > 200:
                   robot.DeployVirus(100)
                return 4
        
        if robot.investigate_up()=='enemy-base':
                if robot.GetVirus() > 1000:
                   robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                a=str(x)
                b=str(y-1)
                signal="enemy base "+a+b
                robot.setSignal(signal)
                if robot.GetVirus() > 300:
                   robot.DeployVirus(300)
                return 1
                
        if robot.investigate_down()=='enemy-base':
                if robot.GetVirus() > 1000:
                   robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                a=str(x)
                b=str(y+1)
                signal="enemy base "+a+b
                robot.setSignal(signal)
                if robot.GetVirus() > 300:
                   robot.DeployVirus(300)
                return 3

        if robot.investigate_left()=='enemy-base':
                if robot.GetVirus() > 1000:
                   robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                a=str(x-1)
                b=str(y)
                signal="enemy base "+a+b
                robot.setSignal(signal)
                if robot.GetVirus() > 300:
                   robot.DeployVirus(300)
                return 4   
            
        if robot.investigate_down()=='enemy-base':
                if robot.GetVirus() > 1000:
                   robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                a=str(x+1)
                b=str(y)
                signal="enemy base "+a+b
                robot.setSignal(signal)
                if robot.GetVirus() > 300:
                   robot.DeployVirus(300)
                return 2 


        else:
         return randint(1,4)


def ActBase(base):
    '''
    Add your code here
    
    '''
    
    if base.GetElixir() > 500:
            base.create_robot('')
    S=base.GetListOfSignals()
    for s in S:
     if len(s)>0:
       base.SetYourSignal(s)
    if base.GetVirus() > 500:
            base.DeployVirus(400)

    return