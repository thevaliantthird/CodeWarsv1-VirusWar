from random import randint
from random import choice
#firstsubmission
def CoordStr(x,y): # x,y<100
    if x<10:
        xs='0'+str(x)
    else:
        xs=str(x)
    if y<10:
        ys='0'+str(y)
    else:
        ys=str(y)
    return xs+ys

def randmoves(robot): # for attack bots
    rosig=robot.GetYourSignal()
    M=[1,2,3,4]
    if robot.investigate_up()=='wall':
        M.remove(1)
    elif robot.investigate_down()=='wall':
        M.remove(3)
    if robot.investigate_left()=='wall':
        M.remove(4)
    elif robot.investigate_right()=='wall':
        M.remove(2)
    if 'm' in rosig:
        ind=rosig.index('m')+1
        x=int(rosig[ind])+2
        if x>4: x=x-4
        if x in M:
            M.remove(x)
        move=choice(M)
        robot.setSignal(rosig[:ind]+str(move)+rosig[ind+1:])
    else:
        move=choice(M)
        robot.setSignal(rosig+'m'+str(move))

    return move

def rand_roam(bot_x, bot_y, base_x, base_y, radius): #for defense bots
    if abs(base_x - bot_x) <= radius and abs(base_y - bot_y) <= radius:
        return(randint(1, 4))
    if bot_x - base_x > radius:
        return 4
    elif bot_x - base_x < -radius:
        return 2
    if bot_y - base_y > radius:
        return 1
    elif bot_y - base_y < -radius:
        return 3	

def WalkTo(x_r,y_r,x_d,y_d,randomiser):
    if randomiser:
        pstring='1234'
    else:
        pstring='0'
    if x_r<x_d:
        pstring+='2'*(x_d-x_r) 
    else:
        pstring+='4'*(x_r-x_d)
    if y_r>y_d:
        pstring+='1'*(y_r-y_d)
    else:
        pstring+='3'*(y_d-y_r)
    return int(choice(pstring))

