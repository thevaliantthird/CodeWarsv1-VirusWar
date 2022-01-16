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

def moveTowardsEnemy(enemy_position,robot_position ):
        if enemy_position[0]>robot_position[0]:
                return 2
        elif enemy_position[0]<robot_position[0]:
                return 4
        elif enemy_position[1]>robot_position[1]:
                return 3
        elif enemy_position[1]<robot_position[1]:
                return 1
        

def GetEnemyCount(obj):
        enemycount=0
        enemy_positions = ["enemy","enemy-base"]
        if obj.investigate_up() in enemy_positions:
                enemycount += 1
        if obj.investigate_down() in enemy_positions:
                enemycount += 1
        if obj.investigate_left() in enemy_positions:
                enemycount += 1
        if obj.investigate_right() in enemy_positions:
                enemycount += 1
        if obj.investigate_ne() in enemy_positions:
                enemycount += 1
        if obj.investigate_nw() in enemy_positions:
                enemycount += 1
        if obj.investigate_se() in enemy_positions:
                enemycount += 1
        if obj.investigate_sw() in enemy_positions:
                enemycount += 1       
        return enemycount

def ActRobot(robot):
        deployvirusamt=1200
        reservevirus=0   
              
        en = robot.GetCurrentBaseSignal()
        if en.startswith("E:") :
                # Guide other robots to enemy base by using some algorithm


                e = en.split(":")[1].split(",")

                enemy_position = (int(e[0]), int(e[1]))
                robot_position = robot.GetPosition()
                if isRobotCloseToEnemy(enemy_position,robot_position):
                        virus_amt = 1000
                        while(robot.GetVirus() > virus_amt):
                                robot.DeployVirus(virus_amt)
                        return 0
                else:
                        counter = GetEnemyCount(robot)
                        while(robot.GetVirus()>1000 and counter>0):
                                robot.DeployVirus(deployvirusamt) #deploying normal 
                                counter -= 1
                        '''
                        complete this function
                        '''
                        return moveTowardsEnemy(enemy_position,robot_position)
        
        res = nextMove(robot)
        
        if type(res) == dict:
                e = res["enemy_base"]
                robot.setSignal("E:{},{}".format(e[0],e[1]))
                virus_amt = 1000
                while(robot.GetVirus() > virus_amt):
                        robot.DeployVirus(robot.GetVirus())
                return 0
        else:
                if res[1]["release_virus"]:  #check whether to release virus or not
                        counter=res[1]["release_virus"]
                           
                        if robot.GetInitialSignal().startswith("Guard"): 
                                while(robot.GetVirus()>reservevirus and counter>0):
                                        guardvirusamt=2*deployvirusamt
                                        while(robot.GetVirus()>reservevirus and guardvirusamt>0):

                                                robot.DeployVirus(200)
                                                guardvirusamt-=200 
                                        counter -= 1
                        else:
                                while(robot.GetVirus()>reservevirus and counter>0):
                                        robot.DeployVirus(deployvirusamt)
                                        counter -= 1  

        
        direction_map = defaultdict(lambda : 0,{
                "up":1, 
                "right":2, 
                "down":3,
                "left":4,
        }      )

        complementDirection ={
                "up":"down",
                "down":"up",
                "left":"right",
                "right":"left",

        }
        if robot.GetInitialSignal() == "Moving Robot":
                pos = robot.GetYourSignal()
                if pos in res[0]:    #for removal
                        res[0].remove(pos)
                        if len(res[0]) == 0:
                                next=choice(list(direction_map.keys()))
                        else:
                                #if length>0 after removing
                                next = choice(res[0])
                else :   #no removal
                        if len(res[0]) == 0:
                                next=choice(list(direction_map.keys()))
                        else:
                                next = choice(res[0])

                
                robot.setSignal(complementDirection[next])

                return direction_map[next]
                

        if robot.GetInitialSignal().startswith('Guard Robot') :
                for i in range(1,9):
                        if robot.GetInitialSignal()[11]==str(i):
                                robot.setSignal('G:'+str(i))

               
                if robot.GetPosition()[1] < (int(robot.GetInitialSignal().split(',')[2])):
                        return 3
                
                elif robot.GetPosition()[1] > (int(robot.GetInitialSignal().split(',')[2])):
                        return 1
                
                elif robot.GetPosition()[0] < (int(robot.GetInitialSignal().split(',')[1])):
                        return 2
                
                elif robot.GetPosition()[0] > (int(robot.GetInitialSignal().split(',')[1])):
                        return 4
                else:
                        return 0


def ActBase(base):
        
        (x,y)=base.GetPosition()
        base.SetYourSignal(str(x) + ',' + str(y))
        alive=[0,0,0,0,0,0,0,0]
        n='Guard Robot1,' + str(x) + ',' + str(y-2)
        ne='Guard Robot2,' + str(x+2) + ',' + str(y-2)
        e='Guard Robot3,' + str(x+2) + ',' + str(y)
        se='Guard Robot4,' + str(x+2) + ',' + str(y+2)
        s='Guard Robot5,' + str(x) + ',' + str(y+2)
        sw='Guard Robot6,' + str(x-2) + ',' + str(y+2)
        w='Guard Robot7,' + str(x-2) + ',' + str(y)
        nw='Guard Robot8,' + str(x-2) + ',' + str(y-2)

        

        create=[n,ne,e,se,s,sw,w,nw]


        reserveElixir = 50
        signals = []
        # check if robots have signalled anything
        signals = base.GetListOfSignals()
        
        
        # set signal if enemy location found optimize this
        for s in signals :

                if s.startswith("G:"):
                        for i in range(8):
                                if int(s[2])==(i+1):
                                        alive[i]=(i+1)

                 
                if s.startswith("E:"):
                        base.SetYourSignal(s)
                        while(base.GetElixir()>reserveElixir):
                                base.create_robot('Moving Robot')
        
        for p in range(8):
                if alive[p]==0:
                        counter=20
                        reservevirus=0
                        while(base.GetVirus()>reservevirus and counter>0):
                                        base.DeployVirus(200)  # 200x20=4000
                                        counter -= 1  

                                
                        if base.GetElixir()>reserveElixir:
                                base.create_robot(create[p])
        up = base.investigate_up()
        down = base.investigate_down()
        left = base.investigate_left()
        right = base.investigate_right()
        northe = base.investigate_ne()
        northw = base.investigate_nw()
        southe = base.investigate_se()
        southw = base.investigate_sw()
        if up=="enemy" or down=="enemy" or left=="enemy" or right=="enemy" or northe=="enemy" or northw=="enemy" or southe=="enemy" or southw=="enemy":
                base.DeployVirus(base.GetVirus()*0.5)


         # constant rate of robot deployment```````````
        if base.GetElixir() > 500:
                        base.create_robot('Moving Robot')
        




