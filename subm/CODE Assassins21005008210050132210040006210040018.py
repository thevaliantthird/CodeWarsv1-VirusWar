from random import randint


def ActRobot(robot):
      t=robot.GetInitialSignal()  
      if t.find('a1')!=-1 or t.find('a3')!=-1 or t.find('d3')!=-1 or t.find('a2')!=-1:
       
       up = robot.investigate_up()
       down = robot.investigate_down()
       left=robot.investigate_left()
       right=robot.investigate_right()
       nw=robot.investigate_nw()
       ne=robot.investigate_ne()
       sw=robot.investigate_sw()
       se=robot.investigate_se()    
       if up=='enemy' or down =='enemy'or left =='enemy'or right =='enemy' or nw =='enemy'or ne=='enemy' or sw =='enemy' or se=='enemy' :
        if robot.GetVirus() > 800:
                robot.DeployVirus(800)
       if up =='enemy-base' or left=='enemy-base' or down=='enemy-base' or right == 'enemy-base' or nw=='enemy-base' or ne=='enemy-base' or sw=='enemy-base' or se=='enemy-base' :
        r,j=robot.GetPosition()
        if r<10 :
            msg_r ='0'+str(r)
        elif r>=10:
            msg_r = str(r)
        if j<10 :
            msg_j ='0'+str(j)
        elif j>=10:
            msg_j = str(j)
        robot.setSignal( 'm' +msg_r + msg_j)    
        o=robot.GetYourSignal()
        b=robot.GetVirus()            
        if b>=4000:
                robot.DeployVirus(4000)
        if b>=3000:
                robot.DeployVirus(3000)
        if b>=2000 and b<=3000 :
                robot.DeployVirus(2000)
        if b>=1000 and b<2000 :
                robot.DeployVirus(1000) 
        if b<=1000:
                robot.DeployVirus(b/2)              
       return randint(1,4)    
      
      if -1==-1:
        if t.find('a1')!=-1 or t.find('a3')!=-1 or t.find('d3')!=-1 or t.find('a2')!=-1:
            x3,y3=robot.GetPosition()  
            print(type(x3))
            z=robot.GetCurrentBaseSignal() 
            ex=z[0:2]
            ey=z[2:]        
            x4=int(ex)
            y4=int(ey)
            if (abs(x4-x3)<10):
               if x3< x4:
                        return 2
               if x3> x4:
                        return 4
               if y3< y4 :
                        return 3
               if y3 > y4:
                        return 1
               return randint(1,4)
                   
            up = robot.investigate_up()
            down = robot.investigate_down()
            left=robot.investigate_left()
            right=robot.investigate_right()
            nw=robot.investigate_nw()
            ne=robot.investigate_ne()
            sw=robot.investigate_sw()
            se=robot.investigate_se()
            if up=='enemy' or down =='enemy'or left =='enemy'or right =='enemy' or nw =='enemy'or ne=='enemy' or sw =='enemy' or se=='enemy' :
              if robot.GetVirus() > 800:
                robot.DeployVirus(800)
            if up =='enemy-base' or left=='enemy-base' or down=='enemy-base' or right == 'enemy-base' or nw=='enemy-base' or ne=='enemy-base' or sw=='enemy-base' or se=='enemy-base' :
               b=robot.GetVirus()  
               if b>=4000:
                robot.DeployVirus(4000)
               if b>=3000:
                robot.DeployVirus(3000)
               if b>=2000 and b<=3000 :
                robot.DeployVirus(2000)
               if b>=1000 and b<2000 :
                robot.DeployVirus(1000)   
               if b<=1000:
                robot.DeployVirus(b/2)              
            return randint(1,4)

      if t.find('d')!=-1:
       base_h= t[1:3]
       base_k= t[3:]
     
       x,y=robot.GetPosition() 
       if x==int(base_h) and y==int(base_k)  :
           return randint(1,4)
       if (x <=int(base_h)+4 and x>=int(base_h)-4) and (y>=int(base_k)-4 and y<=int(base_k)+4) :
         if x<int(base_h)+4 and x>int(base_h)-4 and y<int(base_k)+4 and y>int(base_k)-4:
            return randint(1,4)
         if x==int(base_h)+4:
          return 4
         if x==int(base_h)-4:
          return 2
         if y ==int(base_k)-4: 
          return 3
         if y== int(base_k)+4:
           return 1    
     
       up = robot.investigate_up()
       down = robot.investigate_down()
       left=robot.investigate_left()
       right=robot.investigate_right()
       nw=robot.investigate_nw()
       ne=robot.investigate_ne()
       sw=robot.investigate_sw()
       se=robot.investigate_se()    
       if up=='enemy' or down =='enemy'or left =='enemy'or right =='enemy' or nw =='enemy'or ne=='enemy' or sw =='enemy' or se=='enemy' :
        if robot.GetVirus() > 800:
                robot.DeployVirus(800)
        elif robot.GetVirus()>600:
                robot.DeployVirus(600)        
        elif robot.GetVirus()>400:
                robot.DeployVirus(400)
        elif robot.GetVirus()>200:
                robot.DeployVirus(200)     
       
      if t.find('d1')!=-1:
       base_h= t[2:4]
       base_k= t[4:]
      
       x,y=robot.GetPosition() 
       if x==int(base_h) and y==int(base_k)  :
          return randint(1,4)
       if (x <=int(base_h)+4 and x>=int(base_h)-4) and (y>=int(base_k)-4 and y<=int(base_k)+4) :
         if x<int(base_h)+4 and x>int(base_h)-4 and y<int(base_k)+4 and y>int(base_k)-4:
            return randint(1,4)
         if x==int(base_h)+4:
          return 4
         if x==int(base_h)-4:
          return 2
         if y ==int(base_k)-4: 
          return 3
         if y== int(base_k)+4:
           return 1
          
       up = robot.investigate_up()
       down = robot.investigate_down()
       left=robot.investigate_left()
       right=robot.investigate_right()
       nw=robot.investigate_nw()
       ne=robot.investigate_ne()
       sw=robot.investigate_sw()
       se=robot.investigate_se()    
       if up=='enemy' or down =='enemy'or left =='enemy'or right =='enemy' or nw =='enemy'or ne=='enemy' or sw =='enemy' or se=='enemy' :
        if robot.GetVirus() > 800:
                robot.DeployVirus(800)
        elif robot.GetVirus()>600:
                robot.DeployVirus(600)        
        elif robot.GetVirus()>400:
                robot.DeployVirus(400)
        elif robot.GetVirus()>200:
                robot.DeployVirus(200) 

