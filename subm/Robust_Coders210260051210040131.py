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
        count=0
        if (up=='enemy' or down=='enemy' or left=='enemy' or right=='enemy' or ne=='enemy' or nw=='enemy' or se=='enemy' or sw=='enemy'):
                count= int(up=='enemy') + int(down=='enemy') + int(left=='enemy') + int(right=='enemy') + int(ne=='enemy') + int(nw=='enemy') + int(se=='enemy') + int(sw=='enemy')
        if (count<3 and count>0):
                robot.DeployVirus(400)
        elif (count>2 and count<6):
                robot.DeployVirus(500)
        elif(count>5 and count<9):
                robot.DeployVirus(800)               

        if (up == "enemy-base" or down=='enemy-base' or left=='enemy-base' or right=='enemy-base' or ne=='enemy-base' or nw=='enemy-base' or se=='enemy-base' or sw=='enemy-base'):                    
                p = robot.GetPosition()
                eb_pos = (p[0], p[1]-1)
                signal = "eb" + " " + str(eb_pos[0]) + " " + str(eb_pos[1])
                robot.setSignal(signal)
                robot.DeployVirus(robot.GetVirus())           

        b_signal = robot.GetCurrentBaseSignal()
        p = robot.GetPosition()
        i = 0
        if b_signal.startswith("eb") : # we have a signal frm base tht is enemy base 
                while (i < len(robot.GetCurrentBaseSignal())):
                        msg = b_signal[i]
                        d = msg.split()
                        eb = (int(d[1]), int(d[2]))    
                        if (eb == p) or ((abs(eb[0]-p[0]))==1 or (abs(eb[1]-p[1]))==1):       
                                return 0 #stationary
                        elif eb[1] > p[1]+1:                        
                                return 3 #up
                        elif eb[1]+1 < p[1]:
                                return 1 #down
                        elif eb[0]+1 < p[0]:
                                return 4 #left
                        elif eb[0] > p[0]+1 :
                                return 2 #right
                        i+= 1        

        elif (b_signal.find("base")!=-1):
                b_pos=b_signal.split()
                base_x = b_pos[1]
                base_y = b_pos[2]
                if (base_x == p[0] and base_y==p[1]):
                        print("me")
                        robot.setSignal()
                        return(b_pos[3])
                        
        else :
                return randint(1,4)   #when there's no signal from the base                                             




def ActBase(base):
        up = base.investigate_up()
        down = base.investigate_down()
        left = base.investigate_left()
        right = base.investigate_right()
        ne = base.investigate_ne()
        nw = base.investigate_nw()
        se = base.investigate_se()
        sw = base.investigate_sw()
        total_virus = base.GetVirus()
        if (up == "enemy" or down=='enemy' or left=='enemy' or right=='enemy' or ne=='enemy' or nw=='enemy' or se=='enemy' or sw=='enemy'):    
                base.DeployVirus(total_virus * 0.25)
                
        #to protect the base
        x,y = base.GetPosition()
        c=1
        if(up=='blank' or down=='blank' or left=='blank' or right=='blank') and (base.GetElixir()>1000): 
                while((up=='blank' or down=='blank' or left=='blank' or right=='blank') and c<5):
                        signal = "base" + " " + str(x) + " " + str(y) + " " + str(c)
                        base.create_robot(signal) 
                        c+=1 
      
        #creating robots
        if base.GetElixir() > 1000:
                base.create_robot('')
        #when enemy location is found
        l = base.GetListOfSignals()
        i = l[0]
        if len(l) > 0:                            
                base.SetYourSignal(i)
                while (base.GetElixir() > 500):
                        base.create_robot(i)    
