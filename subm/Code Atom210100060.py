  

from random import randint,choice
from collections import defaultdict
def nextMove(robot):
        friend_positions = ["friend", "friend-base"]
        enemy_positions = ["enemy","enemy-base"]
        empty_positions =  ["blank"]
        safe_positions = []
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        
        resultant_step = {
                "release_virus" : 0,
                "enemy_base" : (-1,-1),
        }
        
        if up in enemy_positions:
                if up == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0], t[1]-1)
                        return resultant_step
        else:
                safe_positions.append("up")

        if down in enemy_positions:
                if down == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0], t[1]+1)
                        return resultant_step
        else:
                safe_positions.append("down")
        if left in enemy_positions:
                if left == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]-1, t[1])
                        return resultant_step
        else:
                safe_positions.append("left")
        if right in enemy_positions:
                if right == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]+1, t[1])
                        return resultant_step
        else:
                safe_positions.append("right")
        
        if ne in enemy_positions:
                if ne == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]+1, t[1]-1)
                        return resultant_step
        # else:
        #         safe_positions.append("ne")
        if nw in enemy_positions:
                if nw == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]-1, t[1]-1)
                        return resultant_step
        # else:
        #         safe_positions.append("nw")
        if se in enemy_positions:
                if se == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]+1, t[1]+1)
                        return resultant_step
        # else:
        #         safe_positions.append("se")
        if sw in enemy_positions:
                if sw == "enemy":
                        resultant_step["release_virus"] = 1
                else:
                        t = robot.GetPosition()
                        resultant_step["enemy_base"] = (t[0]-1, t[1]+1)
                        return resultant_step
        # else:
        #         safe_positions.append("sw")

        return (safe_positions,resultant_step)

def isRobotCloseToEnemy(enemy_position,robot_position):
        if abs(enemy_position[0]-robot_position[0])<=1 and abs(enemy_position[1]-robot_position[1])<=1:
                return True
        return False


def ActRobot(robot):
        en = robot.GetCurrentBaseSignal()
        if en.startswith("E:") :
                # Guide other robots to enemy base by using some algorithm


                e = en.split(":")[1].split(",")

                enemy_position = (int(e[0]), int(e[1]))
                robot_position = robot.GetPosition()
                if enemy_position == robot_position or isRobotCloseToEnemy(enemy_position,robot_position):
                        virus_amt = 1000
                        while(robot.GetVirus() > virus_amt):
                                robot.DeployVirus(virus_amt)
                        return 0
        
        res = nextMove(robot)
        if type(res) == dict:
                e = res["enemy_base"]
                robot.setSignal("E:{},{}".format(e[0],e[1]))
                virus_amt = 1000
                while(robot.GetVirus() > virus_amt):
                        robot.DeployVirus(virus_amt)
                return 0
        else:
                if res[1]["release_virus"]:
                        if robot.GetVirus() > 1000:
                                robot.DeployVirus(200)  
        direction_map = defaultdict(lambda : 0,{
                "up":1, 
                "right":2, 
                "down":3,
                "left":4,
        }      )
        return direction_map[choice(res[0])]


def ActBase(base):
        '''
        Add your code here
        
        '''
        reserveElixir = 100
        signals = []
        # check if robots have signalled anything
        try:
                signals = base.GetListOfSignals()
        except:
                print("no signal yet")

        # set signal if enemy location found optimize this
        for s in signals :
                        if s.startswith("E:"):
                                base.SetYourSignal(s)
                                while(base.GetElixir()>reserveElixir):
                                        base.create_robot('')

        # make a enemies near function and check enemy base
        enemies_near = 0
        if enemies_near:
                base.DeployVirus(200)

        # constant rate of robot deployment
        if base.GetElixir() > 500:
                        base.create_robot('')