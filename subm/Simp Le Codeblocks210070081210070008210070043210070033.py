from random import randint

#Function to check if bot is in the direct neighbourhood of a point. Returns boolean
def isNearTo(initPos, finalPos):
    return (abs(initPos[0] - finalPos[0]) <= 1 and abs(initPos[1] - finalPos[1]) <= 1)

#Function to check if bot is exactly at a point. Returns boolean
def isExactlyAt(initPos, finalPos):
    return ((initPos[0] - finalPos[0] == 0) and (initPos[1] - finalPos[1] == 0))

#Function to determine which step to take to move towards a point. Returns integer
def moveTowards(initPos, finalPos, exact = True):
    if (exact) :
        if(isExactlyAt(initPos, finalPos)):
            return 0
    elif (isNearTo(initPos, finalPos)):
        return 0

    difX = finalPos[0] - initPos[0]
    difY = finalPos[1] - initPos[1]
    decide = randint(1, abs(difX) + abs(difY))
    if(decide <= abs(difX)):
        return (2 if difX > 0 else 4)
    else:
        return (3 if difY > 0 else 1)

#Function to make random class bots move in a random circle clockwise. Returns integer
def randoCircleCW(initPos, basePos):
    #Final pos is actually "centre" of the random circle
    finalPos = basePos
    if(isExactlyAt(initPos, finalPos)):
        return 1
    difX = finalPos[0] - initPos[0]
    difY = finalPos[1] - initPos[1]
    decide = randint(1, abs(difX) + abs(difY))
    if(decide <= abs(difY)):
        return (2 if difY >= 0 else 4)
    else:
        return (1 if difX >= 0 else 3)

#Function to make random class bots move in a random circle anticlockwise. Returns integer
def randoCircleACW(initPos, basePos):
    #Final pos is actually "centre" of the random circle
    finalPos = basePos
    if(isExactlyAt(initPos, finalPos)):
        return 1
    difX = finalPos[0] - initPos[0]
    difY = finalPos[1] - initPos[1]
    decide = randint(1, abs(difX) + abs(difY))
    if(decide <= abs(difY)):
        return (4 if difY >= 0 else 2)
    else:
        return (3 if difX >= 0 else 1)

