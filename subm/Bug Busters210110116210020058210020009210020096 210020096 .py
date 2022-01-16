from random import randint




def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        x,y = robot.GetPosition()
        sgnl = str(x)+","+str(y)
        
        
        bse = str(robot.GetCurrentBaseSignal())
        if len(bse) > 0:
                
                q = int(bse.find(","))
                w = len(bse) 
                if robot.GetElixir() > 0:
                        
                        while int(x) < int(bse[0:q]):
                                        
                                return 2
                        while int(x) > int(bse[0:q]):
                                        
                                return 4
                        while int(y) < int(bse[q+1:w]):
                                        
                                return 3
                        while int(y) > int(bse[q+1:w]):

                                        
                                return 1
                        
                        
               
        else:
                if up == "enemy-base":
        
                        y = y - 1
                        robot.DeployVirus(200)
                        robot.setSignal(str(str(x)+","+str(y)))  
                elif down == "enemy-base":
                        y = y + 1
                        robot.DeployVirus(200)
                        robot.setSignal(str(str(x)+","+str(y)))
                elif left == "enemy-base":
                        robot.DeployVirus(200)
                        x = x - 1
                        robot.setSignal(str(str(x)+","+str(y)))
                elif right == "enemy-base":
                        x = x + 1
                        robot.setSignal(str(str(x)+","+str(y)))
                elif se == "enemy-base":
                
                        y = y + 1
                        x = x + 1
                        robot.DeployVirus(200)
                        robot.setSignal(str(str(x)+","+str(y)))
                elif sw == "enemy-base":


                        x = x - 1
                        y = y + 1
                        
                        robot.setSignal(str(str(x)+","+str(y)))
                elif ne == "enemy-base":
                        
                        x = x + 1
                        y = y - 1
                        robot.DeployVirus(200)
                        robot.setSignal(str(str(x)+","+str(y)))
                elif nw == "enemy-base":
                        robot.DeployVirus(200)
                        x = x - 1
                        y = y - 1
                        
                        robot.setSignal(str(str(x)+","+str(y)))
                elif up == "enemy" and robot.GetVirus() > 500:
                        return randint(2,4)
                        robot.DeployVirus(200)
                elif down == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                        return 1 or 2 or 4
                elif right == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                        return 1 or 3 or 4
                elif left == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                        randint(1,3)
                elif se == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                        return 2 or 4
                elif sw == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                        return randint(3,4)
                elif ne == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                        return randint(1,2)
                elif nw == "enemy" and robot.GetVirus() > 500:
                        robot.DeployVirus(200)
                else:
                        return randint(1,4)
                


                                



                


          
        
       
             

                
                       

        
        
        
        


def ActBase(base):

        
        
        

    
    
    
        if base.GetElixir() > 250:
            base.create_robot('')
        elif base.investigate_up() == "enemy":
            base.DeployVirus(200)
        elif base.investigate_down() == "enemy":
            base.DeployVirus(200)
        elif base.investigate_left() =="enemy":
             base.DeployVirus(200)
        elif base.investigate_right() == "enemy":
            base.DeployVirus(200)
        elif base.investigate_sw() == "enemy":
            base.DeployVirus(200)
        elif base.investigate_se() == "enemy":
            base.DeployVirus(200)
        elif base.investigate_ne() =="enemy":
          base.DeployVirus(200)
        elif base.investigate_nw() == "enemy":
            base.DeployVirus(200)
        
        L = base.GetListOfSignals()
        
        for sgnl in L:
                if len(sgnl) > 0:
                        base.SetYourSignal(sgnl)
                        return
        
        return