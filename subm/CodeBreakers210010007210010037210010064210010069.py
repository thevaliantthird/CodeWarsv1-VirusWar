from random import randint


def ActBase(base):
        brght = base.investigate_right()
        bleft = base.investigate_left()
        bup = base.investigate_up()
        bdown = base.investigate_down()
        bnw = base.investigate_nw()
        bne = base.investigate_ne()
        bse = base.investigate_se()
        bsw = base.investigate_sw()
        virus = base.GetVirus()
        global x; global y
        x,y = base.GetPosition()
        int(x); int(y)
        ActBase.counter+=1
        
        if virus>3999:
                base.SetYourSignal(">3999")
        elif virus>1499:
                base.SetYourSignal(">1499")
        elif virus>499:
                base.SetYourSignal(">499")
        elif virus>299:
                base.SetYourSignal(">299")
        elif virus>199:
                base.SetYourSignal(">199")
        elif virus>99:
                base.SetYourSignal(">99")
        
        if virus>6000:
                if base.GetElixir()>300:
                        base.create_robot("Time to win")
                base.SetYourSignal("Time to Attack")
        if ActBase.counter<81:
                if base.GetElixir()>700:
                        base.create_robot('')
        if ActBase.counter>80:
                if base.GetElixir()>500:
                        base.create_robot('')
        
        if base.GetElixir() > 299:
                if brght=="enemy" or bleft=="enemy" or bup=="enemy" or bdown=="enemy" or bnw=="enemy" or bne=="enemy" or bse=="enemy" or bsw=="enemy":
                        if virus>1499:
                                base.DeployVirus(1500)
                        elif virus>999:
                                base.DeployVirus(1000)
                        elif virus>499:
                                base.DeployVirus(500)
                        elif virus>199:
                                base.DeployVirus(200)
                        else :
                                base.DeployVirus(100)
        return
ActBase.counter = 0 


def ActRobot(robot):
        right = robot.investigate_right();
        left = robot.investigate_left();
        up = robot.investigate_up();
        down = robot.investigate_down();
        nw = robot.investigate_nw();
        ne = robot.investigate_ne();
        se = robot.investigate_se();
        sw = robot.investigate_sw();
        currentsignal = robot.GetCurrentBaseSignal();
        initialsignal = robot.GetInitialSignal()
        a,b = robot.GetPosition()
        int(a); int(b)
        global stratazy
        ActRobot.counter+=1
        if x>15:
                if a==x-1 and b==y :
                        if right=="friend-base":
                                stratazy=4
                        if left=="friend-base":
                                stratazy=2
        if x<15:
                if a==x+1 and b==y :
                        if right=="friend-base":
                                stratazy=4
                        if left=="friend-base":
                                stratazy=2
        
        
        if currentsignal =="Time to Attack":
                if initialsignal=="Time to win":
                        return(2)
                if right == "enemy":
                        robot.DeployVirus(800)
                elif left == "enemy":
                        robot.DeployVirus(800)
                elif up == "enemy":
                        robot.DeployVirus(800)
                elif down == "enemy":
                        robot.DeployVirus(800)
                elif nw == "enemy":
                        robot.DeployVirus(800)
                elif ne == "enemy":
                        robot.DeployVirus(800)
                elif se == "enemy":
                        robot.DeployVirus(800)
                elif sw == "enemy":
                        robot.DeployVirus(800)
                        
                if right == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif left == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif up == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif down == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif nw == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif ne == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif se == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                elif sw == "enemy-base":
                        robot.DeployVirus(4000)
                        return(0)
                return (int(stratazy))
        
        if right == "friend":
                return(4)
        elif left == "friend":
                return(2)
        elif up == "friend":
                return(3)
        elif down == "friend":
                return(1)
        elif nw == "friend":
                return(2)
        elif ne == "friend":
                return(4)
        elif se == "friend":
                return(4)
        elif sw == "friend":
                return(2)
        
        if ActRobot.counter<2001:
                
                if right == "enemy" :
                        robot.DeployVirus(200)
                        return(4)
                elif left == "enemy":
                        robot.DeployVirus(200)
                        return(2)
                elif up == "enemy":
                        robot.DeployVirus(200)
                        return(3)
                elif down == "enemy":
                        robot.DeployVirus(200)
                        return(1)
                elif nw == "enemy":
                        robot.DeployVirus(200)
                        return(2)
                elif ne == "enemy":
                        robot.DeployVirus(200)
                        return(4)
                elif se == "enemy":
                        robot.DeployVirus(200)
                        return(4)
                elif sw == "enemy":
                        robot.DeployVirus(200)
                        return(2)
        
        
        if ActRobot.counter>2000:
                if right == "enemy" and left != "enemy-base" and up != "enemy-base" and down!= "enemy-base" and ne != "enemy-base" and nw != "enemy-base" and se != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(4)
                elif left == "enemy" and right != "enemy-base" and up != "enemy-base" and down!= "enemy-base" and ne != "enemy-base" and nw != "enemy-base" and se != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(2)
                elif up == "enemy" and left != "enemy-base" and right != "enemy-base" and down!= "enemy-base" and ne != "enemy-base" and nw != "enemy-base" and se != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(3)
                elif down == "enemy" and left != "enemy-base" and up != "enemy-base" and right!= "enemy-base" and ne != "enemy-base" and nw != "enemy-base" and se != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(1)
                elif nw == "enemy" and left != "enemy-base" and up != "enemy-base" and down!= "enemy-base" and ne != "enemy-base" and right != "enemy-base" and se != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(2)
                elif ne == "enemy" and left != "enemy-base" and up != "enemy-base" and down!= "enemy-base" and right != "enemy-base" and nw != "enemy-base" and se != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(4)
                elif se == "enemy" and left != "enemy-base" and up != "enemy-base" and down!= "enemy-base" and ne != "enemy-base" and nw != "enemy-base" and right != "enemy-base" and sw != "enemy-base":
                        robot.DeployVirus(800)
                        return(4)
                elif sw == "enemy" and left != "enemy-base" and up != "enemy-base" and down!= "enemy-base" and ne != "enemy-base" and nw != "enemy-base" and se != "enemy-base" and right != "enemy-base":
                        robot.DeployVirus(800)
                        return(2)
                
        if right == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)

        elif left == "enemy-base":
                if currentsignal==">3999":  
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" : 
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
                        
        elif up == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
        elif down == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
        elif nw == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
        elif ne == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
        elif se == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
        elif sw == "enemy-base":
                if currentsignal==">3999":
                        robot.DeployVirus(4000)
                        return(0)
                elif currentsignal==">1499":
                        robot.DeployVirus(1500)
                        return(0)
                elif currentsignal==">499" :
                        robot.DeployVirus(500)
                        return(0)
                elif currentsignal==">299":
                        robot.DeployVirus(300)
                        return(0)
                elif currentsignal==">199":
                        robot.DeployVirus(200)
                        return(0)
                elif currentsignal==">99":
                        robot.DeployVirus(100)
                        return(0)
                else:
                        robot.DeployVirus(50)
                        return(0)
                
        return randint(1,4)
ActRobot.counter=0