from random import randint


def ActRobot(robot): 
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        x,y = robot.GetPosition()

        cnt = int(up=='enemy') + int(down=='enemy') + int(left=='enemy') + int(right=='enemy') + int(robot.investigate_nw()=='enemy') + int(robot.investigate_ne()=='enemy') + int(robot.investigate_sw()=='enemy') + int(robot.investigate_se()=='enemy')

        if cnt >= 6:
                robot.DeployVirus(150) # robot.getvirus(0.9)
        elif cnt >= 3:
                robot.DeployVirus(145)       
        elif cnt==0:
                robot.DeployVirus(0)
        else :
               robot.DeployVirus(125)

        init_signal = robot.GetInitialSignal()
        if init_signal.find('defender')!=-1:
                base_x = int(init_signal[8:10])
                base_y = int(init_signal[10:])
                x,y = robot.GetPosition()
                if x > base_x:
                        return 4        
                if x < base_x:
                        return 2
                if y > base_y:
                        return 1        
                if y < base_y:
                        return 3                                
                if x == base_x and y == base_y:
                        for i in range(5):
                                k = randint(1,4)
                        return k  

        init_signal = robot.GetInitialSignal()
        if init_signal.find('scavange')!=-1:
                base_x = int(init_signal[8:10])
                base_y = int(init_signal[10:])
                x,y = robot.GetPosition()

                if robot.investigate_up()=='friend-base':
                        return 3
                if robot.investigate_down()=='friend-base':
                        return 1
                if robot.investigate_left()=='friend-base':
                        return 2
                if robot.investigate_right()=='friend-base':
                        return 4

                x,y = robot.GetPosition()
                if robot.investigate_up()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x) + ',' +str(y-1))
                if robot.investigate_left()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x-1) + ',' +str(y))
                if robot.investigate_right()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x+1) + ',' +str(y))
                if robot.investigate_down()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x) + ',' +str(y+1))

                if robot.investigate_ne()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x+1) + ',' +str(y-1))
                if robot.investigate_se()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x+1) + ',' +str(y+1))

                if robot.investigate_sw()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x-1) + ',' +str(y+1))
                if robot.investigate_nw()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x-1) + ',' +str(y-1))
                
                if (robot.GetYourSignal()!=''):
                        print(robot.GetYourSignal())
                        
                if len(robot.GetCurrentBaseSignal()) > 0:
                        # s = robot.GetCurrentBaseSignal()[4:]
                        list2 = robot.GetCurrentBaseSignal().split(',')
                        sx =int(list2[1])
                        sy =int(list2[2])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist==(1 or 0 or 2):
                                robot.DeployVirus(robot.GetVirus()*0.80)
                                return (1,4)
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy :
                                return 3
                        if y > sy:
                                return 1
                else:
                        return randint(1,4)
        

        init_signal = robot.GetInitialSignal()
        if init_signal.find('attacker')!=-1:
                base_x = int(init_signal[8:10])
                base_y = int(init_signal[10:])
                x,y = robot.GetPosition()
                if robot.investigate_up()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x) + ',' +str(y-1))
                if robot.investigate_left()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x-1) + ',' +str(y))
                if robot.investigate_right()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x+1) + ',' +str(y))
                if robot.investigate_down()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x) + ',' +str(y+1))

                if robot.investigate_ne()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x+1) + ',' +str(y-1))
                if robot.investigate_se()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x+1) + ',' +str(y+1))

                if robot.investigate_sw()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x-1) + ',' +str(y+1))
                if robot.investigate_nw()=='enemy-base':
                        robot.setSignal('basefound' + ','+ str(x-1) + ',' +str(y-1))
                
                if (robot.GetYourSignal()!=''):
                        print(robot.GetYourSignal())
                 
                if len(robot.GetCurrentBaseSignal()) > 0:
                        # s = robot.GetCurrentBaseSignal()[4:]
                        list2 = robot.GetCurrentBaseSignal().split(',')
                        sx =int(list2[1])
                        sy =int(list2[2])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist==(1 or 2 or 0):
                                robot.DeployVirus(robot.GetVirus()*0.80)
                                return (1,4)
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy :
                                return 3
                        if y > sy:
                                return 1
                else:
                        return randint(1,4)

        init_signal = robot.GetInitialSignal()
        if init_signal.find('nihekadh')!=-1:
                base_x = int(init_signal[8:10])
                base_y = int(init_signal[10:])
                base_x = int(init_signal[8:10])
                base_y = int(init_signal[10:])
                x,y = robot.GetPosition()

                if robot.investigate_up()=='friend-base':
                        return 3
                if robot.investigate_down()=='friend-base':
                        return 1
                if robot.investigate_left()=='friend-base':
                        return 2
                if robot.investigate_right()=='friend-base':
                        return 4




def ActBase(base):
#     base.SetYourSignal('move,'+'10'+','+'20')
    '''
    Add your code here
    
    '''
    if base.GetElixir() > 300:

        for i in range(34):
                if i <=4:
                        x,y = base.GetPosition()    
                        msg_x = str(x)
                        msg_y = str(y)
                        if x < 10:
                                 msg_x = '0' + msg_x
                        if y < 10:
                                msg_y = '0' + msg_y 
                        base.create_robot('defender'+msg_x+msg_y)
        
                elif i <15:
                        x,y = base.GetPosition()    
                        msg_x = str(x)
                        msg_y = str(y)
                        if x < 10:
                                msg_x = '0' + msg_x
                        if y < 10:
                                msg_y = '0' + msg_y 
                        base.create_robot('scavange'+msg_x+msg_y)
                elif i <23:
                        x,y = base.GetPosition()    
                        msg_x = str(x)
                        msg_y = str(y)
                        if x < 10:
                                msg_x = '0' + msg_x
                        if y < 10:
                                msg_y = '0' + msg_y 
                        base.create_robot('attacker'+msg_x+msg_y)
                elif i <36:
                        x,y = base.GetPosition()    
                        msg_x = str(x)
                        msg_y = str(y)
                        if x < 10:
                                 msg_x = '0' + msg_x
                        if y < 10:
                                msg_y = '0' + msg_y 
                        base.create_robot('nihekadh'+msg_x+msg_y)
                


        

    for signal in base.GetListOfSignals():
        if (signal!=''):
                print('signal'+signal)
        if signal.find('basefound')!=-1:
                print('signal'+signal)
                list1 = signal.split(',')

                base.SetYourSignal('move,'+ list1[1] +  ',' + list1[2])
                print('move,'+ list1[1] +  ',' + list1[2])
        

    cnt = int(base.investigate_up()=='enemy') + int(base.investigate_right()=='enemy') + int(base.investigate_left()=='enemy') + int(base.investigate_down()=='enemy') + int(base.investigate_nw()=='enemy') + int(base.investigate_ne()=='enemy') + int(base.investigate_sw()=='enemy') + int(base.investigate_se()=='enemy')

    if cnt >= 1:
        base.DeployVirus(base.GetVirus()*0.75) # robot.getvirus(0.9)
  