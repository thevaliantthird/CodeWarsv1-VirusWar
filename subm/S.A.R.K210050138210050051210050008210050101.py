from random import randint

def ActRobot(robot):
   
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        sw = robot.investigate_sw()
        se = robot.investigate_se()
        nw = robot.investigate_nw()
        ne = robot.investigate_ne()
        x,y = robot.GetPosition()
        s = robot.GetCurrentBaseSignal()[6:]
        sx = int(s[0:2])
        sy = int(s[2:4])
                
        A = robot.GetDimensionX()
        B = robot.GetDimensionY()  
        dist_x = abs(sx-x)
        dist_y = abs(sy-y)

        if up == 'enemy':
                a = 1
        elif up == 'enemy-base': 
                a = 10  
                if x < 10:
                        msg_x = '0' + str(x)
                else: 
                        msg_x = str(x)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg_EB = str(50) + msg_x + msg_y
                robot.setSignal(msg_EB)
        else:
                a = 0
        if down == 'enemy':
                b = 1
        elif down == 'enemy-base':
                b = 10 
                if x < 10:
                        msg_x = '0' + str(x)
                else: 
                        msg_x = str(x)
                if y-1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg_EB = str(50) + msg_x + msg_y
                robot.setSignal(msg_EB)
        else:
                b = 0               
        if left == 'enemy':
                c = 1
        elif left == 'enemy-base':
                c = 10
                if x-1 < 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg_EB =str(50) + msg_x + msg_y
                robot.setSignal(msg_EB)
        else:
                c = 0 
        if right== 'enemy':
                d = 1
        elif right == 'enemy-base':
                d = 10 
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                msg_EB =str(50) + msg_x + msg_y
                robot.setSignal(msg_EB)      
        else:
                d = 0
        if nw == 'enemy':
                e = 1   
        elif nw == 'enemy-base':
                e = 10 
                if x-1< 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg_EB = str(50)+ msg_x + msg_y
                robot.setSignal(msg_EB)       
        else:
                e = 0
        if ne == 'enemy':
                f = 1    
                
        elif ne=='enemy-base':
                f=10
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg_EB = str(50) + msg_x + msg_y
                robot.setSignal(msg_EB) 
        else:
                f = 0 
        if sw == 'enemy':
                g = 1
       
        elif sw=='enemy-base':
                g = 10
                if x-1< 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y+1< 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg_EB = str(50) + msg_x + msg_y
                robot.setSignal(msg_EB)   
        else:
                g = 0                              
        if se == 'enemy':
                h = 1  
        elif se=='enemy-base':
                h = 10
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg_EB = str(50)+ msg_x + msg_y
                robot.setSignal(msg_EB)
                
        else:
                h = 0 
        
        
        number = a + b + c + d + e + f + g + h
        if number >= 10 :                                     #Changed signs
                robot.DeployVirus(robot.GetVirus()*0.7)
        elif number >= 4 :
                robot.DeployVirus(800)
        elif number == 3 :
                robot.DeployVirus(500)                
        elif number>=2 :
                robot.DeployVirus(400)        
        elif number>=1 :
                robot.DeployVirus(400)          # Deploy virus
        if sx <= 2*A/3 and sx  >= A/3 and sy <= B/2 :                              #Begins the up mid base case.
                if robot.GetCurrentBaseSignal()[0:2] == str(50) and len(robot.GetInitialSignal()) == 1:   #Enemy base found
               
                        F = robot.GetCurrentBaseSignal()[2:]
                        E_x = int(F[0:2])
                        E_y = int (F[2:4])
                        G = robot.GetInitialSignal()[0:]
                        Pos = int(G[0])
                        if Pos == 1 or Pos == 2 or Pos == 3:
                                if x < E_x-1:
                                        return 2
                                if x > E_x+1:
                                        return 4
                                if y < E_y-1 :
                                        return 3
                                if y > E_y+1:
                                        return 1
                        else:
                                if x < E_x-5:
                                        return 2
                                if x > E_x+5:
                                        return 4
                                if y < E_y-5 :
                                        return 3
                                if y > E_y+5:
                                        return 1
                                else:
                                        return randint(1,4)
                elif robot.GetCurrentBaseSignal()[0:2] == str(98) and len(robot.GetInitialSignal()) == 3 :    #Threat around our base
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 5 or Pos == 6:
                                
                                
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        if y > sy + 3:                                  #changed
                                                return 1
                                        if x > sx + 3:
                                                return 4
                                        if x < sx - 3:
                                                return 2
                                        else:
                                                return randint(1,4)
                        if Pos == 4 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if y > sy + 3:
                                                return 1
                                        if x > sx + 3:
                                                return 4
                                        if x < sx - 3:
                                                return 2
                                        else:
                                                return randint(1,4)
                        if Pos == 7 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if y > sy + 3:
                                                return 1
                                        if x > sx + 3:
                                                return 4
                                        if x < sx - 3:
                                                return 2
                                        else:
                                                return randint(1,4)

                elif len(robot.GetInitialSignal()) > 3 :
                        F = robot.GetInitialSignal()[3:]
                        Pos = int(F[0])
                        if Pos == 1 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 4 
                        if Pos == 4 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 1 
                        if Pos == 2 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 4  # bigger boundary army # ORR     
                        if Pos == 3 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 1
                elif len(robot.GetInitialSignal()) == 3:
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 4 :                
                                if y >= sy - 1:
                                        return 1        
                                elif x >= A/4 :
                                        return 4             
                                else:
                                        return randint(1,4)
                        if Pos == 5:
                                if y >= sy - 1:
                                        return 1        
                                elif x <= A/4 :
                                        return 2
                                elif x >= A/2:
                                        return 4
                                else:
                                        return randint(1,4)             

                        if Pos == 6: 
                                if y >= sy - 1:
                                        return 1       
                                elif x <= A/2 :
                                        return 2
                                elif x >= 3*A/4:
                                        return 4
                                else:
                                        return randint(1,4)          

                        if Pos == 7 :
                                if y > sy:
                                        return 1
                                elif  x <= 3*A/4 and y <= sy:
                                        return 2
                                elif y <= sy and x > 3*A/4:
                                        return randint (1,4)
                                                                      
                                

                elif len(robot.GetInitialSignal()) == 1:                        #attackers star
                        F = robot.GetInitialSignal()[0:]
                        Pos = int(F[0])
                        if Pos == 0:                            #changed
                                if x >= A/4+5:
                                        return 4
                                if dist_y <= 10:
                                        return randint(2,4)
                                if dist_y > 10:
                                        return randint(1,4)
                                
                                
                        if Pos == 1:                                    #changed
                                if dist_y < 7:
                                        if x <= A/4:
                                                return 2
                                        elif x >= A/2+5:
                                                return 4
                                        else :
                                                return randint(2,4)
                                else :
                                        return randint(1,4)  

                        if Pos == 2:                                    #changed
                                if dist_y < 7:
                                        if x <= A/2:
                                                return 2
                                        elif x >= 3*A/4+5:
                                                return 4  
                                        else :
                                                return randint(2,4)
                                else :
                                        return randint(1,4)                             


                        if Pos == 3:                                            #changed
                                if x <= 3*A/4:
                                        return 2
                                if dist_y <= 7:
                                        return randint(2,4)
                                if dist_y > 7:
                                        return randint(1,4)                        #Ends the left mid base case
       

        if sx <= 2*A/3 and sx  >= A/3 and sy >= B/2 :                              #Begins the down mid base case.
                if robot.GetCurrentBaseSignal()[0:2] == str(50) and len(robot.GetInitialSignal()) == 1:   #Enemy base found
               
                        F = robot.GetCurrentBaseSignal()[2:]
                        E_x = int(F[0:2])
                        E_y = int (F[2:4])
                        G = robot.GetInitialSignal()[0:]
                        Pos = int(G[0])
                        if Pos == 1 or Pos == 2 or Pos == 3:
                                if x < E_x-1:
                                        return 2
                                if x > E_x+1:
                                        return 4
                                if y < E_y-1 :
                                        return 3
                                if y > E_y+1:
                                        return 1
                        else:
                                if x < E_x-5:
                                        return 2
                                if x > E_x+5:
                                        return 4
                                if y < E_y-5 :
                                        return 3
                                if y > E_y+5:
                                        return 1
                                else:
                                        return randint(1,4)
                elif robot.GetCurrentBaseSignal()[0:2] == str(98) and len(robot.GetInitialSignal()) == 3 :    #Threat around our base
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 5 or Pos == 6:
                                
                                
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:                                                   #changed
                                        if y < sy - 3:
                                                return 3 
                                        if x > sx + 3:
                                                return 4
                                        if x < sx - 3:
                                                return 2
                                        else:
                                                return randint(1,4)
                        if Pos == 4 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if y < sy - 3:                          #changed
                                                return 3
                                        if x > sx + 3:
                                                return 4
                                        if x < sx - 3:
                                                return 2
                                        else:
                                                return randint(1,4)
                        if Pos == 7 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if y < sy - 3:                          #changed
                                                return 3
                                        if x > sx + 3:
                                                return 4
                                        if x < sx - 3:
                                                return 2
                                        else:
                                                return randint(1,4)

                elif len(robot.GetInitialSignal()) > 3 :
                        F = robot.GetInitialSignal()[3:]
                        Pos = int(F[0])
                        if Pos == 1 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 1
                        if Pos == 4 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 3 
                        if Pos == 2 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 1   # bigger boundary army # ORR     
                        if Pos == 3 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 3
                elif len(robot.GetInitialSignal()) == 3:
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 4 :                
                                if y >= sy - 1:
                                        return 3        
                                elif x >= A/4 :
                                        return 4             
                                else:
                                        return randint(1,4)
                        if Pos == 5:
                                if y >= sy - 1:
                                        return 3       
                                elif x <= A/4 :
                                        return 2
                                elif x >= A/2:
                                        return 4
                                else:
                                        return randint(1,4)             

                        if Pos == 6: 
                                if y >= sy - 1:
                                        return 3       
                                elif x <= A/2 :
                                        return 2
                                elif x >= 3*A/4:
                                        return 4
                                else:
                                        return randint(1,4)          

                        if Pos == 7 :
                                if y > sy:
                                        return 3
                                elif  x <= 3*A/4 and y <= sy:
                                        return 2
                                elif y <= sy and x >= 3*A/4:
                                        return randint (1,4)
                                                                      
                                

                elif len(robot.GetInitialSignal()) == 1:                        #attackers star
                        F = robot.GetInitialSignal()[0:]
                        Pos = int(F[0])
                        if Pos == 0:                            #changed changed
                                if x >= A/4+5:
                                        return 4
                                if dist_y <= 7:
                                       list = [1,2,4]
                                       return list[randint(0,2)]
                                if dist_y > 7:
                                        return randint(1,4)
                                
                                
                        if Pos == 1:                                    #changed
                                if dist_y < 7:
                                        if x <= A/4:
                                                return 2
                                        elif x >= A/2+5:
                                                return 4
                                        else :
                                                list = [1,2,4]
                                                return list[randint(0,2)]
                                else :
                                        return randint(1,4)  

                        if Pos == 2:                                    #changed
                                if dist_y < 7:
                                        if x <= A/2:
                                                return 2
                                        elif x >= 3*A/4+5:
                                                return 4  
                                        else :
                                                list = [1,2,4]
                                                return list[randint(0,2)]        
                                else :
                                        return randint(1,4)                             


                        if Pos == 3:                                            #changed
                                if x <= 3*A/4:
                                        return 2
                                if dist_y <= 7:
                                        list = [1,2,4]
                                        return list[randint(0,2)]
                                if dist_y > 7:
                                        return randint(1,4)                        #Ends the left mid base case
        if sx < A/2:                              #Begins the left mid base case.
                if robot.GetCurrentBaseSignal()[0:2] == str(50) and len(robot.GetInitialSignal()) == 1:   #Enemy base found
               
                        F = robot.GetCurrentBaseSignal()[2:]
                        E_x = int(F[0:2])
                        E_y = int (F[2:4])
                        G = robot.GetInitialSignal()[0:]
                        Pos = int(G[0])
                        if Pos == 1 or Pos == 2 or Pos == 3:
                                if x < E_x-1:
                                        return 2
                                if x > E_x+1:
                                        return 4
                                if y < E_y-1 :
                                        return 3
                                if y > E_y+1:
                                        return 1
                        else:
                                if x < E_x-5:
                                        return 2
                                if x > E_x+5:
                                        return 4
                                if y < E_y-5 :
                                        return 3
                                if y > E_y+5:
                                        return 1
                                else:
                                        return randint(1,4)
                elif robot.GetCurrentBaseSignal()[0:2] == str(98) and len(robot.GetInitialSignal()) == 3 :    #Threat around our base
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 5 or Pos == 6:
                                
                                
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        if x > sx + 3:
                                                return 4
                                        if y > sy + 3:
                                                return 1
                                        if y < sy - 3:
                                                return 3
                                        else:
                                                return randint(1,3)
                        if Pos == 4 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if x > sx + 3:
                                                return 4
                                        if y > sy + 3:
                                                return 1
                                        if y < sy - 3:
                                                return 3
                                        else:
                                                return randint(1,3)
                        if Pos == 7 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if x > sx + 3:
                                                return 4
                                        if y > sy + 3:
                                                return 1
                                        if y < sy - 3:
                                                return 3
                                        else:
                                                return randint(1,3)

                elif len(robot.GetInitialSignal()) > 3 :
                        F = robot.GetInitialSignal()[3:]
                        Pos = int(F[0])
                        if Pos == 1 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 2 
                        if Pos == 4 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 4 
                        if Pos == 2 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 2   # bigger boundary army # ORR     
                        if Pos == 3 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 4
                elif len(robot.GetInitialSignal()) == 3:                #Here generalised
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 4 :                
                                if x >= sx - 1:
                                        return 4        
                                elif y >= B/4 :
                                        return 1             
                                else:
                                        return randint(1,4)
                        if Pos == 5:
                                if x >= sx - 1:
                                        return 4        
                                elif y <= B/4 :
                                        return 3
                                elif y>= B/2:
                                        return 1
                                else:
                                        return randint(1,4)             

                        if Pos == 6: 
                                if x >= sx - 1:
                                        return 4        
                                elif y <= B/2 :
                                        return 3
                                elif y>= 3*B/4:
                                        return 1
                                else:
                                        return randint(1,4)          

                        if Pos == 7 :
                                if x > sx:
                                        return 4
                                elif  y <= 3*B/4 and x <= sx:
                                        return 3
                                elif x <= sx and y >= 3*B/4:
                                        return randint (1,4)
                                                                      
                                

                elif len(robot.GetInitialSignal()) == 1:                        #attackers Rangers
                        F = robot.GetInitialSignal()[0:]                        #Here generalised
                        Pos = int(F[0])
                        if Pos == 0:
                                if y >= (B/4)+5:
                                        return 1
                                if dist_x <= 7:
                                        return randint(1,3)
                                if dist_x > 7:
                                        return randint(1,4)
                                
                                
                        if Pos == 1:
                                if dist_x < 7:
                                        if y <= (B/4):
                                                return 3
                                        elif y >= (B/2)+5:
                                                return 1
                                        else :
                                                return randint(1,3)
                                else :
                                        return randint(1,4)  

                        if Pos == 2:
                                if dist_x < 7:
                                        if y <= (B/2):
                                                return 3
                                        elif y >= (3*B/4) + 5:
                                                return 1
                                        else :
                                                return randint(1,3)
                                else :
                                        return randint(1,4)                             


                        if Pos == 3: 
                                if y <= (3*B/4) :
                                        return 3
                                if dist_x <= 7:
                                        return randint(1,3)
                                if dist_x > 7:
                                        return randint(1,4)                        #Ends the left mid base case
        if sx >= A/2:                                                #Begins the right mid base case
                if robot.GetCurrentBaseSignal()[0:2] == str(50) and len(robot.GetInitialSignal()) == 1:   #Enemy base found
               
                        F = robot.GetCurrentBaseSignal()[2:]
                        E_x = int(F[0:2])
                        E_y = int (F[2:4])
                        G = robot.GetInitialSignal()[0:]
                        Pos = int(G[0])
                        if Pos == 1 or Pos == 2 or Pos == 3:
                                if x > E_x+1:
                                        return 4
                                if x < E_x-1:
                                        return 2
                                if y < E_y-1 :
                                        return 3
                                if y > E_y+1:
                                        return 1
                        else:
                                if x < E_x-5:
                                        return 2
                                if x > E_x+5:
                                        return 4
                                if y < E_y-5 :
                                        return 3
                                if y > E_y+5:
                                        return 1
                                else:
                                        return randint(1,4)
                elif robot.GetCurrentBaseSignal()[0:2] == str(98) and len(robot.GetInitialSignal()) == 3 :    #Threat around our base
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 5 or Pos == 6:
                                
                                
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        if x > sx + 3:
                                                return 4
                                        if y > sy + 3:
                                                return 1
                                        if y < sy - 3:
                                                return 3
                                        else:
                                              return randint(1,4)
                        if Pos == 4 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if x < sx - 3:
                                                return 2
                                        if y > sy + 3:
                                                return 1
                                        if y < sy - 3:
                                                return 3
                                        else:
                                                list = [1,3,4]
                                                return list[randint(0,2)]
                        if Pos == 7 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        if x < sx + 3:
                                                return 2
                                        if y > sy + 3:
                                                return 1
                                        if y < sy - 3:
                                                return 3
                                        else:
                                                list = [1,3,4]
                                                return list[randint(0,2)]

                elif len(robot.GetInitialSignal()) > 3 :
                        F = robot.GetInitialSignal()[3:]
                        Pos = int(F[0])
                        if Pos == 1 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 2  
                        if Pos == 4 :
                                if x == sx + 1 and  y == sy  :
                                        return 1
                                elif x == sx + 1 and y == sy - 1:  #This makes 1 to rotate in lower circle
                                        return 4        
                                elif y == sy - 1 and x == sx:
                                        return 4
                                elif y == sy - 1 and x == sx - 1:
                                        return 3 
                                elif x == sx - 1 and y == sy :
                                        return 3
                                elif x == sx - 1 and y == sy + 1:
                                        return 2               
                                elif y == sy + 1 and x == sx:
                                        return 2
                                elif y == sy + 1 and x == sx + 1:
                                        return 1 
                                else:
                                        return 4 
                        if Pos == 2 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 2   # bigger boundary army # ORR     
                        if Pos == 3 :
                                if x== sx + 2 and ( y == sy or y == sy + 1 or y == sy - 1 or y == sy - 2):
                                        return 3
                                elif x == sx + 2 and ( y == sy + 2):
                                        return 4
                                elif (x == sx or x == sx + 1 or x == sx - 1 ) and y == sy + 2:
                                        return 4
                                elif x == sx - 2 and ( y == sy + 2 or y == sy + 1 or y == sy or y == sy - 1):
                                        return 1
                                elif (x == sx - 2 or x == sx - 1 or x == sx or x == sx + 1 ) and y == sy - 2:
                                        return 2
                                else:
                                        return 4
                elif len(robot.GetInitialSignal()) == 3:
                        F = robot.GetInitialSignal()[2:]
                        Pos = int(F[0])
                        if Pos == 4 :                
                                if x <= sx :
                                        return 2        
                                elif y >= B/4 :
                                        return 1             
                                else:
                                        return randint(1,4)
                        if Pos == 5:
                                if x <= sx :
                                        return 2        
                                elif y <= B/4 :
                                        return 3
                                elif y>= B/2 :
                                        return 1
                                else:
                                        return randint(1,4)             

                        if Pos == 6: 
                                if x <= sx :
                                        return 2       
                                elif y <= B/2 :
                                        return 3
                                elif y>= 3*B/4:
                                        return 1
                                else:
                                        return randint(1,4)          

                        if Pos == 7 :
                                if x <= sx:
                                        return 2
                                elif  y <= 3*B/4 :
                                        return 3
                                elif x > sx and y >= 3*B/4:
                                        return randint (1,4)               

                elif len(robot.GetInitialSignal()) == 1:                        #attackers star
                        F = robot.GetInitialSignal()[0:]
                        Pos = int(F[0])
                        if Pos == 0:
                                if y >= B/4+5:
                                        return 1
                                if dist_x <= 7:
                                                list = [1,3,4]
                                                return list[randint(0,2)]
                                if dist_x > 7:
                                        return randint(1,4)
                                
                        
                        if Pos == 1:
                                if dist_x < 7:
                                        if y <= B/4:
                                                return 3
                                        elif y >= B/2 +5:
                                                return 1
                                        else :
                                                list = [1,3,4]
                                                return list[randint(0,2)]
                                else :
                                        return randint(1,4)  

                        if Pos == 2:
                                if dist_x < 7:
                                        if y <= B/2:
                                                return 3
                                        elif y >= 3*B/4 + 5:
                                                return 1
                                        else :
                                                list = [1,3,4]
                                                return list[randint(0,2)]
                                else :                                                      
                                        return randint(1,4)                             


                        if Pos == 3: 
                                if y <= 3*B/4 :
                                        return 3
                                if dist_x <= 7:
                                        list = [1,3,4]
                                        return list[randint(0,2)]
                                if dist_x > 7:
                                        return randint(1,4)       
                                        
                
                                else:      
                                        return 0                                #Ends the right mid base case
                
                                
                
        else:      
                return 0

