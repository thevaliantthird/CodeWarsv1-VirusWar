from random import randint


def ActRobot(robot):
    # main useful variables 
    virusdeployer = 0

    drxn = {'wait': 0, 'up': 1, 'right': 2, 'down': 3, 'left': 4}
    move = randint(1, 4)
    pos = robot.GetPosition()
    base_signal = robot.GetCurrentBaseSignal()


    if (pos[0] == 0 or pos[0] == 39 or pos[1] == 0 or pos[1] == 39) and robot.GetInitialSignal != 'defender':
        identity = 'attacker'
    else:
        identity = robot.GetInitialSignal()
        

    
    surroundings = [robot.investigate_nw(), robot.investigate_up(), robot.investigate_ne(), robot.investigate_right(),
                    robot.investigate_se(), robot.investigate_down(), robot.investigate_sw(), robot.investigate_left()]

    enemy_base_found = 0

    # creation of base_pos and decision of whether state is calm or attackattacker

    if "my pos" in base_signal:
        state = "calm"

        base_pos = int(base_signal[base_signal.find("(") + 1:base_signal.find(",")]), int(
            base_signal[base_signal.find(",") + 2:base_signal.find(")")])
    else:
        state = "attack"
    
    centre_pos = (robot.GetDimensionX()/2,robot.GetDimensionY()/2)
    # surrounding reader

    for i in surroundings:
        if i == 'enemy':
            virusdeployer = 1
        if i == 'enemy-base':
            virusdeployer = 2 
            enemy_base_found = 1

    # signals for count of bots of each identity

    if identity == "defender":
        robot.setSignal("defender")
    elif identity == "attacker":
        robot.setSignal("attacker")
    elif identity == "attackernorth":
        robot.setSignal("attackernorth")
    elif identity == "attackersouth":
        robot.setSignal("attackersouth")
    elif identity == "attackereast":
        robot.setSignal("attackereast")
    elif identity == "attackerwest":
        robot.setSignal("attackerwest")

    # base found
    if enemy_base_found == 1:
        if surroundings[0] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0] - 1) + ", " + str(pos[1] - 1) + ")")
        elif surroundings[1] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0]) + ", " + str(pos[1] - 1) + ")")
        elif surroundings[2] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0] + 1) + ", " + str(pos[1] - 1) + ")")
        elif surroundings[3] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0] + 1) + ", " + str(pos[1]) + ")")
        elif surroundings[4] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0] + 1) + ", " + str(pos[1] + 1) + ")")
        elif surroundings[5] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str((pos[0])) + ", " + str(pos[1] + 1) + ")")
        elif surroundings[6] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0] - 1) + ", " + str(pos[1] + 1) + ")")
        elif surroundings[7] == "enemy-base":
            robot.setSignal("enemy base: " + "(" + str(pos[0] - 1) + ", " + str(pos[1]) + ")")

    # distinguishing defender and attacker robots
    farmer_count = int(
        robot.GetCurrentBaseSignal()[-1])  # to store the number robots farming 								   # around the border
    max_farmer = 4
    attacker_count=int(base_signal[base_signal.find("%")+1:base_signal.find("&")])

    if attacker_count <= 20 :
        max_farmer = 0
        
    rotation = 0
    if attacker_count <= 20:
        rotation = 1

    if state == "calm" and identity == "defender":

        if pos[0] >= base_pos[0] + 2:  # Right Wall
            move = drxn["left"]

        if pos[0] <= base_pos[0] - 2:  # left Wall
            move = drxn["right"]

        if pos[1] >= base_pos[1] + 2:  # Upper Wall
            move = drxn["up"]

        if pos[1] <= base_pos[1] - 2:  # Lower Wall
            move = drxn["down"]

    elif state == "calm" and identity == "attackernorth":
        if base_pos[1] <= pos[1]+robot.GetDimensionY()/4 and base_pos[0] == pos[0] and pos[1] != 0:
            move = drxn["up"]


            
    elif state == "calm" and identity == "attackersouth":
        if base_pos[1] >= pos[1]-robot.GetDimensionY()/4 and base_pos[0] == pos[0] and pos[1] != robot.GetDimensionY()-1:
            move = drxn["down"]


    elif state == "calm" and identity == "attackerwest":
        if base_pos[0] <= pos[0]+robot.GetDimensionX()/4 and base_pos[1] == pos[1] and pos[0] != 0:
            move = drxn["left"]

            
    elif state == "calm" and identity == "attackereast":
        if base_pos[0] >= pos[0] - robot.GetDimensionX()/4 and base_pos[1] == pos[1] and pos[0] != robot.GetDimensionX()/4:
            move = drxn["right"]

        

    elif state == "calm" and "attacker" in identity and farmer_count < max_farmer:  # attackers performing random movements 
        if (pos[0] == 0 and pos[1] != 0):
            robot.setSignal("farmer")
            move = drxn["up"]
            identity = "farmer"

        if (pos[1] == 0 and pos[0] != robot.GetDimensionX() - 1):
            robot.setSignal("farmer")
            move = drxn["right"]
            identity = "farmer"


        if (pos[0] == robot.GetDimensionX() - 1 and pos[1] != robot.GetDimensionY() - 1):  # Change 40 to X dimension of the Canvas
            robot.setSignal("farmer")
            move = drxn["down"]
            identity = "farmer"


        if (pos[1] == robot.GetDimensionY() - 1 and pos[0] != 0):  # Change 40 to Y dimension of the Canvas
            robot.setSignal("farmer")
            move = drxn["left"]
            identity = "farmer"

    
    elif state == "calm" and "attacker" in identity and rotation == 1:  # attackers performing random movements 
        x = pos[0] - centre_pos[0]
        y = pos[1] - centre_pos[1]
        move_drxn = randint(0,5)
        if x-y >=0  and x+y>=0:
            l = ["down","down","down","down","left","right"]
            move = drxn[l[move_drxn]]

        elif x+y >=0 and x-y <= 0:
            l = ["left","left","left","left","up","down"]
            move = drxn[l[move_drxn]]
            
        elif x+y <= 0 and x-y <= 0:
            l = ["up","up","up","up","left","right"]
            move = drxn[l[move_drxn]]
            

        elif x+y <= 0 and x-y >= 0:
            l = ["right","right","right","right","up","down"]
            move = drxn[l[move_drxn]]
                        
    elif state == "attack" and identity == "attacker":
        i = robot.GetCurrentBaseSignal()  # attack state, no identities everyne just attacks
        attack_location = i[i.find("(") + 1:i.find(",")], i[i.find(",") + 2:i.find(")")]
        if pos[0] > int(attack_location[0]):
            move = drxn["left"]
        elif pos[0] < int(attack_location[0]):
            move = drxn["right"]
        elif pos[1] > int(attack_location[1]):
            move = drxn["up"]
        elif pos[1] < int(attack_location[1]):
            move = drxn["down"]

            # to set the number of robots farming at the border
    # makes the robot move clockwise once it reaches border

    if virusdeployer == 1 and "attacker" in identity:
        robot.DeployVirus(robot.GetVirus()/50 )
        
    elif virusdeployer == 1 and identity == "defender":
        robot.DeployVirus(robot.GetVirus()/20)
    elif virusdeployer == 2:
        robot.DeployVirus(robot.GetVirus() )
    return move


