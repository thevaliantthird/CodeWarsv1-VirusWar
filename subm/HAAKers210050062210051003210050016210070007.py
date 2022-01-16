from random import randint, choice, choices


def undomove(n, norandom=False):
        """
        Returns the move that will undo n, helper for move()
        """
        if n == 1:
                return 3
        if n==3:
                return 1
        if n == 2:
                return 4
        if n == 4:
                return 2   
        else:
                if norandom:
                        return 0
                return randint(1, 4)

def move(robot, motion=-1): 
        """
        Function to handle moving. Does 2 things:
        1) Smart Random, don't undo the previous move in random
        2) Store the value of previous move in ActBase.last_move
        """

        id = robot.GetInitialSignal()[0:3]
        
        last_m_undo = undomove(ActBase.last_move[id])

        if motion == -1:
                list_of_moves = [0, 1, 2, 3, 4]
                list_of_moves.remove(last_m_undo)
                pos = robot.GetPosition()
                canv_x = robot.GetDimensionX()
                canv_y = robot.GetDimensionY()
                if (pos[1] <= 0):
                        ActBase.last_move[id] = 3
                        return 3
                if (pos[1] >= canv_y-1):
                        ActBase.last_move[id] = 1
                        return 1
                if (pos[0] <= 0):
                        ActBase.last_move[id] = 2
                        return 2
                if (pos[0] >= canv_x-1):
                        ActBase.last_move[id] = 4
                        return 4
                
                # if (pos[1] <= 0):
                #         list_of_moves.remove('1') if '1' in list_of_moves else None
                # if (pos[1] >= canv_y-1):
                #         list_of_moves.remove('3') if '3' in list_of_moves else None
                # if (pos[0] <= 0):
                #         list_of_moves.remove('4') if '4' in list_of_moves else None
                # if (pos[0] >= canv_x-1):
                #         list_of_moves.remove('2') if '2' in list_of_moves else None
                        
                n = choice(list_of_moves)
        else:
                n = motion
        
        # print(n)
        ActBase.last_move[id] = n
        return n

        
def move_to(robot, sx, sy):
        """
        Move robot to a particular position sx, sy
        """
        x, y = robot.GetPosition()
        # print(f"{x=}, {y=}, {sx=}, {sy=}")
        # if(robot.GetInitialSignal()[0] == 'C'):
        #         print("move_to")
        if x < sx:
                return move(robot, 2)
        if x > sx:
                return move(robot, 4)
        if y < sy :
                
                return move(robot, 3)
        if y > sy:
                return move(robot, 1)


def protect_home(robot, exact=False):
        """
        Makes robot move towards home, if exact=false, they'll dance around home, else reach exactly home
        """
        # print(f"moving {robot}")
        basex = ActBase.posofbase[0]
        basey = ActBase.posofbase[1]
        x,y = robot.GetPosition()
        if abs(x-basex) <= 1 and abs(y-basey) <= 1 and not exact:
                return move(robot)
        return move_to(robot, basex, basey)
       

def collect(robot):
    x, y = robot.GetPosition()
    z, w = ActBase.posofbase
    n = int(robot.GetInitialSignal()[1:3]) 
    canv_x, canv_y = robot.GetDimensionX(), robot.GetDimensionY()
    side = int(0.1 * min(canv_x, canv_y))
    if (n == 0):
            pos_x, pos_y = canv_x // 2, canv_y // 2
    if (n == 1):
            pos_x, pos_y = canv_x - side, side   
    if (n == 2):
            pos_x, pos_y = side, side
    if (n == 3):
            pos_x, pos_y = side, canv_y - side
    if (n == 4):
            pos_x, pos_y = canv_x - side, canv_y - side
    
    if (abs(x - pos_x) > 4 or abs(y - pos_y) > 4):
            return choices([move_to(robot, pos_x, pos_y), move(robot)], [1, 1])[0]

    return move(robot)            
         

