from random import randint,choice

def investigate(robot):
        return (robot.investigate_nw(), robot.investigate_up(), robot.investigate_ne(),
                robot.investigate_left(), "blank", robot.investigate_right(),
                robot.investigate_sw(), robot.investigate_down(), robot.investigate_se())

def moveTo(x,y,robot):
        position=robot.GetPosition()
        if position[0] == x and position[1] == y:
                return 0
        if position[0] == x:
                return (position[1]<y)*2+1
        if position[1] == y :
                return (position[0]>x)*2+2  
        if randint(1,2)==1:
                return (position[0]>x)*2+2
        else:
                return (position[1]<y)*2+1

def moveAway(x,y,robot):
        position=robot.GetPosition()
        if position[0] == x and position[1] == y:
                return randint(1,4)
        if randint(1,2)==1:
                return (position[0]<x)*2+2
        else:
                return (position[1]>y)*2+1

def circleAround(x,y,radius,robot,initial = "abc",clockwise=True):
        position=robot.GetPosition()
        rx=position[0]
        ry=position[1]
        pos=[[x+i,y+radius] for i in range(-1*radius,radius+1)]
        pos.extend([[x+radius,y+i] for i in range(radius-1,-1*radius-1,-1)])
        pos.extend([[x+i,y-radius] for i in range(radius-1,-1*radius-1,-1)])
        pos.extend([[x-radius,y+i] for i in range(-1*radius+1,radius)])
        if [rx,ry] not in pos:
                if initial != "abc":
                        return moveTo(initial[0],initial[1],robot)
                if rx in [x+i for i in range(-1*radius,radius+1)] and ry in [y+i for i in range(-1*radius,radius+1)]:
                        return moveAway(x,y,robot)
                else :
                        return moveTo(x,y,robot)
        else:
                index=pos.index([rx,ry])
                return moveTo(pos[(index+(clockwise*2)-1)%len(pos)][0],pos[(index+(clockwise*2)-1)%len(pos)][1],robot)

