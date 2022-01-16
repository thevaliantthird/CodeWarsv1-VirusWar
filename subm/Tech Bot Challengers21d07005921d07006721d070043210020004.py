from random import randint,choice,sample,randrange


def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        ne = robot.investigate_ne()
        nw = robot.investigate_nw()
        se = robot.investigate_se()
        sw = robot.investigate_sw()
        x,y = robot.GetPosition()
        msg = []
        sig_i = robot.GetInitialSignal()
        sig_e = robot.GetCurrentBaseSignal()
        sig_c = sig_e.split(" ") #sig_c is list of enemies provided currently by base
        
        
        #msg.append("enemy" + msg_x + msg_y)
        #msg.append("e-base" + msg_x + msg_y)
        if up == "enemy" :
                
                if x < 10:
                        msg_x = '0' + str(x)
                else: 
                        msg_x = str(x)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)
                msg_1 = "" + msg_x + msg_y
                msg.append(msg_1)
                        
                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
                        
        elif up == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)
                        
        if down == "enemy" :

                if x < 10:
                        msg_x = '0' + str(x)
                else: 
                        msg_x = str(x)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)

                msg.append("" + msg_x + msg_y)        

                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
        elif down == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)
        
        if left == "enemy" :
                if x - 1 < 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)
                
                msg.append("" + msg_x + msg_y)        
                        
                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
        elif left == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)
                
        if right == "enemy" :

                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y < 10:
                        msg_y = '0' + str(y)
                else:
                        msg_y = str(y)

                msg.append("" + msg_x + msg_y) 
                        
                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
        elif right == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)
        
        if ne == "enemy" :
                
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)

                msg.append("" + msg_x + msg_y) 
                        
                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)

        elif ne == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)

        
        if nw  == "enemy" :
                
                if x-1 < 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y-1 < 10:
                        msg_y = '0' + str(y-1)
                else:
                        msg_y = str(y-1)

                msg.append("" + msg_x + msg_y) 

                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
        elif nw == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)

       
       
        if se == "enemy" :
                if x+1 < 10:
                        msg_x = '0' + str(x+1)
                else: 
                        msg_x = str(x+1)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)
                
                msg.append("" + msg_x + msg_y)

                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
        elif se == "enemy-base":
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)
       
       
        if sw == "enemy" :
                if x-1 < 10:
                        msg_x = '0' + str(x-1)
                else: 
                        msg_x = str(x-1)
                if y+1 < 10:
                        msg_y = '0' + str(y+1)
                else:
                        msg_y = str(y+1)

                msg.append("" + msg_x + msg_y) 
                        
                if robot.GetVirus() >= 6000:
                        robot.DeployVirus(1000)
                else: 
                        a=robot.GetVirus()
                        robot.DeployVirus(0.2*a)
        elif sw == "enemy-base":        
                if robot.GetVirus() >= 8000:
                        robot.DeployVirus(2500)
                else:
                        a=robot.GetVirus()
                        robot.DeployVirus(0.7*a)

        if len(msg) > 0 : 
                bot_sig = msg[0]
                robot.setSignal(bot_sig)
        if len(sig_i) > 2 and sig_i != "velle":

                if sig_i=="left":
                        if up != "wall" and right != "wall" and left != "wall" and down != "wall" : return 4
                        if left == "wall" and up != "wall" : return 1 
                        else :
                                if down == "wall" : return 4
                                elif right == "wall" : return 3
                                elif up == "wall" : return 2
                                else : return 2
                elif sig_i=="right":
                        if up != "wall" and right != "wall" and left != "wall" and down != "wall" : return 2
                        if right == "wall" and down != "wall" : return 3 
                        else :
                                if up == "wall" : return 2
                                elif left == "wall" : return 1
                                elif down == "wall" : return 4
                                else : return 3
                elif sig_i=="upup":
                        if up != "wall" and right != "wall" and left != "wall" and down != "wall" : return 1
                        if up == "wall" and right != "wall" : return 2 
                        else :
                                if left == "wall" : return 1
                                elif down == "wall" : return 4
                                elif right == "wall" : return 3
                                else : return 2
                elif sig_i=="down":
                        if up != "wall" and right != "wall" and left != "wall" and down != "wall" : return 3
                        if down == "wall" and left != "wall" : return 4
                        else :
                                if right == "wall" : return 3
                                elif up == "wall" : return 2
                                elif left == "wall" : return 1
                                else : return 4
                
                else : 
                        bx = int(sig_i[8:10])
                        by = int(sig_i[11:13])
                        if sig_i.endswith("nw"):
                                sx = bx - 1
                                sy = by - 1
                                dist = abs(sx-x) + abs(sy-y)
                                lol = randint(0,1)
                                if dist==0:
                                        return 0
                                if lol == 1 :
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                else:
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                
                                
                        elif sig_i.endswith("ne"):
                                sx = bx + 1
                                sy = by - 1
                                dist = abs(sx-x) + abs(sy-y)
                                lol = randint(0,1)
                                if dist==0:
                                        return 0
                                if lol == 1 :
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                else:
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                
                        elif sig_i.endswith("se"):
                                sx = bx + 1 
                                sy = by + 1
                                dist = abs(sx-x) + abs(sy-y)
                                lol = randint(0,1)
                                if dist==0:
                                        return 0
                                if lol == 1 :
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                else:
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4

                        elif sig_i.endswith("sw"):
                                sx = bx - 1
                                sy = by + 1
                                dist = abs(sx-x) + abs(sy-y)
                                lol = randint(0,1)
                                if dist==0:
                                        return 0
                                if lol == 1 :
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                else:
                                        if y < sy:
                                                return 3
                                        if y > sy:
                                                return 1
                                        if x < sx:
                                                return 2
                                        if x > sx:
                                                return 4
                                        
                
        elif up=="friend" or down=="friend" or right=="friend" or left=="friend" or ne=="friend" or nw=="friend" or se=="friend" or sw=="friend" :        
                if up=="friend" : return 3
                elif down=="friend": return 1
                elif right=="friend" : return 4
                elif left=="friend" :  return 2   
                elif ne == "friend" : return randint(3,4)
                elif nw == "friend" : return randint(2,3)
                elif se == "friend" : return randrange(1,5,3)
                elif sw == "friend" : return randint(1,2)
        elif sig_i == "velle" : return randint(1,4)        
        elif len(sig_c) > 0  :
                e_list = []
                for s in sig_c:
                        if len(s) > 2 : e_list.append(s)
                lol = randint(0,1)
                if len(e_list) > 0 and lol ==1:
                        target = choice(e_list)
                        sx = int(target[0:2])
                        sy = int(target[2:4])
                        dist = abs(sx-x) + abs(sy-y)
                        lol = randint(0,1)
                        if dist==0:
                                return randint(1,4)
                        if lol == 1 :
                                if x < sx:
                                        return 2
                                if x > sx:
                                        return 4
                                if y < sy:
                                        return 3
                                if y > sy:
                                        return 1
                        else:
                                if y < sy:
                                        return 3
                                if y > sy:
                                        return 1
                                if x < sx:
                                        return 2
                                if x > sx:
                                        return 4
                else :
                        return randint(1,4)
        else:
                return randint(1,4)               

        
