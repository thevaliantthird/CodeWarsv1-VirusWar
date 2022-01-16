from random import randint


def ActRobot(robot):
        U = robot.investigate_up()
        D = robot.investigate_down()
        R = robot.investigate_right()
        L = robot.investigate_left()
        TR = robot.investigate_ne()
        BR = robot.investigate_se()
        TL = robot.investigate_nw()
        BL = robot.investigate_sw()

        if robot.GetInitialSignal() == "def1":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX:
                                return 2
                        elif X > SX:
                                return 4
                        if Y < SY-1:
                                return 3
                        elif Y > SY-1:
                                return 1
                        elif Y == SY-1:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)

        elif robot.GetInitialSignal() == "def2":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX+1:
                                return 2
                        elif X > SX+1:
                                return 4
                        if Y < SY-1:
                                return 3
                        elif Y > SY-1:
                                return 1
                        elif Y == SY-1:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)

        elif robot.GetInitialSignal() == "def3":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX+1:
                                return 2
                        elif X > SX+1:
                                return 4
                        if Y < SY:
                                return 3
                        elif Y > SY:
                                return 1
                        elif Y == SY:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                
        elif robot.GetInitialSignal() == "def4":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX+1:
                                return 2
                        elif X > SX+1:
                                return 4
                        if Y < SY+1:
                                return 3
                        elif Y > SY+1:
                                return 1
                        elif Y == SY+1:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)

        elif robot.GetInitialSignal() == "def5":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX:
                                return 2
                        elif X > SX:
                                return 4
                        if Y < SY+1:
                                return 3
                        elif Y > SY+1:
                                return 1
                        elif Y == SY+1:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)

        elif robot.GetInitialSignal() == "def6":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX-1:
                                return 2
                        elif X > SX-1:
                                return 4
                        if Y < SY+1:
                                return 3
                        elif Y > SY+1:
                                return 1
                        elif Y == SY+1:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)

        elif robot.GetInitialSignal() == "def7":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX-1:
                                return 2
                        elif X > SX-1:
                                return 4
                        if Y < SY:
                                return 3
                        elif Y > SY:
                                return 1
                        elif Y == SY:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)

        elif robot.GetInitialSignal() == "def8":
                X,Y = robot.GetPosition()
                if len(robot.GetCurrentBaseSignal()) == 9:
                        S = robot.GetCurrentBaseSignal()[5:]
                        SX = int(S[0:2])
                        SY = int(S[2:4])
                        if X < SX-1:
                                return 2
                        elif X > SX-1:
                                return 4
                        if Y < SY-1:
                                return 3
                        elif Y > SY-1:
                                return 1
                        elif Y == SY-1:
                                return 0
                if U == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if D == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if R == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if L == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if TL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                if BR == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6) 
                if BL == "enemy":
                        robot.DeployVirus(robot.GetVirus()*0.6)
                
        elif robot.GetInitialSignal() == "scout1":
                if U == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif U == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif U == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif U == "enemy-base":
                        x,y = robot.GetPosition()
                        if x<10:
                                msg_x = '0' + str(x)
                        else:
                                msg_x = str(x)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif U == "friend-base":
                        x,y = robot.GetPosition()
                        if x<10:
                                msg_x = '0' + str(x)
                        else:
                                msg_x = str(x)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)
        
                if D == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif D == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif D == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif D == "enemy-base":
                        x,y = robot.GetPosition()
                        if x<10:
                                msg_x = '0' + str(x)
                        else:
                                msg_x = str(x)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif D == "friend-base":
                        x,y = robot.GetPosition()
                        if x<10:
                                msg_x = '0' + str(x)
                        else:
                                msg_x = str(x)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)

                if R == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif R == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif R == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif R == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 <10:
                                msg_x = '0' + str(x+1)
                        else:
                                msg_x = str(x+1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif R == "friend-base":
                        x,y = robot.GetPosition()
                        if x+1<10:
                                msg_x = '0' + str(x+1)
                        else:
                                msg_x = str(x+1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)

                if L == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif L == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif L == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif L == "enemy-base":
                        x,y = robot.GetPosition()
                        if x-1 <10:
                                msg_x = '0' + str(x-1)
                        else:
                                msg_x = str(x-1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif L == "friend-base":
                        x,y = robot.GetPosition()
                        if x-1<10:
                                msg_x = '0' + str(x-1)
                        else:
                                msg_x = str(x-1)
                        if y < 10:
                                msg_y = '0' + str(y)
                        else:
                                msg_y = str(y)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)

                if TR == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif TR == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif TR == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif TR== "enemy-base":
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
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif TR == "friend-base":
                        x,y = robot.GetPosition()
                        if x+1<10:
                                msg_x = '0' + str(x+1)
                        else:
                                msg_x = str(x+1)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)

                if TL == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif TL == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif TL == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif TL == "enemy-base":
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
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif TL == "friend-base":
                        x,y = robot.GetPosition()
                        if x-1<10:
                                msg_x = '0' + str(x-1)
                        else:
                                msg_x = str(x-1)
                        if y-1 < 10:
                                msg_y = '0' + str(y-1)
                        else:
                                msg_y = str(y-1)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)

                if BR == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif BR == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif BR == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif BR == "enemy-base":
                        x,y = robot.GetPosition()
                        if x+1 <10:
                                msg_x = '0' + str(x+1)
                        else:
                                msg_x = str(x+1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif BR == "friend-base":
                        x,y = robot.GetPosition()
                        if x+1<10:
                                msg_x = '0' + str(x+1)
                        else:
                                msg_x = str(x+1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)

                if BL == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif BL == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif BL == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                elif BL == "enemy-base":
                        x,y = robot.GetPosition()
                        if x-1 <10:
                                msg_x = '0' + str(x-1)
                        else:
                                msg_x = str(x-1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "base" + msg_x + msg_y
                        robot.setSignal(msg)
                        if robot.GetVirus() > 0:
                                robot.DeployVirus(robot.GetVirus())
                elif BL == "friend-base":
                        x,y = robot.GetPosition()
                        if x-1<10:
                                msg_x = '0' + str(x-1)
                        else:
                                msg_x = str(x-1)
                        if y+1 < 10:
                                msg_y = '0' + str(y+1)
                        else:
                                msg_y = str(y+1)
                        msg = "fbase" + msg_x + msg_y
                        robot.setSignal(msg)
                if len(robot.GetCurrentBaseSignal()) == 8:
                        x,y = robot.GetPosition()
                        s = robot.GetCurrentBaseSignal()[4:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist==1:
                                robot.DeployVirus(robot.GetVirus())
                                return 0
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy:
                                return 3
                        if y > sy:
                                return 1
        
                elif len(robot.GetYourSignal()) == 12:
                        return randint(1,4)

                else:
                        x,y = robot.GetPosition()
                        CX = robot.GetDimensionX()//2
                        CY = robot.GetDimensionY()//2 
                        if x < CX:
                                return 2
                        if x > CX:
                                return 4
                        if y < CY:
                                return 3
                        if y > CY:                                       
                                return 1
                        if x == CX and y == CY:
                                robot.setSignal("moverandomly")
        
        elif robot.GetInitialSignal() == "scout2":
                if U == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif U == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif U == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                
                if D == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif D == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif D == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)

                if R == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif R == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif R == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)

                if L == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif L == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif L == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)

                if TR == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif TR == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif TR == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)

                if TL == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif TL == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif TL == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)

                if BR == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif BR == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif BR == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)

                if BL == "enemy" and robot.GetVirus() > 2000:
                        robot.DeployVirus(1200)
                elif BL == "enemy" and robot.GetVirus() > 1000 and robot.GetVirus() < 2000:
                        robot.DeployVirus(1000)
                elif BL == "enemy" and robot.GetVirus() < 1000:
                        robot.DeployVirus(600)
                        
                return randint(1,4)


