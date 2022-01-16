from random import randint,choice
from collections import defaultdict
from base import Base
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
        #defending robots code
        res=nextMove(robot)
        
        robocrd=list(robot.GetPosition())
        xr=robocrd[0]
        yr=robocrd[1]
        
        initial=robot.GetInitialSignal()
        if 'defc' in initial:
                if type(res)==tuple:
                        if res[1]["release_virus"]>0:
                                if 'innerdefc' in initial:
                                        if robot.GetVirus()>4000:
                                                robot.DeployVirus(4000)
                                        else:
                                                robot.DeployVirus(robot.GetVirus()*0.9)
                                else:
                                        if robot.GetVirus()>1200:
                                                robot.DeployVirus(1200)
                                        elif robot.GetVirus()>600:
                                                robot.DeployVirus(600)
        

        if 'defc' in initial:
                basecrd=[int(initial.split()[2]), int(initial.split()[3])]
                xb=basecrd[0]
                yb=basecrd[1]
        
        if ('defc' in initial) and (robocrd==basecrd) :
                if 'innerdefc' in initial:
                        re=int(initial.split()[1])
                        if re==5:
                                re=1
                else:
                        re=int(initial.split()[1].split(':')[0])
                return re
        elif 'innerdefc' in initial:
            if xr<xb and yr>=yb:
                return 1
            elif xr>xb and yr<=yb:
                return 3
            elif xr>=xb and yr>yb:
                return 4
            elif xr<=xb and yr<yb:
                return 2
        elif 'defc' in initial:
                        re=int(initial.split()[1].split(':')[0])
                        pos=int(initial.split()[1].split(':')[1])
                        if xr==xb and abs(yr-yb)==1 :
                                if re==1 and pos==1:
                                        return 4
                                elif re==1 and pos==2:
                                        return 2
                                elif re==3 and pos==1:
                                        return 2
                                elif re==3 and pos==2:
                                        return 4
                        elif yr==yb and abs(xr-xb)==1 :
                                if re==2 and pos==1:
                                        return 1
                                elif re==2 and pos==2:
                                        return 3
                                elif re==4 and pos==1:
                                        return 3
                                elif re==4 and pos==2:
                                        return 1
                        
                        elif abs(xr-xb)==1 and abs(yr-yb)==1:
                                if re==1:
                                        return 1
                                elif re==2:
                                        return 2
                                elif re==3:
                                        return 3
                                elif re==4:
                                        return 4

                        elif xr-xb==2 and yr-yb<=2 and yr-yb>=-1 :
                                return 1
                        elif xr-xb==-2 and yb-yr<=2 and yb-yr>=-1 :
                                return 3
                        elif yr-yb==-2 and xr-xb<=2 and xr-xb>=-1 :
                                return 4
                        elif yr-yb==2 and xb-xr<=2 and xb-xr>=-1 :
                                return 2
                
                
        
        pos=int(initial.split()[2])   
        #attacking robots code
        en = robot.GetCurrentBaseSignal()
        if en.startswith("E:") and pos==1:
                # Guide other robots to enemy base by using some algorithm
                e = en.split(":")[1].split(",")
                xe=int(e[0])
                ye=int(e[1])
                enemy_position = (xe, ye)
                robot_position = robot.GetPosition()
                xr=robot_position[0]
                yr=robot_position[1]
                if isRobotCloseToEnemy(enemy_position,robot_position)==False:
                    if xr<xe:
                        return 2
                    elif xr>xe:
                        return 4
                    if yr>ye:
                        return 1
                    elif yr<ye:
                        return 3
                


                if enemy_position == robot_position or isRobotCloseToEnemy(enemy_position,robot_position):
                        virus_amt = 1000
                        while(robot.GetVirus() > virus_amt):
                                robot.DeployVirus(virus_amt)
                        if xr==xe:
                                if 'friend' not in robot.investigate_right():
                                        return 2
                                elif 'friend' not in robot.investigate_left():
                                        return 4
                        if yr==ye:
                                if 'friend' not in robot.investigate_up():
                                        return 1
                                elif 'friend' not in robot.investigate_down():
                                        return 3
                        
                        return 0  
        
        res = nextMove(robot)
        if type(res) == dict:
                e = res["enemy_base"]
                robot.setSignal("E:{},{}".format(e[0],e[1]))
                virus_amt = 4000
                while(robot.GetVirus() > virus_amt):
                        robot.DeployVirus(virus_amt)
                if robot.GetVirus()>2800:
                        robot.DeployVirus(2800)
                else:
                        robot.DeployVirus(robot.GetVirus()*0.8)
                return 0
        else:
                if res[1]["release_virus"]==1:
                        if robot.GetVirus() > 1000:
                                robot.DeployVirus(960)

        if 'attack' in initial:
                grid=int(initial.split()[1])
                pos=int(initial.split()[2])
                xc=int(initial.split()[3])
                yc=int(initial.split()[4])
                #send signal of survival
                
                options=[1,2,3,4]
                if 'Alive' in robot.GetYourSignal():
                        prevmove=int(robot.GetYourSignal().split()[2])
                        #print(robot.GetYourSignal())
                        #print(prevmove)
                        if prevmove>=3:
                                options.remove(prevmove-2)
                                options.append(prevmove)
                                
                        elif prevmove<=2:
                                options.remove(prevmove+2)
                                options.append(prevmove) #dilemma here, do this or not?
                              
                else:
                        print('fail')
                move=choice(options)
                #try:
                        
                        
                #except:
                        #move=choice(options)
                        #print('fail')
                        
                
                robot.setSignal('Alive {} {}'.format(str(grid), str(move)))
                #make 10 grids of 8x20 each
                if grid%2==1:
                        if (xr<=xc/2 and yr>yc*(grid-1)/10 and yr<= yc*(grid+1)/10 )==False:
                                if xr>xc/2:
                                        return choice([4,4,4,4,4,4,1,3,1,3])
                                if yr<=yc*(grid-1)/10:
                                        return choice([3,3,3,3,3,3,4,2,2,4])
                                if yr>yc*(grid+1)/10:
                                        return choice([1,1,1,1,1,1,4,2,2,4])
                        elif (xr==xc/2):
                                return 4
                        elif robot.investigate_left()=='wall':
                                return 2
                        elif (yr==yc*(grid-1)/10+1) or robot.investigate_up()=='wall':
                                return 3
                        elif (yr==yc*(grid+1)/10) or robot.investigate_down()=='wall':
                                return 1
                        else:     
                                return move
                elif grid%2==0:
                        if (xr>xc/2 and yr>yc*(grid-2)/10 and yr<= yc*(grid)/10 )==False:
                                if xr<=xc/2:
                                        return choice([2,2,2,2,2,2,3,1,1,3])
                                if yr<=yc*(grid-2)/10:
                                        return choice([3,3,3,3,3,3,4,2,2,4])
                                if yr>yc*(grid)/10:
                                        return choice([1,1,1,1,1,1,4,2,2,4])
                        elif (xr==xc) or robot.investigate_right()=='wall':
                                return 4
                        elif (xr==1+xc/2):
                                return 2
                        elif (yr==yc*(grid-2)/10+1) or robot.investigate_up()=='wall':
                                return 3
                        elif (yr==yc*(grid)/10) or robot.investigate_down()=='wall':
                                return 1
                        else:  
                                return move
                        



        