def hilbertmove(robot, quadrant=1):
        x, y = robot.GetPosition()
        z, w = ActBase.posofbase
        robot_edgeup=''
        robot_edgedown=''
        robot_edgeright=''
        robot_edgeleft=''
        if (y==0):
                robot_edgeup   = "wall"
        if (y+1 >= robot.GetDimensionY()):
                robot_edgedown = "wall"
        if (x==0):
                robot_edgeleft = "wall"
        if (x+1 >= robot.GetDimensionX()):
                robot_edgeright= "wall"
                   

        if quadrant == 1:
                relative_x, relative_y = x-z+hilbertmove.correction1x, w-y-hilbertmove.correction1y
                
                listofmoves = [0, 1, 2, 3, 4]
                if(relative_x>0 and relative_y>0):
                        if (robot_edgeup=="wall"   and relative_x %2 == 0 and relative_x > relative_y):
                                hilbertmove.correction1y -= 1 #nextmove1
                        if (robot_edgedown=="wall" and relative_x%2 != 0 and relative_x >= relative_y):
                                hilbertmove.correction1y += 1 #nextmove3
                        if (robot_edgeleft=="wall" and relative_y %2 == 0 and relative_x <= relative_y) :
                                hilbertmove.correction1x -= 1 #nextmove4
                        if (robot_edgeright=="wall"and relative_y %2 !=0 and relative_x < relative_y):
                                hilbertmove.correction1x += 1 #nextmove2
                                
                                
                elif (robot_edgeup=="wall" and relative_x == 0 and relative_y%2==0 and relative_y !=0):
                        hilbertmove.correction1y -= 1 #nextmove1
                elif (robot_edgeright=="wall" and relative_x == 0 and relative_y%2 !=0):
                        hilbertmove.correction1x += 1 #nextmove2
                        
                elif (robot_edgeup=="wall" and relative_y == 0 and relative_x != 0 and relative_x %2 == 0):
                        hilbertmove.correction1y -= 1 #nextmove1
                elif (robot_edgeright=="wall" and relative_y ==0 and relative_x %2 != 0):
                        hilbertmove.correction1x += 1 #nextmove2                                              
                elif (robot_edgeup=="wall" and relative_x == 0 and relative_y == 0):
                        hilbertmove.correction1y -= 1 #nextmove1
                relative_x, relative_y = x-z+hilbertmove.correction1x, w-y-hilbertmove.correction1y
                
        
        if quadrant == 3:
                relative_x, relative_y = z-x-hilbertmove.correction3x, y-w+hilbertmove.correction3y                
                
                listofmoves = [0, 3, 4, 1, 2]
                if(relative_x>0 and relative_y>0):
                        if (robot_edgedown=="wall"   and relative_x %2 == 0 and relative_x > relative_y):
                                hilbertmove.correction3y += 1 #nextmove3
                        if (robot_edgeup=="wall" and relative_x%2 != 0 and relative_x >= relative_y):
                                hilbertmove.correction3y -= 1 #nextmove1
                        if (robot_edgeright=="wall" and relative_y %2 == 0 and relative_x <= relative_y) :
                                hilbertmove.correction3x += 1 #nextmove2
                                # print('leftwall')
                        if (robot_edgeleft=="wall"and relative_y %2 !=0 and relative_x < relative_y):
                                hilbertmove.correction3x -= 1 #nextmove4
                elif (robot_edgedown=="wall" and relative_x == 0 and relative_y%2==0 and relative_y !=0):
                        hilbertmove.correction3y += 1 #nextmove3
                elif (robot_edgeleft=="wall" and relative_x == 0 and relative_y%2 !=0):
                        hilbertmove.correction3x -= 1 #nextmove4
                        # print('leftwall')
                elif (robot_edgedown=="wall" and relative_y == 0 and relative_x != 0 and relative_x %2 == 0):
                        hilbertmove.correction3y += 1 #nextmove3
                elif (robot_edgeleft=="wall" and relative_y ==0 and relative_x %2 != 0):
                        hilbertmove.correction3x -= 1 #nextmove4
                        # print('leftwall')
                elif (robot_edgedown=="wall" and relative_x == 0 and relative_y == 0):
                        hilbertmove.correction3y += 1 #nextmove3
                relative_x, relative_y = z-x-hilbertmove.correction3x, y-w+hilbertmove.correction3y
                
        if quadrant == 2:
                relative_x, relative_y = z-x-hilbertmove.correction2x, w-y-hilbertmove.correction2y
                
                listofmoves = [0, 1, 4, 3, 2]                
                if(relative_x>0 and relative_y>0):
                        if (robot_edgeup=="wall"   and relative_x %2 == 0 and relative_x > relative_y):
                                hilbertmove.correction2y -= 1 #nextmove1
                        if (robot_edgedown=="wall" and relative_x%2 != 0 and relative_x >= relative_y):
                                hilbertmove.correction2y += 1 #nextmove3
                        if (robot_edgeright=="wall" and relative_y %2 == 0 and relative_x <= relative_y) :
                                hilbertmove.correction2x += 1 #nextmove2
                        if (robot_edgeleft=="wall"and relative_y %2 !=0 and relative_x < relative_y):
                                hilbertmove.correction2x -= 1 #nextmove4

                elif (robot_edgeup=="wall" and relative_x == 0 and relative_y%2==0 and relative_y !=0):
                        hilbertmove.correction2y -= 1 #nextmove1
                elif (robot_edgeleft=="wall" and relative_x == 0 and relative_y%2 !=0):
                        hilbertmove.correction2x -= 1 #nextmove4
                elif (robot_edgeup=="wall" and relative_y == 0 and relative_x != 0 and relative_x %2 == 0):
                        hilbertmove.correction2y -= 1 #nextmove1
                elif (robot_edgeleft=="wall" and relative_y ==0 and relative_x %2 != 0):
                        hilbertmove.correction2x -= 1 #nextmove4
                elif (robot_edgeup=="wall" and relative_x == 0 and relative_y == 0):
                        hilbertmove.correction2y -= 1 #nextmove1
                relative_x, relative_y = z-x-hilbertmove.correction2x, w-y-hilbertmove.correction2y

        if quadrant == 0:
                relative_x, relative_y = x-z+hilbertmove.correction0x, y-w+hilbertmove.correction0y
                
                listofmoves = [0, 3, 2, 1, 4]
                if(relative_x>0 and relative_y>0):
                        if (robot_edgedown=="wall"   and relative_x %2 == 0 and relative_x > relative_y):
                                hilbertmove.correction0y += 1 #nextmove3
                        if (robot_edgeup=="wall" and relative_x%2 != 0 and relative_x >= relative_y):
                                hilbertmove.correction0y -= 1 #nextmove1
                        if (robot_edgeleft=="wall" and relative_y %2 == 0 and relative_x <= relative_y) :
                                hilbertmove.correction0x -= 1 #nextmove4
                        if (robot_edgeright=="wall"and relative_y %2 !=0 and relative_x < relative_y):
                                hilbertmove.correction0x += 1 #nextmove2
                elif (robot_edgedown=="wall" and relative_x == 0 and relative_y%2==0 and relative_y !=0):
                        hilbertmove.correction0y += 1 #nextmove3
                elif (robot_edgeright=="wall" and relative_x == 0 and relative_y%2 !=0):
                        hilbertmove.correction0x += 1 #nextmove2
                elif (robot_edgedown=="wall" and relative_y == 0 and relative_x != 0 and relative_x %2 == 0):
                        hilbertmove.correction0y += 1 #nextmove3
                elif (robot_edgeright=="wall" and relative_y ==0 and relative_x %2 != 0):
                        hilbertmove.correction0x += 1 #nextmove2
                elif (robot_edgedown=="wall" and relative_x == 0 and relative_y == 0):
                        hilbertmove.correction0y += 1 #nextmove3
                relative_x, relative_y = x-z+hilbertmove.correction0x, y-w+hilbertmove.correction0y
        

        
                
        
                
        if (relative_x > 0 and relative_y > 0):
                if (relative_x%2 != 0 and relative_x >= relative_y):
                        return move(robot, listofmoves[3])
                elif (relative_x %2 == 0 and relative_x > relative_y):
                        return move(robot, listofmoves[1])
                elif (relative_y %2 == 0 and relative_x <= relative_y):
                        return move(robot, listofmoves[4])
                elif (relative_y %2 !=0 and relative_x < relative_y):
                        return move(robot, listofmoves[2])
        elif (relative_x == 0 and relative_y%2==0 and relative_y !=0):
                return move(robot, listofmoves[1])
        elif (relative_x == 0 and relative_y%2 !=0):
                return move(robot,listofmoves[2])
        elif (relative_y == 0 and relative_x != 0 and relative_x %2 == 0):
                return move(robot, listofmoves[1])
                # print(listofmoves[1])
        elif (relative_y ==0 and relative_x %2 != 0):
                return move(robot, listofmoves[2])
        elif (relative_x == 0 and relative_y == 0):
                return move(robot, listofmoves[1])
        else:
                print(f"{relative_x=}, {relative_y=}")
                print(robot.GetInitialSignal())
                print(f"{x=} {y=}")
                print(f"{z=} {w=}")
                return move(robot)
                 