def ActBase(base):
        base_up = base.investigate_up()
        base_down = base.investigate_down()
        base_left = base.investigate_left()
        base_right = base.investigate_right()
        base_nw = base.investigate_nw()
        base_ne = base.investigate_ne()
        base_se = base.investigate_se()
        base_sw = base.investigate_sw()
        x,y = base.GetPosition()
        
        if x < 10:
                msg_x = '0' + str(x)  
        else: 
                msg_x = str(x)
        if y < 10:
                msg_y = '0' + str(y)
        else:
                msg_y = str(y)
        if base.GetElixir() > 1300 : 
                base.create_robot("left") 
                base.create_robot("right")
                base.create_robot("upup")
                base.create_robot("down")
      
        while True:
                if base.GetElixir() > 1300 : 
                        base.create_robot("velle")
                elif base.GetElixir() > 550:
                        base.create_robot(" ")
                else:
                        break
        if base.GetElixir() > 150 and base.GetVirus()>15000 : base.create_robot(" ")

        if base_up != "friend" and base_down != "friend" and base_right != "friend" and base_left != "friend" and base.GetElixir() > 50 :
                if base_nw != "friend":
                        base.create_robot("defense " + msg_x +" " + msg_y + "nw")                        
                if base_ne != "friend":
                        base.create_robot("defense " + msg_x +" " + msg_y + "ne")
                if base_se != "friend":
                        base.create_robot("defense " + msg_x +" " + msg_y + "se")
                if base_sw != "friend":
                        base.create_robot("defense " + msg_x +" " + msg_y + "sw")
                               
        M = [] #list of new targets from bots 
        X = base.GetListOfSignals() # X vo hai jo bots se mil rhe hai
        Y = base.GetYourSignal() # Y purana signal (STRING)
        N = Y.split(" ") # N = purana signal (LIST) 
        
        for i in X:
                 if len(i) != 0 and i not in M : M.append(i) # X ke elements are added to M
        N1 = [] # list which is to be set as a signal
        if len(M) >= 4 : n = 4
        else : n = len(M)
        N1 = sample(M,n)
        for i in N :
                if len(N1) >= 4 and i not in N1 : break
                if len(i) != 0 : N1.append(i)
        Q = ""
        for i in N1:
                Q = Q + " " + i
        
        base.SetYourSignal(Q)

#1. 0 : Let the robot stay where it is
#2. 1 : Let the robot move up
#3. 2 : Let the robot move right
#4. 3 : Let the robot move down
#5. 4 : Let the robot move left