def basedefence(base):
        up =base.investigate_up()
        down =base.investigate_down()
        left =base.investigate_left()
        right =base.investigate_right()
        ne =base.investigate_ne()
        nw =base.investigate_nw()
        se =base.investigate_se()
        sw =base.investigate_sw()
        basecoord=base.GetPosition()
        resultant_step= {'release_virus' : 0}
        directions=[up, down, left, right, ne, nw, se, sw]
        enemycount=0
        for dire in directions:
                if 'enemy' in dire:
                        enemycount+=1
        if enemycount>4:
                if base.GetVirus()>6000:
                        base.DeployVirus(5500)
                else :
                        base.DeployVirus(base.GetVirus()*0.9)
        elif enemycount>0:
                if base.GetVirus()>5000:
                        base.DeployVirus(4500)
                else :
                        base.DeployVirus(base.GetVirus()*0.85)

        friendcount=0
        for dire in directions:
                if 'friend' in dire:
                        friendcount+=1
        #will keep 4 friends immediately around the base
        if friendcount<4:
                if base.GetElixir()-50*(4-friendcount)>200:
                        for i in range(1,5-friendcount):
                                base.create_robot('innerdefc '+ str(i) + ' ' + str(basecoord[0]) + ' ' + str(basecoord[1]))
        # 8 robots outer, 4 robots inner. 
        if base.GetElixir()>600:
                for i in range(1,5):
                        for j in range(1,3):
                                base.create_robot('defc ' + str(i)+':'+str(j) + ' ' + str(basecoord[0]) + ' ' + str(basecoord[1]) )
                

 

def ActBase(base):
        '''
        Add your code here
        
        '''
        basedefence(base)
        basecoord=base.GetPosition()
        xb=basecoord[0]
        yb=basecoord[1]
        xc=base.GetDimensionX()
        yc=base.GetDimensionY()

        for i in range(1,10,2):
            if yb>yc*(i-1)/10 and yb<=yc*(i+1)/10:
                if xb>xc/2:
                    basegrid=i+1
                else:
                    basegrid=i
                break
        #print('basegrid=', basegrid)


        reserveElixir = 400
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
                #while(base.GetElixir()>reserveElixir):
                    #base.create_robot('')
        
        # make a enemies near function and check enemy base
        #enemies_near = 0
        #if enemies_near:
            #base.DeployVirus(200)
        
        
        # constant rate of robot deployment
        if base.GetElixir()-950 > 440:
            for i in range(1,11):
                if i!=basegrid:
                    for j in range(1,3):
                        base.create_robot('attack '+ str(i) + ' ' + str(j) + ' ' + str(xc) + ' ' + str(yc))
                if i==basegrid:
                        base.create_robot('attack '+ str(i) + ' ' + str(1) + ' ' + str(xc) + ' ' + str(yc))
        
        alive=[]
        dead=[]
        for s in signals:
            if 'Alive' in s:
                grid=int(s.split()[1])
                alive.append(grid)
        #print(alive)
        if len(alive)>0:
            for i in range(1,11):
                if (i not in alive) and base.GetElixir()>310:
                    base.create_robot('attack '+ str(i) + ' ' + str(1) + ' ' + str(xc) + ' ' + str(yc))
        if len(alive)>0 and len(alive)<=12:
                for i in range(1,11):
                        if i not in alive:
                                dead.append(i)
                if len(dead)>=4 and base.GetElixir()>260:
                        for j in dead[0:4]:
                                base.create_robot('attack '+ str(j) + ' ' + str(randint(1,2)) + ' ' + str(xc) + ' ' + str(yc))
                if base.GetVirus()>58000 and base.GetElixir()-50*(len(dead))>80:
                        for j in dead[0:len(dead)]:
                                base.create_robot('attack '+ str(j) + ' ' + str(randint(1,2)) + ' ' + str(xc) + ' ' + str(yc))


