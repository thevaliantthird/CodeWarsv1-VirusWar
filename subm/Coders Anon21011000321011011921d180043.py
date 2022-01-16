from random import randint
import random

def ActRobot(robot):
        
        return_list = [1,2,3,4]
        X = robot.GetDimensionX() 
        Y = robot.GetDimensionY()
        
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        nw = robot.investigate_nw()
        sw = robot.investigate_sw()
        ne = robot.investigate_ne()
        se = robot.investigate_se()
        M=[up,down,left,right,nw,se,sw,ne]
        global x,y
        x,y = robot.GetPosition()
        
       
        if robot.GetInitialSignal()=='Def1':
            if ((up!='friend')and(down!='friend-base')):
                   return 1               
            else:
                for r in M:
                        if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                robot.setSignal('Breach1')
                                
                return 0                
        if robot.GetInitialSignal()=='Def2':
              if ((right!='friend')and(left!='friend-base')):
                        return 2
              else: 
                      for r in M:
                        if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                robot.setSignal('Breach1')
                             
                      return 0 
        if robot.GetInitialSignal()=='Def3':
              if ((down!='friend')and(up!='friend-base')):
                      return 3
              else: 
                      for r in M:
                        if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                robot.setSignal('Breach1')
                                
                      return 0
        if robot.GetInitialSignal()=='Def4':
              if ((left!='friend')and(right!='friend-base')):
                        return 4
              else: 
                      for r in M:
                        if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                robot.setSignal('Breach1')
                                
                      return 0
                      
        if robot.GetInitialSignal()=='Def6':
                a,b=robot.GetPosition()
                robot.setSignal('Def6')
                if a==h and (b==k or b==k-1 or b==k-2):
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 1
                        else: 
                                return 1  
                elif h-3<=a and a<h+3 and b==k-3:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 2
                         else:
                                 return 2
                elif a==h+3 and k-3<=b and b<k+3:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 3
                         else:
                                 return 3        
                elif h-3<a and a<=h+3 and b==k+3:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 4
                         else: 
                                return 4
                elif a==h-3 and b<=k+3 and b>=k-3:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 1
                         else:
                                 return 1             
        
        
        if robot.GetInitialSignal()=='Def5':
                m,n=robot.GetPosition()
                robot.setSignal('Def5')
                if m==h and (n==k or n==k-1):
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 1
                         else:
                                 return 1
                elif h-2<=m and m<h+2 and n==k-2:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 2
                         else:
                                return 2
                elif m==h+2 and k-2<=n and n<k+2:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 3
                         else:
                                return 3        
                elif h-2<m and m<=h+2 and n==k+2:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 4
                         else :
                                return 4
                elif m==h-2 and n<=k+2 and n>=k-2:
                        for r in M:
                         if r=='enemy':
                                robot.DeployVirus(robot.GetVirus()*0.6)
                                return 1
                         else:
                                        return 1 
        
        if up == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(200)
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
                robot.DeployVirus(200)
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
                robot.DeployVirus(200)
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
                robot.DeployVirus(200)
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
      

        if nw == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(200)
        elif nw == "enemy-base":
                
                if x < 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y+1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
      

        if sw == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(200)
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
      
        if se == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(200)
        elif se == "enemy-base":
                if x < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y-1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)   
       
                        
        if ne == "enemy" and robot.GetVirus() > 1000:
                robot.DeployVirus(200)
        elif ne == "enemy-base":
                
                if x < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y+1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg = "base" + msg_x + msg_y
                robot.setSignal(msg)
                if robot.GetVirus() > 500:
                        robot.DeployVirus(500)
        
        if robot.GetYourSignal()=='Limit':
                dist = abs(int(X/2)-x) + abs(int(Y/2)-y)
                
                if dist==1:
                        robot.setSignal('')
                        return 0
                if x < int(X/2):
                        return 2
                if x > int(X/2):
                        return 4
                if y < int(Y/2) :
                        return 3
                if y > int(Y/2):
                        return 1
        
        if robot.GetInitialSignal()=='Attacker' and robot.GetYourSignal()!='Limit':
                if robot.GetCurrentBaseSignal().startswith('base'):
                        
                        s = robot.GetCurrentBaseSignal()[4:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist==1:
                                robot.DeployVirus(robot.GetVirus()*0.5)
                                return 0
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy :
                                return 3
                        if y > sy:
                                return 1
                elif x>X-3 or x<3 or y<3 or y>Y-3:
                        robot.setSignal('Limit')
                                        
                elif h>(2*X/3):
                        if k<Y/3:
                                J = [1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4]
                                return random.choice(J)
                        elif k>=Y/3 and k<(2*Y/3):
                                J = [1,1,1,1,2,2,3,3,3,3,4,4,4,4,4]
                                return random.choice(J)
                        else:
                                J = [1,1,1,1,1,2,2,3,3,4,4,4,4,4]
                                return random.choice(J)
                elif h>(X/3) and h<(2*X/3):
                        if k<Y/3:
                                J = [1,1,2,2,2,3,3,3,3,3,4,4,4]
                                return random.choice(J)
                        elif k>=Y/3 and k<(2*Y/3):
                                J = [1,2,3,4]
                                return random.choice(J)
                        else:
                                J = [1,1,1,1,1,2,2,2,3,3,4,4,4]
                                return random.choice(J)
                else:
                        if k<Y/3:
                                J = [1,1,2,2,2,2,2,3,3,3,3,3,4,4]
                                return random.choice(J)
                        elif k>=Y/3 and k<(2*Y/3):
                                J = [1,1,1,2,2,2,2,2,3,3,3,4,4]
                                return random.choice(J)
                        else:
                                J = [1,1,1,1,1,2,2,2,2,2,3,3,4,4]
                                return random.choice(J)
        elif robot.GetInitialSignal()=='Defender':
                if x>(2*X/3):
                        if y<Y/3:
                                J = [1,1,1,2,2,2,3,3,3,3,3,4,4,4,4,4]
                                return random.choice(J)
                        elif y>=Y/3 and y<(2*Y/3):
                                J = [1,1,1,1,2,2,3,3,3,3,4,4,4,4,4]
                                return random.choice(J)
                        else:
                                J = [1,1,1,1,1,2,2,3,3,4,4,4,4,4]
                                return random.choice(J)
                if x>(X/3) and x<(2*X/3):
                        if y<Y/3:
                                J = [1,1,2,2,2,3,3,3,3,3,4,4,4]
                                return random.choice(J)
                        elif y>=Y/3 and y<(2*Y/3):
                                J = [1,2,3,4]
                                return random.choice(J)
                        else:
                                J = [1,1,1,1,1,2,2,2,3,3,4,4,4]
                                return random.choice(J)
                if x<(X/3):
                        if y<Y/3:
                                J = [1,1,2,2,2,2,2,3,3,3,3,3,4,4]
                                return random.choice(J)
                        elif y>=Y/3 and y<(2*Y/3):
                                J = [1,1,1,2,2,2,2,2,3,3,3,4,4]
                                return random.choice(J)
                        else:
                                J = [1,1,1,1,1,2,2,2,2,2,3,3,4,4]
                                return random.choice(J)
        else:
                robot.setSignal('')
                return randint(1,4)



def ActBase(base):
        global h,k
        h,k=base.GetPosition()
        c=0
        z=0
        q=len(base.GetListOfSignals())           
        if(base.investigate_up()!='friend'):
                base.create_robot('Def1')
        if(base.investigate_left()!='friend'):
                base.create_robot('Def4')
        if(base.investigate_right()!='friend'):
                base.create_robot('Def2')
        if(base.investigate_down()!='friend'):
                base.create_robot('Def3') 

        if len(base.GetListOfSignals()) < 5:
                base.create_robot('Def5')
               
        if len(base.GetListOfSignals()) < 6:
                base.create_robot('Def6')
                
        
        if (base.GetElixir() >= 500)and (q>=4) and (q<=11):
                base.create_robot('Defender')

        if(base.GetElixir() >= 500) and (q>11) and (q<=16):
                base.create_robot('')

        if (base.GetElixir() >= 500) and q>16 :
                base.create_robot('Attacker')
        
        
        L = base.GetListOfSignals()
        for i in L:
                if (i=='Def5') :
                        z=1 
        if z==0:
                base.create_robot('Def5')    
        
        
        for t in L:
                if (t=='Def6') :
                        c=1
        if c==0:
                base.create_robot('Def6')    

        for l in L:
                if (len(l) > 6) and (l!='Breach1'):
                        base.SetYourSignal(l)
                        return