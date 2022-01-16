from numpy import int0
def ActRobot(robot):
        if robot.GetYourSignal()=='':
                if int(robot.GetCurrentBaseSignal())<=20:
                        robot.setSignal(robot.GetInitialSignal()+'39')
                else:        
                        robot.setSignal(robot.GetInitialSignal()+'00')                
        if robot.GetPosition()[0]==00:
                robot.setSignal(shuffle2(robot)+'39')
                return 2
        if robot.GetPosition()[0]==39:        
                robot.setSignal(shuffle2(robot)+'00')
                return 4        
        if robot.investigate_up() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_down() == 'enemy-base':
                robot.DeployVirus(2000)
                return  0
        if robot.investigate_right() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_left() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_nw() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_ne() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_se() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_sw() == 'enemy-base':
                robot.DeployVirus(2000)
                return 0
        if robot.investigate_up() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        if robot.investigate_down() == 'enemy':
                robot.DeployVirus(1000)
                return  0
        if robot.investigate_right() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        if robot.investigate_left() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        if robot.investigate_nw() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        if robot.investigate_ne() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        if robot.investigate_se() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        if robot.investigate_sw() == 'enemy':
                robot.DeployVirus(1000)
                return 0
        return goposition(robot)
        
def ActBase(base):
    defense(base)
    base.SetYourSignal(str(base.GetPosition()[0]))
    if base.GetElixir() > 50:
                 s=str(int((2000-base.GetElixir())/50))
                 if int(s)<10:
                     base.create_robot('0'+s)
                 else:
                     base.create_robot(s)    
    else:
                 base.SetYourSignal(shuffle(base))
    return

def goposition(robot):
     if robot.GetPosition()[1]>int((int(robot.GetYourSignal()))/100):
             return 1
     elif robot.GetPosition()[1]<int((int(robot.GetYourSignal()))/100):
             return 3
     else :
             if int((int(robot.GetYourSignal()))%100)==39:
                     return 2
             else:
                     return 4


def defense(base):
        if base.investigate_up() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_down() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_right() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_left() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_nw() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_ne() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_se() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_sw() == 'enemy-base':
                base.DeployVirus(2000)
        if base.investigate_up() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_down() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_right() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_left() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_nw() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_ne() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_se() == 'enemy':
                base.DeployVirus(1000)
        if base.investigate_sw() == 'enemy':
                base.DeployVirus(1000)
        return

def shuffle(base):
        x=0
        s=''
        for i in range(0,(len(base.GetListOfSignals())-1)):
                if int(int(base.GetListOfSignals()[i+1])/100)-int(int(base.GetListOfSignals()[i])/100)>=3:# or int(int(base.GetListOfSignals()[i+1])/100)-int(int(base.GetListOfSignals()[i])/100)==5:
                       if int(int(base.GetListOfSignals()[i])/100)<10:
                          s= '0'+str(int(int(base.GetListOfSignals()[i])/100))
                       else:
                          s=str(int(int(base.GetListOfSignals()[i])/100))     
                       if int(int(base.GetListOfSignals()[i])/100)+1<10:
                          s+='0'+str(int(int(base.GetListOfSignals()[i])/100)+1)+','
                       else:
                          s+=str(int(int(base.GetListOfSignals()[i])/100)+1)+','
                       if int(int(base.GetListOfSignals()[i+1])/100)<10:           
                          s=s+'0'+str(int(int(base.GetListOfSignals()[i+1])/100))
                       else:
                          s+=str(int(int(base.GetListOfSignals()[i+1])/100))
                       if int(int(base.GetListOfSignals()[i+1])/100)-1<10:
                          s+='0'+str(int(int(base.GetListOfSignals()[i+1])/100)-1)+','
                       else:
                          s+=str(int(int(base.GetListOfSignals()[i+1])/100)-1)+','                   
        return  s              
def shuffle2(robot):
        i=0
        while i<len(robot.GetCurrentBaseSignal()):  
              x=robot.GetCurrentBaseSignal()[int(i):int(i+2)]
              if robot.GetYourSignal()[0:2]==x:
                      return  robot.GetCurrentBaseSignal()[int(i+2):int(i+4)]
              i+=5
        return robot.GetYourSignal()[0:2]