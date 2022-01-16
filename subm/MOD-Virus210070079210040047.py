from random import randint

def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne =  robot.investigate_ne()
        nw =   robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        (x,y) = robot.GetPosition()
        
        

        if ne=='enemy-base':
                robot.DeployVirus(500)
        if nw=='enemy-base':
                robot.DeployVirus(500)
        if se=='enemy-base':
                robot.DeployVirus(500)
        if sw=='enemy-base':
                robot.DeployVirus(500)
        if up=='enemy-base':
                robot.DeployVirus(500)
        if down=='enemy-base':
                robot.DeployVirus(500)
        if left=='enemy-base':
                robot.DeployVirus(500)
        if right=='enemy-base':
                robot.DeployVirus(500)

        
        
        robot.setSignal('')
        if up == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(1000)
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
                        robot.DeployVirus(2500)
        if down == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(1000)
        
                
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
                        robot.DeployVirus(2500)
        
        if left == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(1000)
        
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
                        robot.DeployVirus(2500)
                
        if right == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(1000)
        
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
                        robot.DeployVirus(1000)

        if nw =='enemy':
                robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                if x-1<10:
                  msg_x='0' + str(x-1)  
                else:
                        msg_x=str(x-1) 
                if y-1<10:
                        msg_y='0' + str(y-1)
                else:
                        msg_y=str(y-1)
                msg= "base" + msg_x + msg_y 
                robot.setSignal(msg)
                robot.DeployVirus(1000)                             

        if ne=='enemy':
                robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                if x+1 <10:
                        msg_x='0' + str(x+1)
                else:
                        msg_x=str(x+1)
                if y-1 <10:
                        msg_y='0' + str(y-1)
                else:
                        msg_y=str(y-1)
                msg= "base" + msg_x + msg_y
                robot.setSignal(msg)
                robot.DeployVirus(1000)

        if se=='enemy':
                robot.DeployVirus(1000)
                x,y=robot.GetPosition()
                if x+1 <10:
                        msg_x='0'+str(x+1)
                else:
                        msg_x=str(x+1)
                if y+1 <10:
                        msg_y= '0' + str(y+1)
                else:
                        msg_y=str(y+1)
                msg="base" + msg_x + msg_y
                robot.setSignal(msg)
                robot.DeployVirus(1000)                                   
        
        if sw=='enemy':
                robot.DeployVirus(1000) 
                x,y=robot.GetPosition()
                if x-1 <10:
                        msg_x='0' + str(x-1)
                else:
                        msg_x=str(x-1)  
                if y+1 < 10:
                        msg_y='0' + str(y+1) 
                else:
                        msg_y=str(y+1)
                msg="base" + msg_x + msg_y
                robot.setSignal(msg)
                robot.DeployVirus(1000)   

          

                                       
         
                                
        if len(robot.GetCurrentBaseSignal())> 0 and robot.GetInitialSignal()=='a':
                o = robot.GetCurrentBaseSignal()[4:]
                msg_x = int(o[0:2])
                msg_y = int(o[2:4])
                dist = abs(msg_x-x) + abs(msg_y-y)
                if dist==0:
                        return randint(0,4)
                if x<  msg_x:
                        while msg_x!=x:
                                return 2
                if x > msg_x:
                        while msg_x!=x:
                                return 4
                if y < msg_y :
                        while y !=msg_y:
                                return 3
                if y > msg_y:
                        while msg_y!=y:
                                return 1
        else:
                return randint(1,4)        

        
        
        
              
        


                 


                 
                 

                
  


        
        
        


def ActBase(base):

    up = base.investigate_up()
    down = base.investigate_down()
    left = base.investigate_left()
    right = base.investigate_right()
    ne = base.investigate_ne()
    nw = base.investigate_nw()
    se = base.investigate_se()
    sw=base.investigate_sw()
    p,q =base.GetPosition() 
    if p <10:
            p='0' + str(p)
    else:
            p=str(p)  
    if q < 10:
            q='0' + str(q) 
    else:
            q=str(q)   
    while(base.GetElixir()>1900):
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                base.create_robot('a')
                


    

    if base.GetElixir()>50:
            base.create_robot('')

    L=base.GetListOfSignals()
    for l in L:
            if len(l) >0:
                    base.SetYourSignal(l)
                    return 
    if ne=='enemy':
             base.DeployVirus(500)
    if nw=='enemy':
            base.DeployVirus(500)
    if se=='enemy':
            base.DeployVirus(500)
    if sw=='enemy':
            base.DeployVirus(500)
    if up=='enemy':
            base.DeployVirus(500)
    if down=='enemy':
            base.DeployVirus(500)
    if left=='enemy':
            base.DeployVirus(500)
    if right=='enemy':
            base.DeployVirus(500)