def Refuel(robot, base_x, base_y, bot_x, bot_y, id):
    # will need base coordinates base_x,base_y and robot coordinates bot_x, bot_y
    up = robot.investigate_up()
    down = robot.investigate_down()
    left = robot.investigate_left()
    right = robot.investigate_right()
    elixir = robot.GetElixir()
    elixirmin = 50
    elixirmax = 500
    
    #elixir < elixirmin or elixir < elixirmax

    X, Y = robot.GetDimensionX(), robot.GetDimensionY()

    if elixir < elixirmin:
        if id%2 == 0:	#Clockwise scanners
            i = id//2
            if (base_x<X/2 and base_y<Y/2):
                if (bot_x==base_x and not(bot_y==2+3*i)):
                    if (bot_y<2+3*i and up != 'wall'):
                        return 1	#move up
                    else:
                        return 3	#move down
                elif (bot_y==2+3*i and bot_x<X+2-3*i and right != 'wall'):
                    return 2	 #move right
                elif (bot_x==X+2-3*i and down != 'wall'):
                    return 3	#move down
    
            elif (base_x>= X/2 and base_y<Y/2):
                if (bot_y==base_x and not(bot_x==X+2-3*i)):
                    if (bot_x<X+2-3*i and right != 'wall'):
                        return 2	#move right
                    else:
                        return 4	#move left
                elif (bot_x==X+2-3*i and bot_y<Y+2-3*i and down != 'wall'):
                    return 3	 #move down
                elif (bot_y==Y+2-3*i and left != 'wall'):
                    return 4	#move left
            
            elif (base_x<X/2 and base_y>=Y/2):
                if (bot_y==base_y and not(bot_x==2+3*i)):
                    if (bot_x<2+3*i and right != 'wall'):
                        return 2	#move right
                    else:
                        return 4	#move left
                elif (bot_x==2+3*i and bot_y<2+3*i and up != 'wall'):
                    return 1	 #move up
                elif (bot_y==2+3*i and right != 'wall'):
                    return 2	#move right
            
            elif (base_x>=X/2 and base_y>=Y/2):
                if (bot_x==base_x and not(bot_y==Y+2-3*i)):
                    if (bot_y<Y+2-3*i and down != 'wall'):
                        return 3	#move down
                    else:
                        return 1	#move up
                elif (bot_y==Y+2-3*i and bot_x>2+3*i and left != 'wall'):
                    return 4	 #move left
                elif (bot_x==2+3*i and up != 'wall'):
                    return 1	#move up
                    
        else:   #Anticlockwise scanners
            i = id//2
            if (base_x<X/2 and base_y<Y/2):
                if (bot_y==base_y and not(bot_x==2+3*i)):
                    if (bot_x<2+3*i and right != 'wall'):
                        return 2	#move right
                    else:
                         return 4	#move left
                elif (bot_x==2+3*i and bot_y<Y+2-3*i and down != 'wall'):
                    return 3	 #move down
                elif (bot_y==Y+2-3*i and right != 'wall'):
                    return 2	#move right
    
            elif (base_x>= X/2 and base_y<Y/2):
                if (bot_x==base_x and not(bot_y==2+3*i)):
                    if (bot_y<2+3*i):
                        return 1	#move up
                    else:
                         return 3	#move down
                elif (bot_y==2+3*i and bot_x>2+3*i):
                    return 4	 #move left
                elif (bot_x==2+3*i):
                    return 3	#move down
            
            elif (base_x<X/2 and base_y>=Y/2):
                if (bot_x==base_x and not(bot_y==Y+2-3*i)):
                    if (bot_y<Y+2-3*i and down != 'wall'):
                        return 3	#move down
                    else:
                         return 1	#move up
                elif (bot_y==Y+2-3*i and bot_x<X+2-3*i and right != 'wall'):
                    return 2	 #move right
                elif (bot_x==X+2-3*i and up != 'wall'):
                    return 1	#move up
            
            elif (base_x>=X/2 and base_y>=Y/2):
                if (bot_y==base_y and not(bot_x==X+2-3*i)):
                    if (bot_x<X+2-3*i and right != 'wall'):
                        return 2	#move right
                    else:
                         return 4	#move left
                elif (bot_x==X+2-3*i and bot_y>2+3*i and up != 'wall'):
                    return 1	 #move up
                elif (bot_y==2+3*i and left != 'wall'):
                    return 4	#move left
        
        return randint(1,4)
        
    else:
        #The center of the region of patrol (patrol_x, patrol_y) should be the area right next to our base along the line joining our base and enemy base. In most cases this will be the lien joining our base with centre.
        patrol_x = (0.70*base_x + 0.3*(X/2)) 
        patrol_y = (0.70*base_y + 0.3*(Y/2))
        if abs(patrol_x - bot_x) <= 3 and abs(patrol_y - bot_y) <= 3 :
            return randint(1, 4)
        if bot_x - patrol_x > 3:
            return 4
        elif bot_x - patrol_x < -3:
            return 2
        if bot_y - patrol_y > 3:
            return 1
        elif bot_y - patrol_y < -3:
            return 3

def Form(robot, id, base_x, base_y, bot_x, bot_y, robsig, basesig):
                    
    if id == 1 or id == 2:
        if bot_x == base_x-1 and bot_y == base_y-1:
            robot.setSignal(robsig+'ad')      #'a'+'d'
                
            return 0
        if bot_x < base_x-1:
            return 2
        elif bot_x > base_x-1:
            return 4
        if bot_y < base_y-1:
            return 3
        elif bot_y > base_y-1:
            return 1
    elif id == 3 or id == 4:
        if bot_x == base_x+1 and bot_y == base_y-1:
            
            robot.setSignal(robsig+'ao')     #'a'+'o'
            return 0
        if bot_x < base_x+1:
            return 2
        elif bot_x > base_x+1:
            return 4
        if bot_y < base_y-1:
            return 3
        elif bot_y > base_y-1:
            return 1
    elif id == 5 or id == 6:
        if bot_x == base_x+1 and bot_y == base_y+1:
            
            robot.setSignal(robsig+'an')          #'a'+'n'
            return 0
        if bot_x < base_x+1:
            return 2
        elif bot_x > base_x+1:
            return 4
        if bot_y < base_y+1:
            return 3
        elif bot_y > base_y+1:
            return 1
    elif id == 7 or id == 8:
        if bot_x == base_x-1 and bot_y == base_y+1:
                
            robot.setSignal(robsig+'ae')              #'a'+'e'
            return 0
        if bot_x < base_x-1:
            return 2
        elif bot_x > base_x-1:
            return 4
        if bot_y < base_y+1:
            return 3
        elif bot_y > base_y+1:
            return 1
    if 'H' in basesig and not 'b' in basesig:
        if bot_x < base_x-1:
            return 2
        elif bot_x > base_x-1:
            return 4
        if bot_y < base_y+1:
            return 3
        elif bot_y > base_y+1:
            return 1           						