def ActRobot(robot):
    enemy = ["enemy", "enemy-base"]
    enemy_base = ["enemy-base"]

    # Get data about neighbouring cells
    location_data = {}
    location_data["up"] = robot.investigate_up()
    location_data["down"] = robot.investigate_down()
    location_data["left"] = robot.investigate_left()
    location_data["right"] = robot.investigate_right()
    location_data["ne"] = robot.investigate_ne()
    location_data["nw"] = robot.investigate_nw()
    location_data["se"] = robot.investigate_se()
    location_data["sw"] = robot.investigate_sw()
    location_data["Map"] = (robot.GetDimensionX(), robot.GetDimensionY())
    location_data["self_coor"] = robot.GetPosition()

    # Check if there is an enemy bot or base near it and deploy virus
    if (((location_data["up"] in enemy)+(location_data["down"] in enemy)+(location_data["left"] in enemy)+(location_data["right"] in enemy)+(location_data["ne"] in enemy)+(location_data["nw"] in enemy)+(location_data["se"] in enemy)+(location_data["sw"] in enemy))):
        robot.DeployVirus(200 if (robot.GetVirus() >= 1000) else robot.GetVirus()/5) #About 200
    
    #Deal extra damage for enemy base
    if (((location_data["up"] in enemy_base)+(location_data["down"] in enemy_base)+(location_data["left"] in enemy_base)+(location_data["right"] in enemy_base)+(location_data["ne"] in enemy_base)+(location_data["nw"] in enemy_base)+(location_data["se"] in enemy_base)+(location_data["sw"] in enemy_base))):
        robot.DeployVirus(200 if (robot.GetVirus() >= 1000) else robot.GetVirus()/5) #About 200

    Initsig = robot.GetInitialSignal()
    sig = Initsig

    robx = location_data["self_coor"][0]
    roby = location_data["self_coor"][1]

    # If found Enemy base then send signal to base
    if (location_data["up"] == 'enemy-base') :
       sig = ("T" + f"{(robx):02d}" + f"{(roby - 1):02d}")

    if (location_data["down"] == 'enemy-base') :
        sig = ("T" + f"{(robx):02d}" + f"{(roby + 1):02d}")

    if (location_data["left"] == 'enemy-base') :
        sig = ("T" + f"{(robx - 1):02d}" + f"{(roby):02d}")

    if (location_data["right"] == 'enemy-base') :
        sig = ("T" + f"{(robx + 1):02d}" + f"{(roby):02d}")

    if (location_data["nw"] == 'enemy-base') :
        sig = ("T" + f"{(robx - 1):02d}" + f"{(roby - 1):02d}")

    if (location_data["ne"] == 'enemy-base') :
        sig = ("T" + f"{(robx + 1):02d}" + f"{(roby - 1):02d}")

    if (location_data["se"] == 'enemy-base') :
        sig = ("T" + f"{(robx + 1):02d}" + f"{(roby + 1):02d}")

    if (location_data["sw"] == 'enemy-base') :
        sig = ("T" + f"{(robx - 1):02d}" + f"{(roby + 1):02d}")

    #Check base signal for attacker signal
    base_sig = robot.GetCurrentBaseSignal()
    if (len(base_sig) > 0 and base_sig[0] == "a" and robot.GetElixir() >= 125):
        sig = base_sig

    robot.setSignal(sig)
    if(Initsig[0:2] == "Rd"):
        if abs(robx-int(Initsig[2:4])) > 4:
            return (4 if robx-int(Initsig[2:4]) > 0 else 2)
        if abs(roby-int(Initsig[4:6])) > 4:
            return (1 if roby-int(Initsig[4:6]) > 0 else 3)
        else:
            return randoCircleCW(location_data["self_coor"], (int(Initsig[2:4]) - 1, int(Initsig[4:6]) + 1))
    if(sig[0:2] == "Ra"):
        if abs(robx-int(Initsig[2:4])) > 5:
            return (4 if robx-int(Initsig[2:4]) > 0 else 2)
        if abs(roby-int(Initsig[4:6])) > 5:
            return (1 if roby-int(Initsig[4:6]) > 0 else 3)
        else:    
            return randoCircleACW(location_data["self_coor"], (int(Initsig[2:4]) + 1, int(Initsig[4:6]) - 1))
    if(sig[0] == "r"):
        if (sig[1] == "a"):
            return randoCircleACW(location_data["self_coor"], (robot.GetDimensionX()//2, robot.GetDimensionY()//2))
        elif (sig[1] == "c"):
            return randoCircleCW(location_data["self_coor"], (robot.GetDimensionX()//2, robot.GetDimensionY()//2))
    elif(sig[0] == "a"):
        move =  moveTowards(location_data["self_coor"], (int(sig[1:3]), int(sig[3:5])), False)
        if (move >0): 
            return move
        else:
            return randint(1,4)
    else:
        return moveTowards(location_data["self_coor"], (15, 15))


def ActBase(base):
    '''
    Add your code here

    '''
    #Basic base defence
    enemy = ["enemy", "enemy-base"]
    base_location_data = {}
    base_location_data["up"] = base.investigate_up()
    base_location_data["down"] = base.investigate_down()
    base_location_data["left"] = base.investigate_left()
    base_location_data["right"] = base.investigate_right()
    base_location_data["nw"] = base.investigate_nw()
    base_location_data["ne"] = base.investigate_ne()
    base_location_data["sw"] = base.investigate_sw()
    base_location_data["se"] = base.investigate_se()

    if ((base_location_data["up"] in enemy) + (base_location_data["down"] in enemy) + (base_location_data["left"] in enemy) + (base_location_data["right"] in enemy) + (base_location_data["ne"] in enemy) + (base_location_data["nw"] in enemy) + (base_location_data["se"] in enemy) + (base_location_data["sw"] in enemy)):
        base.DeployVirus((base.GetVirus()/4))  #About 250  

    basePos = base.GetPosition()
    baseX = f"{basePos[0]:02d}"
    baseY = f"{basePos[1]:02d}"

    if (base.GetElixir() > 1650):
        base.create_robot("Rd" + baseX + baseY + "f")
    if (base.GetElixir() > 1250):
        base.create_robot("Rd" + baseX + baseY + "f")  
    if (base.GetElixir() > 950):
        base.create_robot("ra" + baseX + baseY + "f")      
    if (base.GetElixir() > 500):
        base.create_robot("rc" + baseX + baseY + "f")
        return

    # Get all signals
    sig_list = base.GetListOfSignals()
    for s in sig_list:
        if (s[0] == "T"):
            base.SetYourSignal("a" + s[1:])

    return


    