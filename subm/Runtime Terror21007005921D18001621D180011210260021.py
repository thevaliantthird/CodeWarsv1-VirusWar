from random import randint

def ActRobot(robot):
        
        canvas_x=robot.GetDimensionX()
        canvas_y=robot.GetDimensionY() 
        up = robot.investigate_up()
        down = robot.investigate_down()
        right = robot.investigate_right()
        left = robot.investigate_left()
        nw = robot.investigate_nw()
        ne = robot.investigate_ne()
        sw = robot.investigate_sw()
        se = robot.investigate_se()
        rx,ry=robot.GetPosition()
        str_rx = str(rx)
        if rx < 10:
                str_rx = '0' + str(rx)
        str_ry = str(ry)
        if ry < 10:
                str_ry = '0' + str(ry)
        inisig = robot.GetInitialSignal()
        fb_x = int(inisig[0:2])
        fb_y = int(inisig[2:4])
        peb_x = canvas_x - fb_x
        peb_y = canvas_y - fb_y
        role = inisig[9]
        enemy_near = False
        if (up == 'enemy' or down == 'enemy' or right == 'enemy' or left == 'enemy' or nw == 'enemy' or ne == 'enemy' or sw == 'enemy' or se == 'enemy') :
                enemy_near = True
        if enemy_near:
                if robot.GetVirus() > 5000:
                        robot.DeployVirus(800)
                elif robot.GetVirus() > 2000:
                        robot.DeployVirus(320)
                else:
                        robot.DeployVirus(robot.GetVirus()*0.16)

        time = 0
        cbsig = ''
        rc = 'Y'
        at_part = 'NNNN'
        df_part = 'NNNN'
        d_time = 'S'
        strtot_elx = '000'
        alert = 'N'
        if len(robot.GetCurrentBaseSignal()) > 0:
                cbsig = robot.GetCurrentBaseSignal()
                time = int(cbsig[10:14])
                rc = cbsig[9]
                at_part = cbsig[0:4]
                df_part = cbsig[4:8]
                d_time = cbsig[8]       
                strtot_elx = cbsig[15:18]
                alert = cbsig[14]
        if time == 0:
                elx_per = robot.GetElixir()
                if elx_per/5 < 9:
                        strelx_per = '0' + str(int(elx_per/5))
                else:
                        strelx_per = str(int(elx_per/5))
        else:
                strelx_per = cbsig[18:20]
                
        strt = str(time + 1)
        if time + 1 < 10:
                strt = '000' + str(time + 1)
        elif time + 1 < 100:
                strt = '00' + str(time + 1)
        elif time + 1 < 1000:
                strt = '0' + str(time + 1)
        
        robot.setSignal(at_part + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)

# EXPANSION

        if 10 < time < 15 + (abs(peb_x - fb_x) + abs(peb_y - fb_y))/8 and role != 'W' :     #Good for 20 unit horizontal distance  10-15
                one = peb_y <= fb_y
                two = peb_x >= fb_x
                three = peb_y >= fb_y
                four = peb_x <= fb_x
                                                                                   
                if (ry-fb_y-rx+fb_x)<0 and (ry-fb_y+rx-fb_x)<0 and one:
                        return 1
                elif (ry-fb_y-rx+fb_x)>0 and (ry-fb_y+rx-fb_x)>0 and three:
                        return 3
                elif (ry-fb_y-rx+fb_x)<0 and (ry-fb_y+rx-fb_x)>0 and two:
                        return 2
                elif (ry-fb_y-rx+fb_x)>0 and (ry-fb_y+rx-fb_x)<0 and four:
                        return 4



# DETECTING ENEMY IN OUR PREMISES

        if (abs(rx - fb_x) < 10 and abs(ry - fb_y) < 10):               #original 5
                if enemy_near:
                        robot.DeployVirus(320)
                        if time < 50:
                                d_time = 'A'
                        robot.setSignal(at_part + str_rx + str_ry + d_time + 'N' + strt + role + strtot_elx + strelx_per)
        

