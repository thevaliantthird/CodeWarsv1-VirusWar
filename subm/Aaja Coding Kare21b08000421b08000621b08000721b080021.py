from random import randint


def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        nw = robot.investigate_nw()
        ne = robot.investigate_ne()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        x,y = robot.GetPosition()
        robot.setSignal('')
        if up == "enemy-base":
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if up == "enemy" and robot.GetVirus() > 6000:
                        robot.DeployVirus(1000)  
        
        if down == "enemy-base":
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if down == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)
        
        if left == "enemy-base":
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if left == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)
                
        
        if right == "enemy-base":
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if right == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)

        if ne == "enemy-base":
                x,y = robot.GetPosition()
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if ne == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)
        
        if nw == "enemy-base":
                x,y = robot.GetPosition()
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if nw == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)

        if se == "enemy-base":
                x,y = robot.GetPosition()
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if se == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)

        if sw == "enemy-base":
                x,y = robot.GetPosition()
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
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(3000)
                else:
                        robot.DeployVirus(500)
        if sw == "enemy" and robot.GetVirus() > 6000:
                robot.DeployVirus(1000)
        if robot.investigate_right()=="friend base" and robot.GetVirus>8000:
                return 4
        if robot.investigate_left()=="friend base" and robot.GetVirus>8000:
                return 2
        
        
        
        
        if robot.GetInitialSignal()=='':
              if len(robot.GetCurrentBaseSignal()) > 0:
                
                    s = robot.GetCurrentBaseSignal()[4:]
                    sx = int(s[0:2])
                    sy = int(s[2:4])
                    dist = abs(sx-x) + abs(sy-y)
                    if dist==1 or (dist ==2 and (abs(sx-x)<2 and abs(sy-y)<2)) :
                             robot.DeployVirus(robot.GetVirus()*0.75)
                             return randint(1,4)
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

        if len(robot.GetInitialSignal())==9:
                v=robot.GetInitialSignal()[5:]
                vx = int(v[0:2])
                vy = int(v[2:4])
                x,y = robot.GetPosition()
                mv=0
                if abs(x-vx)<3 and abs(y-vy)<3:
                        mv= randint(1,4)
                if x>vx+2:
                        mv=4
                if x<vx-2:
                        mv=2
                if y<vy-2:
                        mv=3
                        
                if y>vy+2:
                        mv=1
                k=1
                while k%5==0:
                        robot.DeployVirus(200)
                        k=k+1
                        if k>=1200:
                                break
      
                return mv

        
        
        
        if len(robot.GetInitialSignal())==6:
                v=robot.GetInitialSignal()[2:]
                vx = int(v[0:2])
                vy = int(v[2:4])
                pika=int(robot.GetDimensionX())
                chu=int(robot.GetDimensionY())
                sx = pika - vx
                sy= chu - vy
                x,y = robot.GetPosition()
                dist = abs(sx-x) + abs(sy-y)
                if robot.GetVirus()<=4000:
                        ps=0
                        if abs(x-vx)<3 and abs(y-vy)<3:
                                ps= randint(1,4)
                        if x>vx+2:
                                ps=4
                        if x<vx-2:
                                ps=2
                        if y<vy-2:
                                ps=3
                        
                        if y>vy+2:
                                ps=1
                        return ps
                
                elif robot.GetVirus()<=6000  :
                        return randint(1,4)
                       
                        
                                        
                elif robot.GetVirus()>=6000:

                        if dist==1 or (dist ==2 and (abs(sx-x)<2 and abs(sy-y)<2)) :
                                robot.DeployVirus(robot.GetVirus()*0.75)
                                return randint(1,4)
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

                
                
                                


                         
                
       
        
                    
                         

        
                

        

      
                
        

def ActBase(base):
    u = base.investigate_up()
    d = base.investigate_down()
    r = base.investigate_right()
    le = base.investigate_left()
    now = base.investigate_nw()
    noe = base.investigate_ne()
    sow = base.investigate_sw()
    soe = base.investigate_se()
   

    if u == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
    


    if d == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
   
    if r == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
    
    if le == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
   
    if now == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
    
    if noe == "enemy" and base.GetVirus() >5000:
            base.DeployVirus(5000)
   
    if sow == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
       
    if soe == "enemy" and base.GetVirus() > 5000:
            base.DeployVirus(5000)
           

        


    while base.GetElixir() > 1300:
        base.create_robot('')
    
        if base.GetElixir()<=1300 and base.GetElixir()>=650 :
                i=1
                while (i<14):

                        q,s=base.GetPosition()
                        if q< 10:
                                msg_q = '0' + str(q)
                        else: 
                                msg_q = str(q)
                        if s < 10:
                               msg_s = '0' + str(s)
                        else: 
                               msg_s = str(s)
                        msg = "robot" + msg_q + msg_s
                        base.create_robot(msg)
                        i+=1
        if base.GetElixir()<=650 : 
                bhai=1
                while (bhai < 13):
                        chal,hat=base.GetPosition()
                        if chal< 10:
                                msg_chal = '0' + str(chal)
                        else: 
                                msg_chal = str(chal)
                        if hat < 10:
                               msg_hat = '0' + str(hat)
                        else: 
                               msg_hat = str(hat)
                               msg = "yo" + msg_chal + msg_hat
                        base.create_robot(msg)
                        bhai= bhai +1
               
                
    
    
    



                        

    L = base.GetListOfSignals()
    for l in L:
        if len(l) > 0:
                base.SetYourSignal(l)
                return 


