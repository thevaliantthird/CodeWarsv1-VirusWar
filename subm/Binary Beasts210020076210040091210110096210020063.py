from random import randint

def enemy_base_loc(x, y):
        if x < 10:
                ebx = "0" + str(x)
        else:
                ebx = str(x)
        if y < 10:
                eby = "0" + str(y)
        else:
                eby = str(y)
        enemy_base = "base" + ebx + eby
        return enemy_base


def staynearme(x, y, bx, by):
        if x == bx and y == by:
                return 0
        if x < bx:
                return 2
        elif x > bx:
                return 4
        if y < by:
                return 3
        elif y > by:
                return 1


def ActBase(base):

        ax,by = base.GetPosition()
        ActBase.ax = ax
        ActBase.by = by
    
        if base.GetElixir() > 1850:
                base.create_robot('1')
        elif base.GetElixir() <= 1850 and base.GetElixir() > 1700:
                base.create_robot('1_resource')
        elif base.GetElixir()> 1550 and base.GetElixir()<=1700:
                base.create_robot('2')
        elif base.GetElixir() <= 1550 and base.GetElixir() > 1400:
                base.create_robot('2_resource')
        elif base.GetElixir()>1250 and base.GetElixir()<= 1400:
                base.create_robot('3')
        elif base.GetElixir() <= 1250 and base.GetElixir() > 1100:
                base.create_robot('3_resource')
        elif base.GetElixir()>950 and base.GetElixir()<= 1100:
                base.create_robot('4')
        elif base.GetElixir() <= 950 and base.GetElixir() > 800:
                base.create_robot('4_resource')
        up = base.investigate_up()
        down = base.investigate_down()
        right = base.investigate_right()
        left = base.investigate_left()
        ne = base.investigate_ne()
        nw = base.investigate_nw()
        se = base.investigate_se()
        sw = base.investigate_sw()
        if up=='enemy' or down == "enemy" or left == "enemy" or right == "enemy" or ne == "enemy" or nw == "enemy" or se == "enemy" or sw == "enemy":
                base.DeployVirus(base.GetVirus())
        if base.GetElixir() > 750 and base.GetElixir() <=800:
                base.create_robot('staynearme_ne')
        if base.GetElixir() > 700 and base.GetElixir() <=750:
                base.create_robot('staynearme_nw')
        if base.GetElixir() > 650 and base.GetElixir() <=700:
                base.create_robot('staynearme_sw')
        if base.GetElixir() > 600 and base.GetElixir() <=650:
                base.create_robot('staynearme_se')
        if base.GetElixir()<=600 and base.GetElixir()>550:
                base.create_robot('staynearme_n')
        if base.GetElixir()<=550 and base.GetElixir()>500:
                base.create_robot('staynearme_s')
        if base.GetElixir()<=500 and base.GetElixir()>450:
                base.create_robot('staynearme_e')
        if base.GetElixir()<=450 and base.GetElixir()>400:
                base.create_robot('staynearme_w')

        L = base.GetListOfSignals()
        ActBase.no = len(L)
        for l in L:
                if len(l) > 0:
                        if l[0:4] == "base":
                                base.SetYourSignal(l)
                        return


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
        i=1
        j=2
        initial_signal = ['1','2','3','4']
        resource = ['1_resource','2_resource','3_resource','4_resource']
        stay_near_me = ['staynearme_n', 'staynearme_s', 'staynearme_e', 'staynearme_w', 'staynearme_ne', 'staynearme_nw', 'staynearme_se', 'staynearme_sw']
        robot.setSignal('')

        no_of_bots = ActBase.no

        canvas_x = (robot.GetDimensionX())/2
        canvas_y = (robot.GetDimensionY())/2
        new_dist = abs(canvas_x-x) + abs(canvas_y-y)

        if robot.GetInitialSignal() in initial_signal or robot.GetInitialSignal() in resource:
                if up == 'enemy' or down == "enemy" or left == "enemy" or right == "enemy" or ne == "enemy" or nw == "enemy" or se == "enemy" or sw == "enemy":
                        if robot.GetVirus() > 2000:
                                robot.DeployVirus(800)
                        else:
                                robot.DeployVirus(400)
                elif up == 'enemy-base':
                        robot.setSignal(enemy_base_loc(x, y-1))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif down == "enemy-base":
                        robot.setSignal(enemy_base_loc(x, y+1))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif left == "enemy-base":
                        robot.setSignal(enemy_base_loc(x-1, y))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif right == "enemy-base":
                        robot.setSignal(enemy_base_loc(x+1, y))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif ne == "enemy-base":
                        robot.setSignal(enemy_base_loc(x+1, y-1))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif nw == "enemy-base":
                        robot.setSignal(enemy_base_loc(x-1, y-1))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif se == "enemy-base":
                        robot.setSignal(enemy_base_loc(x+1, y+1))
                        robot.DeployVirus(robot.GetVirus()*0.6)
                elif sw == "enemy-base":
                        robot.setSignal(enemy_base_loc(x-1, y+1))
                        robot.DeployVirus(robot.GetVirus()*0.6)

                #Also add some other kind of signals like enemy location and unsearched tiles
                #try to make a strategy to find the enemy base

                if len(robot.GetCurrentBaseSignal())>0 and robot.GetInitialSignal() in initial_signal:
                        s = robot.GetCurrentBaseSignal()[4:]
                        sx = int(s[0:2])
                        sy = int(s[2:4])
                        dist = abs(sx-x) + abs(sy-y)
                        if dist==1:
                                robot.DeployVirus(robot.GetVirus()*0.75)
                                return 0
                        if x < sx:
                                return 2
                        if x > sx:
                                return 4
                        if y < sy :
                                return 3
                        if y > sy:
                                return 1
                elif len(robot.GetCurrentBaseSignal())>0 and robot.GetInitialSignal() in resource:
                        return randint(1,4)
                
                if robot.GetInitialSignal() == '1' or robot.GetInitialSignal()=='1_resource':
                        if new_dist == 0 and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if x <canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if x>= canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return 4
                        if y< canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if y >= canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return 1

                if robot.GetInitialSignal() == '2' or robot.GetInitialSignal()=='2_resource':
                        if new_dist == 0 and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if x <=canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return 2
                        if x>canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if y<canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if y >= canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return 1

                if robot.GetInitialSignal() == '3' or robot.GetInitialSignal()=='3_resource':
                        if new_dist == 0 and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if x <canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if x>=canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return 4
                        if y<=canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return 3
                        if y > canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)

                if robot.GetInitialSignal() == '4' or robot.GetInitialSignal()=='4_resource':
                        if new_dist == 0 and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if x <=canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return 2
                        if x>canvas_x and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)
                        if y<=canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return 3
                        if y > canvas_y and len(robot.GetCurrentBaseSignal())==0:
                                return randint(1,4)

        elif robot.GetInitialSignal() in stay_near_me:
                if down=='enemy' or up=='enemy' or left=='enemy' or right=='enemy' or ne=='enemy' or nw=='enemy' or se=='enemy' or sw=='enemy':
                        if no_of_bots <= 12 and robot.GetVirus() > 8000:
                                robot.DeployVirus(4000)
                        else:
                                robot.DeployVirus(2000)

                if robot.GetInitialSignal() == 'staynearme_sw':
                        return staynearme(x, y, ActBase.ax+i, ActBase.by+i)

                elif robot.GetInitialSignal() == 'staynearme_ne':
                        return staynearme(x, y, ActBase.ax+i, ActBase.by-i)
                
                elif robot.GetInitialSignal() == 'staynearme_nw':
                        return staynearme(x, y, ActBase.ax-i, ActBase.by-i)

                elif robot.GetInitialSignal() == 'staynearme_se':
                        return staynearme(x, y, ActBase.ax-i, ActBase.by+i)   
                
                elif robot.GetInitialSignal() == "staynearme_n":
                        return staynearme(x, y, ActBase.ax, ActBase.by-j)
                
                elif robot.GetInitialSignal() == "staynearme_s":
                        return staynearme(x, y, ActBase.ax, ActBase.by+j)
                
                elif robot.GetInitialSignal() == "staynearme_w":
                        return staynearme(x, y, ActBase.ax-j, ActBase.by)
                
                elif robot.GetInitialSignal() == "staynearme_e":
                        return staynearme(x, y, ActBase.ax+j, ActBase.by)