def ActBase(base):
    
        if base.GetElixir() > 1950:
            base.create_robot("def1")
        elif base.GetElixir() > 1900:
            base.create_robot("def2")
        elif base.GetElixir() > 1850:
            base.create_robot("def3")
        elif base.GetElixir() > 1800:
            base.create_robot("def4")
        elif base.GetElixir() > 1750:
            base.create_robot("def5")
        elif base.GetElixir() > 1700:
            base.create_robot("def6")
        elif base.GetElixir() > 1650:
            base.create_robot("def7")
        elif base.GetElixir() > 1600:
            base.create_robot("def8")
        elif base.GetElixir() > 800:
            base.create_robot("scout1")
        elif base.GetElixir() > 600:
            base.create_robot("scout2")

        u = base.investigate_up()
        d = base.investigate_down()
        r = base.investigate_right()
        l = base.investigate_left()
        tr = base.investigate_ne()
        br = base.investigate_se()
        tl = base.investigate_nw()
        bl = base.investigate_sw()
        
        if u == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif u == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)
        
        if d == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif d == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)

        if r == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif r == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)

        if l == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif l == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)

        if tr == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif tr == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)

        if tl == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif tl == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)

        if br == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif br == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)

        if bl == "enemy" and base.GetElixir() > 500:
                base.DeployVirus(base.GetVirus()*0.5)
        elif bl == "enemy" and base.GetElixir() < 500:
                base.DeployVirus(base.GetVirus()*0.8)        


        L = base.GetListOfSignals()
        for l in L:
                if len(l) == 8:
                        base.SetYourSignal(l)
                        return
                elif len(l) == 9:
                        base.SetYourSignal(l) 

                