hilbertmove.correction1x=0
hilbertmove.correction1y=0
hilbertmove.correction2x=0
hilbertmove.correction2y=0
hilbertmove.correction3x=0
hilbertmove.correction3y=0
hilbertmove.correction0x=0
hilbertmove.correction0y=0                        

def give_instruction_wall(robot):
    """
    Gives instructions to each of the wall's robots to build wall
    """
    
    n = int(robot.GetInitialSignal()[1:3]) 
    instructions = []

    if (n == 1):
        instructions = [1,1,1,0]
    if (n == 2):
        instructions = [4,4,4,0]
    if (n == 3):
        instructions = [3,3,3,0]
    if (n == 4):
        instructions = [2,2,2,0]
    if (n == 5):
        instructions = [1,1,2,2]
    if (n == 6):
        instructions = [4,4,1,1]
    if (n == 7):
        instructions = [3,3,4,4]
    if (n == 8):
        instructions = [2,2,3,3]
    if (ActBase.walltimeframe > 140):
            instructions = [undomove(i, norandom=True) for i in instructions]
    return instructions


def give_instruction_es(n):
    if (n == 1):
        return [2,]*2
    if (n == 2):
        return [4,]*2
    if (n == 3):
        return [1,2]
    if (n == 4):
        return [1,4]
    if (n == 5):
        return [3,4]
    if (n == 6):
        return [3,2]
    if (n == 7):
        return [3,]*2
    if (n == 8):
        return [1,]*2


