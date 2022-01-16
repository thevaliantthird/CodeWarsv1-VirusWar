from random import randint, seed
import numpy as np
from numpy.core.numeric import identity

def to_str(num): #converts int to 2 places string
        if num < 10:
                str_num = '0'+str(num)
        else:
             str_num = str(num)
        return str_num 


def ActRobot(robot):
     inisig = robot.GetInitialSignal()
     id = int(inisig[0:2])
     base_x = int(inisig[2:4])
     base_y = int(inisig[4:6])
     canvas_size = (robot.GetDimensionX(), robot.GetDimensionY())

     curr_pos = robot.GetPosition() #tuple
     goal = get_goal(id, (base_x,base_y), canvas_size)
     out = move_to(goal, curr_pos,id)
     
     while robot.GetVirus() > 100:
             up = robot.investigate_up()
             down = robot.investigate_down()
             left = robot.investigate_left()
             right = robot.investigate_right()
             ne = robot.investigate_ne()
             nw = robot.investigate_nw()
             se = robot.investigate_se()
             sw = robot.investigate_sw()

             if(up == 'enemy' or right == 'enemy' or left == 'enemy' or down == 'enemy' or ne == 'enemy' or se == 'enemy' or nw == 'enemy' or sw == 'enemy' ):
                     robot.DeployVirus(100)
             elif(up == 'enemy-base' or right == 'enemy-base' or left == 'enemy-base' or down == 'enemy-base' or ne == 'enemy-base' or se == 'enemy-base' or nw == 'enemy-base' or sw == 'enemy-base' ):
                     robot.DeployVirus(100)
             else:
                      break  
     
     return out

   


def ActBase(base):
 
 x,y = base.GetPosition()
 str_x = to_str(x)
 str_y = to_str(y)
 id = 0
 str_id = to_str(id)
 while base.GetElixir()>500:
         base.create_robot(str_id + str_x + str_y) #id(2)+baselocation(4) eg. robot1 at(19,9) so id = 01199
 #7 defenders, rest attackers
 #id 1-7 defenders >7 attackers
 while base.GetVirus() > 100:
             up = base.investigate_up()
             down = base.investigate_down()
             left = base.investigate_left()
             right = base.investigate_right()
             ne = base.investigate_ne()
             nw = base.investigate_nw()
             se = base.investigate_se()
             sw = base.investigate_sw()

             if(up == 'enemy' or right == 'enemy' or left == 'enemy' or down == 'enemy' or ne == 'enemy' or se == 'enemy' or nw == 'enemy' or sw == 'enemy' ):
                     base.DeployVirus(100)
             else :
                     break

 return

def in_canvas(pos, canvas_size):
        if pos[0]<0 or pos[0]>=canvas_size[0]:
                return False
        if pos[1]<0 or pos[1]>=canvas_size[1]:
                return False
        return True        

def get_goal(id, base_pos, canvas_size):
        if id < 7:
                #Defender
                
                add_x = randint(-20,20)
                add_y = randint(-20,20)
                x,y = np.array(base_pos) + np.array([add_x, add_y])
                while not in_canvas((x,y), canvas_size):
                         add_x = randint(-15,15)
                         add_y = randint(-15,15)
                         x,y = np.array(base_pos) + np.array([add_x, add_y])
        else:
                x,y = np.array(canvas_size) - np.array(base_pos) #Attacker
        return (x,y)

def move_to(goal, curr_pos, id):
         pos = goal
         if (np.array(pos) == curr_pos).all() :
                return 0
         if pos[0] == curr_pos[0]:
                return 2 - np.sign(curr_pos[1]+pos[1])
         if pos[1] == curr_pos[1]:
                return 3 + np.sign(curr_pos[1]-pos[1]) 

         if randint(0,1):
                 return 2 - np.sign(curr_pos[1]-pos[1])
         if id>7:
                 return randint(1,4)

         else:
                 return 3 + np.sign(curr_pos[0]-pos[0])