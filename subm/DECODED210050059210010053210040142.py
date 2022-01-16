from random import randint
msg=str()
def sendSignal(x,y):
        if x<10:
                mx="0"+str(x)
        else:
                mx=str(x)
        if y<10:
                my="0"+str(y)
        else:
                my=str(y)
        msg=mx+my
        return msg
        
def ActRobot(robot):
        u=robot.investigate_up()
        d=robot.investigate_down()
        l=robot.investigate_left()
        r=robot.investigate_right()
        ne=robot.investigate_ne()
        nw=robot.investigate_nw()
        se=robot.investigate_se()
        sw=robot.investigate_sw()
        robot.setSignal('')
        x,y=robot.GetPosition()                                 
        if len(robot.GetCurrentBaseSignal() )==16:#attackonbase____
                z=robot.GetCurrentBaseSignal()[13:]
                A=z[0:2]
                B=z[2:4]
                while x!=int(A) and y!=int(B):
                                if x>int(A):
                                        return 4
                                elif x<int(A) :
                                        return 2
                                if y>int(B):
                                        return 1
                                elif y<int(B):
                                        return 3              
                if x==int(A) and y==int(B):
                        if robot.GetVirus() > 240:
                                robot.DeployVirus(240)
                        return 0 

        else:
                if u == "enemy":
                        if robot.GetVirus() > 700:
                                robot.DeployVirus(160)
                        if d == "enemy":
                                if l=="enemy":
                                        if r=="enemy":
                                                if robot.GetVirus() > 700:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else :
                                                return 2
                                else:
                                        return 4
                        else:
                                return 3                     

                elif u=="enemy-base":
                        sendSignal(x,y-1)
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                        if d == "enemy":
                                if l=="enemy":
                                        if r=="enemy":
                                                if robot.GetVirus() > 500:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else :
                                                return 2
                                else:
                                        return 4
                        else:
                                return 3 
                if d == "enemy":
                        if robot.GetVirus() > 700:
                                robot.DeployVirus(160)
                        if u == "enemy":
                                if l=="enemy":
                                        if r=="enemy":
                                                if robot.GetVirus() > 700:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else : 
                                                return 2
                                else:
                                        return 4
                        else:
                                return 1                     

                elif d=="enemy-base":
                        sendSignal(x,y+1)
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                        if u == "enemy":
                                if l=="enemy":
                                        if r=="enemy":
                                                if robot.GetVirus() > 500:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else : 
                                                return 2
                                else:
                                        return 4
                        else:
                                return 1
                if l== "enemy":
                        if robot.GetVirus() > 700:
                                robot.DeployVirus(160)
                        if r == "enemy":
                                if u=="enemy":
                                        if d=="enemy":
                                                if robot.GetVirus() > 700:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else : 
                                                return 3
                                else:
                                        return 1
                        else:
                                return 2                     

                elif l=="enemy-base":
                        sendSignal(x-1,y)
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                        if r == "enemy":
                                if u=="enemy":
                                        if d=="enemy":
                                                if robot.GetVirus() > 700:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else : 
                                                return 3
                                else:
                                        return 1
                        else:
                                return 2  
                if r== "enemy":
                        if robot.GetVirus() > 700:
                                robot.DeployVirus(160)
                        if l == "enemy":
                                if u=="enemy":
                                        if d=="enemy":
                                                if robot.GetVirus() > 700:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else : 
                                                return 3
                                else:
                                        return 1
                        else:
                                return 4                     

                elif r=="enemy-base":
                        sendSignal(x+1,y)
                        robot.setSignal(msg)
                        robot.DeployVirus(robot.GetVirus())
                        if l == "enemy":
                                if u=="enemy":
                                        if d=="enemy":
                                                if robot.GetVirus() > 700:
                                                        robot.DeployVirus(240)
                                                else:
                                                        return randint(1,4)
                                        else : 
                                                return 3
                                else:
                                        return 1
                        else:
                                return 4  
                if len(robot.GetCurrentBaseSignal() )==4:
                        sig=robot.GetCurrentBaseSignal()
                        X=sig[0:2]
                        Y=sig[2:4]
                        while x!=X and y!=Y:
                                if x>X:
                                        return 4
                                elif x<X :
                                        return 2
                                if y>Y:
                                        return 1
                                elif y<Y:
                                        return 3
                        if x==X and y==Y:
                                if robot.GetVirus() > 300:
                                        robot.DeployVirus(robot.GetVirus()*0.25)
                                return 0
                else : 
                        return randint(1,4)          
                


def ActBase(base):
        a,b=base.GetPosition()
        up=base.investigate_up()
        nw=base.investigate_nw()
        left=base.investigate_left()
        sw=base.investigate_sw()
        down=base.investigate_down()
        se=base.investigate_se()
        right=base.investigate_right()
        ne=base.investigate_ne()
        if up=="enemy" or nw=="enemy" or left=="enemy" or sw=="enemy" or down=="enemy" or se=="enemy" or right=="enemy" or ne=="enemy":
                if base.GetVirus()>1000:
                        base.DeployVirus(500)
                elif base.GetVirus()>500:
                        base.DeployVirus(300)
                elif base.GetVirus()>100:
                        base.DeployVirus(100)
         
        if base.GetElixir()<400:
                signal=sendSignal(a,b)
                finalsignal='attackonbase'+signal
                base.SetYourSignal(finalsignal)
        else:
                for w in base.GetListOfSignals():
                        if len(w)>0:
                                base.SetYourSignal(w)
        if base.GetElixir()>500:
                base.create_robot('')                    

        return 