def ActBase(base):
    '''
    ActRobot(0):
    '''
    h,k=base.GetPosition()
    L=base.GetListOfSignals()
    for l in L:
         if 'm' in l:
          ebase_x =l[1:3]
          ebase_y=l[3:]
         
          base.SetYourSignal(ebase_x + ebase_y)
          
      
    if base.GetElixir() > 400:
     p=randint(0,1)
     if p==0:
      f=randint(0,2)
      if f==0:
       base.create_robot('a1'+ str(h) +str(k))
      if f==1:
       base.create_robot('a2'+ str(h) +str(k))
      if f==2:
       base.create_robot('a3'+ str(h) +str(k))
     if p==1:
        w=randint(0,2)
        if w==1:
         base.create_robot('d'+str(h)+str(k))
        if w==0:
         base.create_robot('d1'+str(h)+str(k))  
        if w==2:
         base.create_robot('d3'+str(h)+str(k))        
    up1=base.investigate_up()
    down1=base.investigate_down()
    left1=base.investigate_left()
    right1=base.investigate_right()
    nw1=base.investigate_nw()
    ne1=base.investigate_ne()
    sw1=base.investigate_sw()
    se1=base.investigate_se()
    if up1=='enemy'or down1=='enemy' or right1=='enemy' or left1=='enemy' or nw1=='enemy' or ne1=='enemy ' or sw1 =='enemy' or se1=='enemy':
       v= base.GetVirus()       
       if v>=800 :         
         base.DeployVirus(800)
       if v<800 :
          base.DeployVirus(v/2)  #strv or v?           
    return