def Defence(robot,id):
    robsig=robot.GetYourSignal()
    basesig=robot.GetCurrentBaseSignal()
    if robsig=='': 
        robsig= basesig[3:7]
        robot.setSignal(robsig)
    base_x=int(robsig[:2])
    base_y=int(robsig[2:4])
    x_r,y_r=robot.GetPosition()
    if 'c' in basesig:
        c_ind = basesig.find('c')
        num = int(basesig[c_ind + 1])
        if num == 1:
            if id == 9:
                id = 1
        if num == 3:
            if id == 10:
                id = 3
        if num == 5:
            if id == 11:
                id == 5                

    
    if 'a' in basesig:
        if id <= 8: 
            if not ('f' in basesig):
                return Form(robot, id, base_x, base_y, x_r, y_r, robsig, basesig)
            elif 'f' in basesig:
                t_ind = basesig.find('t')
                ticks = 0
                if(t_ind != -1):
                    ticks = int(basesig[t_ind + 1])
                if not ticks >= 5:
                    robot.setSignal('aft' + str(ticks))
                else:
                    robot.setSignal('r')
                    ticks = 0	 	
        elif id >= 9:
            size_x=robot.GetDimensionX()
            size_y=robot.GetDimensionY()            
            if base_x >= size_x/2:
                if base_y >= size_y/2:
                    return rand_roam(x_r, y_r, (base_x + size_x)/2, (base_y + size_y)/2, 5)
                elif base_y < size_y/2:
                    return rand_roam(x_r, y_r, (base_x + size_x)/2, (base_y)/2, 5)
            elif base_x < size_x/2:
                if base_y >= size_y/2:
                    return rand_roam(x_r, y_r, (base_x)/2, (base_y + size_y)/2, 5)
                elif base_y < size_y/2:
                    return rand_roam(x_r, y_r, (base_x)/2, (base_y)/2, 5)
    elif ('H' in basesig):   
        return WalkTo(x_r, y_r, base_x, base_y,1)
    else:
        return Refuel(robot, base_x, base_y, x_r, y_r, id)


def VirusPolicy(robot,typ):
    viral=robot.GetVirus()
    up = robot.investigate_up()
    down = robot.investigate_down()
    left = robot.investigate_left()
    right = robot.investigate_right()
    ne = robot.investigate_ne()
    nw = robot.investigate_down()
    se = robot.investigate_left()
    sw = robot.investigate_right()
    locale=(up,down,left,right,ne,nw,se,sw)

    if 'enemy-base' in locale:
        robot.DeployVirus(viral)
    elif 'enemy' in locale:
        if typ=='d':
            robot.setSignal(robot.GetYourSignal()+'a')
        numen=locale.count('enemy')        
        if (numen>2 and robot.GetVirus()>2000):
            robot.DeployVirus(1600)	#alter the values
        elif robot.GetVirus()>5000 or typ=='d':
            robot.DeployVirus(2000)
        else:
            robot.DeployVirus(800)	#alter the values
    return locale  

def FirstPhaseM(robot,robsig,id): #~
    x_r,y_r=robot.GetPosition()
    baes=robot.GetCurrentBaseSignal()
    
    if len(robsig)==1:
        x_h=int(baes[3:5]) #home
        y_h=int(baes[5:7])
        X=robot.GetDimensionX()
        Y=robot.GetDimensionY()
        if robsig[0]=='0': robsig+=CoordStr(X-x_h-1,Y-y_h-1)
        elif robsig[0]=='1': robsig+=CoordStr(X-x_h-1,y_h)
        elif robsig[0]=='2': robsig+=CoordStr(x_h,Y-y_h-1)
    
    x_d=int(robsig[1:3])
    y_d=int(robsig[3:5])
    
    if robot.investigate_up()=='enemy-base': #rem--chk 
        robsig='b'+CoordStr(x_r,y_r-1)   
    elif robot.investigate_down()=='enemy-base':
        robsig='b'+CoordStr(x_r,y_r+1)       
    elif robot.investigate_left()=='enemy-base':
        robsig='b'+CoordStr(x_r-1,y_r)
    elif robot.investigate_right()=='enemy-base':
        robsig='b'+CoordStr(x_r+1,y_r) 
    elif robot.investigate_ne()=='enemy-base':
        robsig='b'+CoordStr(x_r+1,y_r-1)
    elif robot.investigate_nw()=='enemy-base':
        robsig='b'+CoordStr(x_r-1,y_r-1)
    elif robot.investigate_se()=='enemy-base':
        robsig='b'+CoordStr(x_r+1,y_r+1)
    elif robot.investigate_sw()=='enemy-base':
        robsig='b'+CoordStr(x_r-1,y_r+1)
    elif abs(x_d-x_r)+abs(y_d-y_r)<2:
        if '!' not in robsig: robsig+='!'
        #print("no")
        #print(robsig)
    #the movement defining code
    robot.setSignal(robsig)
    return WalkTo(x_r,y_r,x_d,y_d,1)

