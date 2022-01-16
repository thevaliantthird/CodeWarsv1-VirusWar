from random import randint

#to check around robot
# robot.investigate_up()=='' or robot.investigate_left()=='' or robot.investigate_down()=='' or robot.investigate_right()=='' or robot.investigate_ne()=='' or robot.investigate_se()=='' or robot.investigate_nw()=='' or robot.investigate_sw()==''

#to store what all directions are explored
DISCOVERED_ALGO_MESSIAH=[False]*9
#To store position of opponent base to eternity
OPPONENT_BASE_ALGO_MESSIAH=[-1,-1]
MY_BASE_ALGO_MESSIAH=[-1,-1]
def ActRobot(robot):
        #If any robot finds opponent base
        # print('red robot')
        if robot.investigate_up()=='enemy-base' or robot.investigate_left()=='enemy-base' or robot.investigate_down()=='enemy-base' or robot.investigate_right()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_se()=='enemy-base' or robot.investigate_nw()=='enemy-base' or robot.investigate_sw()=='enemy-base':
                robot.DeployVirus(robot.GetVirus())
                
                if robot.investigate_up()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]-1
                        return 3
                elif robot.investigate_right()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]+1
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]
                        return 4
                elif robot.investigate_down()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]+1
                        return 1
                elif robot.investigate_left()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]-1
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]
                        return 2
                elif robot.investigate_ne()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]+1
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]-1
                        return 4
                elif robot.investigate_nw()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]-1
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]-1
                        return 2
                elif robot.investigate_se()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]+1
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]+1
                        return 1
                elif robot.investigate_sw()=='enemy-base':
                        OPPONENT_BASE_ALGO_MESSIAH[0]=robot.GetPosition()[0]-1
                        OPPONENT_BASE_ALGO_MESSIAH[1]=robot.GetPosition()[1]+1
                        return 1
        #life signal of coll robots
        if robot.GetInitialSignal()[0:4]=='coll':
                robot.setSignal('Alive'+robot.GetInitialSignal())
        #IF opponent base is found and search robots are still not dead
        if OPPONENT_BASE_ALGO_MESSIAH[0]!=-1 and robot.GetInitialSignal()[0:3]!='bpr' and robot.GetInitialSignal()[0:4]!='coll':
                #send this robot to opponent base
                if robot.investigate_up()=='friend' or robot.investigate_left()=='friend' or robot.investigate_down()=='friend' or robot.investigate_right()=='friend' or robot.investigate_ne()=='friend' or robot.investigate_se()=='friend' or robot.investigate_nw()=='friend' or robot.investigate_sw()=='friend':
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-2 and robot.investigate_se()=='friend':
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-1 and (robot.investigate_right()=='friend' or robot.investigate_se()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1] and (robot.investigate_right()=='friend' or robot.investigate_se()=='friend' or robot.investigate_ne()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+1 and (robot.investigate_right()=='friend' or robot.investigate_ne()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+2 and robot.investigate_ne()=='friend':
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-2 and robot.investigate_sw()=='friend':
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-1 and (robot.investigate_left()=='friend' or robot.investigate_sw()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1] and (robot.investigate_left()=='friend' or robot.investigate_sw()=='friend' or robot.investigate_nw()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+1 and (robot.investigate_left()=='friend' or robot.investigate_nw()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+2 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+2 and robot.investigate_nw()=='friend':
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-1 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-2 and (robot.investigate_down()=='friend' or robot.investigate_se()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]-1 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+2 and (robot.investigate_up()=='friend' or robot.investigate_ne()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0] and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-2 and (robot.investigate_down()=='friend' or robot.investigate_se()=='friend' or robot.investigate_sw()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0] and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+2 and (robot.investigate_up()=='friend' or robot.investigate_ne()=='friend' or robot.investigate_nw()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+1 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]-2 and (robot.investigate_down()=='friend' or robot.investigate_sw()=='friend'):
                                return 0
                        if robot.GetPosition()[0]==OPPONENT_BASE_ALGO_MESSIAH[0]+1 and robot.GetPosition()[1]==OPPONENT_BASE_ALGO_MESSIAH[1]+2 and (robot.investigate_up()=='friend' or robot.investigate_nw()=='friend'):
                                return 0
                in_x=0
                in_y=1
                if robot.GetPosition()[0]+in_x!=OPPONENT_BASE_ALGO_MESSIAH[0]:
                        if robot.GetPosition()[0]+in_x>OPPONENT_BASE_ALGO_MESSIAH[0]:
                                if robot.investigate_left()=='enemy':
                                        robot.DeployVirus(min(500,robot.GetVirus()))
                                return 4
                        else:
                                if robot.investigate_right()=='enemy':
                                        robot.DeployVirus(min(500,robot.GetVirus()))
                                return 2
                if robot.GetPosition()[1]+in_y!=OPPONENT_BASE_ALGO_MESSIAH[1]:
                        if robot.GetPosition()[1]+in_y>OPPONENT_BASE_ALGO_MESSIAH[1]:
                                if robot.investigate_up()=='enemy':
                                        robot.DeployVirus(min(500,robot.GetVirus()))
                                return 1
                        else:
                                if robot.investigate_down()=='enemy':
                                        robot.DeployVirus(min(500,robot.GetVirus()))
                                return 3
        # #if search robots are found dead:
        if robot.GetCurrentBaseSignal()=='ATT1':
                if robot.GetInitialSignal()[0:4]=='coll' and int(robot.GetInitialSignal()[5]) in range(0,4):
                        #send this robot to opponent base
                        if robot.investigate_up()=='enemy-base' or robot.investigate_left()=='enemy-base' or robot.investigate_down()=='enemy-base' or robot.investigate_right()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_se()=='enemy-base' or robot.investigate_nw()=='enemy-base' or robot.investigate_sw()=='enemy-base':
                                robot.DeployVirus(robot.GetVirus())
                                if robot.investigate_up()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_nw()=='enemy-base':
                                        return 3
                                if robot.investigate_down()=='enemy-base' or robot.investigate_se()=='enemy-base' or robot.investigate_sw()=='enemy-base':
                                        return 1
                                if robot.investigate_left()=='enemy-base':
                                        return 2
                                if robot.investigate_right()=='enemy-base':
                                        return 4
                        if robot.investigate_up()=='friend' or robot.investigate_left()=='friend' or robot.investigate_down()=='friend' or robot.investigate_right()=='friend' or robot.investigate_ne()=='friend' or robot.investigate_se()=='friend' or robot.investigate_nw()=='friend' or robot.investigate_sw()=='friend':
                                return 0
                        randlist=[-1,1,0]
                        in_x=-1
                        in_y=1
                        if robot.GetPosition()[0]+in_x!=OPPONENT_BASE_ALGO_MESSIAH[0]:
                                if robot.GetPosition()[0]+in_x>OPPONENT_BASE_ALGO_MESSIAH[0]:
                                        if robot.investigate_left()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 4
                                else:
                                        if robot.investigate_right()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 2
                        if robot.GetPosition()[1]+in_y!=OPPONENT_BASE_ALGO_MESSIAH[1]:
                                if robot.GetPosition()[1]+in_y>OPPONENT_BASE_ALGO_MESSIAH[1]:
                                        if robot.investigate_up()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 1
                                else:
                                        if robot.investigate_down()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 3
        #if ATT2 needed:
        if robot.GetCurrentBaseSignal()=='ATT2':
                if robot.GetInitialSignal()[0:4]=='coll' and int(robot.GetInitialSignal()[5]) in range(4,6):
                        #send this robot to opponent base
                        if robot.investigate_up()=='enemy-base' or robot.investigate_left()=='enemy-base' or robot.investigate_down()=='enemy-base' or robot.investigate_right()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_se()=='enemy-base' or robot.investigate_nw()=='enemy-base' or robot.investigate_sw()=='enemy-base':
                                robot.DeployVirus(robot.GetVirus())
                                if robot.investigate_up()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_nw()=='enemy-base':
                                        return 3
                                if robot.investigate_down()=='enemy-base' or robot.investigate_se()=='enemy-base' or robot.investigate_sw()=='enemy-base':
                                        return 1
                                if robot.investigate_left()=='enemy-base':
                                        return 2
                                if robot.investigate_right()=='enemy-base':
                                        return 4
                        if robot.investigate_up()=='friend' or robot.investigate_left()=='friend' or robot.investigate_down()=='friend' or robot.investigate_right()=='friend' or robot.investigate_ne()=='friend' or robot.investigate_se()=='friend' or robot.investigate_nw()=='friend' or robot.investigate_sw()=='friend':
                                return 0
                        randlist=[-1,1,0]
                        in_x=randlist[randint(0,2)]
                        in_y=randlist[randint(0,2)]
                        if robot.GetPosition()[0]+in_x!=OPPONENT_BASE_ALGO_MESSIAH[0]:
                                if robot.GetPosition()[0]+in_x>OPPONENT_BASE_ALGO_MESSIAH[0]:
                                        if robot.investigate_left()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 4
                                else:
                                        if robot.investigate_right()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 2
                        if robot.GetPosition()[1]+in_y!=OPPONENT_BASE_ALGO_MESSIAH[1]:
                                if robot.GetPosition()[1]+in_y>OPPONENT_BASE_ALGO_MESSIAH[1]:
                                        if robot.investigate_up()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 1
                                else:
                                        if robot.investigate_down()=='enemy':
                                                robot.DeployVirus(min(robot.GetVirus(),500))
                                        return 3
         
        #search robots
        if True:
                #this robot is to go up to find enemy-base
                # base.create_robot('1'+str(base.GetPosition()[0]))#to go n(1)
                if robot.GetInitialSignal()[0]=='1':
                        robot.setSignal('Alives1')
                        if DISCOVERED_ALGO_MESSIAH[0]:
                                return randint(1,4)
                        #if enemy base is above
                        if robot.GetPosition()[0]==MY_BASE_ALGO_MESSIAH[0] and robot.GetPosition()[1]==MY_BASE_ALGO_MESSIAH[1]:
                                return 2
                        if robot.investigate_up()=='enemy':
                                robot.DeployVirus(robot.GetVirus()/2)
                        #if top is reached
                        if robot.GetPosition()[1]==0:
                                DISCOVERED_ALGO_MESSIAH[0]=True
                                return randint(1,4)
                        return 1
                #this robot is to go right to find enemy-base
                # base.create_robot('2'+str(base.GetPosition()[1]))#to go e(2)
                if robot.GetInitialSignal()[0]=='2':
                        robot.setSignal('Alives2')
                        #if reached rightmost
                        if DISCOVERED_ALGO_MESSIAH[1]:
                                return randint(1,4)
                        if robot.GetPosition()[0]==MY_BASE_ALGO_MESSIAH[0] and robot.GetPosition()[1]==MY_BASE_ALGO_MESSIAH[1]:
                                return 3
                        if robot.investigate_right()=='enemy':
                                robot.DeployVirus(robot.GetVirus()/2)
                        if robot.GetPosition()[0]==robot.GetDimensionX()-1:
                                DISCOVERED_ALGO_MESSIAH[1]=True
                                return randint(1,4)
                        return 2
                #this robot is to go down to find enemy-base
                # base.create_robot('3'+str(base.GetPosition()[0]))#to go s(3)
                if robot.GetInitialSignal()[0]=='3':
                        robot.setSignal('Alives3')
                        #explored 3
                        if DISCOVERED_ALGO_MESSIAH[2]:
                                return randint(1,4)
                        if robot.GetPosition()[0]==MY_BASE_ALGO_MESSIAH[0] and robot.GetPosition()[1]==MY_BASE_ALGO_MESSIAH[1]:
                                return 4
                        if robot.investigate_down()=='enemy':
                                robot.DeployVirus(robot.GetVirus()/2)
                        #if bottom is reached
                        if robot.GetPosition()[1]==robot.GetDimensionY()-1:
                                DISCOVERED_ALGO_MESSIAH[2]=True
                                return randint(1,4) #starting to right
                        return 3
                #this robot is to go left to find enemy-base
                # base.create_robot('4'+str(base.GetPosition()[1]))#to go w(4)
                if robot.GetInitialSignal()[0]=='4':
                        robot.setSignal('Alives4')
                        #if top is reached some day
                        if DISCOVERED_ALGO_MESSIAH[3]:
                                return randint(1,4)
                        if robot.GetPosition()[0]==MY_BASE_ALGO_MESSIAH[0] and robot.GetPosition()[1]==MY_BASE_ALGO_MESSIAH[1]:
                                return 1
                        if robot.investigate_left()=='enemy':
                                robot.DeployVirus(robot.GetVirus()/2)
                        #if left is reached
                        if robot.GetPosition()[0]==0:
                                DISCOVERED_ALGO_MESSIAH[3]=True
                                return randint(1,4)                
                        return 4
                #this robot is to go ne to find enemy-base
                # base.create_robot('ne'+basepos)#to go ne(5)
                if robot.GetInitialSignal()[0:2]=='ne':
                        robot.setSignal('Alives5')
                        if DISCOVERED_ALGO_MESSIAH[4]:
                                return randint(1,4)
                        x_base=int(robot.GetInitialSignal()[2:4])
                        y_base=int(robot.GetInitialSignal()[4:6])
                        x_pos=robot.GetPosition()[0]
                        y_pos=robot.GetPosition()[1]
                        if y_base-y_pos+1<x_pos-x_base:
                                return randint(1,4)
                        
                        if y_base-y_pos==x_pos-x_base:
                                if y_pos==0 or x_pos==robot.GetDimensionX()-1:
                                        DISCOVERED_ALGO_MESSIAH[4]=True
                                        return 3
                                if robot.investigate_up()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 1
                        elif y_base-y_pos>x_pos-x_base:
                                if robot.investigate_right()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 2
                        else:
                                return 3
                #this robot is to go nw to find enemy-base
                # base.create_robot('nw'+basepos)#to go nw(8)
                if robot.GetInitialSignal()[0:2]=='nw':
                        robot.setSignal('Alives8')
                        if DISCOVERED_ALGO_MESSIAH[7]:
                                return randint(1,4)
                        x_base=int(robot.GetInitialSignal()[2:4])
                        y_base=int(robot.GetInitialSignal()[4:6])
                        x_pos=robot.GetPosition()[0]
                        y_pos=robot.GetPosition()[1]
                        if y_base-y_pos+1<x_base-x_pos:
                                return randint(1,4)
                        
                        if y_base-y_pos==x_base-x_pos:
                                if y_pos==0 or x_pos==0:
                                        DISCOVERED_ALGO_MESSIAH[7]=True
                                        return 3
                                if robot.investigate_up()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 1
                        elif y_base-y_pos>x_pos-x_base:
                                if robot.investigate_left()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 4
                        else:
                                return 3
                #this robot is to go se to find enemy-base
                # base.create_robot('se'+basepos)#to go se(6)
                if robot.GetInitialSignal()[0:2]=='se':
                        robot.setSignal('Alives6')
                        if DISCOVERED_ALGO_MESSIAH[5]:
                                return randint(1,4)
                        x_base=int(robot.GetInitialSignal()[2:4])
                        y_base=int(robot.GetInitialSignal()[4:6])
                        x_pos=robot.GetPosition()[0]
                        y_pos=robot.GetPosition()[1]
                        if y_pos-y_base+1<x_pos-x_base:
                                return randint(1,4)
                        
                        if y_pos-y_base==x_pos-x_base:
                                if y_pos==robot.GetDimensionY()-1 or x_pos==robot.GetDimensionX()-1:
                                        DISCOVERED_ALGO_MESSIAH[5]=True
                                        return 1
                                if robot.investigate_down()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 3
                        elif y_pos-y_base>x_pos-x_base:
                                if robot.investigate_right()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 2
                        else:
                                return 1
                #this robot is to go sw to find enemy-base
                # base.create_robot('sw'+basepos)#to go sw(7)
                if robot.GetInitialSignal()[0:2]=='sw':
                        if DISCOVERED_ALGO_MESSIAH[6]:
                                return randint(1,4)
                        robot.setSignal('Alives7')
                        x_base=int(robot.GetInitialSignal()[2:4])
                        y_base=int(robot.GetInitialSignal()[4:6])
                        x_pos=robot.GetPosition()[0]
                        y_pos=robot.GetPosition()[1]
                        if y_pos-y_base+1<x_base-x_pos:
                                return randint(1,4)
                        
                        if y_pos-y_base==x_base-x_pos:
                                if y_pos==robot.GetDimensionY()-1 or x_pos==0:
                                        DISCOVERED_ALGO_MESSIAH[6]=True
                                        return 1
                                if robot.investigate_down()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 3
                        elif y_pos-y_base>x_base-x_pos:
                                if robot.investigate_left()=='enemy':
                                        robot.DeployVirus(robot.GetVirus()/2)
                                return 4
                        else:
                                return 1
                #this robot is to go about center to find enemy base
                # base.create_robot('o'+basepos)#to go origin(9)
                if robot.GetInitialSignal()[0]=='o':
                        if DISCOVERED_ALGO_MESSIAH[8]:
                                return randint(1,4)
                        robot.setSignal('Alives9')
                        #expected position of enemy base is:(x_opp,y_opp)
                        x_base=int(robot.GetInitialSignal()[1:3])
                        y_base=int(robot.GetInitialSignal()[3:5])
                        x_opp=robot.GetDimensionX()-1-x_base
                        y_opp=robot.GetDimensionY()-1-y_base
                        x_pos=robot.GetPosition()[0]
                        y_pos=robot.GetPosition()[1]
                        
                        if x_opp==x_pos and y_opp==y_pos:
                                DISCOVERED_ALGO_MESSIAH[8]=True
                                return randint(1,4)
                        if x_opp!=x_pos:
                                if x_opp>x_pos:
                                        if robot.investigate_right()=='enemy':
                                                robot.DeployVirus(robot.GetVirus()/2)
                                        return 2
                                else:
                                        if robot.investigate_left()=='enemy':
                                                robot.DeployVirus(robot.GetVirus()/2)
                                        return 4
                        if y_opp!=y_pos:
                                if y_opp>y_pos:
                                        if robot.investigate_down()=='enemy':
                                                robot.DeployVirus(robot.GetVirus()/2)
                                        return 3
                                else:
                                        if robot.investigate_up()=='enemy':
                                                robot.DeployVirus(robot.GetVirus()/2)
                                        return 1
        #base protection robots
        if True:
                #robot is on e,ne
                # base.create_robot('bpr1'+basepos)#base protection on e,ne
                if robot.GetInitialSignal()[0:4]=='bpr1':
                        robot.setSignal('Alivebpr1')
                        x_base=int(robot.GetInitialSignal()[4:6])
                        y_base=int(robot.GetInitialSignal()[6:8])
                        #e==x_base+1,y_base
                        #ne==x_base+1,y_base-1
                        if robot.GetPosition()[0]==x_base+1 and robot.GetPosition()[1]==y_base:
                                return 1
                        if robot.GetPosition()[0]==x_base+1 and robot.GetPosition()[1]==y_base-1:
                                return 3
                        if robot.GetPosition()[0]!=x_base+1:
                                if robot.GetPosition()[0]>x_base+1:
                                        return 4
                                return 2
                        if robot.GetPosition()[1]!=y_base:
                                if robot.GetPosition()[1]>y_base:
                                        return 1
                                else:
                                        return 3
                #robot is on n,nw
                # base.create_robot('bpr2'+basepos)#base protection on n,nw
                if robot.GetInitialSignal()[0:4]=='bpr2':
                        robot.setSignal('Alivebpr2')
                        x_base=int(robot.GetInitialSignal()[4:6])
                        y_base=int(robot.GetInitialSignal()[6:8])
                        #n==x_base,y_base-1
                        #nw==x_base-1,y_base-1
                        if robot.GetPosition()[0]==x_base and robot.GetPosition()[1]==y_base-1:
                                return 4
                        if robot.GetPosition()[0]==x_base-1 and robot.GetPosition()[1]==y_base-1:
                                return 2
                        if robot.GetPosition()[0]!=x_base:
                                if robot.GetPosition()[0]>x_base:
                                        return 4
                                return 2
                        if robot.GetPosition()[1]!=y_base-1:
                                if robot.GetPosition()[1]>y_base-1:
                                        return 1
                                else:
                                        return 3
                #robot is on w,sw
                # base.create_robot('bpr3'+basepos)#base protection on w,sw
                if robot.GetInitialSignal()[0:4]=='bpr3':
                        robot.setSignal('Alivebpr3')
                        x_base=int(robot.GetInitialSignal()[4:6])
                        y_base=int(robot.GetInitialSignal()[6:8])
                        #w==x_base-1,y_base
                        #sw==x_base-1,y_base+1
                        if robot.GetPosition()[0]==x_base-1 and robot.GetPosition()[1]==y_base:
                                return 3
                        if robot.GetPosition()[0]==x_base-1 and robot.GetPosition()[1]==y_base+1:
                                return 1
                        if robot.GetPosition()[0]!=x_base-1:
                                if robot.GetPosition()[0]>x_base-1:
                                        return 4
                                return 2
                        if robot.GetPosition()[1]!=y_base:
                                if robot.GetPosition()[1]>y_base:
                                        return 1
                                else:
                                        return 3
                #robot is on s,se
                # base.create_robot('bpr4'+basepos)#base protection on s,se
                if robot.GetInitialSignal()[0:4]=='bpr4':
                        robot.setSignal('Alivebpr4')
                        x_base=int(robot.GetInitialSignal()[4:6])
                        y_base=int(robot.GetInitialSignal()[6:8])
                        #s==x_base,y_base+1
                        #se==x_base+1,y_base+1
                        if robot.GetPosition()[0]==x_base and robot.GetPosition()[1]==y_base+1:
                                return 2
                        if robot.GetPosition()[0]==x_base+1 and robot.GetPosition()[1]==y_base+1:
                                return 4
                        if robot.GetPosition()[0]!=x_base:
                                if robot.GetPosition()[0]>x_base:
                                        return 4
                                return 2
                        if robot.GetPosition()[1]!=y_base+1:
                                if robot.GetPosition()[1]>y_base+1:
                                        return 1
                                else:
                                        return 3
        #collection squad
        # base.create_robot('coll0'+basepos)        
        if robot.GetInitialSignal()[0:4]=='coll':
                robot.setSignal('Alive'+robot.GetInitialSignal())
                x_base=int(robot.GetInitialSignal()[5:7])
                y_base=int(robot.GetInitialSignal()[7:9])
                x_map=robot.GetDimensionX()
                y_map=robot.GetDimensionY()
                if int(robot.GetInitialSignal()[4]) in range(0,4):
                        if robot.investigate_up()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_se()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_sw()=='enemy':
                                robot.DeployVirus(min(500,robot.GetVirus()))
                        randint(1,4)
                else:
                        y=abs(y_map//2-y_base)
                        x=abs(x_map//2-x_base)
                        if x>y:
                                if x_base>x_map//2:
                                        if robot.GetPosition()[0]>x_map//2-5:
                                                return randint(1,4)
                                        else:
                                                return 2
                                else:
                                        if robot.GetPosition()[0]<x_map//2+5:
                                                return randint(1,4)
                                        else:
                                                return 4
                        else:
                                if y_base>y_map//2:
                                        if robot.GetPosition()[1]>y_map//2-5:
                                                return randint(1,4)
                                        else:
                                                return 3
                                else:
                                        if robot.GetPosition()[1]<y_map//2+5:
                                                return randint(1,4)
                                        else:
                                                return 1
        return randint(1,4)


def ActBase(base):
        # print('red base')
        # print(OPPONENT_BASE_ALGO_MESSIAH)
        MY_BASE_ALGO_MESSIAH[0]=base.GetPosition()[0]
        MY_BASE_ALGO_MESSIAH[1]=base.GetPosition()[1]
        #to get pos of base as a string
        basepos=''
        if base.GetPosition()[0]<10:
                basepos+='0'+str(base.GetPosition()[0])
        else:
                basepos+=str(base.GetPosition()[0])
        if base.GetPosition()[1]<10:
                basepos+='0'+str(base.GetPosition()[1])
        else:
                basepos+=str(base.GetPosition()[1])
        #pos of base of string made

        if base.GetElixir() == 2000:
                #search robot creation in all symm dirns
                base.create_robot('1'+str(base.GetPosition()[0]))#to go n(1)
                base.create_robot('2'+str(base.GetPosition()[1]))#to go e(2)
                base.create_robot('3'+str(base.GetPosition()[0]))#to go s(3)
                base.create_robot('4'+str(base.GetPosition()[1]))#to go w(4)
                base.create_robot('ne'+basepos)#to go ne(5)
                base.create_robot('nw'+basepos)#to go nw(8)
                base.create_robot('se'+basepos)#to go se(6)
                base.create_robot('sw'+basepos)#to go sw(7)
                base.create_robot('o'+basepos)#to go origin(9)
                base.create_robot('bpr1'+basepos)#base protection on e,ne
                base.create_robot('bpr2'+basepos)#base protection on n,nw
                base.create_robot('bpr3'+basepos)#base protection on w,sw
                base.create_robot('bpr4'+basepos)#base protection on s,se
                base.create_robot('coll0'+basepos)#brave collector
                base.create_robot('coll1'+basepos)#brave collector
                base.create_robot('coll2'+basepos)#brave collector
                base.create_robot('coll3'+basepos)#brave collector
                base.create_robot('coll4'+basepos)#coward collector
                base.create_robot('coll5'+basepos)#coward collector
                base.create_robot('coll6'+basepos)#coward collector
                base.create_robot('coll7'+basepos)#coward collector
                base.create_robot('coll4'+basepos)#coward collector
                base.create_robot('coll5'+basepos)#coward collector
                base.create_robot('coll6'+basepos)#coward collector
                base.create_robot('coll7'+basepos)#coward collector
                return

        if base.investigate_up()=='enemy' or base.investigate_down()=='enemy' or base.investigate_left()=='enemy' or base.investigate_right()=='enemy' or base.investigate_ne()=='enemy' or base.investigate_se()=='enemy' or base.investigate_nw()=='enemy' or base.investigate_sw()=='enemy':
                base.DeployVirus(base.GetVirus())
        

        Signals=base.GetListOfSignals()
        DICOVERING=[False]*9
        
        Discovering=[False]*9
        Protecting=[False]*4
        Collecting=[False]*8
        for i in range(0,len(Signals)):
                if OPPONENT_BASE_ALGO_MESSIAH[0]==-1:
                        if Signals[i][0:4]=='base':
                                OPPONENT_BASE_ALGO_MESSIAH[0]=int(Signals[i][5:7])
                                OPPONENT_BASE_ALGO_MESSIAH[1]=int(Signals[i][7:9])
                                #opponent base found!!
                if Signals[i][0:5]=='Alive':
                        if Signals[i][5]=='s':
                                Discovering[int(Signals[i][6])-1]=True
                        elif Signals[i][5:8]=='bpr':
                                Protecting[int(Signals[i][8])-1]=True
                        if Signals[i][5]=='c':
                                Collecting[int(Signals[i][9])]=True
        #to create dead discovering robots if needed
        if OPPONENT_BASE_ALGO_MESSIAH[0]==-1:
                for j in range(0,9):
                        if ((not DISCOVERED_ALGO_MESSIAH[j]) and (not Discovering[j])):
                                if j==0 and base.GetElixir()>600:
                                        base.create_robot('1'+str(base.GetPosition()[0]))#to go n(1)
                                elif j==1 and base.GetElixir()>600:
                                        base.create_robot('2'+str(base.GetPosition()[1]))#to go e(2)
                                elif j==2 and base.GetElixir()>600:
                                        base.create_robot('3'+str(base.GetPosition()[0]))#to go s(3)
                                elif j==3 and base.GetElixir()>600:
                                        base.create_robot('4'+str(base.GetPosition()[1]))#to go w(4)
                                elif j==4 and base.GetElixir()>600:
                                        base.create_robot('ne'+basepos)#to go ne(5)
                                elif j==5 and base.GetElixir()>600:
                                        base.create_robot('se'+basepos)#to go se(6)
                                elif j==6 and base.GetElixir()>600:
                                        base.create_robot('sw'+basepos)#to go sw(7)
                                elif j==7 and base.GetElixir()>600:
                                        base.create_robot('nw'+basepos)#to go nw(8)
                                elif j==8 and base.GetElixir()>600:
                                        base.create_robot('o'+basepos)#to go origin(9)
        # to create dead bprs:
        for i in range(0,4):
                if not Protecting[i] and base.GetElixir()>200:
                        base.create_robot('bpr'+str(i+1)+basepos)
        #to send coll robots to opp base if needed
        if Discovering==[False]*9 and OPPONENT_BASE_ALGO_MESSIAH[0]!=-1:
                if Collecting[0:4]!=[False]*4:
                        base.SetYourSignal('ATT1')
                elif base.GetElixir()>500:
                        for p in range(0,4):
                                if base.GetElixir()>500:
                                        base.create_robot('coll'+str(p)+basepos)
                else:
                        base.SetYourSignal('ATT2')

        