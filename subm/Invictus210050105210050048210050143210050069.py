from random import randint

def ActRobot(robot):
        if robot.investigate_up() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 3
        if robot.investigate_up() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)      
                
                (x,y)=robot.GetPosition()
                if x<10 :
                        x1=str(0)+str(x)
                else:
                        x1=x
                if y-1<10 :
                         y1=str(0)+str(y-1)
                else:       
                        y1=y-1
                signal= str(x1)+str(y1)
                robot.setSignal(signal) 
        if robot.investigate_down() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 1
        if robot.investigate_down() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x<10 :
                        x1=str(0)+str(x)
                else:
                        x1=x        
                if y+1<10 :
                        y1=str(0)+str(y+1)
                else:
                        y1=y+1         
                signal= str(x1)+str(y1)
                robot.setSignal(signal)        
        if robot.investigate_right() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 4
        if robot.investigate_right() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x+1<10 :
                        x1=str(0)+str(x+1)
                else:
                        x1=x+1
                if y<10 :
                        y1=str(0)+str(y) 
                else:
                        y1=y
                signal= str(x1)+str(y1)
                robot.setSignal(signal)
        if robot.investigate_left() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 2
        if robot.investigate_left() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x-1<10 :
                        x1=str(0)+str(x-1)
                else:
                        x1=x-1        
                if y<10 :
                        y1=str(0)+str(y)
                else:
                        y1=y         
                signal= str(x1)+str(y1)
                robot.setSignal(signal)                  
        if robot.investigate_nw() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 3
        if robot.investigate_nw() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x-1<10 :
                        x1=str(0)+str(x-1)
                else:
                        x1=x-1
                if y-1<10 :
                        y1=str(0)+str(y-1) 
                else:
                        y1=y-1
                signal= str(x1)+str(y1)
                robot.setSignal(signal)
        if robot.investigate_ne() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 3
        if robot.investigate_ne() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x+1<10 :
                        x1=str(0)+str(x+1)
                else: x1=x+1
                if y-1<10 :
                        y1=str(0)+str(y-1) 
                else :y1=y-1
                signal= str(x1)+str(y1)
                robot.setSignal(signal)
        if robot.investigate_sw() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 1
        if robot.investigate_sw() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x-1<10 :
                        x1=str(0)+str(x-1)
                else:
                        x1=x-1        
                if y+1<10 :
                        y1=str(0)+str(y+1)
                else:
                        y1= y+1        
                signal= str(x1)+str(y1)
                robot.setSignal(signal)          
        if robot.investigate_se() == 'enemy' :
                if robot.GetVirus() > 5000:
                      robot.DeployVirus(1000)
                elif robot.GetVirus()>3500:
                      robot.DeployVirus(750)
                elif robot.GetVirus()>1200:
                      robot.DeployVirus(350)
                else:
                      return 1
        if robot.investigate_se() == 'enemy-base': 
                if robot.GetVirus() > 1200:
                      robot.DeployVirus(robot.GetVirus()*0.8)
                
                (x,y)=robot.GetPosition()
                if x+1<10 :
                        x1=str(0)+str(x+1)
                else:
                        x1=x+1
                if y+1<10 :
                        y1=str(0)+str(y+1) 
                else:
                        y1=y+1
                signal= str(x1)+str(y1)
                robot.setSignal(signal)
        if len(robot.GetCurrentBaseSignal()) > 0:
                K=robot.GetCurrentBaseSignal()[0:]
                x2=int(K[0:2])
                y2=int(K[2:4])
                (x3,y3)=robot.GetPosition()
                if x3 < x2:
                        return 2
                if x3 > x2:
                        return 4
                if y3 < y2 :
                        return 3
                if y3 > y2:
                        return 1

        else:
                return randint(1,4)
def ActBase(base):
        
        if base.investigate_up()=='enemy':
                base.DeployVirus(500)
        if base.investigate_down()=='enemy':
                base.DeployVirus(500)
        if base.investigate_left()=='enemy':
                base.DeployVirus(500)
        if base.investigate_right()=='enemy':
                base.DeployVirus(500)
        if base.investigate_nw()=='enemy':
                base.DeployVirus(500)
        if base.investigate_ne()=='enemy':
                base.DeployVirus(500)
        if base.investigate_se()=='enemy':
                base.DeployVirus(500)
        if base.investigate_sw()=='enemy':
                base.DeployVirus(500)
        if base.GetElixir() > 600:
            base.create_robot('')
        signals = base.GetListOfSignals()
        for l in signals:
                if len(l)>0:
                        base.SetYourSignal(l)
        return randint(1,4)