def SecondPhaseM(robot,robsig,id): #!
    x_r,y_r=robot.GetPosition()
    #insert base finding code
    if robot.investigate_up()=='enemy-base': #rem--chk 
        robot.setSignal('b'+CoordStr(x_r,y_r-1))
        return choice((2,4))     
    elif robot.investigate_down()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r,y_r+1))
        return choice((2,4))       
    elif robot.investigate_left()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r-1,y_r))
        return choice((1,3)) 
    elif robot.investigate_right()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r+1,y_r))
        return choice((1,3)) 
    elif robot.investigate_ne()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r+1,y_r-1))
        return choice((1,2))
    elif robot.investigate_nw()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r-1,y_r-1))
        return choice((1,4))
    elif robot.investigate_se()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r+1,y_r+1))
        return choice((3,2))
    elif robot.investigate_sw()=='enemy-base':
        robot.setSignal('b'+CoordStr(x_r-1,y_r+1))
        return choice((3,4))
       
    #the movement defining code
    baes=robot.GetCurrentBaseSignal()
    #print(robsig +'\t'+ baes)
    #try:
    if id%2==0:
        robsig=str(baes.index('~'))
    else:
        robsig=str(baes.rindex('~'))
    #except: robsig='0'

    robot.setSignal(robsig)  
    return randint(1,4)
    
def EndPhase(robot,typ,id):
    x_r,y_r=robot.GetPosition()
    baes=robot.GetCurrentBaseSignal()  
    x_d=int(baes[1:3]) #destination
    y_d=int(baes[3:5])
    

    if typ=='a':
        if abs(x_r-x_d)+abs(y_r-y_d)==1:
            #print('circling')
            if 2*robot.GetVirus()>robot.GetElixir():
                if x_r==x_d:
                    return choice((2,4))
                else:
                    return choice((1,3))
            else:
                if x_r>x_d : return 4
                elif x_r<x_d : return 2
                else: 
                    if y_r>y_d : return 1
                    else: return 3
        else :
            return WalkTo(x_r,y_r,x_d,y_d,0)
    elif typ=='m':
        if robot.GetElixir()>150:
            if abs(x_r-x_d)+abs(y_r-y_d)==1:
                if x_r==x_d:
                    return choice((2,4))
                else:
                    return choice((1,3))
            else :
                return WalkTo(x_r,y_r,x_d,y_d,0)
        else:
            return randmoves(robot)

def ActRobot(robot):
    #return 0
    typ=robot.GetInitialSignal()[0]
    id=int(robot.GetInitialSignal()[1:])
    basesig=robot.GetCurrentBaseSignal()
    #investigation
    locale = VirusPolicy(robot,typ) #(up,down,left,right,ne,nw,se,sw)
                                  #0-stay,1-up,2-right,3-down,4-left
    #movement    
    if typ=='d':
        return Defence(robot,id)
    elif basesig[0]=='b':
        #print('ok')
        return EndPhase(robot,typ,id) 
    elif basesig[0:3]=='!!!': return randint(1,4)
    elif typ=='a':       
        robsig=robot.GetYourSignal()
        if robsig=='':robsig=str(id%3)
        #print(basesig, robsig,id)
        if robsig[0]=='b': return randint(1,4)
        elif basesig[int(robsig[0])]=='~':
            return FirstPhaseM(robot,robsig,id)
        elif basesig[int(robsig[0])]=='!':
            #print("changed")
            return SecondPhaseM(robot,robsig,id)
    else:
        x_r,y_r=robot.GetPosition()
        if robot.investigate_up()=='enemy-base': #rem--chk 
            robot.setSignal('b'+CoordStr(x_r,y_r-1))
            return choice((2,4))     
        elif robot.investigate_down()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r,y_r+1))
            return choice((2,4))       
        elif robot.investigate_left()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r-1,y_r))
            return choice((1,3)) 
        elif robot.investigate_right()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r+1,y_r))
            return choice((1,3)) 
        elif robot.investigate_ne()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r+1,y_r-1))
            return choice((1,2))
        elif robot.investigate_nw()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r-1,y_r-1))
            return choice((1,4))
        elif robot.investigate_se()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r+1,y_r+1))
            return choice((3,2))
        elif robot.investigate_sw()=='enemy-base':
            robot.setSignal('b'+CoordStr(x_r-1,y_r+1))
            return choice((3,4))
        else:  return randint(1,4)

