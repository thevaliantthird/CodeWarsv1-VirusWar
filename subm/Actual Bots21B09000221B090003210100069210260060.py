
from random import randint

def SelectiveRandint(P):
        numlist=[1,2,3,4]
        numlist.remove(P)
        X = randint(1,3)
        return numlist[X-1]


def locconvert(u,v):
    if u < 10: 
        loc = '0'+str(int(u))
    else:
        loc = str(int(u))
    if v < 10:
        loc = loc + '0'+str(int(v))
    else:
        loc = loc + str(int(v))
    return loc

def Goto(x,y,xe,ye):
    S = 0
    if x<xe: 
        S = 2
    elif x>xe: 
        S = 4
    else : 
        if y<ye: S = 3
        elif y>ye: S = 1
    return S
    
def Stay(x,y,xp,yp,xq,yq,P):
    xa = min(xp,xq)
    xb = max(xp,xq)
    ya = min(yp,yq)
    yb = max(yp,yq)
    S = 0
    if x>xa and x<xb and y>ya and y<yb:
        S = SelectiveRandint(P)
    else :
        if x<=xa:
            S = 2
        elif x>=xb:
            S = 4
        else:
            if y<=ya:
                S = 3
            elif y>=yb:
                S = 1
    return S


def ActRobot(robot):
        T = 0
        inisig =  robot.GetInitialSignal()
        x,y = robot.GetPosition()
        u = robot.GetDimensionX()
        u = u / 2
        v = robot.GetDimensionY()
        v = v / 2 
        PrevT = randint(1,4)
        if len(robot.GetYourSignal())!=0:
                PrevT = int(robot.GetYourSignal())

        if PrevT==1: PrevT = 3
        elif PrevT == 3 : PrevT = 1
        elif PrevT == 2 : PrevT = 4
        elif PrevT == 4 : PrevT = 2
        elif PrevT == 0 : PrevT = randint(1,4)
        ##getting location of base
        if inisig[2] == 0: xb = int(inisig[3])
        
        else : xb = int(inisig[2]+inisig[3])

        if inisig[4] == 0: yb = int(inisig[5])
        else : yb = int(inisig[4]+inisig[5])
        
        vert = (yb>=v)
        horiz = (xb>=u)


        totalvirus = robot.GetVirus()

        ##movement mechanism
        if robot.investigate_up()=='enemy-base' or robot.investigate_down()=='enemy-base' or robot.investigate_left()=='enemy-base' or robot.investigate_right()=='enemy-base' or robot.investigate_nw()=='enemy-base' or robot.investigate_ne()=='enemy-base' or robot.investigate_sw()=='enemy-base' or robot.investigate_se()=='enemy-base' :
            robot.DeployVirus(totalvirus)
        else:
            if inisig[0]=='d' :
                if robot.GetTotalElixir() > 2500: 
                    if inisig[1]=='A':
                        T = Goto(x,y,xb+1,yb-1)
                    elif inisig[1]=='B':
                        T= Goto(x,y,xb+1,yb+1)
                    elif inisig[1]=='C':
                        T= Goto(x,y,xb-1,yb+1)
                    elif inisig[1]=='D':
                        T= Goto(x,y,xb-1,yb-1)
                    elif inisig[1] == 'E' and horiz:
                        T = Goto(x,y,xb-2,yb)
                    elif inisig[1] == 'E' :
                        T = Goto(x,y,xb+2,yb)
                    elif inisig[1] == 'F' and vert:
                        T = Goto(x,y,xb,yb-2)
                    elif inisig[1] == 'F' :
                        T = Goto(x,y,xb,yb+2)
                    
                else: 
                    if x == xb:
                        if xb >= u: T = 2
                        elif xb<u : T = 4
                    elif y == yb:
                        if yb >= v :T = 3
                        elif yb<v : T = 1
                    else : T = SelectiveRandint(PrevT)

            elif inisig[0]=='c' : 
                if robot.GetTotalElixir() < 2500 and ord(inisig[1])-64<5:
                    if inisig[1]=='A':
                        T = Goto(x,y,xb+1,yb-1)
                    elif inisig[1]=='B':
                        T= Goto(x,y,xb+1,yb+1)
                    elif inisig[1]=='C':
                        T= Goto(x,y,xb-1,yb+1)
                    elif inisig[1]=='D':
                        T= Goto(x,y,xb-1,yb-1)
                    
                else:   
                    if xb>=u and x <= xb: T = 2
                    elif xb<u and x>=xb : T = 4
                    elif yb>v and y <= yb: T= 3
                    elif yb<v and y >= yb: T = 1
                    else : T = SelectiveRandint(PrevT)  
            elif inisig[0]=='a':
                T = SelectiveRandint(PrevT)
            elif inisig[0] == 'm' :
                T = Stay(x,y,u/2,v/2,(3*u)/2,(3*v)/2,PrevT)

            
            #Detecting opponents
            
            if inisig[0] == 'd' :
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    robot.DeployVirus(min(8000,totalvirus))
            elif inisig[0] == 'c' and ord(inisig[1])-64<5:
                    if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                        robot.DeployVirus(min(8000,totalvirus))
            else:
                if robot.investigate_up()=='enemy' or robot.investigate_down()=='enemy' or robot.investigate_left()=='enemy' or robot.investigate_right()=='enemy' or robot.investigate_nw()=='enemy' or robot.investigate_ne()=='enemy' or robot.investigate_sw()=='enemy' or robot.investigate_se()=='enemy' :
                    if totalvirus>10000:
                        robot.DeployVirus(4000) 
                    elif totalvirus>8000:
                        robot.DeployVirus(2000)
                    elif totalvirus>2000:
                        robot.DeployVirus(1000)    
                    elif totalvirus>800:
                        robot.DeployVirus(500)
                    
        robot.setSignal(str(T))        
        return T


def ActBase(base):
    x = 0
    u,v = base.GetPosition()
    loc = locconvert(u,v)

    if len(base.GetYourSignal())==0:
        TEl = base.GetElixir()
    else :
        TEl = int(base.GetYourSignal()[0:4])
    base.SetYourSignal(str(TEl))

    #getting location in string format  1,12 loc = '0112
    

    #maaking robots
    el = base.GetElixir()
    if el > TEl-300 and el>50:
        x = (TEl-el)//50 + 1
        base.create_robot('d'+str(chr(x+64))+loc)
    elif el > TEl - 600 and el > 50:  
        x = (TEl - 300 -el)//50 + 1
        base.create_robot('c'+str(chr(x+64))+loc)
    elif el > TEl - 1300 and el > 50:
        x = (TEl - 600 - el)//50 + 1
        base.create_robot('m'+str(chr(x+64))+loc)
    elif el > 50:  
        x = (TEl - 1300 -el)//50 + 1
        base.create_robot('a'+str(chr(x+64))+loc)
  
    return
