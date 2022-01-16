from random import randint
from random import choice

translation = {}
inversetranslation = {}

for x in range(5000):
    translation[x] = chr(x)
    inversetranslation[chr(x)] = x
    
opposite = {
    1 : 3, 
    2 : 4,
    3 : 1,
    4 : 2
}

addjacent_1 = {
    1 : 2, 
    2 : 3,
    3 : 4,
    4 : 1 
}

addjacent_2 = {
    1 : 4, 
    2 : 1,
    3 : 2,
    4 : 3 
}

second_move = {
    1:2,
    2:3,
    3:4,
    4:1
}

third_move = {
    1:4,
    2:1,
    3:2,
    4:3
}

#All robots are identified by the first letter of their signal

#Surrounding:
#7 0 1
#6 R 2
#5 4 3

#Quadrants
# 2  1
# 3  4

# 1 = up
# 2 = right
# 3 = down
# 4 = left

def GetTo(x, y, X, Y):
    if x != X:
        if y == Y:
            if x<X:
                return(2)
            else:
                return(4)
        else:
            if y < Y:
                if x<X:
                    return(choice([2, 3]))
                else:
                    return(choice([4, 3]))
            else:
                if x<X:
                    return(choice([2, 1]))
                else:
                    return(choice([4, 1]))
    else:
        if y<Y:
            return(3)
        else:
            return(1)
        
def deployvirusfarm(availablevirus):
    backupvirus = 1000
    deploymax = 3000
    if availablevirus <= backupvirus:
        return(0)
    elif availablevirus > backupvirus and availablevirus <= backupvirus + deploymax:
        return(availablevirus - backupvirus)
    else:
        return(deploymax)
    
def gettoquadrant(robotquadrant, targetquadrant):
    if robotquadrant == targetquadrant:
        return (randint(1, 4))
    
    elif robotquadrant == 1:
        if targetquadrant == 2:
            return(4)
        elif targetquadrant == 3:
            return(choice([4, 3]))
        elif targetquadrant == 4:
            return(3)
    
    elif robotquadrant == 2:
        if targetquadrant == 1:
            return(2)
        elif targetquadrant == 3:
            return(3)
        elif targetquadrant == 4:
            return(choice([3, 2]))
    
    elif robotquadrant == 3:
        if targetquadrant == 2:
            return(1)
        elif targetquadrant == 1:
            return(choice([1, 2]))
        elif targetquadrant == 4:
            return(2)
    
    elif robotquadrant == 4:
        if targetquadrant == 2:
            return(choice([1, 4]))
        elif targetquadrant == 3:
            return(4)
        elif targetquadrant == 1:
            return(1)
    
def ActRobot(robot):
    basesignal = robot.GetCurrentBaseSignal()
    move = 0
    x, y = robot.GetPosition()
    (X, Y) = (robot.GetDimensionX(), robot.GetDimensionY())
    if x<= X/2-1 and y <= Y/2-1:
        robotquadrant = 2
    
    elif x>=X/2 and y<= Y/2-1:
        robotquadrant = 1
    
    elif x<=X/2 - 1 and y>= Y/2:
        robotquadrant = 3
    
    elif x>=X/2 and y>= Y/2:
        robotquadrant = 4
    surrounding = [robot.investigate_up(), robot.investigate_ne(), robot.investigate_right(), robot.investigate_se(), robot.investigate_down(), robot.investigate_sw(), robot.investigate_left(), robot.investigate_nw()]
    signal = robot.GetInitialSignal()
    try:
        if signal[0] == "D":
            if len(robot.GetYourSignal()) == 0:
                move = int(signal[1])
                robot.setSignal("DE0N") 
            elif robot.GetYourSignal() == "DE0N":
                move = second_move[int(signal[1])]
                robot.setSignal("DC0N")
            elif robot.GetYourSignal() == "DC0N":
                move = third_move[int(signal[1])]
                robot.setSignal("DE0N")
            if "enemy" in surrounding:
                robot.DeployVirus(min(6400, robot.GetVirus()))
            
        elif signal[0] == "N":
            if len(robot.GetYourSignal()) == 0:
                robot.setSignal("N" + signal[2] + "0N")
            if robot.GetYourSignal() == "NM0N":
                move = int(signal[1])
                robot.setSignal("NE0N")
            elif robot.GetYourSignal == "NW0N":
                move = 0
                robot.setSignal("NM0N")
            elif robot.GetYourSignal() == "NE0N":
                move = second_move[int(signal[1])]
                robot.setSignal("NC0N")
            elif robot.GetYourSignal() == "NC0N":
                move = third_move[int(signal[1])]
                robot.setSignal("NE0N")
            if "enemy" in surrounding:
                robot.DeployVirus(min(6400, robot.GetVirus()))
            
            
            
        elif signal[0] == "F":
            if basesignal[5] == "Y":
                move = GetTo(x, y, inversetranslation[basesignal[6]], inversetranslation[basesignal[7]])
            else:
                if len(robot.GetYourSignal()) == 0:
                    if x < X/2:
                        robot.setSignal(signal + "N  02")
                    else:
                        robot.setSignal(signal + "N  04")
                
                if robot.GetYourSignal()[6] == "0" and ((Y%2 == 0 and  inversetranslation[signal[2]] <= Y/2-1 )or(Y%2 == 1 and  inversetranslation[signal[2]]<= Y//2)):
                    if (robot.GetYourSignal()[7] == "2" and x == X-1) or (robot.GetYourSignal()[7] == "4" and x == 0):
                        dummy = robot.GetYourSignal()[0:6]
                        robotsignal = dummy + "1" 
                        robot.setSignal(robotsignal)
                        move = randint(1, 4)
                    elif y == 2*inversetranslation[signal[2]] + 1:
                        move = int(robot.GetYourSignal()[7])
                    elif y < 2*inversetranslation[signal[2]] + 1:
                        move = 3
                    else:
                        move = 1
                else:       
                    move = gettoquadrant(robotquadrant, int(signal[1]))
            
            if "enemy" in surrounding:
                robot.DeployVirus(deployvirusfarm(robot.GetVirus()))
                
            if "enemy-base" in surrounding:
                robotsignal = robot.GetYourSignal()
                robot.DeployVirus(robot.GetVirus())
                if surrounding[0] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x] + translation[y - 1]
                    robot.setSignal(robotsignal)
                
                elif surrounding[1] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x + 1] + translation[y - 1]
                    robot.setSignal(robotsignal)
                
                elif surrounding[2] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x + 1] + translation[y]
                    robot.setSignal(robotsignal)
                    
                elif surrounding[3] == "enemy-base":
                    dummy = signal[0:3]
                    robotsignal = dummy + "Y" + translation[x + 1] + translation[y + 1]
                    robot.setSignal(robotsignal)
                    
                elif surrounding[4] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x] + translation[y + 1]
                    robot.setSignal(robotsignal)
                    
                elif surrounding[5] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x - 1] + translation[y + 1]
                    robot.setSignal(robotsignal)
                    
                elif surrounding[6] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x - 1] + translation[y]
                    robot.setSignal(robotsignal)
                    
                elif surrounding[7] == "enemy-base":
                    dummy = robotsignal[0:3]
                    robotsignal = dummy + "Y" + translation[x - 1] + translation[y - 1]
                    robot.setSignal(robotsignal)
            
    except:
        pass        
             
    return(move)