def ActRobot(robot):
        surr=investigate(robot)
        if "enemy-base" in surr:
                index=surr.index("enemy-base")
                oppo_base=robot.GetPosition()
                robot.setSignal("e"+str(oppo_base[0]+(index%3)-1)+","+str(oppo_base[1]+(int(index/3))-1))
                if robot.GetVirus()>100:
                        robot.DeployVirus(robot.GetVirus())
                        return circleAround(oppo_base[0]+(index%3)-1,oppo_base[1]+(int(index/3))-1,1,robot)
        if "enemy" in surr:
                if 'Defender' in robot.GetInitialSignal() and robot.GetElixir()>2000:
                        robot.DeployVirus(1600)
                index=surr.index("enemy")
                enemy=robot.GetPosition()
                robot.setSignal("r"+str(enemy[0]+(index%3)-1)+","+str(enemy[1]+(int(index/3))-1))
                if robot.GetVirus()>200:
                        if robot.GetVirus()>1000:
                                if robot.GetVirus()>10000:
                                        robot.DeployVirus(1000)
                                else:
                                        robot.DeployVirus(500)
                        else:
                                robot.DeployVirus(200)
                        return circleAround(enemy[0]+(index%3)-1,enemy[1]+(int(index/3))-1,1,robot)
        elif robot.GetYourSignal() != "" and robot.GetYourSignal()[0] == 'r':
                robot.setSignal("")
        baseSignal=robot.GetCurrentBaseSignal()
        base_signal=baseSignal[1:].split(",")
        if baseSignal != "" and baseSignal[0] == "b": #and robot.GetVirus()>1:
                base_signal=[float(base_signal[0]),float(base_signal[1])]
                return circleAround(base_signal[0],base_signal[1],randint(0,2),robot,clockwise=choice([True,False]))
        if 'Defender' in robot.GetInitialSignal():
                if robot.GetYourSignal() == "":
                        if 'Defender1' in robot.GetInitialSignal():
                                robot.setSignal("do200")
                        else:
                                robot.setSignal("du200")
                if robot.GetYourSignal()[0] == 'd':
                        if robot.GetYourSignal()[1] == "o":
                                if robot.GetYourSignal()[2:] == "1":
                                        robot.setSignal("du201")
                                base_position=robot.GetInitialSignal()[11:]
                                base_position=base_position.split()
                                base_position=[int(base_position[0]),int(base_position[1])]
                                number=int(robot.GetInitialSignal()[10])
                                robot.setSignal(robot.GetYourSignal()[:2]+str(int(robot.GetYourSignal()[2:])-1))
                                return circleAround(base_position[0],base_position[1],1,robot,[base_position[0]+1*((number%4)-1)*((number%2)-1),base_position[1]+1*(number%4-2)*(number%2)],number%2==0)
                        else:
                                if robot.GetYourSignal()[2:] == "1":
                                        robot.setSignal("do201")
                                robot.setSignal(robot.GetYourSignal()[:2]+str(int(robot.GetYourSignal()[2:])-1))
        if 'Attacker' in robot.GetInitialSignal():
                num=int(robot.GetInitialSignal()[8])
                base_position=robot.GetInitialSignal()[9:]
                base_position=base_position.split(",")
                if robot.GetVirus()>1000:
                        if num==0:
                                return circleAround(robot.GetDimensionX()-int(base_position[0]),robot.GetDimensionY()-int(base_position[1]),randint(1,3),robot)
                        elif num==1:
                                return circleAround(robot.GetDimensionX()-int(base_position[0]),int(base_position[1]),randint(1,3),robot)
                        elif num==2:
                                return circleAround(int(base_position[0]),robot.GetDimensionY()-int(base_position[1]),randint(1,3),robot)
                if robot.GetVirus()>2000:
                        if num==3:
                                return circleAround(robot.GetDimensionX()-int(base_position[0]),robot.GetDimensionY()-int(base_position[1]),randint(1,3),robot)
                        elif num==4:
                                return circleAround(robot.GetDimensionX()-int(base_position[0]),int(base_position[1]),randint(1,3),robot)
                        elif num==5:
                                return circleAround(int(base_position[0]),robot.GetDimensionY()-int(base_position[1]),randint(1,3),robot)
        if baseSignal != "" and baseSignal[0] == "e": 
                if robot.GetInitialSignal() == 'Attacker' or randint(1,3)==1:
                        if robot.GetVirus()<100:
                                pass
                        else:
                                base_signal=[float(base_signal[0]),float(base_signal[1])]
                                return circleAround(base_signal[0],base_signal[1],1,robot)
                if robot.GetInitialSignal() == 'Destroyer':
                        base_signal=[float(base_signal[0]),float(base_signal[1])]
                        return circleAround(base_signal[0],base_signal[1],1,robot)
        selfSignal=robot.GetYourSignal()
        selfSignal=selfSignal.split(",")
        if baseSignal != "" and baseSignal[0] == "r":
                if selfSignal != [""] and selfSignal[0] != "E":
                        if randint(1,10)==1:
                                base_signal=[float(base_signal[0]),float(base_signal[1])]
                                return circleAround(base_signal[0],base_signal[1],1,robot)
        if selfSignal == [""] or selfSignal[0] == "r":
                move=randint(1,4)
                robot.setSignal("U,"+str(move)+","+str(int(robot.GetElixir())))
                return move
        elif selfSignal[0]=="U":
                li=[1,2,3,4]
                dic={1:3,3:1,2:4,4:2}
                li.remove(int(dic[int(selfSignal[1])]))
                move=choice(li)
                if int(robot.GetElixir()) > int(selfSignal[2]):
                        robot.setSignal("E,"+str(move)+","+str(int(robot.GetElixir())))
                else:
                        robot.setSignal("U,"+str(move)+","+str(int(robot.GetElixir())))
                return move
        elif selfSignal[0]=="E":
                if int(robot.GetElixir()) <= int(selfSignal[2])+5:
                        dic={1:3,3:1,2:4,4:2}
                        move=dic[int(selfSignal[1])]
                        robot.setSignal("U,"+str(move)+","+str(int(robot.GetElixir())))
                        return move
                else:
                        li=[1,2,3,4]
                        dic={1:3,3:1,2:4,4:2}
                        li.remove(dic[int(selfSignal[1])])
                        move=choice(li)
                        robot.setSignal("E,"+str(move)+","+str(int(robot.GetElixir())))
                        return move
        return randint(1,4)

def ActBase(base):
        signals=base.GetListOfSignals()
        if len(signals)==0:
                for i in range(6):
                        base.create_robot('Attacker'+str(i)+str(base.GetPosition()[0])+","+str(base.GetPosition()[1]))
                for i in range(4):
                        base.create_robot('Defender1 '+str(i)+str(base.GetPosition()[0])+" "+str(base.GetPosition()[1]))
                for i in range(4):
                        base.create_robot('Defender2 '+str(i)+str(base.GetPosition()[0])+" "+str(base.GetPosition()[1]))
        numro=int((base.GetElixir()-500)/50)               
        for i in range(numro):
                base.create_robot('Collector')
        if base.GetElixir()>=500 and base.GetYourSignal() != "" and base.GetYourSignal()[0]=='e':
                for i in range(4):
                        base.create_robot("Destroyer")
        signals=base.GetListOfSignals()
        for signal in signals:
                if signal != "" and signal[0] == "e":
                        base.SetYourSignal(signal)
                if signal != "" and signal[0] == "r" and not( base.GetYourSignal() !=  "" and base.GetYourSignal()[0] == "e"):
                        base.SetYourSignal(signal)
        if base.GetYourSignal() !=  "":
                base.SetYourSignal(base.GetYourSignal())
        else :
                base.SetYourSignal("")
        surr = investigate(base)
        if "enemy" in surr:
                base.SetYourSignal("b"+str(base.GetPosition()[0])+","+str(base.GetPosition()[1]))
                if base.GetVirus()>800:
                        base.DeployVirus(800)
                else:
                        base.DeployVirus(base.GetVirus())
        if "enemy" not in surr and base.GetYourSignal() != "" and base.GetYourSignal()[0] == "b":
                base.SetYourSignal("")