def reach_enemy_base(robot):
        base_sig = robot.GetCurrentBaseSignal()
        x, y = robot.GetPosition()
        # print(robot.GetVirus())
        if robot.GetVirus() < 100:
                move(robot)
        if len(base_sig)>4:
                if base_sig[0:4] == 'base':
                        s = base_sig[4:]

                        sx = int(s[0:2])
                        sy = int(s[2:4])
                        # print(f"{sx=} {sy=}")
                        dist = abs(sx-x) + abs(sy-y)
                        if dist == 1:
                                robot.DeployVirus(robot.GetVirus()*0.75)
                        #         return move(robot, 0)
                        return move_to(robot, sx, sy)


def ActRobot(robot):
    role=robot.GetInitialSignal()[0]
#     print(role)
    timeframe = ActBase.timeframe
    walltimeframe = ActBase.walltimeframe
    up = robot.investigate_up()
    down = robot.investigate_down()
    left = robot.investigate_left()
    right = robot.investigate_right()
    nw=robot.investigate_nw()
    ne=robot.investigate_ne()
    sw=robot.investigate_sw()
    se=robot.investigate_se()
    x,y = robot.GetPosition()
    robot.setSignal('')
    basex, basey = ActBase.posofbase
    cx,cy=ActBase.cx,ActBase.cy
    bcord=ActBase.bcord
    base_sig = robot.GetCurrentBaseSignal() 
    enemy_found = False
    base_attacked = False
    found_quad = False
    if (ActBase.enemyquadrant > 0):
        found_quad = True
    if role == 'C':
            ActBase.aliveresources[int(robot.GetInitialSignal()[1:3])] = True

    if len(base_sig)>4:
            if base_sig[0:4] == 'base':
                    enemy_found = True
            if len(base_sig) == 9 and base_sig[8] == 'H':
                    base_attacked = True
                #     print("Base Attacked")
    
    if role == 'W':
        virus = 800
    else:
        virus = 500
    virus = min(virus, robot.GetVirus())
    
        
    if up == "enemy" and robot.GetVirus() > 1000:
        robot.DeployVirus(virus)
    elif up == "enemy-base":
        if x < 10:
            msg_x = '0' + str(x)
        else: 
            msg_x = str(x)
        if y-1 < 10:
            msg_y = '0' + str(y-1)
        else:
            msg_y = str(y-1)
        msg = "base" + msg_x + msg_y
        robot.setSignal(msg)
        if robot.GetVirus() > 500:
            robot.DeployVirus(virus)
            
    if down == "enemy" and robot.GetVirus() > 1000:
            robot.DeployVirus(virus)
    elif down == "enemy-base":
            
            if x < 10:
                    msg_x = '0' + str(x)
            else: 
                    msg_x = str(x)
            if y+1 < 10:
                    msg_y = '0' + str(y+1)
            else:
                    msg_y = str(y+1)
            msg = "base" + msg_x + msg_y
            robot.setSignal(msg)
            if robot.GetVirus() > 500:
                    robot.DeployVirus(virus)
    
    if left == "enemy" and robot.GetVirus() > 1000:
            robot.DeployVirus(virus)
    elif left == "enemy-base":
            if x - 1 < 10:
                    msg_x = '0' + str(x-1)
            else: 
                    msg_x = str(x-1)
            if y < 10:
                    msg_y = '0' + str(y)
            else:
                    msg_y = str(y)
            msg = "base" + msg_x + msg_y
            robot.setSignal(msg)
            if robot.GetVirus() > 500:
                    robot.DeployVirus(virus)
            
    if right == "enemy" and robot.GetVirus() > 1000:
            robot.DeployVirus(virus)
    elif right == "enemy-base":
            x,y = robot.GetPosition()
            if x+1 < 10:
                    msg_x = '0' + str(x+1)
            else: 
                    msg_x = str(x+1)
            if y < 10:
                    msg_y = '0' + str(y)
            else:
                    msg_y = str(y)
            msg = "base" + msg_x + msg_y
            robot.setSignal(msg)
            if robot.GetVirus() > 500:
                    robot.DeployVirus(virus)

    if nw == "enemy" and robot.GetVirus() > 1000:
        robot.DeployVirus(virus)
    elif nw == "enemy-base":
        if x-1 < 10:
            msg_x = '0' + str(x-1)
        else: 
            msg_x = str(x-1)
        if y-1 < 10:
            msg_y = '0' + str(y-1)
        else:
            msg_y = str(y-1)
        msg = "base" + msg_x + msg_y
        robot.setSignal(msg)
        if robot.GetVirus() > 500:
            robot.DeployVirus(virus)

    if ne == "enemy" and robot.GetVirus() > 1000:
        robot.DeployVirus(virus)
    elif ne == "enemy-base":
        if x+1 < 10:
            msg_x = '0' + str(x+1)
        else: 
            msg_x = str(x+1)
        if y-1 < 10:
            msg_y = '0' + str(y-1)
        else:
            msg_y = str(y-1)
        msg = "base" + msg_x + msg_y
        robot.setSignal(msg)
        if robot.GetVirus() > 500:
            robot.DeployVirus(virus)

    if se == "enemy" and robot.GetVirus() > 1000:
        robot.DeployVirus(virus)
    elif se == "enemy-base":
        if x+1 < 10:
            msg_x = '0' + str(x+1)
        else: 
            msg_x = str(x+1)
        if y+1 < 10:
            msg_y = '0' + str(y+1)
        else:
            msg_y = str(y+1)
        msg = "base" + msg_x + msg_y
        robot.setSignal(msg)
        if robot.GetVirus() > 500:
            robot.DeployVirus(virus)

    if sw == "enemy" and robot.GetVirus() > 1000:
        robot.DeployVirus(virus)
    elif sw == "enemy-base":
        if x-1 < 10:
            msg_x = '0' + str(x-1)
        else: 
            msg_x = str(x-1)
        if y+1 < 10:
            msg_y = '0' + str(y+1)
        else:
            msg_y = str(y+1)
        msg = "base" + msg_x + msg_y
        robot.setSignal(msg)
        if robot.GetVirus() > 500:
            robot.DeployVirus(virus)
            
    if (role=='C' or role == 'W' or role=='S' or role=='P'):
                if base_attacked:
                        return protect_home(robot)        
    if(role == 'W'):
        # if enemy_found and not base_attacked:
        #     return reach_enemy_base(robot)
        if ActBase.walltimeframe < 0:
            return protect_home(robot, exact=True) # Move exactly to home
        n = int(robot.GetInitialSignal()[1:3]) 
        
        instructions = give_instruction_wall(robot)
        if (walltimeframe <= len(instructions)-1) :
            return move(robot, instructions[walltimeframe])
        elif(walltimeframe <= 120):
                return hilbertmove(robot,n%4)
        elif(walltimeframe <= 145): 
            return move_to(robot, basex, basey)
        elif(walltimeframe - 145 <= len(instructions)):
             return move(robot, instructions[walltimeframe - 146])
        elif(walltimeframe == 146 + len(instructions)):
                return move(robot, 4)
        else:
             list_of_moves=[1,2,2,3,3,4,4,1]
             return move(robot, list_of_moves[(walltimeframe-146 - len(instructions) - 1)%8])  

    if(role == 'C'):    
        if not enemy_found:
                return collect(robot)
        return reach_enemy_base(robot)          
        
    if(role == 'E'):
        if enemy_found:
            return reach_enemy_base(robot)
        id = robot.GetInitialSignal()[0:3]
        
        wy=min(abs(cy-bcord[1]),bcord[1])
        wx=min(abs(cx-bcord[0]),bcord[0])
        wx=min(wx,wy)
        wy=wx
        # print(ActBase.Emotion[id])
        if (bcord[0]>cx/2-4) and (bcord[0]<cx/2+4):
                if bcord[1]<cy/2:
                        if x<=max(wx-2, 0):
                                ActBase.Emotion[id] = 6 
                        elif y<=max(wy-3, 0) :
                                ActBase.Emotion[id] = 5
                        elif y>=min(cy-(wy-2),cy-1) :
                                ActBase.Emotion[id] = 4
                        elif x>=min(cx-(wx-3), cx-1) :
                                ActBase.Emotion[id] = 5
                else:
                        if x<=max(wx-2, 0):
                                ActBase.Emotion[id] = 3 
                        elif y<=max(wy-3, 0) :
                                ActBase.Emotion[id] = 5
                        elif y>=min(cy-(wy-2),cy-1) :
                                ActBase.Emotion[id] = 3
                        elif x>=min(cx-(wx-3), cx-1) :
                                ActBase.Emotion[id] = 4
        elif bcord[0]>cx/2:
                if x<=max(wx-2, 0):
                        #if n == 4:
                        ActBase.Emotion[id] = 6 
                elif y<=max(wy-2, 0) :
                        ActBase.Emotion[id] = 5
                elif y>=min(cy-(wy-2),cy-1) :
                        ActBase.Emotion[id] = 4
                elif x>=min(cx-(wx-3), cx-1) :
                        ActBase.Emotion[id] = 5
        
        else:
                if x<=max(wx-2, 0):
                        ActBase.Emotion[id] = 3 
                elif y<=max(wy-2, 0) :
                        ActBase.Emotion[id] = 6
                elif y>=min(cy-(wy-2),cy-1) :
                        ActBase.Emotion[id] = 3
                elif x>=min(cx-(wx-3), cx-1) :
                        ActBase.Emotion[id] = 5
        
        if x<=max(wx-2, 0) and y<=max(wy-2, 0):
                ActBase.Emotion[id] = 6
        if x>=min(cx-(wx-2), cx-1) and y<=max(wy-2, 0):
                ActBase.Emotion[id] = 5
        if x<= max(wx-2, 0) and y>= min(cy-(wy-2), cy-1):
                ActBase.Emotion[id] = 4
        if x>=min(cx-(wx-2), cx-1) and y>= min(cy-(wy-2), cy-1):
                ActBase.Emotion[id] = 3

        n = ActBase.Emotion[id]
        instructions = give_instruction_es(n)           
        # TODO: Fine tune
        return move(robot, choices([instructions[timeframe%2], 1, 2, 3, 4], weights=[6, 0.25, 0.25, 0.25, 0.25])[0]) 


    if(role == 'S'):
        if enemy_found and not base_attacked :
                return reach_enemy_base(robot)
        if walltimeframe<180:
                f,r,l,b=4,1,3,2
                n = int(robot.GetInitialSignal()[1:3]) 
                if (bcord[0]>cx/2-5) and (bcord[0]<cx/2+5):
                        r,l=2,4
                        if bcord[1]>cy/2:
                                f,b=1,3
                        else:
                                f,b=3,1
                elif (bcord[0]>cx/2):
                        f,b=4,2
                else :
                        f,b=2,4
                if (n == 1):instructions=[f,0]
                if (n == 2):instructions= [f,f]
                if (n == 3):instructions= [f,r]
                if (n == 0):instructions= [f,l]
                if walltimeframe<3:
                        instructions = instructions[walltimeframe-1]
                elif walltimeframe<140:
                        if (walltimeframe-3) % 14<6:
                                instructions = f
                        elif (walltimeframe-3) % 14==6:
                                instructions = r                                
                        elif (walltimeframe-3) % 14<13:
                                instructions = b
                        elif (walltimeframe-3) % 14==13:
                                instructions = l 

                return move(robot,instructions)
        elif walltimeframe<400:
                x1,y1=int(cx/2),int(cy/2)
                x2,y2=int(cx/4),int(cy/4)
                if ActBase.enemyquadrant==1:
                        x1,y1=x1+x2,y2
                elif ActBase.enemyquadrant == 2:
                        x1,y1=x2,y2
                elif ActBase.enemyquadrant == 3:
                        x1,y1=x2,y1+y2
                elif ActBase.enemyquadrant == 4:
                        x1,y1=x1+x2,y1+y2
                # print(x1, y1)
                # print(ActBase.enemyquadrant)
                if (abs(x - x1) > 6 or abs(y - y1) > 6):
                        return move_to(robot, x1,y1)
                else:
                        return move(robot)
        else:
                x1,y1=basex,basey
                if (abs(x - x1) > 4 or abs(y - y1) > 4):
                        return move_to(robot, x1,y1)
                else:
                        return move(robot) 
                                              
    if (role == 'R' and found_quad):
                id = int(robot.GetInitialSignal()[1:3])
                centre_x, centre_y = robot.GetDimensionX() / 2, robot.GetDimensionY() / 2
                z, w = abs(basex - centre_x), abs(basey - centre_y)
                quadrant = ActBase.enemyquadrant
                if enemy_found:
                        return reach_enemy_base(robot)
                
                if quadrant == 1:
                        if id in [0, 1, 2] and (abs(x - centre_x - z) > 2 or abs(y - centre_y + w) > 2):
                                return choices([move_to(robot, centre_x + z, centre_y - w), move(robot)], [1, 1])[0]
                        elif id in [3, 4, 5] and (abs(x - centre_x - w) > 2 or abs(y - centre_y + z) > 2):
                                return choices([move_to(robot, centre_x + w, centre_y - z), move(robot)], [1, 1])[0]
                if quadrant == 2:
                        if id in [0, 1, 2] and (abs(x - centre_x + z) > 2 or abs(y - centre_y + w) > 2):
                                return choices([move_to(robot, centre_x - z, centre_y - w), move(robot)], [1,1])[0]
                        elif id in [3, 4, 5] and (abs(x - centre_x + w) > 2 or abs(y - centre_y + z) > 2):
                                return choices([move_to(robot, centre_x - w, centre_y - z), move(robot)], [1,1])[0]
                if quadrant == 3:
                        if id in [0, 1, 2] and (abs(x - centre_x + z) > 2 or abs(y - centre_y - w) > 2):
                                return choices([move_to(robot, centre_x - z, centre_y + w), move(robot)], [1, 1])[0]
                        elif id in [3, 4, 5] and (abs(x - centre_x + w) > 2 or abs(y - centre_y - z) > 2):
                                return choices([move_to(robot, centre_x - w, centre_y + z), move(robot)], [1, 1])[0]
                if quadrant == 4:
                        if id in [0, 1, 2] and (abs(x - centre_x - z) > 2 or abs(y - centre_y - w) > 2):
                                return choices([move_to(robot, centre_x + z, centre_y + w), move(robot)], [1, 1])[0]
                        elif id in [3, 4, 5] and (abs(x - centre_x - w) > 2 or abs(y - centre_y - z) > 2):
                                return choices([move_to(robot, centre_x + w, centre_y + z), move(robot)], [1,1])[0]

                return move(robot)                                                    
    if role=='P':
            return move(robot)

