from random import randint
import random

def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        
        t = robot.GetCurrentBaseSignal()
        x1 = int(t[0:2])
        y1 = int(t[2:4])
        
        x2 = robot.GetDimensionX() 
        y2 = robot.GetDimensionY() 
        x,y = robot.GetPosition()
        v=robot.GetVirus()
        if x1>x2*3/5 and y1<y2*2/5:
                q=1
        if x1>x2*3/5 and y1>y2*3/5:
                q=4
        if x1<x2*2/5 and y1<y2*2/5:
                q=2        
        if x1<x2*2/5 and y1>y2*3/5:
                q=3
        if x1<x2*3/5 and x1>x2*2/5 and y1<y2/2:
                q=6
        if y1<y2*3/5 and y1>y2*2/5 and x1>x2/2:
                q=5         
        if x1<x2*3/5 and x1>x2*2/5 and y1>y2/2:
                q=8
        if y1<y2*3/5 and y1>y2*2/5 and x1<x2/2:
                q=7
        
        if up == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0

        if down == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
                        
        
        if left == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
                
        if right == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
        if robot.investigate_ne() == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
        elif robot.investigate_ne() == "enemy-base":
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
        if robot.investigate_nw() == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
        elif right == "enemy-base":
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
        if robot.investigate_sw() == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
        elif right == "enemy-base":
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
        if robot.investigate_se() == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(500)
        elif robot.investigate_se() == "enemy-base":
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
                robot.DeployVirus(robot.GetVirus()*0.75)
                return 0
        



        # returns from here on
        if robot.GetInitialSignal()[0:1] == "d":
                if robot.investigate_up() == "enemy":
                        robot.DeployVirus(v/4)  
                if robot.investigate_down() == "enemy":
                        robot.DeployVirus(v/4)
                if robot.investigate_right() == "enemy":
                        robot.DeployVirus(v/4)
                if robot.investigate_left() == "enemy":
                        robot.DeployVirus(v/4)
                if robot.investigate_ne() == "enemy":
                        robot.DeployVirus(v/4)
                if robot.investigate_nw() == "enemy":
                        robot.DeployVirus(v/4)
                if robot.investigate_se() == "enemy":
                        robot.DeployVirus(v/4)
                if robot.investigate_sw() == "enemy":
                        robot.DeployVirus(v/4)
       
        if (robot.GetInitialSignal() == "g1" or robot.GetInitialSignal() == "g2" or robot.GetInitialSignal() == "g3" ) :

