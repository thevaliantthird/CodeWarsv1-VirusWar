from random import randint, choice
guards=False
# TODO
# IMPLEMENT PATHFINDING TO ENEMY BASE ONCE LOC IS KNOWN
# IMPLEMENT KNOWLEDGE OF DIRECTION OF ENEMY BASE


def ActRobot(robot):
    en={"enemy":False,"enemy-base":False}
    up = robot.investigate_up()
    down = robot.investigate_down()
    left = robot.investigate_left()
    right = robot.investigate_right()
    ne = robot.investigate_ne()
    nw = robot.investigate_nw()
    se = robot.investigate_se()
    sw = robot.investigate_sw()
    #create list of all squares around robot
    pos=[up,down,left,right,ne,nw,se,sw]
    #check through every square for either an enemy or an enemy base
    for i,e in enumerate(pos):
        #robot coords
        rx,ry=robot.GetPosition()
        #check for enemy
        if e=='enemy':
            en["enemy"]=True
        #check for enemy-base
        #if it is an enemy base, add coordinates of enemy base to dictionary 
        elif e=='enemy-base':
            en["enemy-base"]=True
            if i==0:
                en["base-coords"]=(rx,ry-1)
            elif i==1:
                en["base-coords"]=(rx,ry+1)
            elif i==2:
                en["base-coords"]=(rx-1,ry)
            elif i==3:
                en["base-coords"]=(rx+1,ry)
            elif i==4:
                en["base-coords"]=(rx+1,ry-1)
            elif i==5:
                en["base-coords"]=(rx-1,ry-1)           
            elif i==6:
                en["base-coords"]=(rx+1,ry+1)
            elif i==7:
                en["base-coords"]=(rx-1,ry+1)
    #if the robot is a guard
    if robot.GetInitialSignal().startswith('guard'):
        #check for enemy & deploy
        if en["enemy"]:
            if robot.GetVirus()>=1000 and robot.GetVirus()<3000:
                robot.DeployVirus(1000)
            elif robot.GetVirus()>=3000 and robot.GetVirus()<10000:
                robot.DeployVirus(2000)
            elif robot.GetVirus()>=10000 and robot.GetVirus()<15000:
                robot.DeployVirus(2500)
            elif robot.GetVirus()>=15000:
                robot.DeployVirus(4000)
            return 0
        if robot.GetYourSignal()=='' or not robot.GetYourSignal():
            res = robot.GetInitialSignal().split(':')[1]
            robot.setSignal('guard:{}:d'.format(res))
            return int(res)
        else:
            return 0
        
    #if it found an enemy base, signal the coordinates of base
    if en["enemy-base"]:
        robot.setSignal('e{},{}'.format(en["base-coords"][0],en["base-coords"][1]))
        if robot.GetVirus()>=1000 and robot.GetVirus()<3000:
            robot.DeployVirus(1000)
        elif robot.GetVirus()>=3000 and robot.GetVirus()<7500:
            robot.DeployVirus(1500)
        elif robot.GetVirus()>=7500 and robot.GetVirus()<12500:
            robot.DeployVirus(2000)
        elif robot.GetVirus()>=12500:
            robot.DeployVirus(3000)
        return 0
    #replace with code to go towards enemy base if signal
    if en["enemy"]:
        if robot.GetVirus()>=1000 and robot.GetVirus()<3000:
            robot.DeployVirus(500)
        elif robot.GetVirus()>=3000 and robot.GetVirus()<7500:
            robot.DeployVirus(750)
        elif robot.GetVirus()>=7500 and robot.GetVirus()<12500:
            robot.DeployVirus(1250)
        elif robot.GetVirus()>=12500 and robot.GetVirus()<20000:
            robot.DeployVirus(1500)
        elif robot.GetVirus()>=20000:
            robot.DeployVirus(2000)

        return randint(1,4)
    return randint(1,4)
def deployGuards(base):
    global guards
    #deploy 4 guards, each being numbered 0-3
    for i in range(1,5):
        base.create_robot('guard:{}'.format(i))
    #establish that guards have been deployed
    guards=True

def ActBase(base):
    global guards
    #if guards have not been deployed, deploy guards
    if not guards:
        deployGuards(base)
    #else, if base elixir > 500, deploy standard robots
    elif base.GetElixir() > 500:
        base.create_robot('')
    up = base.investigate_up()
    down = base.investigate_down()
    left = base.investigate_left()
    right = base.investigate_right()
    ne = base.investigate_ne()
    nw = base.investigate_nw()
    se = base.investigate_se()
    sw = base.investigate_sw()
    pos=[up,down,left,right,ne,nw,se,sw]
    eg=[]
    for e in pos:
        if e=='enemy':
            while base.GetVirus()>2000:
                base.DeployVirus(2000)
    try:
        signals=base.GetListOfSignals()
    except:
        None
    for signal in signals:
        if signal.startswith('e'):
            base.SetYourSignal(signal)
            while base.GetElixir()>200:
                base.create_robot('')
        elif signal.startswith('guard'):
            eg.append(int(signal.split(':')[1]))
    for i in range(1,5):
        if i not in eg:
            base.create_robot('guard:{}'.format(i))
    return