def ActBase(base):
    '''
    Add your code here

    '''
        # which robots are made
    wall = True
    enemy_scout = True
    resource = True
    sidewall = True
    raid_robot = True
    random_robot = True

#     wall = False
#     enemy_scout = False
#     resource = False
#     sidewall = False
#     raid_robot = False
#     random_robot = False

    ActBase.timeframe+=1
    ActBase.walltimeframe+=1
    for i in range(1, 5):
            if resource and ActBase.aliveresources[i] == False and ActBase.enemyquadrant == -1:
                #     print("Found quadrant ", i)
                    ActBase.enemyquadrant = i
                    
    
    ActBase.aliveresources = [False, False, False, False, False]

    up = base.investigate_up()
    down = base.investigate_down()
    left = base.investigate_left()
    right = base.investigate_right()
    nw=base.investigate_nw()
    ne=base.investigate_ne()
    sw=base.investigate_sw()
    se=base.investigate_se()


    
    # Kill enemies if they are near
    lst = [up,down,left,right,nw,ne,sw,se]
    if  'enemy' in lst:
            base.DeployVirus(min(200 * lst.count("enemy") , base.GetVirus()))
    if  'enemy' in lst:
            ActBase.unattacked_for = 0
            l = base.GetYourSignal() 

            if l == '':
                base.SetYourSignal("XXXXXXXXH")
            elif len(l) == 8:
                if l[0:4] == 'base':
                        base.SetYourSignal(l+'H')
                        
           
    else:
            ActBase.unattacked_for += 1
            if ActBase.unattacked_for >= threshold_unattacked_for and len(base.GetYourSignal()) > 8 and base.GetYourSignal()[8] == 'H':
                    ActBase.walltimeframe = -5
                    old_sig = base.GetYourSignal()
                    new_sig = old_sig[0:8] + 'S' + old_sig[9:]
                    base.SetYourSignal(new_sig)
                    

        
    #print(ActBase.timeframe)

    #Dimensions of Canvas
    if ActBase.timeframe==0:
        ActBase.cx,ActBase.cy=base.GetDimensionX(),base.GetDimensionY()
        ActBase.posofbase = base.GetPosition()
        ActBase.bcord=base.GetPosition()

    # Wall
    if (ActBase.timeframe == 0) and wall: 
        
        for i in range(1, 9):
            base.create_robot(f'W0{i}')    
            ActBase.last_move[f'W0{i}'] = randint(0,4)   
        # for i in range(10, 17):
        #     base.create_robot(f'W{i}')
        #     ActBase.last_move[f'W{i}'] = randint(0,4) 