# taking midline x2/2-1  and y2/2-1
                # base on central horizontal axis

                if(q==7 or q==5): #abs(x2-2*x1)<=X2/2 and similarly for vertical keeping the conditions for the quadrants the same
                        if(abs(x2-x1)>x1):
                                if(robot.GetInitialSignal() == "g1"):#g1
                                        if(x==0 and y!=0):
                                                return 1
                                        elif(y==0 and x!=x1):
                                                return 2
                                        elif(x==x1 and y!=(y2-1)/3 and y!=y1):
                                                return 3        
                                        elif((y==(y2-1)/3 or y==y1) and x!=0):
                                                return 4
                                elif(robot.GetInitialSignal() == "g2"):#g2
                                        if(x==0 and y!=(y2-1)/3+1):
                                                return 1
                                        elif(y==(y2-1)/3+1 and x!=x1):
                                                return 2
                                        elif(x==x1 and y!=(y2-1)*2/3):
                                                        return 3        
                                        elif(y==(y2-1)*2/3 and x!=0):
                                                return 4
                                elif(robot.GetInitialSignal() == "g3"):#g3
                                        if(x==0 and y!=(y2-1)*2/3+1):
                                                return 1
                                        elif(y==(y2-1)*2/3+1 and x!=x1):
                                                return 2
                                        elif(x==x1 and y!=(y2-1)):
                                                return 3        
                                        elif(y==(y2-1) and x!=0):
                                                return 4
                               
                        else:
                                if(robot.GetInitialSignal() == "g1"):#g1
                                        if(x==x1 and y!=0):
                                                return 1
                                        elif(y==0 and x!=x2-1):
                                                return 2
                                        elif(x==x2-1 and y!=(y2-1)/3):
                                                return 3        
                                        elif(y==(y2-1)/3 and x!=x1):
                                                return 4
                                elif(robot.GetInitialSignal() == "g2"):#g2
                                        if(x==x1 and y!=(y2-1)/3+1):
                                                return 1
                                        elif(y==(y2-1)/3+1 and x!=x2-1):
                                                return 2
                                        elif(x==x2-1 and y!=(y2-1)*2/3):
                                                return 3        
                                        elif(y==(y2-1)*2/3 and x!=x1):
                                                return 4
                                elif(robot.GetInitialSignal() == "g3"):#g3
                                        if(x==x1 and y!=(y2-1)*2/3+1 and y!=y1):
                                                return 1
                                        elif((y==(y2-1)*2/3+1 or y==y1) and x!=x2-1):
                                                return 2
                                        elif(x==x2-1 and y!=(y2-1)):
                                                return 3        
                                        elif(y==(y2-1) and x!=x1):
                                                return 4        

                elif(q==6 or q==8):  #base on central vertical axis   split for g1,g2,g3
                        if(abs(y2-y1)>y1):
                                if(robot.GetInitialSignal() == "g1"):#g1
                                        if(x==0 and y!=0):
                                                return 1
                                        elif(y==0 and x!=(x2-1)/3):
                                                return 2
                                        elif(x==(x2-1)/3 and y!=y1):
                                                return 3        
                                        elif(y==y1 and x!=0):
                                                return 4
                                elif(robot.GetInitialSignal() == "g2"):#g2
                                        if(x==(x2-1)/3 +1 and y!=0):
                                                return 1
                                        elif(y==0 and x!=(x2-1)*2/3):
                                                return 2
                                        elif(x==(x2-1)*2/3 and y!=y1):
                                                return 3        
                                        elif(y==y1 and x!=(x2-1)/3+1):
                                                return 4
                                elif(robot.GetInitialSignal() == "g3"):#g3
                                        if((x==(x2-1)*2/3 +1  or x==x1) and y!=0):
                                                return 1
                                        elif(y==0 and x!=(x2-1)):
                                                return 2
                                        elif(x==(x2-1) and y!=y1):
                                                return 3        
                                        elif(y==y1 and x!=(x2-1)*2/3 +1 and x!=x1):
                                                return 4
                        else:
                                if(robot.GetInitialSignal() == "g1"):#g1
                                        if(x==0 and y!=y1):
                                                return 1
                                        elif(y==y1 and x!=(x2-1)/3 and x!=x1):
                                                return 2
                                        elif((x==(x2-1)/3 or x==x1)  and y!=y2-1):
                                                return 3        
                                        elif(y==y2-1 and x!=0):
                                                return 4
                                elif(robot.GetInitialSignal() == "g2"):#g2
                                        if(x==(x2-1)/3+1 and y!=y1):
                                                return 1
                                        elif(y==y1 and x!=(x2-1)*2/3):
                                                return 2
                                        elif(x==(x2-1)*2/3 and y!=y2-1):
                                                return 3        
                                        elif(y==y2-1 and x!=(x2-1)/3+1):
                                                return 4
                                elif(robot.GetInitialSignal() == "g3"):#g3
                                        if(x==(x2-1)*2/3+1 and y!=y1):
                                                return 1
                                        elif(y==y1 and x!=(x2-1)):
                                                return 2
                                        elif(x==(x2-1) and y!=y2-1):
                                                return 3        
                                        elif(y==y2-1 and x!=(x2-1)*2/3+1 ):
                                                return 4
                elif(q==1):  #Q1 different for g1,g2,g3
                        #g1
                        if(robot.GetInitialSignal() == "g1"):
                                if(x==x2/2-1 and y!=0):
                                        return 1
                                elif(y==0 and x!=x1-1):
                                        return 2
                                elif(x==x1-1 and y!=y1):
                                        return 3        
                                elif( y==y1 and x!=x2/2-1):
                                        return 4
                        #g2
                        elif(robot.GetInitialSignal() == "g2"):
                                if(x==x1 and y!=y1+1 and y!=y1):
                                        return 1
                                elif((y==y1+1 or y==y1) and x!=x2-1):
                                        return 2
                                elif(x==x2-1 and y!=y2/2-1):
                                        return 3        
                                elif( y==y2/2-1 and x!=x1):
                                        return 4
                        #g3
                        elif(robot.GetInitialSignal() == "g3"):
                                if(x==x1 and y!=0):
                                        return 1
                                elif(y==0 and x!=x2-1):
                                        return 2
                                elif(x==x2-1 and y!=y1):
                                        return 3        
                                elif( y==y1 and x!=x1):
                                        return 4

                elif(q==2):#Q2
                        #g1
                        if(robot.GetInitialSignal() == "g1"):
                                if(x==0 and y!=y1+1):
                                        return 1
                                elif(y==y1+1 and x!=x1):
                                        return 2
                                elif(x==x1 and y!=y2/2-1):
                                        return 3        
                                elif( y==y2/2-1 and x!=0):
                                        return 4
                        #g2
                        elif(robot.GetInitialSignal() == "g2"):
                                if((x==x1+1 or x==x1) and y!=0):
                                        return 1
                                elif(y==0 and x!=x2/2-1):
                                        return 2
                                elif(x==x2/2-1 and y!=y1):
                                        return 3        
                                elif( y==1 and (x!=x1+1 and x!=x1)):
                                        return 4
                        #g3
                        elif(robot.GetInitialSignal() == "g3"):
                                if(x==0 and y!=0):
                                        return 1
                                elif(y==0 and x!=x1):
                                        return 2
                                elif(x==x1 and y!=y1):
                                        return 3        
                                elif( y==y1 and x!=0):
                                        return 4

                elif(q==3): #Q3
                        #g1
                        if(robot.GetInitialSignal() == "g1"):
                                if(x==x1+1 and y!=y1):
                                        return 1
                                elif(y==y1 and x!=x2/2-1):
                                        return 2
                                elif(x==x2/2-1 and y!=y2-1):
                                        return 3        
                                elif( y==y2-1 and x!=x1+1):
                                        return 4
                        #g2
                        elif(robot.GetInitialSignal() == "g2"):
                                if(x==0 and y!=y2/2-1):
                                        return 1
                                elif(y==y2/2-1 and x!=x1):
                                        return 2
                                elif(x==x1 and (y!=y1 and y!=y1-1)):
                                        return 3        
                                elif(( y==y1 or y==y1-1) and x!=0):
                                        return 4
                        #g3
                        elif(robot.GetInitialSignal() == "g3"):
                                if(x==0 and y!=y1):
                                        return 1
                                elif(y==y1 and x!=x1):
                                        return 2
                                elif(x==x1 and y!=y2-1):
                                        return 3        
                                elif( y==y2-1 and x!=0):
                                        return 4
                elif(q==4):#Q4
                        #g1
                        if(robot.GetInitialSignal() == "g1"):
                                if(x==x1 and y!=y2/2-1):
                                        return 1
                                elif(y==y2/2-1 and x!=x2-1):
                                        return 2
                                elif(x==x2-1 and y!=y1-1):
                                        return 3        
                                elif( y==y1-1 and x!=x1):
                                        return 4
                        #g2
                        elif(robot.GetInitialSignal() == "g2"):
                                if(x==x2/2-1 and y!=y1):
                                        return 1
                                elif(y==y1 and (x!=x1-1 and x!=x1)):
                                        return 2
                                elif((x==x1-1 or x==x1 )and y!=y2-1):
                                        return 3        
                                elif( y==y2-1 and x!=x2/2-1):
                                        return 4
                        #g3
                        elif(robot.GetInitialSignal() == "g3"):
                                if(x==x1 and y!=y1):
                                        return 1
                                elif(y==y1 and x!=x2-1):
                                        return 2
                                elif(x==x2-1 and y!=y2-1):
                                        return 3        
                                elif( y==y2-1 and x!=x1):
                                        return 4
        
        
        

        if q==1:
                if robot.GetInitialSignal() == "d1":
                        
                        if x == x1-1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 4  
                if robot.GetInitialSignal() == "d2":
                        
                        if x == x1-1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 4 
                if robot.GetInitialSignal() == "d3":
                        
                        if x == x1+1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d4":
                        
                        if x == x1+1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d5":
                        
                        if x == x1-2:
                                return 0
                        else:
                                return 4
                if robot.GetInitialSignal() == "d6":
                        
                        if y == y1+2:
                                return 0
                        else:
                                return 3

                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal() == "a2":
                        if x >= (x1-5):
                                return 4
                        else:
                                if(x>x1):
                                        return 4
                                elif(y<y1):
                                        return 3
                                else:
                                        return randint(1,4) 
                                                              
                if robot.GetInitialSignal() == "a3":
                        if y<= (y1+5):
                                return 3
                        else:
                                if(x>x1):
                                        return 4
                                elif(y<y1):
                                        return 3
                                else:
                                        return randint(1,4)        
                if robot.GetInitialSignal() == "a1":
                        if(x>x1-3):
                                return 4
                        elif(y<y1+3):
                                return 3
                        else:
                                return randint(1,4)
                                


        if q==2:
                if robot.GetInitialSignal() == "d1":
                        
                        if x == x1+1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 2  
                if robot.GetInitialSignal() == "d2":
                        
                        if x == x1+1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d3":
                        
                        if x == x1-1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 4 
                if robot.GetInitialSignal() == "d4":
                        
                        if x == x1-1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 4
                if robot.GetInitialSignal() == "d5":
                        
                        if x == x1+2:
                                return 0
                        else:
                                return 2
                if robot.GetInitialSignal() == "d6":
                        
                        if y == y1+2:
                                return 0
                        else:
                                return 3
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1                
                if robot.GetInitialSignal() == "a2":
                        if x <= (x1+5):
                                return 2
                        else:
                                if(x<x1):
                                        return 2
                                elif(y<y1):
                                        return 3
                                else:
                                        return randint(1,4)                      
                if robot.GetInitialSignal() == "a3":
                        if y<= (y1+5):
                                return 3
                        else:
                                if(x<x1):
                                        return 2
                                elif(y<y1):
                                        return 3
                                else:
                                        return randint(1,4)        
                if robot.GetInitialSignal() == "a1":
                        if(x<x1-3):
                                return 2
                        elif(y<y1-3):
                                return 3
                        else:
                                return randint(1,4)
                        
        if q==3:
                if robot.GetInitialSignal() == "d1":
                        
                        if x == x1+1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d2":
                        
                        if x == x1-1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 4 
                if robot.GetInitialSignal() == "d3":
                        
                        if x == x1+1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d4":
                        
                        if x == x1-1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 4
                if robot.GetInitialSignal() == "d5":
                        
                        if x == x1+1:
                                return 0
                        else:
                                return 2
                if robot.GetInitialSignal() == "d6":
                        
                        if y == y1-1:
                                return 0
                        else:
                                return 1
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal() == "a2":
                        if x <= (x1+5):
                                return 2
                        else:
                                if(x<x1):
                                        return 2
                                elif(y>y1):
                                        return 1
                                else:
                                        return randint(1,4)                        
                if robot.GetInitialSignal() == "a3":
                        if y>= (y1-5):
                                return 1
                        else:
                                if(x<x1):
                                        return 2
                                elif(y>y1):
                                        return 1
                                else:
                                        return randint(1,4)         
                if robot.GetInitialSignal() == "a1":
                        if(x<x1-3):
                                return 2
                        elif(y>y1+3):
                                return 1
                        else:
                                return randint(1,4)                

        if q==4:
                if robot.GetInitialSignal() == "d1":
                        
                        if x == x1-1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 4  
                if robot.GetInitialSignal() == "d2":
                        
                        if x == x1-1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 4 
                if robot.GetInitialSignal() == "d3":
                        
                        if x == x1+1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d4":
                        
                        if x == x1+1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 2 
                if robot.GetInitialSignal() == "d5":
                        
                        if x == x1-1:
                                return 0
                        else:
                                return 4
                if robot.GetInitialSignal() == "d6":
                        
                        if y == y1-1:
                                return 0
                        else:
                                return 3
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal() == "a2":
                        if x >= (x1-5):
                                return 4
                        else:
                                if x>x1:
                                        return 4
                                elif y>y1:
                                        return 1
                                else:
                                        return randint(1,4)                       
                if robot.GetInitialSignal() == "a3":
                        if y>= (y1-5):
                                return 1
                        else:
                                if x>x1:
                                        return 4
                                elif y>y1:
                                        return 1
                                else:
                                        return randint(1,4)        
                if robot.GetInitialSignal() == "a1":
                        if x>x1+3:
                                return 4
                        elif y>y1+3:
                                return 1
                        else:
                                return randint(1,4)
        if q==5:
                if robot.GetInitialSignal()[0:2] == "d1":
                        
                        if x == x1-2:
                                return 0
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d2":
                        
                        if x == x1+2:
                                return 0
                        else:
                                return 2        
                if robot.GetInitialSignal()[0:2] == "d3":
                        
                        if y == y1-2:
                                return 0
                        else:
                                return 1
                if robot.GetInitialSignal()[0:2] == "d4":
                        
                        if y == y1+2:
                                return 0
                        else:
                                return 3        
                if robot.GetInitialSignal()[0:2] == "d5":
                        
                        if x == x1-1:
                                
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d6":
                        
                        if x == x1-1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 4
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal()[0:1] == "a":
                        if x>x1:
                                return 4
                        else:
                                if(x>x2-x1-2):
                                        return random.choice([1,3,4])
                                else:
                                        return randint(1,4)
        if q==6:
                if robot.GetInitialSignal()[0:2] == "d1":
                        
                        if x == x1-2:
                                return 0
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d2":
                        
                        if x == x1+2:
                                return 0
                        else:
                                return 2        
                if robot.GetInitialSignal()[0:2] == "d3":
                        
                        if y == y1-2:
                                return 0
                        else:
                                return 1
                if robot.GetInitialSignal()[0:2] == "d4":
                        
                        if y == y1+2:
                                return 0
                        else:
                                return 3        
                if robot.GetInitialSignal()[0:2] == "d5":
                        
                        if x == x1-1:
                                
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d6":
                        
                        if x == x1+1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 2
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal()[0:1]== "a":
                        if y<y1:
                                return 3
                        else:
                                if(y<=y2-y1+2):
                                        return random.choice([2,3,4])
                                else:
                                        return randint(1,4)                                
        if q==7:
                if robot.GetInitialSignal()[0:2] == "d1":
                        
                        if x == x1-2:
                                return 0
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d2":
                        
                        if x == x1+2:
                                return 0
                        else:
                                return 2        
                if robot.GetInitialSignal()[0:2] == "d3":
                        
                        if y == y1-2:
                                return 0
                        else:
                                return 1
                if robot.GetInitialSignal()[0:2] == "d4":
                        
                        if y == y1+2:
                                return 0
                        else:
                                return 3        
                if robot.GetInitialSignal()[0:2] == "d5":
                        
                        if x == x1+1:
                                
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 2       
                if robot.GetInitialSignal()[0:2] == "d6":
                        
                        if x == x1+1:
                        
                                if y == y1+1:
                                        return 0
                                return 3
                        else:
                                return 2
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal()[0:1] == "a":
                        if x<x1:
                                return 2
                        else:
                                if(x<=x2-x1+2):
                                     return random.choice([1,2,3])   
                                else:        
                                        return randint(1,4)                                
        if q==8:
                if robot.GetInitialSignal()[0:2] == "d1":
                        
                        if x == x1-2:
                                return 0
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d2":
                        
                        if x == x1+2:
                                return 0
                        else:
                                return 2        
                if robot.GetInitialSignal()[0:2] == "d3":
                        
                        if y == y1-2:
                                return 0
                        else:
                                return 1
                if robot.GetInitialSignal()[0:2] == "d4":
                        
                        if y == y1+2:
                                return 0
                        else:
                                return 3        
                if robot.GetInitialSignal()[0:2] == "d5":
                       
                        if x == x1-1:
                                
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 4        
                if robot.GetInitialSignal()[0:2] == "d6":
                        
                        if x == x1+1:
                        
                                if y == y1-1:
                                        return 0
                                return 1
                        else:
                                return 2
                if len(robot.GetCurrentBaseSignal()) > 8:
                        s = robot.GetCurrentBaseSignal()[8:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                
                       
                        
                        if x < sx:
                                return 2
                                
                        if x > sx:
                                return 4
                        
                        if y < sy :
                                return 3
                        
                        if y > sy:
                                return 1
                if robot.GetInitialSignal()[0:1] == "a":
                        if y>y1:
                                return 1
                        else:
                                if(y>y2-y1-2):
                                        return random.choice([1,2,4])
                                else:
                                        return randint(1,4)                                
                                
                             
        if len(robot.GetCurrentBaseSignal()) > 8:
                s = robot.GetCurrentBaseSignal()[8:]
                sx = int(s[0:2])
                sy = int(s[2:4])
                
                       
                        
                if x < sx:
                        return 2
                        
                if x > sx:
                        return 4
                        
                if y < sy :
                        return 3
                        
                if y > sy:
                        return 1
        return randint(1,4)
        
        

def ActBase(base):
        
        x,y=base.GetPosition()
        if x < 10:
                        msg_xb = '0' + str(x)
        else: 
                msg_xb = str(x)
        if y < 10:
                msg_yb = '0' + str(y)
        else:
                msg_yb = str(y)
        msgb =   msg_xb + msg_yb
        e=base.GetElixir()
        v=base.GetVirus()

         
        while(base.GetElixir()>300):

                if base.GetElixir() > e-50:
                        base.create_robot('d1')
                elif base.GetElixir() > e-100:
                        base.create_robot('d2')
                elif base.GetElixir() > e-150:
                        base.create_robot('d3')
                elif base.GetElixir() > e-200:
                        base.create_robot('d4')
                elif base.GetElixir() > e-250:
                        base.create_robot('d5')
                elif base.GetElixir() > e-300:
                        base.create_robot('d6')
                elif base.GetElixir() > e-350:
                        base.create_robot('g1')
                elif base.GetElixir() > e-400:
                        base.create_robot('g2')
                elif base.GetElixir() > e-450:
                        base.create_robot('g3')
                elif base.GetElixir() > e-650:
                        base.create_robot('a2')
                elif base.GetElixir() > e-850:
                        base.create_robot('a3')
                elif base.GetElixir() > 300:
                        base.create_robot('a1')
        
        if base.investigate_up() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_down() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_right() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_left() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_ne() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_nw() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_se() == "enemy":
                base.DeployVirus(v/4)
        if base.investigate_sw() == "enemy":
                base.DeployVirus(v/4)        
        
        
        L = base.GetListOfSignals()
        for l in L:
                if len(base.GetYourSignal())!=12 :
                        
                        if len(l) > 0  :
                                p = msgb + l
                                base.SetYourSignal(p)
                                break      
                        else:
                                base.SetYourSignal(msgb)
        return
