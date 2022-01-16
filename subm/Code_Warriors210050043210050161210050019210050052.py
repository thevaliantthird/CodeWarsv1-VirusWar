from random import randint


def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()

        x,y = robot.GetPosition()

        init_signal=robot.GetInitialSignal()
        if init_signal.find('defender'):

                '''enemy-detection'''
                
                #robot.setSignal('')
                count=int(up=="enemy")+int(down=="enemy")+int(left=="enemy")+int(right=="enemy")+int(ne=="enemy")+int(nw=="enemy")+int(se=="enemy")+int(sw=="enemy")
                if (count < 2 and count!=0):
                        robot.DeployVirus(100)
                elif (count!=0):
                        '''if x<10 :
                                pos_x = '0' + str(x)
                        else:
                                pos_x = str(x)
                        if y<10 :
                                pos_y = '0' + str(y)
                        else:
                                pos_y = str(y)
                        msg = 'help' + pos_x + pos_y
                        robot.setSignal(msg)'''
                        robot.DeployVirus(400)

                '''movement of defender-robot
                base_x = int( init_signal[9:11] )
                base_y = int( init_signal[11:] )
                x,y=robot.GetPosition()
                id=int(init_signal[8:9])
                if x==base_x and y==base_y:
                        return (id+randint(0,3))
                else:
                        return 0'''
                return randint(1,4)


        if init_signal.find('attacker'):

                #enemy-detection
                robot.setSignal('')
                count=int(up=="enemy")+int(down=="enemy")+int(left=="enemy")+int(right=="enemy")+int(ne=="enemy")+int(nw=="enemy")+int(se=="enemy")+int(sw=="enemy")
                if (count < 2 and count !=0) and robot.GetVirus() > 1000:
                        robot.DeployVirus(100)
                elif (count<4 and count!=0) and robot.GetVirus() > 800:
                        robot.DeployVirus(300)
                elif (count<7 and count!=0):
                        robot.DeployVirus(400)
                if (up =="enemy-base" or down=="enemy-base" or right=="enemy-base" or left=="enemy-base" or ne=="enemy-base" or nw=="enemy-base" or se=="enemy-base" or sw=="enemy-base"):
                        if x<10 :
                                pos_x = '0' + str(x)
                        else:
                                pos_x = str(x)
                        if y<10 :
                                pos_y = '0' + str(y)
                        else:
                                pos_y = str(y)
                        msg = 'help' + pos_x + pos_y
                        robot.setSignal(msg)
                        robot.DeployVirus(400)

                #reaction to signal detected                
                if len(robot.GetCurrentBaseSignal()) > 0:
                        s = robot.GetCurrentBaseSignal()[4:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist==1:
                                robot.DeployVirus(robot.GetVirus()*0.75)
                                return 0
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy :
                                return 3
                        if y > sy:
                                return 1
                else:  #movement of attacker-robot
                        return randint(1,4)



def ActBase(base):

        if base.GetElixir() > 500:
                x,y=base.GetPosition()
                msg_x=str(x)
                msg_y=str(y)
                if x<10:
                        msg_x='0'+msg_x
                if y<10:
                        msg_y='0'+msg_y
                p=randint(0,5)
                if p==0:
                        base.create_robot('defender1'+msg_x+msg_y)
                
                else :
                        base.create_robot('attacker') 
        L = base.GetListOfSignals()
        for l in L:
                if len(l) > 0:
                        base.SetYourSignal(l)           
        return 