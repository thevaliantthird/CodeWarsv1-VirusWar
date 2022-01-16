from random import randint,choice
from collections import defaultdict

#0-stay 1-up 2-right 3-down 4-left
#robot signal- a/g/s/x/c
#a- right, up, count, current_dir  a120
#g- orientation, count, new, shift, moves
#s-
#x- corner, orientation, count xt0
#c- right, up, count, current_dir
#h- enemy_x, enemy_y
#f- orientation, new
def interpretdir(c):
        if c=='l':
                return 4
        elif c=='r':
                return 2
        elif c=='d':
                return 3
        elif c=='u':
                return 1
def inversedir(c):
        if c=='r':
                return 'u'
        elif c=='u':
                return 'r'
def flipmovement(c):
        if c=='u':
                return 'd'
        elif c=='d':
                return 'u'
        elif c=='r':
                return 'l'
        elif c=='l':
                return 'r'
def anticlockwise(c):
        if c=='r':
                return 'u'
        elif c=='u':
                return 'l'
        elif c=='l':
                return 'd'
        elif c=='d':
                return 'r'
def clockwise(c):
        if c=='r':
                return 'd'
        elif c=='d':
                return 'l'
        elif c=='l':
                return 'u'
        elif c=='u':
                return 'r'
def bounce(robot, own_signal):
        if robot.investigate_up()=="wall" or robot.investigate_down()=="wall":
                own_signal=own_signal[:2]+str(3-int(own_signal[2]))+own_signal[3:]
        if robot.investigate_left()=="wall" or robot.investigate_right()=="wall":
                own_signal=own_signal[:1]+str(3-int(own_signal[1]))+own_signal[2:]
        return own_signal
def fbounce(robot, own_signal):
        if robot.investigate_up()=="wall" or robot.investigate_down()=="wall" or robot.investigate_left()=="wall" or robot.investigate_right()=="wall":
                own_signal=own_signal[0]+flipmovement(own_signal[1])+own_signal[2]
        return own_signal