def ActBase(base):
    ##initialisation step
    if base.GetYourSignal()=='':
        minelix=100
        No_of_bots=(base.GetElixir()-minelix)//50  #imp!
        x_b,y_b=base.GetPosition()
        base.SetYourSignal('~~~'+CoordStr(x_b,y_b))#optimise later
        #botcreation
        
        for j in range(1,max(11,No_of_bots//4)+1):
            base.create_robot('d'+str(j))
        for i in range(No_of_bots//2):
            if base.GetElixir()>minelix: base.create_robot('a'+str(i))
        k=0
        while base.GetElixir() > minelix:
            base.create_robot('m'+str(k))  # defence capability ->more conservative with movement
            k+=1
        
    basesig=base.GetYourSignal()        
    AllSig=base.GetListOfSignals()
    #print(AllSig)
    done = [0, 0, 0, 0]
    d_count = 0
    o_count = 0
    n_count = 0
    e_count = 0
    for L in AllSig:
        if len(L)>0 and not(basesig[0]=='b'):
            if L[0]=='b':
                
                basesig=L[:5]+basesig[7:] #checkforerrors
                base.SetYourSignal(basesig)
                #print(basesig)
                continue
            elif '!' in L:
                basesig=basesig[:int(L[0])]+'!'+basesig[int(L[0])+1:]
                base.SetYourSignal(basesig)
                #print(basesig)
                #base.create_robot('f0')
        if 'a' in L and not ('a' in basesig):
            basesig += 'a'
        if ('d' in L):    #make sure that these characters dont appear in s anywhere else
            done[0] = 1
            d_count += 1
        if ('o' in L):    #make sure that these characters dont appear in s anywhere else
            done[1] = 1
            o_count += 1
        if ('n' in L):    #make sure that these characters dont appear in s anywhere else
            done[2] = 1
            n_count += 1
        if ('e' in L):    #make sure that these characters dont appear in s anywhere else
            done[3] = 1
            e_count += 1
        if 'f' in L and not ('f' in basesig):
            basesig += 'f'
        if 't' in L and not ('t' in basesig):    #here, ticks is a single digit number, to make it a double digit number, put a 0 in front of single digit and change the code
            index = L.find('t')
            ticks = int(L[index + 1])
            ticks += 1
            basesig += 't' + str(ticks)  
    if done==[1,1,1,1]:
        basesig += 'f'
    if 'a' in basesig:
        if not (d_count == 2):     #c is the symbol to change the id of a bot to 1
            basesig += 'c1'
        if not (o_count == 2):     #c is the symbol to change the id of a bot to 1
            basesig += 'c3'
        if not (n_count == 2):     #c is the symbol to change the id of a bot to 1
            basesig += 'c5'
        if not (e_count == 2):     #c is the symbol to change the id of a bot to 1
            basesig += 'c7'            

    if basesig[0:3]=='!!!':
        basesig='~~~'+ basesig[3:]

    enemies_near= (base.investigate_up()=='enemy')+(base.investigate_down()=='enemy')+(base.investigate_left()=='enemy')+(base.investigate_right()=='enemy')+(base.investigate_ne()=='enemy')+(base.investigate_nw()=='enemy')+(base.investigate_se()=='enemy')+(base.investigate_sw()=='enemy')    
    if enemies_near:
        base.DeployVirus(base.GetVirus()) 
        if 'H' in basesig:
            ind=basesig.index('H')+1
            basesig+=basesig[:ind]+str(max(9,2*enemies_near))+basesig[ind+1:]
        else:
            basesig+='H'+str(max(9,2*enemies_near))
    else:
        if 'H0' in basesig:
            ind=basesig.index('H')
            basesig=basesig[:ind]+basesig[ind+2:]
        elif 'H' in basesig:
            ind=basesig.index('H')+1
            basesig=basesig[:ind]+str(int(basesig[ind])-1)+basesig[ind+1:]
    #print(basesig)
    base.SetYourSignal(basesig)

    return
