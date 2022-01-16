
from random import randint
from typing import Mapping

def Decode(String): # Decodes the string messages 
     MainMessage = String[4:]
     i = 0
     X = ''
     Y = ''
     for x in MainMessage:      
          if i == 0 and x != ' ':
               X += x
          elif i == 0 and x == ' ':
               i += 1
          
          elif i == 1 and x != ' ' :
               Y += x
     X = int(X)
     Y = int(Y)
     return (X, Y)

def ConvertCoord(x,y,i): # Gives out the position of obstacle taking in position of investigator
     if i==1:
          y -= 1
     elif i == 2:
          x += 1
     elif i == 3:
          y += 1
     elif i == 4:
          x -= 1
     elif i == 5:
          x += 1
          y -= 1
     elif i == 6:
          x += 1
          y += 1
     elif i == 7:
          x -= 1
          y += 1
     elif i == 8:
          x -= 1
          y -= 1
     return (x,y)

def Distance(x1,y1,x2,y2):
     distance = abs(x1-x2)+(y1-y2)
     return distance

def ActRobot(robot): 
     '''1-up, 2-right, 3-down, 4-left, 5-ne, 6-se,
      7-sw, 8-nw'''    
     CurrentSignal = robot.GetCurrentBaseSignal()
     
     if CurrentSignal[0:4] == 'Base':
          X_B, Y_B = Decode(CurrentSignal) 
          
     
     elif CurrentSignal[0:4] == 'EneB':
          X_E, Y_E = Decode(CurrentSignal) 
    

     def InvestigationsR():
          Investigations = [0,0,0,0,0,0,0,0,0]
          Investigations[0] = 0
          Investigations[1] = robot.investigate_up()
          Investigations[2] = robot.investigate_right()
          Investigations[3] = robot.investigate_down()
          Investigations[4] = robot.investigate_left()
          Investigations[5] = robot.investigate_ne()
          Investigations[6] = robot.investigate_se()
          Investigations[7] = robot.investigate_sw()
          Investigations[8] = robot.investigate_nw()
          return Investigations
     Investigate = InvestigationsR() 

     def moveRobot(x,y):
          '''Makes the robot move to the coordinate (x,y). 
          Also deploys minimal virus. '''
          if x == 1000 and y ==1000:
               return randint(1,4)
          X,Y = robot.GetPosition()
          if CurrentSignal[0:4] == 'EneB' and robot.GetInitialSignal()[0] == 'A':
               
                    l = [1,2,3,4] 
                    for i , Data in enumerate(Investigate):
                         if Data == 'enemy':
                              if i in l:
                                   l.remove(i)
                              elif i == 5:
                                   if 1 in l:
                                             l.remove(1)
                                   if 2 in l:
                                             l.remove(2)      
                              elif i == 6 :
                                   if 2 in l:
                                             l.remove(2)
                                   if 3 in l:
                                             l.remove(3)  
                              elif i == 7 :
                                   if 3 in l:
                                             l.remove(3)
                                   if 4 in l:
                                             l.remove(4)
                              elif i == 8 :
                                   if 1 in l:
                                             l.remove(1)
                                   if 4 in l:
                                             l.remove(4)
                         if Distance(X,Y,X_E,Y_E) < 8:
                              if len(l) < 4 and robot.GetVirus() > 1000:
                                   robot.DeployVirus(50)
                                   a =[]
                                   if X > x:
                                        a.append(4)
                                   elif X < x:
                                        a.append(2)
                                   if Y > y:
                                        a.append(1)
                                   elif Y < y:
                                        a.append(3)
                                   if X==x and Y==y:
                                        return 0
                                   return a[randint(0, len(a)-1)]         

                         elif len(l) < 2 :
                              if robot.GetVirus() > 1200:
                                   robot.DeployVirus(200)            
                                   robot.setSignal('Help'+str(X)+' '+str(Y))
                              if robot.GetElixir() > 50:  
                                   return randint(1,4)
                              else:
                                   if len(l) == 0:
                                        return randint(1,4)
                                   else :
                                        return l[randint(0,len(l)-1)]

                         elif len(l) < 4:
                              if robot.GetVirus() > 1040:
                                   robot.DeployVirus(40)
                                   return l[randint(0,len(l)-1)]
                         elif len(l) == 4:
                              a =[]
                              if x == 1000 and y ==1000:
                                   return randint(1,4)
                              if X > x:
                                   a.append(4)
                              elif X < x:
                                   a.append(2)
                              if Y > y:
                                   a.append(1)
                              elif Y < y:
                                   a.append(3)
                              if X==x and Y==y:
                                   return 0
                              return a[randint(0, len(a)-1)]
          l = [1,2,3,4] 
          for i , Data in enumerate(Investigate):
               if Data == 'enemy':
                    if i in l:
                         l.remove(i)
                    elif i == 5:
                         if 1 in l:
                               l.remove(1)
                         if 2 in l:
                               l.remove(2)      
                    elif i == 6 :
                         if 2 in l:
                               l.remove(2)
                         if 3 in l:
                               l.remove(3)  
                    elif i == 7 :
                         if 3 in l:
                               l.remove(3)
                         if 4 in l:
                               l.remove(4)
                    elif i == 8 :
                         if 1 in l:
                               l.remove(1)
                         if 4 in l:
                               l.remove(4)
          

          if len(l) < 2 :
               if robot.GetVirus() > 1200:
                    robot.DeployVirus(200)            
               robot.setSignal('Help'+str(X)+' '+str(Y))
               if robot.GetElixir() > 50:  
                    return randint(1,4)
               else:
                    if len(l) == 0:
                         return randint(1,4)
                    else :
                         return l[randint(0,len(l)-1)]

          elif len(l) < 4:
               if robot.GetVirus() > 1040:
                    robot.DeployVirus(40)
                    return l[randint(0,len(l)-1)]
          elif len(l) == 4:
               a =[]              
               if X > x:
                    a.append(4)
               elif X < x:
                    a.append(2)
               if Y > y:
                    a.append(1)
               elif Y < y:
                    a.append(3)
               if X==x and Y==y:
                    return 0
               return a[randint(0, len(a)-1)]
               
     def moveRobotC(x,y):
          X,Y = robot.GetPosition()
          l = [1,2,3,4] 
          for i , Data in enumerate(Investigate):
               if Data == 'enemy':
                    V = robot.GetVirus()
                    if 500 < V < 1500:
                         robot.DeployVirus(100)
                    elif 1500 <= V <=5000:
                         robot.DeployVirus(500)
                    elif 5000 < V < 10000:
                         robot.DeployVirus(1000)
                    elif 10000 < V:
                         robot.DeployVirus(1000+(V-10000)*0.1)
          a =[]              
          if X > x:
               a.append(4)
          elif X < x:
               a.append(2)
          if Y > y:
               a.append(1)
          elif Y < y:
               a.append(3)
          if X==x and Y==y:
               return 0
          return a[randint(0, len(a)-1)]
                    
                    

                    
     for i, Data in enumerate(Investigate) :           
          if Data == 'enemy-base' :
               x,y = robot.GetPosition()
               x,y = ConvertCoord(x,y,i)
               robot.setSignal('EneB'+str(x)+' '+str(y))
               CurrentSignal = 'EneB'+str(x)+' '+str(y)
               break

          

     if robot.GetInitialSignal()[0] == 'A':       
          if robot.GetInitialSignal()[1] == '1':
               for i, Data in enumerate(Investigate) :  
                    if CurrentSignal[0:4] == 'EneB' :
                         break
                    if Data == 'friend-base':
                      
                              x,y = robot.GetPosition()
                              x,y = ConvertCoord(x,y,i)         
                              robot.setSignal('Base'+str(x)+' '+str(y))
          Index = int(robot.GetInitialSignal()[1:])
          X,Y = robot.GetPosition()
          # if Index > robot.GetDimensionY()//3:
          #      return randint(1,4)
          if CurrentSignal[0:4] == 'EneB'  :
               x,y = robot.GetPosition()
               
               try:
                    if Distance(x,y,X_E,Y_E) < 2:
                         robot.DeployVirus(0.5*robot.GetVirus()) 
                         return moveRobot(x+1, y+1)
                    else:
                         return moveRobot(X_E,Y_E)
               except:
                    X_E, Y_E = Decode(CurrentSignal)
                    return moveRobot(X_E,Y_E)
          else :
               
               if 1 <= Index <= robot.GetDimensionY()//3 :
                    K = 3*Index
                    r = 0 
                    if X == robot.GetDimensionX()-1:
                         r = 1
                    elif X == 1:
                         r = 2
                    if moveRobot(X, K ) == 0 :
                              if r == 1 :
                                   return moveRobot(X,K-1)
                              else:
                                   return 2
                    elif moveRobot(X,K-1) == 0:
                         if r == 2:
                              return moveRobot(X,K)
                         else:
                              return 4
                    else :
                         return moveRobot(X,K)
               elif Index == 17 or Index == 18 :
                    
                    r = 0 
                    x,y = robot.GetPosition()
                    try:
                         

                         if X == robot.GetDimensionX()-1:
                              r = 1
                         elif X == 1:
                              r = 2
                         if moveRobot(X, Y_B ) == 0 :
                                   if r == 1 :
                                        return moveRobot(X,Y_B-1)
                                   else:
                                        return 2
                         elif moveRobot(X,Y_B-1) == 0:
                              if r == 2:
                                   return moveRobot(X,Y_B)
                              else:
                                   return 4
                         else :
                              return moveRobot(X,Y_B)
                    except:
                         return 1
               elif Index == 19 or Index == 20:
                    r = 0 
                    x,y = robot.GetPosition()
                    try:   
                         
                         if Y == robot.GetDimensionY()-1:
                              r = 1
                         elif Y == 1:
                              r = 2
                         if moveRobot(X_B, Y ) == 0 :
                                   if r == 1 :
                                        return moveRobot(X_B-1,Y)
                                   else:
                                        return 3
                         elif moveRobot(X_B-1,Y) == 0:
                              if r == 2:
                                   return moveRobot(X_B,Y)
                              else:
                                   return 1
                         else :
                              return moveRobot(X_B,Y)
                    except:
                         return 1
                        
               else :    
                    return moveRobot(1000,1000)
     
     elif robot.GetInitialSignal()[0] == 'C':
          Index = int(robot.GetInitialSignal()[1:])
          try:
               if Index == 1:
                    return moveRobotC(X_B+1,Y_B+1)
               elif Index == 2:
                    return moveRobotC(X_B+1,Y_B-1)
               elif Index == 3:
                    return moveRobotC(X_B-1,Y_B+1)
               elif Index == 4:
                    return moveRobotC(X_B-1,Y_B-1)
          except:
               return 0
     elif robot.GetInitialSignal()[0] == 'B':
          Index = int(robot.GetInitialSignal()[1:])
          try :
               if 1 <= Index <= 3:
                    X,Y = robot.GetPosition()
                    K = 3*Index + Y_B + 2
                    r = 0 
                    if X == robot.GetDimensionX()-1:
                         r = 1
                    elif X == 1:
                         r = 2
                    if moveRobot(X, K ) == 0 :
                              if r == 1 :
                                   return moveRobot(X,K-1)
                              else:
                                   return 2
                    elif moveRobot(X,K-1) == 0:
                         if r == 2:
                              return moveRobot(X,K)
                         else:
                              return 4
                    else :
                         return moveRobot(X,K)
               else:
                    X,Y = robot.GetPosition()
                    K = -3*(Index-3) + Y_B -2
                    r = 0 
                    if X == robot.GetDimensionX()-1:
                         r = 1
                    elif X == 1:
                         r = 2
                    if moveRobot(X, K ) == 0 :
                              if r == 1 :
                                   return moveRobot(X,K-1)
                              else:
                                   return 2
                    elif moveRobot(X,K-1) == 0:
                         if r == 2:
                              return moveRobot(X,K)
                         else:
                              return 4
                    else :
                         return moveRobot(X,K)
          except:
               return randint(1,4)

               



