


from random import randint


def ActRobot(robot):




        #robots set signal and deploy virus after finding enemy or enemy base in affinity

        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        x,y = robot.GetPosition()
        robot.setSignal('')
        init_signal = robot.GetInitialSignal()
        cx = robot.GetDimensionX()  #for canvas size
        cy = robot.GetDimensionY()
        


        if up == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)


        if down == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)
        
        if left == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)
                
        if right == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)
        
        if ne == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)

        if nw == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)

        if se == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)

        if sw == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(100)
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
                        robot.DeployVirus(500)


        #robots with initial sinal defender
        if init_signal.find('defender')!= -1:
                basex = int(init_signal[8:10])
                basey = int(init_signal[10:])
                if x>basex:
                        return 4
                if x<basex:
                        return 2
                if y>basey:
                        return 1
                if y<basey:
                        return 3        
                if x==basex and y==basey:
                        return randint(1,4)





        #if signal from base is non zero(got coordinates for enemy base) then all robots attack that position                

        if len(robot.GetCurrentBaseSignal()) > 0:
                #
                #for i in range(20):
                 #       return randint(1,4)
                s = robot.GetCurrentBaseSignal()[4:]
                sx = int(s[0:2])
                sy = int(s[2:4])
                dist = abs(sx-x) + abs(sy-y)
                if dist==1:
                        robot.DeployVirus(robot.GetVirus())
                        return 0
                if x < sx:
                        return 2
                if x > sx:
                        return 4
                if y < sy :
                        return 3
                if y > sy:
                        return 1

        #predicting enemy base location
        
        if init_signal.find('finder4')!= -1:
                basex = int(init_signal[7:9])
                basey = int(init_signal[9:]) 
                if left== 'wall' and basex-x < 15:
                    if (cx - basex + 3) < 10:
                            msg_x = '0' + str(cx - basex + 3)
                    else :
                            msg_x = str(cx - basex + 3)
                    msg_y = str(basey)
                    msg = "base" + msg_x + msg_y
                    robot.setSignal(msg)
                if  left!= 'wall':
                    return 4

        if init_signal.find('finder2')!= -1:
                basex = int(init_signal[7:9])
                basey = int(init_signal[9:])  
                if right== 'wall' and x - basex < 15:
                   if ( cx - basex - 2)<10:
                           msg_x = '0' + str( cx - basex - 2)
                   else:
                           msg_x = str( cx - basex - 2)
                   msg_y = str(basey)
                   msg = "base" + msg_x + msg_y
                   robot.setSignal(msg)        
                if  right!= 'wall':
                   return 2

        if init_signal.find('finder1')!= -1:
                basex = int(init_signal[7:9])
                basey = int(init_signal[9:]) 
                if up== 'wall' and basey-y < 15:
                   if  (cy - basey + 3) < 10:
                           msg_y = '0' + str(cy - basey + 3)
                   else:
                           msg_y = str(cy - basey + 3)        
                   msg_x = str(basex)
                   msg = "base" + msg_x + msg_y
                   robot.setSignal(msg)
                if up!= 'wall':
                   return 1

        if init_signal.find('finder3')!= -1:
                basex = int(init_signal[7:9])
                basey = int(init_signal[9:])  
                if down== 'wall' and y-basey < 15:
                   if  (cy - basey - 2)<10:
                           msg_y = '0' + str(cy - basey - 2)
                   else:
                           msg_y = str(cy - basey - 2)        
                   msg_x = str(basex)
                   msg = "base" + msg_x + msg_y
                   robot.setSignal(msg)
                if down!= 'wall':
                   return 3
                       

                       
        #random movement of ronots
        else:
         return randint(1,4)
        

def ActBase(base):
    '''
    Add your code here
    
    '''
    #position of base
    
    basex,basey = base.GetPosition()

    # base defending itself by deploying virus

    upb = base.investigate_up()
    downb =base.investigate_down()
    leftb = base.investigate_left()
    rightb = base.investigate_right()
    neb = base.investigate_ne()
    nwb = base.investigate_nw() 
    seb = base.investigate_se()
    swb = base.investigate_sw()

    

    if upb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)

    if downb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)            

    if rightb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)

    if leftb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)

    if neb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)
   
    if nwb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)

    if seb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)

    if swb == "enemy" and base.GetVirus() > 500:
                base.DeployVirus(100)




    #base creating robots for attacking, defending and finding

    #random robots
    if base.GetElixir() > 900 :
        base.create_robot('')

    #finder robots with native base position    
    if base.GetElixir() > 850 and base.GetElixir()<=900:
            x,y = base.GetPosition()
            basex = str(x)
            basey = str(y)
            if x<10:
                    basex='0' + basex
            if y<10:
                    basey = '0' + basey
            base.create_robot('finder1'+ basex + basey)

    if base.GetElixir() > 800 and base.GetElixir()<=850:
            x,y = base.GetPosition()
            basex = str(x)
            basey = str(y)
            if x<10:
                    basex='0' + basex
            if y<10:
                    basey = '0' + basey
            base.create_robot('finder2'+ basex + basey)        

    if base.GetElixir() > 750 and base.GetElixir()<=800:
            x,y = base.GetPosition()
            basex = str(x)
            basey = str(y)
            if x<10:
                    basex='0' + basex
            if y<10:
                    basey = '0' + basey
            base.create_robot('finder3'+ basex + basey)

    if base.GetElixir() > 700 and base.GetElixir()<=750:
            x,y = base.GetPosition()
            basex = str(x)
            basey = str(y)
            if x<10:
                    basex='0' + basex
            if y<10:
                    basey = '0' + basey
            base.create_robot('finder4'+ basex + basey)       

    #defender robots with native base position       
    if base.GetElixir()>500 and base.GetElixir()<=700:  
            x,y = base.GetPosition()
            basex = str(x)
            basey = str(y)
            if x<10:
                    basex='0' + basex
            if y<10:
                    basey = '0' + basey
            base.create_robot('defender' + basex + basey)                
            


    #checking signals from bases and setting signals to attack the enemy base
                         
    L = base.GetListOfSignals()
    for l in L:
        if len(l) > 0:
                base.SetYourSignal(l)
                return

    