# ATTACK 
       
        if cbsig[0:4] != 'NNNN' and robot.GetVirus() > 500 and role != 'W':  
                eb_x = int(cbsig[0:2])
                eb_y = int(cbsig[2:4])
                if (rx > eb_x + 1):
                        return 4
                if (rx < eb_x - 1):
                        return 2
                if (ry > eb_y + 1):
                        return 1
                if (ry < eb_y - 1):
                        return 3
                if (abs(rx - eb_x) <= 1 and abs(ry - eb_y) <= 1):
                        robot.DeployVirus(robot.GetVirus()*0.75)

                       
# DISCLOSING ENEMY LOCATION

                
        if up == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x<10:
                                strx = '0' + str(x)
                        else:
                                strx = str(x)
                        if y-1<10:
                                stry = '0' + str(y-1)
                        else:
                                stry = str(y-1)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 2
        elif down == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x<10:
                                strx = '0' + str(x)
                        else:
                                strx = str(x)
                        if y+1<10:
                                stry = '0' + str(y+1)
                        else:
                                stry = str(y+1)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 4
        elif right == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x+1<10:
                                strx = '0' + str(x+1)
                        else:
                                strx = str(x+1)
                        if y<10:
                                stry = '0' + str(y)
                        else:
                                stry = str(y)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 3
        elif left == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x-1<10:
                                strx = '0' + str(x-1)
                        else:
                                strx = str(x-1)
                        if y<10:
                                stry = '0' + str(y)
                        else:
                                stry = str(y)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 1
        elif nw == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x-1<10:
                                strx = '0' + str(x-1)
                        else:
                                strx = str(x-1)
                        if y-1<10:
                                stry = '0' + str(y-1)
                        else:
                                stry = str(y-1)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per) 
                robot.DeployVirus(0.05*robot.GetVirus())
                return 1
        elif ne == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x+1<10:
                                strx = '0' + str(x+1)
                        else:
                                strx = str(x+1)
                        if y-1<10:
                                stry = '0' + str(y-1)
                        else:
                                stry = str(y-1)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 2
        elif sw == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x-1<10:
                                strx = '0' + str(x-1)
                        else:
                                strx = str(x-1)
                        if y+1<10:
                                stry = '0' + str(y+1)
                        else:
                                stry = str(y+1)
                        robot.setSignal(strx + stry + df_part + d_time + rc + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 4
        elif se == 'enemy-base' and alert == 'N':
                if at_part == 'NNNN':
                        x,y=robot.GetPosition()
                        if x+1<10:
                                strx = '0' + str(x+1)
                        else:
                                strx = str(x+1)
                        if y+1<10:
                                stry = '0' + str(y+1)
                        else:
                                stry = str(y+1)
                        robot.setSignal(strx + stry + df_part + 'A' + 'N' + strt + role + strtot_elx + strelx_per)
                robot.DeployVirus(0.05*robot.GetVirus())
                return 3
        

# DEFENSE

        if cbsig[4:8] != 'NNNN':
                ex = int(cbsig[4:6])
                ey = int(cbsig[6:8])
                if  role == 'W' :#and (abs(rx - fb_x) < 4 and abs(ry - fb_y) < 4):
                        
                        if (ry > fb_y  + 1):
                                return 1
                        elif (ry < fb_y - 1):
                                return 3
                        if (rx > fb_x + 1):
                                return 4
                        elif (rx < fb_x - 1):
                                return 2
                        if enemy_near:
                                if robot.GetVirus()>1000:
                                        robot.DeployVirus(400)
                                else:
                                        robot.DeployVirus(0.20*robot.GetVirus())
                        if(0 < fb_x < canvas_x and 0 < fb_y < canvas_y):        
                                if (rx==fb_x+1 and ry==fb_y+1):
                                                return 4#randint(1,2)^2
                                elif (rx==fb_x+1 and ry==fb_y-1):
                                                return 3#randint(3,4)
                                elif (rx==fb_x-1 and ry==fb_y-1):
                                                return 2#randint(2,3)
                                elif (rx==fb_x-1 and ry==fb_y+1):
                                                return 1#randint(1,2)
                                elif rx==fb_x+1:
                                                return 3#randint(1,2)*2-1
                                elif rx==fb_x-1:
                                                return 1#randint(1,2)*2-1
                                elif ry==fb_y+1:
                                                return 4#randint(1,2)*2
                                elif ry==fb_y-1:
                                                return 2#randint(1,2)*2
                        else:
                                return randint(1,4)
                if (abs(rx - ex) < 3 and abs(ry - ey) < 3)  or role == 'D':

                        if (ry > ey + 2):
                                return 1
                        elif (ry < ey - 2):
                                return 3
                        if (rx > ex + 2):
                                return 4
                        elif (rx < ex - 2):
                                return 2
                        if (abs(rx - ex) < 2 and abs(ry - ey) < 2):
                                if enemy_near and robot.GetVirus() > 1000:
                                        robot.DeployVirus(320)
                        return randint(1,4)
                        
                                                
                        

# RECONNAISSANCE       
        
        if  rc == 'Y' and role == 'R':   
                
                       
                if (abs(rx - fb_x) > 6  or abs(ry - fb_y) > 6):                         
                        if 40 < time < 50 + abs(peb_x - fb_x)  :
                                if (rx > peb_x ):
                                        return 4
                                elif (rx < peb_x):
                                        return 2
                                if (ry > fb_y):
                                        return 1
                                elif (ry < fb_y):
                                        return 3
                        if (60 + abs(peb_x - fb_x)) < time < (70 + abs(peb_x - fb_x) + abs(peb_y - fb_y)) :
                                if (ry > peb_y):
                                        return 1
                                elif (ry < peb_y):
                                        return 3
                                if (abs(rx - peb_x) < 6 and abs(ry - peb_y) < 6):
                                        if enemy_near:
                                                robot.DeployVirus(320)
                                        return randint(1,4)
                retreat_time = 70 + abs(peb_x - fb_x) + abs(peb_y - fb_y) + 20
                if (abs(rx - fb_x) > 6  or abs(ry - fb_y) > 6):
                        if retreat_time < time < (retreat_time + abs(peb_x - fb_x) + 10):
                                if (rx > fb_x):
                                        return 4
                                elif (rx < fb_x):
                                        return 2
                        if (retreat_time + abs(peb_x - fb_x)) + 20 < time < (retreat_time + abs(peb_x - fb_x) + 30 + abs(peb_y - fb_y)):
                                if (ry > fb_y + 5):                             
                                        return 1
                                elif (ry < fb_y - 5):
                                        return 3
                        
        
        return randint(1,4)         




def ActBase(base):
        
        L = base.GetListOfSignals()
        if len(L) == 0:
                strt = '0000'
                df_part = 'NNNN'
                at_part = 'NNNN'
                d_time = 'Z'
                alert = 'N'
                strelx_per = '00'
                tot_elx = base.GetElixir()
                if tot_elx/10 < 10:
                        strtot_elx = '00' + str(int(tot_elx/10))
                elif tot_elx/10 < 100:
                        strtot_elx = '0' + str(int(tot_elx/10))
                else:
                        strtot_elx = str(int(tot_elx/10))
        else:
                strtot_elx = L[0][15:18]
                strt = L[0][10:14]
                strelx_per = L[0][18:20]
        
        elx_per = int(strelx_per)*5
        tot_elx = int(strtot_elx)*10
        timeframe = int(strt)

        wall_rob_elx = 0.15*tot_elx                              
        min_elixir = 0.15*tot_elx
        def_rob_elx = 0.20*tot_elx
        rec_rob_elx = 0.35*tot_elx
        ext_rob_elx = 0.15*tot_elx

        alive_drobots = 0
        alive_wrobots = 0
        alive_rrobots = 0

        if len(L) == 0 :
                rc = 'Y'
        elif len(L) > 0 :
                for l in L:
                        if timeframe < 50 and l[9] == 'N' :           #50 works best for many even common idea for (680,200);(200,680)                         
                                rc = 'N'
                                break
                        else:
                                rc = l[9]

        for l in L:
                if l[14] == 'D':
                        alive_drobots +=1
                elif l[14] == 'R':
                        alive_rrobots += 1
                elif l[14] == 'W':
                        alive_wrobots +=1
        x,y = base.GetPosition()
        if x<10:
                strx = '0' + str(x)
        else:
                strx = str(x)
        if y<10:
                stry = '0' + str(y)
        else:
                stry = str(y)
        canvas_x=base.GetDimensionX()
        canvas_y=base.GetDimensionY()
        peb_x = canvas_x - x
        peb_y = canvas_y - y
        retreat_time = 40 + abs(peb_x - x) + abs(peb_y - y)
        
        while base.GetElixir() > tot_elx - rec_rob_elx:
                base.create_robot(strx + stry + strt + rc + 'R')
        while base.GetElixir() > tot_elx -(rec_rob_elx + def_rob_elx) :
                base.create_robot(strx + stry + strt + rc + 'D')
        while base.GetElixir() > tot_elx -(rec_rob_elx + def_rob_elx +wall_rob_elx):
                base.create_robot(strx + stry + strt + rc + 'W')
        #if timeframe > (50 + abs(peb_x - x)):
         #       while base.GetElixir() > min_elixir :
          #              base.create_robot(strx + stry + strt + rc + 'R')
        if len(L) > 0 and base.GetElixir() > min_elixir :
                init_drobots = def_rob_elx/elx_per
                init_rrobots = rec_rob_elx/elx_per
                init_wrobots = wall_rob_elx/elx_per
                
                if (alive_wrobots < init_wrobots):
                        base.create_robot(strx + stry + strt + rc + 'W')
                if (alive_drobots < init_drobots):
                        base.create_robot(strx + stry + strt + rc + 'D')
                if (alive_rrobots < init_rrobots):
                        base.create_robot(strx + stry + strt + rc + 'R')
        up = base.investigate_up()
        down = base.investigate_down()
        right = base.investigate_right()
        left = base.investigate_left()
        nw = base.investigate_nw()
        ne = base.investigate_ne()
        sw = base.investigate_sw()
        se = base.investigate_se()

# ENEMY DISCOVERED OR UNDER ATTACK

        for l in L:
                if len(l) > 0 and l[0:4] != 'NNNN':
                        eb_x = l[0:2]
                        eb_y = l[2:4]
                        at_part = eb_x + eb_y
                        break
                else:
                        at_part = l[0:4]
        for l in L:        
                if len(l) > 0 and l[4:8] != "NNNN":
                        if l[8] != 'Z':
                                df_part = l[4:8]
                                temp = ord(l[8])
                                temp +=1
                                d_time = chr(temp)
                        else:
                                df_part = 'NNNN'
                                d_time = 'Z'
                        break
                else:
                        df_part = l[4:8]
                        d_time = 'Z'
        if at_part != 'NNNN' and base.GetVirus()<50:
                alert = 'Y'
        else:
                alert = 'N'
# BASE COMPROMISED
        
        if (up == 'enemy' or down == 'enemy' or right == 'enemy' or left == 'enemy' or nw == 'enemy' or ne == 'enemy' or sw == 'enemy' or se == 'enemy') :
                base.DeployVirus(640)
                df_part = strx + stry
                
        base.SetYourSignal(at_part + df_part + d_time + rc + strt + alert + strtot_elx + strelx_per)               