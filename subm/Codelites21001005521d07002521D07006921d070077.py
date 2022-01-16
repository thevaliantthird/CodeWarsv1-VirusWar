from random import randint


def ActRobot(robot):
    si=robot.GetInitialSignal()
    s=robot.GetYourSignal()
    a=robot.investigate_up()
    b=robot.investigate_down()
    c=robot.investigate_left()
    d=robot.investigate_right()
    e=robot.investigate_nw() 
    f=robot.investigate_ne()
    g=robot.investigate_se()
    h=robot.investigate_sw()
    virus=robot.GetVirus()
    elixir=robot.GetElixir()
    if virus>16000:
        eb=16000
    elif virus>12000:
        eb=8000
    elif virus>8000:
        eb=4000
    elif virus>4000:
        eb=2000
    else:
        eb=0
    if virus*0.3<2000 and virus>2000 :
        pe=2000
    else:
        pe=virus*0.3
    if virus*0.2<1000 and virus>1000:
        be=1000
    else:
        be=virus*0.3
    fe=virus*0.1
    me=virus*0.2
    ae=virus*0.1

    def bg():
            if x==X+2 and y==Y:
                return 3
            if x==X+2 and y==Y+1:
                return 3
            if x==X+2 and y==Y-1:
                return 3
            if x==X+2 and y==Y+2:
                return 4
            if x==X+2 and y==Y-2:
                return 3
            if x==X-2 and y==Y:
                return 1
            if x==X-2 and y==Y+1:
                return 1
            if x==X-2 and y==Y+2:
                return 1
            if x==X-2 and y==Y-1:
                return 1
            if x==X-2 and y==Y-2:
                return 2
            if x==X and y==Y+2:
                return 4
            if x==X+1 and y==Y+2:
                return 4
            if x==X-1 and y==Y+2:
                return 4
            if x==X and y==Y-2:
                return 2
            if x==X+1 and y==Y-2:
                return 2
            if x==X-1 and y==Y-2:
                return  2 
    def sg():
            if x==X+1 and y==Y:
                return 3
            if x==X+1 and y==Y+1:
                return 4
            if x==X+1 and y==Y-1:
                return 3
            if x==X-1 and y==Y+1:
                return 1
            if x==X-1 and y==Y-1:
                return 2
            if x==X-1 and y==Y:
                return 1
            if x==X and y==Y+1:
                return 4
            if x==X and y==Y-1:
                return 2
    def b1():
          if a == "enemy-base":
              robot.DeployVirus(eb)
              
          elif b=="enemy-base":
              
              robot.DeployVirus(eb)
          elif c=="enemy-base":
              
              robot.DeployVirus(eb)
          elif d=="enemy-base":
              robot.DeployVirus(eb)
          elif e=="enemy-base":
              
              robot.DeployVirus(eb)
          elif f=="enemy-base":
              
              robot.DeployVirus(eb)
          elif g=="enemy-base":
              
              robot.DeployVirus(eb)
          elif h=="enemy-base":
              
              robot.DeployVirus(eb)
              
          elif a == "enemy":
              robot.DeployVirus(be)
              
          elif b=="enemy":
              
              robot.DeployVirus(be)
          elif c=="enemy":
              
              robot.DeployVirus(be)
          elif d=="enemy":
              robot.DeployVirus(be)
          elif e=="enemy":
              
              robot.DeployVirus(be)
          elif f=="enemy":
              
              robot.DeployVirus(be)
          elif g=="enemy":
              
              robot.DeployVirus(be)
          elif h=="enemy":
              
              robot.DeployVirus(be)
    def f1():
          if a == "enemy-base":
              robot.DeployVirus(eb)
              
          elif b=="enemy-base":
              
              robot.DeployVirus(eb)
          elif c=="enemy-base":
              
              robot.DeployVirus(eb)
          elif d=="enemy-base":
              robot.DeployVirus(eb)
          elif e=="enemy-base":
              
              robot.DeployVirus(eb)
          elif f=="enemy-base":
              
              robot.DeployVirus(eb)
          elif g=="enemy-base":
              
              robot.DeployVirus(eb)
          elif h=="enemy-base":
              
              robot.DeployVirus(eb)
              
          elif a == "enemy":
              robot.DeployVirus(fe)
              
          elif b=="enemy":
              
              robot.DeployVirus(fe)
          elif c=="enemy":
              
              robot.DeployVirus(fe)
          elif d=="enemy":
              robot.DeployVirus(fe)
          elif e=="enemy":
              
              robot.DeployVirus(fe)
          elif f=="enemy":
              
              robot.DeployVirus(fe)
          elif g=="enemy":
              
              robot.DeployVirus(fe)
          elif h=="enemy":
              
              robot.DeployVirus(fe)
    def m1():
          if a == "enemy-base":
              robot.DeployVirus(eb)
              
          elif b=="enemy-base":
              
              robot.DeployVirus(eb)
          elif c=="enemy-base":
              
              robot.DeployVirus(eb)
          elif d=="enemy-base":
              robot.DeployVirus(eb)
          elif e=="enemy-base":
              
              robot.DeployVirus(eb)
          elif f=="enemy-base":
              
              robot.DeployVirus(eb)
          elif g=="enemy-base":
              
              robot.DeployVirus(eb)
          elif h=="enemy-base":
              
              robot.DeployVirus(eb)
              
          elif a == "enemy":
              robot.DeployVirus(me)
              
          elif b=="enemy":
              
              robot.DeployVirus(me)
          elif c=="enemy":
              
              robot.DeployVirus(me)
          elif d=="enemy":
              robot.DeployVirus(me)
          elif e=="enemy":
              
              robot.DeployVirus(me)
          elif f=="enemy":
              
              robot.DeployVirus(me)
          elif g=="enemy":
              
              robot.DeployVirus(me)
          elif h=="enemy":
              
              robot.DeployVirus(me)
    def p1():
          if a == "enemy-base":
              robot.DeployVirus(eb)
              
          elif b=="enemy-base":
              
              robot.DeployVirus(eb)
          elif c=="enemy-base":
              
              robot.DeployVirus(eb)
          elif d=="enemy-base":
              robot.DeployVirus(eb)
          elif e=="enemy-base":
              
              robot.DeployVirus(eb)
          elif f=="enemy-base":
              
              robot.DeployVirus(eb)
          elif g=="enemy-base":
              
              robot.DeployVirus(eb)
          elif h=="enemy-base":
              
              robot.DeployVirus(eb)
              
          elif a == "enemy":
              robot.DeployVirus(pe)
              
          elif b=="enemy":
              
              robot.DeployVirus(pe)
          elif c=="enemy":
              
              robot.DeployVirus(pe)
          elif d=="enemy":
              robot.DeployVirus(pe)
          elif e=="enemy":
              
              robot.DeployVirus(pe)
          elif f=="enemy":
              
              robot.DeployVirus(pe)
          elif g=="enemy":
              
              robot.DeployVirus(pe)
          elif h=="enemy":
              
              robot.DeployVirus(pe)
    def a1():
          if a == "enemy-base":
              robot.DeployVirus(eb)
              
          elif b=="enemy-base":
              
              robot.DeployVirus(eb)
          elif c=="enemy-base":
              
              robot.DeployVirus(eb)
          elif d=="enemy-base":
              robot.DeployVirus(eb)
          elif e=="enemy-base":
              
              robot.DeployVirus(eb)
          elif f=="enemy-base":
              
              robot.DeployVirus(eb)
          elif g=="enemy-base":
              
              robot.DeployVirus(eb)
          elif h=="enemy-base":
              
              robot.DeployVirus(eb)
              
          elif a == "enemy":
              robot.DeployVirus(ae)
              
          elif b=="enemy":
              
              robot.DeployVirus(ae)
          elif c=="enemy":
              
              robot.DeployVirus(ae)
          elif d=="enemy":
              robot.DeployVirus(ae)
          elif e=="enemy":
              
              robot.DeployVirus(ae)
          elif f=="enemy":
              
              robot.DeployVirus(ae)
          elif g=="enemy":
              
              robot.DeployVirus(ae)
          elif h=="enemy":
              
              robot.DeployVirus(ae)


            
    if X>(bx/2):            
        if si=="bl1":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global bl1i
                bl1i=1
                robot.setSignal('a')
            if bl1i==1:
                while y<(by-1):
                    return 3
                if y==(by-1):
                    bl1i+=1
            if bl1i==2:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl1i+=1
                    return 1
            if bl1i==3:
                while x>X+1:
                    return 4
                if x==X+1:
                    bl1i+=1
                    return 1
            if bl1i==4:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl1i+=1
                    return 1
            if bl1i==5:
                while x>X+1:
                    return 4
                if x==X+1:
                    bl1i+=1
                    return 1
            if bl1i==6:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl1i+=1
                    return 1
            if bl1i==7:
                while x>X:
                    return 4
                if x==X:
                    bl1i+=1
                    return 1
            if bl1i==8:
                while y>Y:
                    return 1
                if y==Y:
                    bl1i+=1
            while 8<bl1i<11:
                bl1i+=1
                return 1 
            if bl1i==11:
                robot.setSignal('protect2')
                return bg()           
        elif si=="br1":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global br1i
                br1i=1
                robot.setSignal('a')
            if br1i==1:
                while y>0:
                    return 1
                if y==0:
                    br1i+=1
            if br1i==2:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br1i+=1
                    return 3
            if br1i==3:
                while x>X+1:
                    return 4
                if x==X+1:
                    br1i+=1
                    return 3
            if br1i==4:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br1i+=1
                    return 3
            if br1i==5:
                while x>X+1:
                    return 4
                if x==X+1:
                    br1i+=1
                    return 3
            if br1i==6:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br1i+=1
                    return 3
            if br1i==7:
                while x>X:
                    return 4
                if x==X:
                    br1i+=1
                    return 3   
            if br1i==8:
                while y<Y:
                    return 3
                if y==Y:
                    br1i+=1
            while 8<br1i<11:
                br1i+=1
                return 2 
            if br1i == 11:
                robot.setSignal('protect2')
                return bg()            
        elif si=="bl2":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global bl2i
                bl2i=1
                robot.setSignal('a')
                return 2
            if bl2i==1:
                while y<33:
                    return 3
                if y==33:
                    bl2i+=1
            if bl2i==2:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl2i+=1
                    return 1
            if bl2i==3:
                while x>X+2:
                    return 4
                if x==X+2:
                    bl2i+=1
                    return 1
            if bl2i==4:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl2i+=1
                    return 1
            if bl2i==5:
                while x>X+2:
                    return 4
                if x==X+2:
                    bl2i+=1
                    return 1
            if bl2i==6:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl2i+=1
                    return 1
            if bl2i==7:
                while x>X+2:
                    return 4
                if x==X+2:
                    bl2i+=1
                    return 1
            if bl2i==8:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl2i+=1
                    return 1
            if bl2i==9:
                while x>X:
                    return 4
                if x==X:
                    bl2i+=1
                    return 1    
            if bl2i==10:
                while y>Y:
                    return 1
                if y==Y:
                    bl2i+=1
            while 10<bl2i<13:
                bl2i+=1
                return 3
            if bl2i ==13:
                robot.setSignal('protect2')
                return bg()                                               
        elif si=="br2":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global br2i
                br2i=1
                robot.setSignal('a')
                return 2
            if br2i==1:
                while y>6:
                    return 1
                if y==6:
                    br2i+=1
            if br2i==2:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br2i+=1
                    return 3
            if br2i==3:
                while x>X+2:
                    return 4
                if x==X+2:
                    br2i+=1
                    return 3
            if br2i==4:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br2i+=1
                    return 3
            if br2i==5:
                while x>X+2:
                    return 4
                if x==X+2:
                    br2i+=1
                    return 3
            if br2i==6:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br2i+=1
                    return 3
            if br2i==7:
                while x>X+2:
                    return 4
                if x==X+2:
                    br2i+=1
                    return 3
            if br2i==8:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br2i+=1
                    return 3
            if br2i==9:
                while x>X:
                    return 4
                if x==X:
                    br2i+=1
                    return 3    
            if br2i==10:
                while y<Y:
                    return 3
                if y==Y:
                    br2i+=1
            while 10<br2i<13:
                br2i+=1
                return 4
            if br2i ==13:
                robot.setSignal('protect2')
                return bg()            
        elif si=="bl3":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global bl3i
                bl3i=1
                robot.setSignal('a')
                return 2
            if bl3i==1:
                while y<25:
                    return 3
                if y==25:
                    bl3i+=1
            if bl3i==2:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl3i+=1
                    return 1
            if bl3i==3:
                while x>X+3:
                    return 4
                if x==X+3:
                    bl3i+=1
                    return 1
            if bl3i==4:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl3i+=1
                    return 1
            if bl3i==5:
                while x>X+3:
                    return 4
                if x==X+3:
                    bl3i+=1
                    return 1
            if bl3i==6:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    bl3i+=1
                    return 1
            if bl3i==7:
                while x>X:
                    return 4
                if x==X:
                    bl3i+=1
                    return 1
            if bl3i==8:
                while y<Y:
                    return 3
                while y>Y:
                    return 1
                if y==Y:
                    bl3i+=1  
                    return 1 
            if bl3i==9:
                robot.setSignal('protect1')
                return sg()           
        elif si=="br3":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global br3i
                br3i=1
                robot.setSignal('a')
                return 2
            if br3i==1:
                while y>14:
                    return 1
                if y==14:
                    br3i+=1
            if br3i==2:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br3i+=1
                    return 3
            if br3i==3:
                while x>X+3:
                    return 4
                if x==X+3:
                    br3i+=1
                    return 3
            if br3i==4:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br3i+=1
                    return 3
            if br3i==5:
                while x>X+3:
                    return 4
                if x==X+3:
                    br3i+=1
                    return 3
            if br3i==6:
                while x<(bx-1):
                    return 2
                if x==(bx-1):
                    br3i+=1
                    return 3
            if br3i==7:
                while x>X:
                    return 4
                if x==X:
                    br3i+=1 
                    return 3
                    
                    
            if br3i==8:
                while y<Y:
                    return 3
                while y>Y:
                    return 1   
                if y==Y:
                    br3i+=1  
                    return 3
            if br3i==9:
                robot.setSignal('protect1')
                return sg()          
        elif si=="p1":
            p1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                robot.setSignal('protect1')
                return 4
            return sg()    
        elif si=="p2":
            p1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                robot.setSignal('protect1')
                return 2
            return sg()    
        elif si=="fl1":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fl1i
                fl1i=1
                robot.setSignal('a')
            while fl1i<2:
                fl1i+=1
                return 4    
            if fl1i==2:
                while y<(by-1):
                    return 3
                if y==(by-1):
                    fl1i+=1 
            if fl1i==3:           
                while x > 0:
                    return 4
                if x==0:
                    fl1i+=1
            if fl1i==4:
                while y>Y:
                    return 1
                if y==Y:
                    fl1i+=1
            if fl1i== 5:
                return randint(1,4)                   
        elif si=="fl2":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fl2i
                fl2i=1
                robot.setSignal('a')
            while fl2i<3:
                fl2i+=1
                return 4
            if fl2i==3:
                while y< 38:
                    return 3
                if y==38:
                    fl2i+=1 
            if fl2i==4:           
                while x > 1:
                    return 4
                if x==1:
                    fl2i+=1
            if fl2i==5:
                while y>Y:
                    return 1
                if y==Y:
                    fl2i+=1
            if fl2i== 6:
                return randint(1,4)
        elif si=="fl3":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fl3i
                fl3i=1
                robot.setSignal('a')
            while fl3i<4:
                fl3i+=1
                return 4 
                robot.setSignal('a')   
            if fl3i==4:
                while y< 37:
                    return 3
                if y==37:
                    fl3i+=1 
            if fl3i==5:           
                while x > 2:
                    return 4
                if x==2:
                    fl3i+=1
            if fl3i==6:
                while y>Y:
                    return 1
                if y==Y:
                    fl3i+=1
            if fl3i== 7:
                return randint(1,4)    
        elif si=="fl4":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fl4i
                fl4i=1
                robot.setSignal('a')
            while fl4i<5:
                fl4i+=1
                return 4    
            if fl4i==5:
                while y< 36:
                    return 3
                if y==36:
                    fl4i+=1 
            if fl4i==6:           
                while x > 3:
                    return 4
                if x==3:
                    fl4i+=1
            if fl4i==7:
                while y>Y:
                    return 1
                if y==Y:
                    fl4i+=1
            if fl4i== 8:
                return randint(1,4)    
        elif si=="fl5":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fl5i
                fl5i=1
            while fl5i<6:
                fl5i+=1
                return 4    
            if fl5i==6:
                while y< 35:
                    return 3
                if y==35:
                    fl5i+=1 
            if fl5i==7:           
                while x > 4:
                    return 4
                if x==4:
                    fl5i+=1
            if fl5i==8:
                while y>Y:
                    return 1 
                if y==Y:
                    fl5i+=1
            if fl5i== 9:
                return randint(1,4)       
        elif si=="fr1":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fr1i
                fr1i=1
                robot.setSignal('a')
            while fr1i<2:
                fr1i+=1
                return 4    
            if fr1i==2:
                while y>0:
                    return 1
                if y==0:
                    fr1i+=1 
            if fr1i==3:           
                while x > 0:
                    return 4
                if x==0:
                    fr1i+=1
            if fr1i==4:
                while y<Y:
                    return 3
                if y==Y:
                    fr1i+=1
            if fr1i== 5:
                return randint(1,4)                       
        elif si=="fr2":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fr2i
                fr2i=1
                robot.setSignal('a')
            while fr2i<3:
                fr2i+=1
                return 4    
            if fr2i==3:
                while y>1:
                    return 1
                if y==1:
                    fr2i+=1 
            if fr2i==4:           
                while x > 1:
                    return 4
                if x==1:
                    fr2i+=1
            if fr2i==5:
                while y<Y:
                    return 3 
            if y==Y:
                    fr2i+=1
            if fr2i== 6:
                return randint(1,4)                   
        elif si=="fr3":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fr3i
                fr3i=1
                robot.setSignal('a')
            while fr3i<4:
                fr3i+=1
                return 4    
            if fr3i==4:
                while y> 2:
                    return 1
                if y==2:
                    fr3i+=1 
            if fr3i==5:           
                while x > 2:
                    return 4
                if x==2:
                    fr3i+=1
            if fr3i==6:
                while y<Y:
                    return 3
                if y==Y:
                    fr3i+=1
            if fr3i== 7:
                return randint(1,4)    
        elif si=="fr4":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fr4i
                fr4i=1
                robot.setSignal('a')
            while fr4i<5:
                fr4i+=1
                return 4    
            if fr4i==5:
                while y> 3:
                    return 1
                if y==3:
                    fr4i+=1 
            if fr4i==6:           
                while x > 3:
                    return 4
                if x==3:
                    fr4i+=1
            if fr4i==7:
                while y<Y:
                    return 3
                if y==Y:
                    fr4i+=1
            if fr4i== 8:
                return randint(1,4)    
        elif si=="fr5":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global fr5i
                fr5i=1
                robot.setSignal('a')
            while fr5i<6:
                fr5i+=1
                return 4    
            if fr5i==6:
                while y> 4:
                    return 1
                if y==4:
                    fr5i+=1 
            if fr5i==7:           
                while x > 4:
                    return 4
                if x==4:
                    fr5i+=1
            if fr5i==8:
                while y<Y:
                    return 3
                if y==Y:
                    fr5i+=1
            if fr5i== 9:
                return randint(1,4)
        elif si=="ml1":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global ml1i
                ml1i=1
                robot.setSignal('a')
            while ml1i<7:
                ml1i+=1
                return 4
            if ml1i == 7:
                while y<(by-1)-5:
                    return 3
                if y==(by-1)-5:
                    ml1i+=1
                    return 4
            if ml1i == 8:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml1i+=1
                    return 1
            if ml1i == 9:
                while x<X-7:
                    return 2
                if x==X-7:
                    ml1i+=1
                    return 1
            if ml1i == 10:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml1i+=1
            if ml1i==11:
                return randint(1,4)

        elif si=="ml2":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global ml2i
                ml2i=1
                robot.setSignal('a')
            while ml2i<8:
                ml2i+=1
                return 4
            if ml2i == 8:
                while y<(by-1)-8:
                    return 3
                if y==(by-1)-8:
                    ml2i+=1
                    return 4
            if ml2i == 9:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml2i+=1
                    return 1
            if ml2i == 10:
                while x<X-7:
                    return 2
                if x==X-7:
                    ml2i+=1
                    return 1
            if ml2i == 11:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml2i+=1
            if ml2i==12:
                return randint(1,4)    
        elif si=="ml3":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global ml3i
                ml3i=1
                robot.setSignal('a')
            while ml3i<9:
                ml3i+=1
                return 4
            if ml3i == 9:
                while y<(by-1)-11:
                    return 3
                if y==(by-1)-11:
                    ml3i+=1
                    return 4
            if ml3i == 10:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml3i+=1
                    return 1
            if ml3i == 11:
                while x<X-7:
                    return 2
                if x==X-7:
                    ml3i+=1
                    return 1
            if ml3i == 12:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml3i+=1
            if ml3i==13:
                return randint(1,4)        

        elif si=="ml4":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global ml4i
                ml4i=1
                robot.setSignal('a')
            while ml4i<10:
                ml4i+=1
                return 4
            if ml4i ==10:
                while y<(by-1)-14:
                    return 3
                if y==(by-1)-14:
                    ml4i+=1
                    return 4
            if ml4i == 11:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml4i+=1
                    return 1
            if ml4i == 12:
                while x<X-7:
                    return 2
                if x==X-7:
                    ml4i+=1
                    return 1
            if ml4i == 13:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml4i+=1
            if ml4i==14:
                return randint(1,4)        
        elif si=="ml5":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global ml5i
                ml5i=1
                robot.setSignal('a')
            while ml5i<11:
                ml5i+=1
                return 4
            if ml5i == 11:
                while y<(by-1)-17:
                    return 3
                if y==(by-1)-17:
                    ml5i+=1
                    return 4
            if ml5i == 12:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml5i+=1
                    return 1
            if ml5i == 13:
                while x<X-7:
                    return 2
                if x==X-7:
                    ml5i+=1
                    return 1
            if ml5i == 14:
                while x>X-12:
                    return 4
                if x==X-12:
                    ml5i+=1        
            if ml5i==15:
                return randint(1,4)     
        elif si=="mr1":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global mr1i
                mr1i=1
                robot.setSignal('a')
            while mr1i<7:
                mr1i+=1
                return 4
            if mr1i == 7:
                while y>5:
                    return 1
                if y==5:
                    mr1i+=1
                    return 4
            if mr1i == 8:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr1i+=1
                    return 3
            if mr1i == 9:
                while x<X-7:
                    return 2
                if x==X-7:
                    mr1i+=1
                    return 3
            if mr1i == 10:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr1i+=1
            if mr1i==11:
                return randint(1,4)        

        elif si=="mr2":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global mr2i
                mr2i=1
                robot.setSignal('a')
            while mr2i<8:
                mr2i+=1
                return 4
            if mr2i == 8:
                while y>8:
                    return 1
                if y==8:
                    mr2i+=1
                    return 4
            if mr2i == 9:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr2i+=1
                    return 3
            if mr2i == 10:
                while x<X-7:
                    return 2
                if x==X-7:
                    mr2i+=1
                    return 3
            if mr2i == 11:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr2i+=1

            if mr2i==12:
                return randint(1,4)
                    
        elif si=="mr3":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global mr3i
                mr3i=1
                robot.setSignal('a')
            while mr3i<9:
                mr3i+=1
                return 4
            if mr3i == 9:
                while y>11:
                    return 1
                if y==11:
                    mr3i+=1
                    return 4
            if mr3i == 10:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr3i+=1
                    return 3
            if mr3i == 11:
                while x<X-7:
                    return 2
                if x==X-7:
                    mr3i+=1
                    return 3
            if mr3i == 12:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr3i+=1
            if mr3i==13:
                return randint(1,4)         

        elif si=="mr4":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global mr4i
                mr4i=1
                robot.setSignal('a')
            while mr4i<10:
                mr4i+=1
                return 4
            if mr4i ==10:
                while y>14:
                    return 1
                if y==14:
                    mr4i+=1
                    return 4
            if mr4i == 11:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr4i+=1
                    return 3
            if mr4i == 12:
                while x<X-7:
                    return 2
                if x==X-7:
                    mr4i+=1
                    return 3
            if mr4i == 13:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr4i+=1
            if mr4i==14:
                return randint(1,4)        
        elif si=="mr5":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                global mr5i
                mr5i=1
                robot.setSignal('a')
            while mr5i<11:
                mr5i+=1
                return 4
            if mr5i == 11:
                while y>17:
                    return 1
                if y==17:
                    mr5i+=1
                    return 4
            if mr5i == 12:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr5i+=1
                    return 3
            if mr5i == 13:
                while x<X-7:
                    return 2
                if x==X-7:
                    mr5i+=1
                    return 3
            if mr5i == 14:
                while x>X-12:
                    return 4
                if x==X-12:
                    mr5i+=1
            if mr5i==15:
                return randint(1,4)
        elif si=="a1":
            a1()     
    elif X<(bx/2):
        if si=="bl1":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                bl1i=1
                robot.setSignal('a')
            if bl1i==1:
                while y<39:
                    return 3
                if y==39:
                    bl1i+=1
            if bl1i==2:
                while x>0:
                    return 4
                if x==0:
                    bl1i+=1
                    return 1
            if bl1i==3:
                while x<X-1:
                    return 2
                if x==X-1:
                    bl1i+=1
                    return 1
            if bl1i==4:
                while x>0:
                    return 4
                if x==0:
                    bl1i+=1
                    return 1
            if bl1i==5:
                while x<X-1:
                    return 2
                if x==X-1:
                    bl1i+=1
                    return 1
            if bl1i==6:
                while x>0:
                    return 4
                if x==0:
                    bl1i+=1
                    return 1
            if bl1i==7:
                while x<X:
                    return 2
                if x==X:
                    bl1i+=1
                    return 1
            if bl1i==8:
                while y>Y:
                    return 1
                if y==Y:
                    bl1i+=1
            while 8<bl1i<11:
                bl1i+=1
                return 1 
            if bl1i==11:
                robot.setSignal('protect2')
                return bg()
        elif si=="br1":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                br1i=1
                robot.setSignal('a')
            if br1i==1:
                while y>0:
                    return 1
                if y==0:
                    br1i+=1
            if br1i==2:
                while x>0:
                    return 4
                if x==0:
                    br1i+=1
                    return 3
            if br1i==3:
                while x<X-1:
                    return 2
                if x==X-1:
                    br1i+=1
                    return 3
            if br1i==4:
                while x>0:
                    return 4
                if x==0:
                    br1i+=1
                    return 3
            if br1i==5:
                while x<X-1:
                    return 2
                if x==X-1:
                    br1i+=1
                    return 3
            if br1i==6:
                while x>0:
                    return 4
                if x==0:
                    br1i+=1
                    return 3
            if br1i==7:
                while x<X:
                    return 2
                if x==X:
                    br1i+=1
                    return 3   
            if br1i==8:
                while y<Y:
                    return 3
                if y==Y:
                    br1i+=1
            while 8<br1i<11:
                br1i+=1
                return 2 
            if br1i == 11:
                robot.setSignal('protect2')
                return bg()            
        elif si=="bl2":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                bl2i=1
                robot.setSignal('a')
                return 4
            if bl2i==1:
                while y<33:
                    return 3
                if y==33:
                    bl2i+=1
            if bl2i==2:
                while x>0:
                    return 4
                if x==0:
                    bl2i+=1
                    return 1
            if bl2i==3:
                while x<X-2:
                    return 2
                if x==X-2:
                    bl2i+=1
                    return 1
            if bl2i==4:
                while x>0:
                    return 4
                if x==0:
                    bl2i+=1
                    return 1
            if bl2i==5:
                while x<X-2:
                    return 2
                if x==X-2:
                    bl2i+=1
                    return 1
            if bl2i==6:
                while x>0:
                    return 4
                if x==0:
                    bl2i+=1
                    return 1
            if bl2i==7:
                while x<X-2:
                    return 2
                if x==X-2:
                    bl2i+=1
                    return 1
            if bl2i==8:
                while x>0:
                    return 4
                if x==0:
                    bl2i+=1
                    return 1
            if bl2i==9:
                while x<X:
                    return 2
                if x==X:
                    bl2i+=1
                    return 1    
            if bl2i==10:
                while y>Y:
                    return 1
                if y==Y:
                    bl2i+=1
            while 10<bl2i<13:
                bl2i+=1
                return 3
            if bl2i ==13:
                robot.setSignal('protect2')
                return bg()                                               
        elif si=="br2":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                br2i=1
                robot.setSignal('a')
                return 4
            if br2i==1:
                while y>6:
                    return 1
                if y==6:
                    br2i+=1
            if br2i==2:
                while x>0:
                    return 4
                if x==0:
                    br2i+=1
                    return 3
            if br2i==3:
                while x<X-2:
                    return 2
                if x==X-2:
                    br2i+=1
                    return 3
            if br2i==4:
                while x>0:
                    return 4
                if x==0:
                    br2i+=1
                    return 3
            if br2i==5:
                while x<X-2:
                    return 2
                if x==X-2:
                    br2i+=1
                    return 3
            if br2i==6:
                while x>0:
                    return 4
                if x==0:
                    br2i+=1
                    return 3
            if br2i==7:
                while x<X-2:
                    return 2
                if x==X-2:
                    br2i+=1
                    return 3
            if br2i==8:
                while x>0:
                    return 4
                if x==0:
                    br2i+=1
                    return 3
            if br2i==9:
                while x<X:
                    return 2
                if x==X:
                    br2i+=1
                    return 3    
            if br2i==10:
                while y<Y:
                    return 3
                if y==Y:
                    br2i+=1
            while 10<br2i<13:
                br2i+=1
                return 4
            if br2i ==13:
                robot.setSignal('protect2')
                return bg()
        elif si=="bl3":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                bl3i=1
                robot.setSignal('a')
                return 4
            if bl3i==1:
                while y<25:
                    return 3
                if y==25:
                    bl3i+=1
            if bl3i==2:
                while x>0:
                    return 4
                if x==0:
                    bl3i+=1
                    return 1
            if bl3i==3:
                while x<X-3:
                    return 2
                if x==X-3:
                    bl3i+=1
                    return 1
            if bl3i==4:
                while x>0:
                    return 4
                if x==0:
                    bl3i+=1
                    return 1
            if bl3i==5:
                while x<X-3:
                    return 2
                if x==X-3:
                    bl3i+=1
                    return 1
            if bl3i==6:
                while x>0:
                    return 4
                if x==0:
                    bl3i+=1
                    return 1
            if bl3i==7:
                while x<X:
                    return 2
                if x==X:
                    bl3i+=1
                    return 1
            if bl3i==8:
                while y<Y:
                    return 3
                while y>Y:
                    return 1
                if y==Y:
                    bl3i+=1  
                    return 1 
            if bl3i==9:
                robot.setSignal('protect1')
                return sg()           
        elif si=="br3":
            b1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                br3i=1
                robot.setSignal('a')
                return 4
            if br3i==1:
                while y>14:
                    return 1
                if y==14:
                    br3i+=1
            if br3i==2:
                while x>0:
                    return 4
                if x==0:
                    br3i+=1
                    return 3
            if br3i==3:
                while x<X-3:
                    return 2
                if x==X-3:
                    br3i+=1
                    return 3
            if br3i==4:
                while x>0:
                    return 4
                if x==0:
                    br3i+=1
                    return 3
            if br3i==5:
                while x<X-3:
                    return 2
                if x==X-3:
                    br3i+=1
                    return 3
            if br3i==6:
                while x>0:
                    return 4
                if x==0:
                    br3i+=1
                    return 3
            if br3i==7:
                while x<X:
                    return 2
                if x==X:
                    br3i+=1 
                    return 3       
            if br3i==8:
                while y<Y:
                    return 3
                while y>Y:
                    return 1   
                if y==Y:
                    br3i+=1  
                    return 3
            if br3i==9:
                robot.setSignal('protect1')
                return sg()          
        elif si=="p1":
            p1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                robot.setSignal('protect1')
                return 4
            return sg()    
        elif si=="p2":
            p1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                robot.setSignal('protect1')
                return 2
            return sg()
        elif si=="fl1":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fl1i=1
                robot.setSignal('a')
            while fl1i<2:
                fl1i+=1
                return 2    
            if fl1i==2:
                while y< 39:
                    return 3
                if y==39:
                    fl1i+=1 
            if fl1i==3:           
                while x < 39:
                    return 2
                if x==39:
                    fl1i+=1
            if fl1i==4:
                while y>Y:
                    return 1
                if y==Y:
                    fl1i+=1
            if fl1i== 5:
                return randint(1,4)                   
        elif si=="fl2":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fl2i=1
                robot.setSignal('a')
            while fl2i<3:
                fl2i+=1
                return 2
            if fl2i==3:
                while y< 38:
                    return 3
                if y==38:
                    fl2i+=1 
            if fl2i==4:           
                while x < 38:
                    return 2
                if x==38:
                    fl2i+=1
            if fl2i==5:
                while y>Y:
                    return 1
                if y==Y:
                    fl2i+=1
            if fl2i== 6:
                return randint(1,4)
        elif si=="fl3":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fl3i=1
                robot.setSignal('a')
            while fl3i<4:
                fl3i+=1
                return 2 
                robot.setSignal('a')   
            if fl3i==4:
                while y< 37:
                    return 3
                if y==37:
                    fl3i+=1 
            if fl3i==5:           
                while x < 37:
                    return 2
                if x==37:
                    fl3i+=1
            if fl3i==6:
                while y>Y:
                    return 1
                if y==Y:
                    fl3i+=1
            if fl3i== 7:
                return randint(1,4)    
        elif si=="fl4":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fl4i=1
                robot.setSignal('a')
            while fl4i<5:
                fl4i+=1
                return 2    
            if fl4i==5:
                while y< 36:
                    return 3
                if y==36:
                    fl4i+=1 
            if fl4i==6:           
                while x < 36:
                    return 2
                if x==36:
                    fl4i+=1
            if fl4i==7:
                while y>Y:
                    return 1
                if y==Y:
                    fl4i+=1
            if fl4i== 8:
                return randint(1,4)    
        elif si=="fl5":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fl5i=1
            while fl5i<6:
                fl5i+=1
                return 2    
            if fl5i==6:
                while y< 35:
                    return 3
                if y==35:
                    fl5i+=1 
            if fl5i==7:           
                while x < 35:
                    return 2
                if x==35:
                    fl5i+=1
            if fl5i==8:
                while y>Y:
                    return 1 
                if y==Y:
                    fl5i+=1
            if fl5i== 9:
                return randint(1,4)       
        elif si=="fr1":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fr1i=1
                robot.setSignal('a')
            while fr1i<2:
                fr1i+=1
                return 2    
            if fr1i==2:
                while y>0:
                    return 1
                if y==0:
                    fr1i+=1 
            if fr1i==3:           
                while x < 39:
                    return 2
                if x==39:
                    fr1i+=1
            if fr1i==4:
                while y<Y:
                    return 3
                if y==Y:
                    fr1i+=1
            if fr1i== 5:
                return randint(1,4)                       
        elif si=="fr2":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fr2i=1
                robot.setSignal('a')
            while fr2i<3:
                fr2i+=1
                return 2    
            if fr2i==3:
                while y>1:
                    return 1
                if y==1:
                    fr2i+=1 
            if fr2i==4:           
                while x < 38:
                    return 2
                if x==38:
                    fr2i+=1
            if fr2i==5:
                while y<Y:
                    return 3 
                if y==Y:
                    fr2i+=1
            if fr2i== 6:
                return randint(1,4)                   
        elif si=="fr3":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fr3i=1
                robot.setSignal('a')
            while fr3i<4:
                fr3i+=1
                return 2   
            if fr3i==4:
                while y> 2:
                    return 1
                if y==2:
                    fr3i+=1 
            if fr3i==5:           
                while x < 37:
                    return 2
                if x==37:
                    fr3i+=1
            if fr3i==6:
                while y<Y:
                    return 3
                if y==Y:
                    fr3i+=1
            if fr3i== 7:
                return randint(1,4)    
        elif si=="fr4":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fr4i=1
                robot.setSignal('a')
            while fr4i<5:
                fr4i+=1
                return 2    
            if fr4i==5:
                while y> 3:
                    return 1
                if y==3:
                    fr4i+=1 
            if fr4i==6:           
                while x < 36:
                    return 2
                if x==36:
                    fr4i+=1
            if fr4i==7:
                while y<Y:
                    return 3
                if y==Y:
                    fr4i+=1
            if fr4i== 8:
                return randint(1,4)    
        elif si=="fr5":
            f1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                fr5i=1
                robot.setSignal('a')
            while fr5i<6:
                fr5i+=1
                return 2    
            if fr5i==6:
                while y> 4:
                    return 1
                if y==4:
                    fr5i+=1 
            if fr5i==7:           
                while x< 35:
                    return 2
                if x==35:
                    fr5i+=1
            if fr5i==8:
                while y<Y:
                    return 3
                if y==Y:
                    fr5i+=1
            if fr5i== 9:
                return randint(1,4)

        if si=="ml1":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                ml1i=1
                robot.setSignal('a')
            while ml1i<7:
                ml1i+=1
                return 2
            if ml1i == 7:
                while y<39-5:
                    return 3
                if y==39-5:
                    ml1i+=1
                    return 2
            if ml1i == 8:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml1i+=1
                    return 1
            if ml1i == 9:
                while x>X+7:
                    return 4
                if x==X+7:
                    ml1i+=1
                    return 1
            if ml1i == 10:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml1i+=1
            if ml1i==11:
                return randint(1,4)

        elif si=="ml2":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                ml2i=1
                robot.setSignal('a')
            while ml2i<8:
                ml2i+=1
                return 2
            if ml2i == 8:
                while y<39-8:
                    return 3
                if y==39-8:
                    ml2i+=1
                    return 2
            if ml2i == 9:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml2i+=1
                    return 1
            if ml2i == 10:
                while x>X+7:
                    return 4
                if x==X+7:
                    ml2i+=1
                    return 1
            if ml2i == 11:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml2i+=1
            if ml2i==12:
                return randint(1,4)    
        elif si=="ml3":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                ml3i=1
                robot.setSignal('a')
            while ml3i<9:
                ml3i+=1
                return 2
            if ml3i == 9:
                while y<39-11:
                    return 3
                if y==39-11:
                    ml3i+=1
                    return 2
            if ml3i == 10:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml3i+=1
                    return 1
            if ml3i == 11:
                while x>X+7:
                    return 4
                if x==X+7:
                    ml3i+=1
                    return 1
            if ml3i == 12:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml3i+=1
            if ml3i==13:
                return randint(1,4)        

        elif si=="ml4":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                ml4i=1
                robot.setSignal('a')
            while ml4i<10:
                ml4i+=1
                return 2
            if ml4i ==10:
                while y<39-14:
                    return 3
                if y==39-14:
                    ml4i+=1
                    return 2
            if ml4i == 11:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml4i+=1
                    return 1
            if ml4i == 12:
                while x>X+7:
                    return 4
                if x==X+7:
                    ml4i+=1
                    return 1
            if ml4i == 13:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml4i+=1
            if ml4i==14:
                return randint(1,4)        
        elif si=="ml5":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                ml5i=1
                robot.setSignal('a')
            while ml5i<11:
                ml5i+=1
                return 2
            if ml5i == 11:
                while y<39-17:
                    return 3
                if y==39-17:
                    ml5i+=1
                    return 2
            if ml5i == 12:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml5i+=1
                    return 1
            if ml5i == 13:
                while x>X+7:
                    return 4
                if x==X+7:
                    ml5i+=1
                    return 1
            if ml5i == 14:
                while x<X+12:
                    return 2
                if x==X+12:
                    ml5i+=1        
            if ml5i==15:
                return randint(1,4)     
        elif si=="mr1":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                mr1i=1
                robot.setSignal('a')
            while mr1i<7:
                mr1i+=1
                return 2
            if mr1i == 7:
                while y>5:
                    return 1
                if y==5:
                    mr1i+=1
                    return 2
            if mr1i == 8:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr1i+=1
                    return 3
            if mr1i == 9:
                while x>X+7:
                    return 4
                if x==X+7:
                    mr1i+=1
                    return 3
            if mr1i == 10:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr1i+=1
            if mr1i==11:
                return randint(1,4)        

        elif si=="mr2":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                mr2i=1
                robot.setSignal('a')
            while mr2i<8:
                mr2i+=1
                return 2
            if mr2i == 8:
                while y>8:
                    return 1
                if y==8:
                    mr2i+=1
                    return 2
            if mr2i == 9:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr2i+=1
                    return 3
            if mr2i == 10:
                while x>X+7:
                    return 4
                if x==X+7:
                    mr2i+=1
                    return 3
            if mr2i == 11:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr2i+=1

            if mr2i==12:
                return randint(1,4)
                    
        elif si=="mr3":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                mr3i=1
                robot.setSignal('a')
            while mr3i<9:
                mr3i+=1
                return 2
            if mr3i == 9:
                while y>11:
                    return 1
                if y==11:
                    mr3i+=1
                    return 2
            if mr3i == 10:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr3i+=1
                    return 3
            if mr3i == 11:
                while x>X+7:
                    return 4
                if x==X+7:
                    mr3i+=1
                    return 3
            if mr3i == 12:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr3i+=1
            if mr3i==13:
                return randint(1,4)         

        elif si=="mr4":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                mr4i=1
                robot.setSignal('a')
            while mr4i<10:
                mr4i+=1
                return 2
            if mr4i ==10:
                while y>14:
                    return 1
                if y==14:
                    mr4i+=1
                    return 2
            if mr4i == 11:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr4i+=1
                    return 3
            if mr4i == 12:
                while x>X+7:
                    return 4
                if x==X+7:
                    mr4i+=1
                    return 3
            if mr4i == 13:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr4i+=1
            if mr4i==14:
                return randint(1,4)        
        elif si=="mr5":
            m1()
            x,y=robot.GetPosition()
            if x==X and y==Y and s=='':
                mr5i=1
                robot.setSignal('a')
            while mr5i<11:
                mr5i+=1
                return 2
            if mr5i == 11:
                while y>17:
                    return 1
                if y==17:
                    mr5i+=1
                    return 2
            if mr5i == 12:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr5i+=1
                    return 3
            if mr5i == 13:
                while x>X+7:
                    return 4
                if x==X+7:
                    mr5i+=1
                    return 3
            if mr5i == 14:
                while x<X+12:
                    return 2
                if x==X+12:
                    mr5i+=1
            if mr5i==15:
                return randint(1,4)
        elif si=="a1":
            a1()
                    

        
def ActBase(base):
        while base.GetElixir() > 1100:
            global X,Y
            X,Y=base.GetPosition()
            global bx,by
            bx=base.GetDimensionX()
            by=base.GetDimensionY()
            base.create_robot("bl1")
            base.create_robot("bl2")
            base.create_robot("bl3")
            base.create_robot("br1")
            base.create_robot("br2")
            base.create_robot("br3")
            base.create_robot("p1")
            base.create_robot("p2")
            base.create_robot("fl1")
            base.create_robot("fl2")
            base.create_robot("fl3")
            base.create_robot("fl4")
            base.create_robot("fl5")
            base.create_robot("fr1")
            base.create_robot("fr2")
            base.create_robot("fr3")
            base.create_robot("fr4")
            base.create_robot("fr5")
            base.create_robot("ml1")
            base.create_robot("ml2")
            base.create_robot("ml3")
            base.create_robot("ml4")
            base.create_robot("ml5")
            base.create_robot("mr1")
            base.create_robot("mr2")
            base.create_robot("mr3")
            base.create_robot("mr4")
            base.create_robot("mr5")
            base.create_robot("a1")


        return