#     Collect Resource
    if (ActBase.timeframe == 0) and resource:
        for i in range(5):
                base.create_robot(f'C0{i}')
                ActBase.last_move[f'C0{i}'] = randint(0,4)  

#     Enemy Scout
    if (ActBase.timeframe == 0) and enemy_scout: 
        for i in range(1, 9):
            base.create_robot(f'E0{i}')    
            ActBase.last_move[f'E0{i}'] = randint(0,4)  
            ActBase.Emotion[f'E0{i}'] = i

#     Sidewall
    if (ActBase.timeframe == 0) and sidewall: 
        for i in range(4):
            base.create_robot(f'S0{i}')    
            ActBase.last_move[f'S0{i}'] = randint(0,4)

#   Raid Robots attack possible enemy positions 
    if (ActBase.enemyquadrant > 0 and raid_robot and not ActBase.rayreleased) :
            for i in range(6):
                base.create_robot(f'R0{i}')    
                ActBase.last_move[f'R0{i}'] = randint(0,4) 
            ActBase.rayreleased = True
            
#     more enemy scouts
    if (ActBase.timeframe >= 150 and ActBase.timeframe%150 == 0) and enemy_scout:
            if base.GetElixir() >= 500:
                    for i in range(10, 14):
                            ActBase.Eid += 1
                            base.create_robot(f"E{ActBase.Eid}")
                            ActBase.last_move[f'E{ActBase.Eid}'] = randint(0,4)  
                            ActBase.Emotion[f'E{ActBase.Eid}'] = i-10+3
# random bots
    if ActBase.timeframe % 40 == 0 and ActBase.timeframe >= 50 :
        for i in range(4):
                if base.GetElixir() >= 1300 :
                        ActBase.Pid += 1
                        base.create_robot(f'P{ActBase.Pid}')    
                        ActBase.last_move[f'P{ActBase.Pid}'] = randint(0,4)


    # check if a robot found enemy base
    L = base.GetListOfSignals()
    for l in L:
        if len(l) > 4:
                if(l[0:4] == 'base'):
                        bs = base.GetYourSignal()
                        if len(bs) == 0:
                                base.SetYourSignal(l)
                        elif len(bs) == 9 and bs[8] == 'H':
                                base.SetYourSignal(l+'H')
                return
    return

ActBase.timeframe=-1
ActBase.walltimeframe=-1
ActBase.last_move = {}
ActBase.posofbase = (29, 19) # Is reset above
ActBase.Emotion = {}
threshold_unattacked_for = 30
ActBase.unattacked_for = threshold_unattacked_for

ActBase.aliveresources = [True, True, True, True, True]
ActBase.enemyquadrant = -1
ActBase.rayreleased = False
ActBase.Eid = 10
ActBase.Pid = 10