def ActRobot(robot):
        #robot.addResource(1000)
        enemy_found=LetsDeploy(robot)
        own_signal=robot.GetYourSignal()
        base_signal=robot.GetCurrentBaseSignal()
        game_x=robot.GetDimensionX()
        game_y=robot.GetDimensionY()
        if own_signal=='':
                own_signal=robot.GetInitialSignal()
        base_signal=robot.GetCurrentBaseSignal()
        partitioned_base_signal=base_signal.split('-')
        base_x=int(partitioned_base_signal[0])
        base_y=int(partitioned_base_signal[1])
        flag=partitioned_base_signal[2]
        base_found=partitioned_base_signal[3]
        if base_found=='y' and len(partitioned_base_signal)>=6:
                enemy_base_x=int(partitioned_base_signal[4])
                enemy_base_y=int(partitioned_base_signal[5])
        if enemy_found=="enemy_bot":
                ReleaseVirus(robot, own_signal)
        if enemy_found=="stay":
                robot_x,robot_y=robot.GetPosition()
                robot.setSignal("e"+"-"+str(robot_x)+"-"+str(robot_y))
                r=robot.GetVirus()
                robot.DeployVirus(r//1)
                return 0
        elif len(own_signal)!=0 and own_signal[0]=='a':
                if base_found=='y' and len(partitioned_base_signal)>=6:
                        robot.setSignal('h'+'-'+str(enemy_base_x)+'-'+str(enemy_base_y))
                        return 0
                own_signal=bounce(robot, own_signal)
                move_right=int(own_signal[1])
                move_up=int(own_signal[2])
                if move_right==2:
                        move_right=-1
                if move_up==2:
                        move_up=-1
                count=int(own_signal[3])
                current_dir=own_signal[4]
                if count<2:
                        count+=1
                else:
                        count=0
                        current_dir=inversedir(current_dir)
                temp_dir=current_dir
                if temp_dir=='r':
                        if move_right==-1:
                                temp_dir='l'
                if temp_dir=='u':
                        if move_up==-1:
                                temp_dir='d'
                tbr=interpretdir(temp_dir)
                own_signal=own_signal[:3]+str(count)+current_dir
                robot.setSignal(own_signal)
                return tbr
        elif len(own_signal)!=0 and own_signal[0]=='f':
                if base_found=='y' and len(partitioned_base_signal)>=6:
                        robot.setSignal('h'+'-'+str(enemy_base_x)+'-'+str(enemy_base_y))
                        return 0
                own_signal=fbounce(robot, own_signal)
                orientation=own_signal[1]
                isnew=own_signal[2]
                if isnew=='n':
                        isnew='o'
                        own_signal=own_signal[0]+clockwise(orientation)+isnew
                        robot.setSignal(own_signal)
                        return interpretdir(orientation)
                else:
                        robot.setSignal(own_signal)
                        return interpretdir(orientation)
        elif len(own_signal)!=0 and own_signal[0]=='c':
                if base_found=='y' and len(partitioned_base_signal)>=6:
                        robot.setSignal('h'+'-'+str(enemy_base_x)+'-'+str(enemy_base_y))
                        return 0
                own_signal=bounce(robot, own_signal)
                move_right=int(own_signal[1])
                move_up=int(own_signal[2])
                if move_right==2:
                        move_right=-1
                if move_up==2:
                        move_up=-1
                count=int(own_signal[3])
                current_dir=own_signal[4]
                if count<3:
                        count+=1
                elif count<4:
                        count+=1
                        current_dir=inversedir(current_dir)
                else:
                        count=0
                        current_dir=inversedir(current_dir)
                temp_dir=current_dir
                if temp_dir=='r' and move_right==-1:
                        temp_dir='l'
                if temp_dir=='u' and move_up==-1:
                        temp_dir='d'
                tbr=interpretdir(temp_dir)
                own_signal=own_signal[:3]+str(count)+current_dir
                robot.setSignal(own_signal)
                return tbr
        elif len(own_signal)!=0 and own_signal[0]=='g':
                orientation=own_signal[1]
                count=own_signal[2]
                isnew=own_signal[3]
                shift=own_signal[4]
                moves=int(own_signal[5:])
                if enemy_found=="enemy_bot":
                        count=1
                        own_signal=own_signal[:2]+str(count)+own_signal[3:]
                else:
                        count=0
                        own_signal=own_signal[:2]+str(count)+own_signal[3:]
                if shift=='2':
                        if isnew=='n':
                                moves+=1
                                own_signal=own_signal[:3]+'f'+own_signal[4]+str(moves) #this can be a source of errors with longer strings
                                robot.setSignal(own_signal)
                                return interpretdir(orientation)
                        elif moves<=2:
                                moves+=1
                                if moves==3:
                                        orientation=anticlockwise(orientation)
                                own_signal=own_signal[0]+orientation+own_signal[2:5]+str(moves)
                                robot.setSignal(own_signal)
                                return interpretdir(orientation)
                        elif isnew=='f' and moves<=11:
                                moves+=1
                                if moves==12:
                                        orientation=flipmovement(orientation)
                                own_signal=own_signal[0]+orientation+own_signal[2:5]+str(moves)
                                robot.setSignal(own_signal)
                                return interpretdir(orientation)
                        elif isnew=='f' and moves<=19:
                                moves+=1
                                if moves==20:
                                        isnew='o'
                                own_signal=own_signal[0]+orientation+own_signal[2]+isnew+own_signal[4]+str(moves)
                                robot.setSignal(own_signal)
                                if robot.GetDimensionX()==base_x or robot.GetDimensionY()==base_y:
                                        return 0
                                else:
                                        return interpretdir(orientation)
                        elif moves<=100:
                                moves+=1
                                own_signal=own_signal[:5]+str(moves)
                                robot.setSignal(own_signal)
                                return 0
                        else:
                                robot.setSignal('s')
                                return choice([1,2,3,4])
                elif shift=='1':
                        if isnew=='n':
                                moves+=1
                                own_signal=own_signal[:3]+'f'+own_signal[4]+str(moves)
                                robot.setSignal(own_signal)
                                return interpretdir(orientation)
                        elif isnew=='f' and moves<=10:
                                moves+=1
                                if moves==11:
                                        orientation=flipmovement(orientation)
                                own_signal=own_signal[0]+orientation+own_signal[2:5]+str(moves)
                                robot.setSignal(own_signal)
                                return interpretdir(orientation)
                        elif isnew=='f' and moves<=20:
                                moves+=1
                                if moves==21:
                                        isnew='o'
                                        orientation=flipmovement(orientation)
                                own_signal=own_signal[0]+orientation+own_signal[2]+isnew+own_signal[4]+str(moves)
                                robot.setSignal(own_signal)
                                if robot.investigate_up()=="friend-base" or robot.investigate_down()=="friend-base" or robot.investigate_left()=="friend-base" or robot.investigate_right()=="friend-base":
                                        return 0
                                else:
                                        return interpretdir(orientation)
                        elif isnew=='o':
                                isnew='d'
                                own_signal=own_signal[:3]+isnew+own_signal[4:]
                                robot.setSignal(own_signal)
                                return interpretdir(orientation)
                        else:
                                return 0
        elif len(own_signal)==0 and own_signal[0]=='x': #disabled
                corner=own_signal[1]
                orientation=own_signal[2]
                count=int(own_signal[3])
                if count<3:
                        count+=1
                        own_signal=own_signal[:3]+str(count)
                        robot.setSignal(own_signal)
                        return interpretdir(orientation)
                elif count<6:
                        count+=1
                        if corner=='t' or corner=='b':
                                orientation='l'
                        elif corner=='T' or corner=='B':
                                orientation='r'
                        own_signal=own_signal[:2]+orientation+str(count)
                        robot.setSignal(own_signal)
                        return interpretdir(orientation)
                else:
                        return 0
        elif len(own_signal)!=0 and own_signal[0]=='h':
                robot.setSignal(own_signal)
                partitioned_signal=own_signal.split('-')
                enemy_x=int(partitioned_signal[1])
                enemy_y=int(partitioned_signal[2])
                robot_x,robot_y=robot.GetPosition()
                if robot_x>enemy_x:
                        return 4
                elif robot_x<enemy_x:
                        return 2
                elif robot_y<enemy_y:
                        return 3
                elif robot_y>enemy_y:
                        return 1
                else:
                        return 0
        elif len(own_signal)==0 or own_signal[0]=='s':
                robot.setSignal(own_signal)
                if len(own_signal)!=0 and flag=='r' and own_signal=='s':
                        robot_x,robot_y=robot.GetPosition()
                        if robot_x>base_x:
                                return 4
                        elif robot_x<base_x:
                                return 2
                        elif robot_y<base_y:
                                return 3
                        elif robot_y>base_y:
                                return 1
                        else:
                                own_signal=own_signal[0]+'h'
                                robot.setSignal(own_signal)
                if own_signal=="sh" and flag!='r':
                        own_signal='s'
                        robot.setSignal(own_signal)
                return choice([1,2,3,4])
                        

def ActBase(base):
        flag='o'
        base_found='n'
        list_of_signals=base.GetListOfSignals()
        for beta in list_of_signals:
                if len(beta)>=3 and beta[0]=='g' and beta[2]=='1':
                        flag='r'
        if base.investigate_up()=="enemy" or base.investigate_down()=="enemy" or base.investigate_left()=="enemy" or base.investigate_right()=="enemy" or base.investigate_ne()=="enemy" or base.investigate_nw()=="enemy" or base.investigate_se()=="enemy" or base.investigate_sw()=="enemy":
                flag='r'
                if base.GetVirus()>15000:
                        base.DeployVirus(14000) 
                else:
                        r=(0.9*base.GetVirus())//1 
                        base.DeployVirus(r)
        base_x,base_y=base.GetPosition()
        signal=str(base_x)+'-'+str(base_y)+'-'+flag
        
        while base.GetElixir()>1600: 
                for theta in range(1,3):
                        for delta in range(1,3):
                                temp_str='a'+str(theta)+str(delta)+str(0)
                                cur1='r'
                                cur2='u'
                                t1=temp_str+cur1
                                t2=temp_str+cur2
                                base.create_robot(t1)
                                base.create_robot(t2)
        while base.GetElixir()>1200: 
                for theta in range(1,3):
                        for delta in range(1,3):
                                temp_str='c'+str(theta)+str(delta)+str(0)
                                cur1='r'
                                cur2='u'
                                t1=temp_str+cur1
                                t2=temp_str+cur2
                                base.create_robot(t1)
                                base.create_robot(t2)
        while base.GetElixir()>800: 
                temp='g'+'l'+str(0)+'n'+'1'+'0'
                base.create_robot(temp)
                temp=temp[0]+'r'+temp[2:]
                base.create_robot(temp)
                temp=temp[0]+'u'+temp[2:]
                base.create_robot(temp)
                temp=temp[0]+'d'+temp[2:]
                base.create_robot(temp)
                temp='g'+'l'+str(0)+'n'+'2'+'0'
                base.create_robot(temp)
                temp=temp[0]+'r'+temp[2:]
                base.create_robot(temp)
                temp=temp[0]+'u'+temp[2:]
                base.create_robot(temp)
                temp=temp[0]+'d'+temp[2:]
                base.create_robot(temp)
        while base.GetElixir()>600: 
                temp='f'+'l'+'n'
                base.create_robot(temp)
                temp=temp[0]+'r'+temp[2]
                base.create_robot(temp)
                temp=temp[0]+'u'+temp[2]
                base.create_robot(temp)
                temp=temp[0]+'d'+temp[2]
                base.create_robot(temp)
        while base.GetElixir()>1200:
                temp_str='x'+'t'+'u'+str(0)
                base.create_robot(temp_str)
                temp_str=temp_str[0]+'T'+temp_str[2:]
                base.create_robot(temp_str)
                temp_str=temp_str[0]+'b'+'d'+temp_str[3]
                base.create_robot(temp_str)
                temp_str=temp_str[0]+'B'+temp_str[2:]
                base.create_robot(temp_str)
        while base.GetElixir()>200:
                temp='s'
                base.create_robot(temp)
        
        for delta in list_of_signals:
                if len(delta)!=0 and delta[0]=='e':
                        base_found='y'
                        partitioned_signal=delta.split('-')
                        enemy_x=int(partitioned_signal[1])
                        enemy_y=int(partitioned_signal[2])
                        if base.GetElixir()>=60 and flag!='r':
                                base.create_robot('h'+'-'+str(enemy_x)+'-'+str(enemy_y))
        signal=signal+'-'+base_found
        if base_found=='y':
                signal=signal+'-'+str(enemy_x)+'-'+str(enemy_y)
        base.SetYourSignal(signal)

def LetsDeploy(robot):
        #if robot.investigate_up()=="enemy" or robot.investigate_down()=="enemy" or robot.investigate_left()=="enemy" or robot.investigate_right()=="enemy" or robot.investigate_ne()=="enemy" or robot.investigate_nw()=="enemy" or robot.investigate_se()=="enemy" or robot.investigate_sw()=="enemy":
                #if robot.GetVirus()>1500:
                        #robot.DeployVirus(1000) 
        if robot.investigate_up()=="enemy-base" or robot.investigate_down()=="enemy-base" or robot.investigate_left()=="enemy-base" or robot.investigate_right()=="enemy-base" or robot.investigate_ne()=="enemy-base" or robot.investigate_nw()=="enemy-base" or robot.investigate_se()=="enemy-base" or robot.investigate_sw()=="enemy-base":
                #r=robot.GetVirus()//1
                #robot.DeployVirus(r)
                return "stay"
        if robot.investigate_up()=="enemy" or robot.investigate_down()=="enemy" or robot.investigate_left()=="enemy" or robot.investigate_right()=="enemy" or robot.investigate_ne()=="enemy" or robot.investigate_nw()=="enemy" or robot.investigate_se()=="enemy" or robot.investigate_sw()=="enemy":
                #if robot.GetVirus()>1500:
                        #robot.DeployVirus(1000)
                return "enemy_bot"
        return "don't_stay"

def ReleaseVirus(robot, own_signal):
        if own_signal[0]=='a' or own_signal[0]=='c' or own_signal[0]=='f':
                if robot.GetVirus()>15000:
                        robot.DeployVirus(5000)
                elif robot.GetVirus()>7500:
                        robot.DeployVirus(2000)
                elif robot.GetVirus()>5000:
                        robot.DeployVirus(2000)
                elif robot.GetVirus()>3000:
                        robot.DeployVirus(1500)
                else:
                        r=robot.GetVirus()
                        robot.DeployVirus(r//2)
        elif own_signal[0]=='s':
                if robot.GetVirus()>15000:
                        robot.DeployVirus(7000)
                elif robot.GetVirus()>12000:
                        robot.DeployVirus(4000)
                elif robot.GetVirus()>7500:
                        robot.DeployVirus(3000)
                elif robot.GetVirus()>3000:
                        robot.DeployVirus(1000)
                else:
                        r=robot.GetVirus()
                        robot.DeployVirus(r//4)
        elif own_signal[0]=='g':
                if robot.GetVirus()>15000:
                        robot.DeployVirus(8000)
                elif robot.GetVirus()>10000:
                        robot.DeployVirus(5000)
                elif robot.GetVirus()>7500:
                        robot.DeployVirus(3000)
                elif robot.GetVirus()>3000:
                        robot.DeployVirus(1800)
                elif robot.GetVirus()>2000:
                        robot.DeployVirus(1500)
                else:
                        r=robot.GetVirus()
                        robot.DeployVirus((0.75*r)//1)
        

#use GetYourSignal, if straight attack then feed into this function with direction
#0-stay 1-up 2-right 3-down 4-left
#robot signal- a/g/s
#a- right, up, count, current_dir  a120l
#g- orientation, count, new
#s-

