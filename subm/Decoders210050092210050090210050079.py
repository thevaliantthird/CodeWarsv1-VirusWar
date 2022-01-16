from random import randint


def ActRobot(robot):
       
        cnt = 0
        cnt = int(robot.investigate_up()=='enemy') + int(robot.investigate_down()=='enemy') + int(robot.investigate_left()=='enemy') + int(robot.investigate_right()=='enemy') + int(robot.investigate_nw()=='enemy') + int(robot.investigate_ne()=='enemy') + int(robot.investigate_sw()=='enemy') + int(robot.investigate_se()=='enemy')

        if cnt >= 3:
                robot.DeployVirus(400)              
        elif cnt>=1 :
                robot.DeployVirus(300) 

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
                        return randint(1,4) 
        if init_signal.find('attacker')!=-1:
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
                return randint(1,4)


def ActBase(base):
    if base.GetElixir() > 500:
            p = randint (0,14)
            if p == 0 :
                x,y = base.GetPosition()    
                msg_x = str(x)
                msg_y = str(y)
                if x < 10:
                        msg_x = '0' + msg_x
                if y < 10:
                        msg_y = '0' + msg_y 
                base.create_robot('teamwork'+msg_x+msg_y)
            elif p== 1:
                x,y = base.GetPosition()    
                msg_x = str(x)
                msg_y = str(y)
                if x < 10:
                        msg_x = '0' + msg_x
                if y < 10:
                        msg_y = '0' + msg_y        
                base.create_robot('defender' + msg_x + msg_y) 
            else:
                x,y = base.GetPosition()    
                msg_x = str(x)
                msg_y = str(y)
                if x < 10:
                        msg_x = '0' + msg_x
                if y < 10:
                        msg_y = '0' + msg_y 
                base.create_robot('attacker'+msg_x+msg_y)           
    return