def ActBase(base):
     def InvestigationsR():
          Investigations = [0,0,0,0,0,0,0,0,0]
          Investigations[0] = 0
          Investigations[1] = base.investigate_up()
          Investigations[2] = base.investigate_right()
          Investigations[3] = base.investigate_down()
          Investigations[4] = base.investigate_left()
          Investigations[5] = base.investigate_ne()
          Investigations[6] = base.investigate_se()
          Investigations[7] = base.investigate_sw()
          Investigations[8] = base.investigate_nw()
          return Investigations
     Investigate = InvestigationsR()
     for i , Data in enumerate(Investigate):
               if Data == 'enemy':
                    V = base.GetVirus()
                    if 500 < V < 1500:
                         base.DeployVirus(100)
                    elif 1500 <= V <=5000:
                         base.DeployVirus(500)
                    elif 5000 < V < 10000:
                         base.DeployVirus(1000)
                    elif 10000 < V:
                         base.DeployVirus(1000+(V-10000)*0.1)
     

     if base.GetElixir() > 1000:
          Robot_Name ='A'
          for i in range(1,21):
               Robot_Name += str(i)
               base.create_robot(Robot_Name)
               Robot_Name = 'A'
     if base.GetElixir() > 700:
          Robot_Name ='B'
          for i in range(1,7):
               Robot_Name += str(i)
               base.create_robot(Robot_Name)
               Robot_Name = 'B'
     elif base.GetElixir() > 500:  
          Robot_Name ='C'
          for i in range(1,5):
               Robot_Name += str(i)
               base.create_robot(Robot_Name)
               Robot_Name = 'C'

     SignalList = base.GetListOfSignals()
     
     for Signal in SignalList:
          #Base- Base Coordinates
          #EneB- Enemy Base found and its coordinates.  
           
          if Signal[0:4] == 'EneB':
               x,y = Decode(Signal)
               base.SetYourSignal('EneB'+str(x)+' '+str(y))
               main = Signal
               break
          
               
          elif Signal[0:4] == 'Base' :
               base.SetYourSignal(Signal)

     return