def ActBase(base):
    X = base.GetDimensionX()
    Y = base.GetDimensionY()
    x, y = base.GetPosition()
    
    if len(base.GetYourSignal()) == 0:
        for i in range(X//2 + 5):
            if i < 4 and base.GetElixir() > 50:
                base.create_robot("D" + str(i+1))
            elif base.GetElixir() >= 300:
                base.create_robot("F" + str(randint(1, 4)) + translation[(i-4)])    
        base.SetYourSignal(translation[1] + "4999N  ")
    else:
        try:
                dummysignal = [x for x in base.GetYourSignal()]
                dummysignal[0] = translation[inversetranslation[dummysignal[0]]+1]
                dummysignalstring = ""
                for x in dummysignal:
                    dummysignalstring = dummysignalstring + x
                base.SetYourSignal(dummysignalstring)
        except:
                pass
        signals = base.GetListOfSignals()
        try:
            rowoccupied = [x[0] + x[2] for x in signals]
            rowtobeoccupied = ["F" + translation[i] for i in range(X//2 + 1)]
            for x in rowtobeoccupied:
                if x not in rowoccupied and base.GetElixir() >= 300:
                    base.create_robot(x[0] + str(randint(1, 4)) + x[1])
        except:
            pass
        if inversetranslation[base.GetYourSignal()[0]] > 400 and base.GetElixir() >= 300:
            base.create_robot("F" + str(randint(1, 4)) + translation[(randint(0, X-1))])
    if base.GetYourSignal() !=0:
        if inversetranslation[base.GetYourSignal()[0]] != "1":
            basesignal = base.GetYourSignal()
            surrounding = [base.investigate_up(), base.investigate_ne(), base.investigate_right(), base.investigate_se(), base.investigate_down(), base.investigate_sw(), base.investigate_left(), base.investigate_nw()]
            signals = base.GetListOfSignals()
            defensebots = 0
            
            if "enemy" in surrounding:
                base.DeployVirus(base.GetVirus())
                
            for x in signals:
                try:
                    if x[0] == "D" or x[0] == "N":
                        defensebots += 1
                except:
                    pass
            for x in signals:
                try: 
                    if x[3] == "Y":
                        x_enemybase = inversetranslation[x[4]]
                        y_enemybase = inversetranslation[x[5]]
                        dummy = basesignal[0:5]
                        dummy = dummy + "Y" + translation[x_enemybase] + translation[y_enemybase] + basesignal[8:10]
                        base.SetYourSignal(dummy)
                        break
                except:
                    pass
            
            if defensebots <= 3 and base.GetElixir() > 50:
                edgeorcorner = "M"
                for x in signals:
                    try:
                        if (x[0] == "D" or x[0] == "N") and x[1] == "C":
                            break
                        elif (x[0] == "D" or x[0] == "N") and x[1] == "E":
                            edgeorcorner = "W"
                            break
                    except:
                        pass
                if surrounding[0] != "friend" and surrounding[1] != "friend":
                    base.create_robot("N1" + edgeorcorner)
                if surrounding[2] != "friend" and surrounding[3] != "friend":
                    base.create_robot("N2" + edgeorcorner)
                if surrounding[4] != "friend" and surrounding[5] != "friend":
                    base.create_robot("N3" + edgeorcorner)
                if surrounding[6] != "friend" and surrounding[7] != "friend":
                    base.create_robot("N4" + edgeorcorner)
    return()