def ActBase(base):
    defendercount = 0
    attackercount = 0
    farmercount = 0
    virusdeployer = 0
    surroundings = [base.investigate_nw(), base.investigate_up(), base.investigate_ne(), base.investigate_right(),
                    base.investigate_se(), base.investigate_down(), base.investigate_sw(), base.investigate_left()]
    
    for i in surroundings:
        if i == 'enemy':
            virusdeployer = 1
    if virusdeployer == 1:
        base.DeployVirus(base.GetVirus()/10)

    if base.GetElixir() > 100 and 4 > len(base.GetListOfSignals()) >= 0 :
        base.create_robot('attackernorth')
    elif base.GetElixir() > 100 and 8 > len(base.GetListOfSignals()) >= 4:
        base.create_robot('attackersouth')
    elif base.GetElixir() > 100 and 12 > len(base.GetListOfSignals()) >= 8:
        base.create_robot('attackereast')
    elif base.GetElixir() > 100 and 16 > len(base.GetListOfSignals()) >= 12:
        base.create_robot('attackerwest')
    elif base.GetElixir() > 100 and len(base.GetListOfSignals()) >= 28:
        base.create_robot('defender')
    elif base.GetElixir() > 100:
        base.create_robot('attacker')
    base_pos = base.GetPosition()

    signals = base.GetListOfSignals()

    for i in base.GetListOfSignals():
        if i == "defender":
            defendercount += 1
        elif "attacker" in i:
            attackercount += 1
        elif i == "farmer":
            farmercount += 1

    base.SetYourSignal("my pos:" + str(base_pos) +"%" + str(attackercount) + "&" +str(farmercount))

    for i in signals:
        if "enemy base:" in i:
            base.SetYourSignal(i[i.find("("):i.find(")") + 1] + "%" + str(attackercount) + "&" + str(farmercount))

    return