import random
from math import floor
def move_robot(ip,jp,kp,lp):
    move_prob=str(1)*ip+str(2)*jp+str(3)*kp+str(4)*lp
    return int(move_prob[random.choice(range(ip+jp+kp+lp))])

def ActRobot(robot):
    invR=[robot.investigate_nw()  , robot.investigate_up()  , robot.investigate_ne(), 
          robot.investigate_left(),                           robot.investigate_right(),  
          robot.investigate_se()  , robot.investigate_down(), robot.investigate_sw()]

    
    #canvas dimensions 
    lR= robot.GetDimensionX()
    bR= robot.GetDimensionY()

    #collecting robot's position
    robotPos=robot.GetPosition()
    robotX= robotPos[0]
    robotY= robotPos[1]

    #collecting robot's inital signal
    iSignal=robot.GetInitialSignal() #R,xx:yy,A
    temp=iSignal.split(',') 
    baseCoordinates=temp[1].split(':') #coordinates in the form ['xx','yy']
    Bx = int(baseCoordinates[0])
    By = int(baseCoordinates[1])
    aType=temp[2]


    #attack on enemies based on robot investigation
    if 'enemy-base' in invR:
        robot.DeployVirus(200)              
        #Case robot detects enemy base (X condition):                            
        if invR[1]== 'enemy-base' or invR[6]== 'enemy-base' :
            Ax = robotX
        if invR[2] == 'enemy-base' or invR[4] == 'enemy-base' or invR[5] == 'enemy-base':
            Ax = robotX+1
        if invR[0]== 'enemy-base' or invR[3]== 'enemy-base' or invR[7] == 'enemy-base':
            Ax = robotX-1
        #Case robot detects enemy base (Y condition):
        if invR[5] == 'enemy-base' or invR[6] == 'enemy-base' or invR[7] == 'enemy-base':
            Ay = robotY+1
        if invR[4] == 'enemy-base' or invR[3] == 'enemy-base':
            Ay = robotY
        if invR[1]=='enemy-base' or invR[2] == 'enemy-base' or invR[0] == 'enemy-base':
            Ay = robotY-1

        sigX=str(Ax)
        sigY=str(Ay)
        if len(sigX)<len(str(lR)):
            sigX='0'*(len(str(lR))-len(sigX))+sigX
        if len(sigY)<len(str(bR)):
            sigY='0'*(len(str(bR))-len(sigY))+sigY
        sendSignal=sigX+':'+sigY  
        robot.setSignal('D '+sendSignal)     

        return 0

    #if robot encounters enemy
    if 'enemy' in invR:
        robot.DeployVirus(200)



    bSignal=robot.GetCurrentBaseSignal()

    if aType=='A':
        if bSignal != '':
            ebaseCoordinates=bSignal.split(':') #coordinates in the form ['xx','yy']
            EBx = int(ebaseCoordinates[0])
            EBy = int(ebaseCoordinates[1])        
            #Attacking enemy base!!!!
            if (EBx-robotX) >= 0:
                goX=2
            if (EBx-robotX) < 0:
                goX=4
            if (EBy-robotY) >= 0:
                goY=3
            if (EBy-robotY) < 0:
                goY=1
            return random.choice([goX,goY])

    #wall bounce
    if robotX == int(baseCoordinates[0]) and robotY == int(baseCoordinates[1]):
        robot.setSignal('N')
        
    if 'wall' in invR:
        robot.setSignal('W')
               
    cSignal = robot.GetYourSignal()
        
    if cSignal == 'N':
        #forward robot movement
         #Coordinate System
        Dx = (lR-1-2*Bx)/(lR-1)
        Dy = (bR-1-2*By)/(bR-1)
        S = 3* max(lR,bR)           
        C1 = floor((S*abs(Dx))/(abs(Dx)+abs(Dy)))
        C2 = floor((S*abs(Dy))/(abs(Dx)+abs(Dy)))
        ip = floor((C2*By)/(bR-1)) + floor(S*5/6)
        lp = floor((C1*Bx)/(lR-1)) + floor(S*5/6)
        kp = floor((C2*(bR-1-By))/(bR-1)) + floor(S*5/6)
        jp = floor((C1*(lR-1-Bx))/(lR-1)) + floor(S*5/6)
    
        return move_robot(ip,jp,kp,lp)
    
        
    if cSignal == 'W':
        return random.randint(1,4)
    
   

def ActBase(base):
    #base investigation of surroundings
    invB=[base.investigate_nw()  , base.investigate_up()  , base.investigate_ne(), 
          base.investigate_left(),                          base.investigate_right(),  
          base.investigate_se()  , base.investigate_down(), base.investigate_sw()]
    
    #canvas dimension
    lB= base.GetDimensionX()
    bB= base.GetDimensionY()

    #position of base
    basePos=base.GetPosition()   
    baseX=str(basePos[0])
    baseY=str(basePos[1])
    if len(baseX)<len(str(lB)):
        baseX='0'*(len(str(lB))-len(baseX))+baseX
    if len(baseY)<len(str(bB)):
        baseY='0'*(len(str(bB))-len(baseY))+baseY
    
    #inital robot generation
    if base.GetElixir() > 500:
        ttype='R'    
        atype=random.choice(['A','V'])
        base.create_robot(ttype+','+baseX+':'+baseY+','+atype) #R,xx:yy,A
    
    #once the robot sends attack signal to base:
    for i in base.GetListOfSignals():
        if i != '':
            if i[0]=='D':
                temp = i.split(' ')
                temp = temp[1]
                base.SetYourSignal(temp)
                break 

    #if base detects enemy bot
    if  'enemy' in invB:
        base.DeployVirus(200)

               
    return