def ActBase(base):
    
        if base.GetElixir() > 1800:                    #Creating Bodyguards
                base.create_robot("Def" + str(1))
                base.create_robot("Def" + str(2))
                base.create_robot("Def" + str(3))
                base.create_robot("Def" + str(4))
        elif base.GetElixir() > 1600:                   #Creating Collectors
                base.create_robot("Co" + str(4))
                base.create_robot("Co" + str(5))
                base.create_robot("Co" + str(6))
                base.create_robot("Co" + str(7))
        elif base.GetElixir() > 600:
                base.create_robot(str(0))
                base.create_robot(str(1))
                base.create_robot(str(2)) 
                base.create_robot(str(3))               #Attackers - writing many times actually creates quickly in first iteration itself.
                base.create_robot(str(0))
                base.create_robot(str(1))
                base.create_robot(str(2)) 
                base.create_robot(str(3))
                base.create_robot(str(0))
                base.create_robot(str(1))
                base.create_robot(str(2)) 
                base.create_robot(str(3))
                base.create_robot(str(0))
                base.create_robot(str(1))
                base.create_robot(str(2)) 
                base.create_robot(str(3))
                base.create_robot(str(0))
                base.create_robot(str(1))
                base.create_robot(str(2)) 
                base.create_robot(str(3))
        X,Y = base.GetPosition()        
        if X < 10:
                msg_X = '0' + str(X)
        else: 
                msg_X = str(X)
        if Y < 10:
                msg_Y = '0' + str(Y)
        else:
                msg_Y = str(Y)
        base.SetYourSignal(str(12) + str(3456) + msg_X + msg_Y)
        
        if base.investigate_up == 'enemy' or base.investigate_down == 'enemy' or base.investigate_right == 'enemy' or base.investigate_left == 'enemy' or base.investigate_ne == 'enemy' or  base.investigate_nw == 'enemy' or base.investigate_se == 'enemy' or  base.investigate_sw == 'enemy':
              base.DeployVirus(1000)
              base.SetYourSignal(str(98) + str(5434) + msg_X + msg_Y )   
        
        if base.GetElixir() < 600:                          #DangerSignals
                base.SetYourSignal(str(98) + str(5434) + msg_X + msg_Y ) 
        L = base.GetListOfSignals()
        for l in L:
                if len(l) == 6:
                        base.SetYourSignal(l + msg_X + msg_Y)        
                
        
        
        return
 
    