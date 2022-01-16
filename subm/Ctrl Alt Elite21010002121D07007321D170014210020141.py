import random
from random import randint
def ActRobot(robot):
        #if u need variables create here or uncomment them      
        #corner=["NE","SW","SE","NW"]
        #side=["UP","DW","RT","LT"]
        #commands=[]
        #dic={0:'UP',1:'NW',2:'LT',3:"SW",4:"DW",5:"SE",6:"RT",7:"NE"}
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGCXCYT"; for blank keep space
                              01234567890123456789
                              t=reached yet? Y/N
                P=attacking or defense(A/D/Resorce collector)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''

        robotSignalOld=robot.GetYourSignal()
        if len(robotSignalOld)==0:
                robotSignalOld=robot.GetInitialSignal()
        #print(robotSignalOld)
        specialStructure="  "
        base_signal=robot.GetCurrentBaseSignal()
        (robotX,robotY) = robot.GetPosition()
        robotXstrNew=createStr(robotX)
        robotYstrNew=createStr(robotY)
        specialStructureX=-1
        specialStructureY=-1
        specialStructurestr="    " 
        isCollected=robotSignalOld[19]
        targetX=0
        targetY=0
        if robotSignalOld[6:10]!=" "*4:
                targetX=int(robotSignalOld[6:8])
                targetY=int(robotSignalOld[8:10])
        targetXNew=targetX
        targetYNew=targetY
        targetXStrNew=createStr(targetXNew)
        targetYStrNew=createStr(targetYNew)
        baseFoundEnemyBase=False
        enemyBaseX=""
        enemyBaseY=""
        shudAttack = False  
        position_performanceOld=robotSignalOld[12]
        position_performanceNew=position_performanceOld
        next_pos=-1
        specialPosition=robotSignalOld[4:6]
        if base_signal[4:8]!=" "*4:
                enemyBaseX=base_signal[4:6]
                enemyBaseY=base_signal[6:8]
                baseFoundEnemyBase=True

        #checking 8 directions
        l1=[]
        l1.append(robot.investigate_up())          
        l1.append(robot.investigate_nw())
        l1.append(robot.investigate_left())
        l1.append(robot.investigate_sw())   
        l1.append(robot.investigate_down())    
        l1.append(robot.investigate_se())
        l1.append(robot.investigate_right())
        l1.append(robot.investigate_ne())
        for i in range(0,8):
                #for finding enemy base
                if l1[i]=="enemy-base":
                        specialStructure="EB"
                        robot.DeployVirus(400)
                        (specialStructureX, specialStructureY, specialStructurestr) = generate(robot.GetPosition(),l1[i])
                        if not baseFoundEnemyBase:
                                enemyBaseX=createStr(specialStructureX)
                                enemyBaseY=createStr(specialStructureY)
                                baseFoundEnemyBase=True
                        shudAttack=True
                        next_pos=0
                        #position_performanceNew="A"
                        break

                if l1[i]=="enemy":
                        specialStructure="EN"                
        
        if specialStructure=="EN":
                robot.DeployVirus(400)
        
        #Attacking
        attrob=int(base_signal[8:10])
                
        
        if attrob<=5 and baseFoundEnemyBase and not shudAttack:    #archit look into this
                shudAttack=True
                targetXNew=int(enemyBaseX)
                targetYNew=int(enemyBaseY)
                targetXStrNew=createStr(targetXNew-1)
                targetYStrNew=createStr(targetYNew-1)
                next_pos=nextmovement(robotXstrNew+robotYstrNew,targetXStrNew+targetYStrNew)
                if specialStructurestr==" "*4:
                        specialStructurestr=enemyBaseY+enemyBaseX

        elif baseFoundEnemyBase:
                #xxs1=int(robotSignalOld[0:2])
                #yys1=int(robotSignalOld[2:4])
                specialStructureX=int(enemyBaseX)
                specialStructureY=int(enemyBaseY)
                targetXStrNew=createStr(specialStructureX-1)
                targetYStrNew=createStr(specialStructureY-1)
                xxdistance=abs(robotX-int(enemyBaseX))
                yydistance=abs(robotY-int(enemyBaseY))
                distance=max(xxdistance,yydistance)
                if distance<=20:
                        #send robot
                        shudAttack=True
        
        if shudAttack:
                if position_performanceNew==" ":
                        position_performanceNew="A"
                else:
                        position_performanceNew="A"
                specialStructure="EB"
                targetYStrNew=createStr(specialStructureY)
                targetXStrNew=createStr(specialStructureX)
                next_pos=nextmovement(robotXstrNew+robotYstrNew,targetXStrNew+targetYStrNew)
        
        if position_performanceNew=="R" and position_performanceOld=="R":
                next_pos=randint(1,4)
        #checking for enemy or b
        """
        #lets spiral out        
        if(position_performanceOld=="R")and not position_performanceNew=="A" :
                #targetYStrNew=createStr(targetY)
                #targetXStrNew=createStr(targetX)
                robotYstrNew=createStr(robotY)
                robotXstrNew=createStr(robotX)
                if robotX==targetX and robotY==targetY:
                        isCollected="Y"
                #next_pos=nextmovement(robotXstrNew+robotYstrNew,targetXStrNew+targetYStrNew)
                if isCollected=="N":
                        next_pos=nextmovement(robotXstrNew+robotYstrNew,targetXStrNew+targetYStrNew)
                
                position_performanceNew="R"
                if isCollected=="Y":
                        if robotX==targetX:
                                next_pos=2
                        elif robotX>targetX:
                                if robotY<=targetY:
                                        if (robotX-targetX)>(targetY-robotY):
                                                next_pos=3
                                        elif (robotX-targetX)==(targetY-robotY):
                                                next_pos=2
                                        else:
                                                next_pos=2
                                        
                                        if (targetY-robotY)==2 and robotX-targetX==2:
                                                isCollected="F"
                                        
                                else:
                                        if (robotX-targetX)>(robotY-targetY):
                                                next_pos=3
                                        else:
                                                next_pos=4
                        else:
                                if robotY<=targetY:
                                        if (targetX-robotX)>(targetY-robotY):
                                                next_pos=1
                                        elif (targetX-robotX)==(targetY-robotY):
                                                next_pos=2
                                        else:
                                                next_pos=2
                                        
                                else:
                                        if (robotX-targetX)>=(robotY-targetY):
                                                next_pos=1
                                        else:
                                                next_pos=4
        
        if isCollected=="F":
                cx=robot.GetDimensionX()
                cy=robot.GetDimensionY()
                targetXNew=random.choice(range(3,cx,5))
                targetYNew=random.choice(range(3,cy,5))
                targetXStrNew=createStr(targetXNew)
                targetYStrNew=createStr(targetYNew)
                isCollected="N"
        """       
        #resetting the signal        
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGURLRT"; for blank keep space
                              01234567890123456789
                              t=reached yet? Y/N
                P=attacking or defense(A/D/Resorce collector)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''
        robotXstrNew=createStr(robotX)
        robotYstrNew=createStr(robotY)
        

        
        
        x=robotXstrNew+robotYstrNew+specialPosition+targetXStrNew+targetYStrNew+specialStructure+position_performanceNew+robotSignalOld[13:19]+isCollected
        if next_pos!=-1:
                return next_pos
        if len(x)==20:
                robot.setSignal(x)
        else:
                robot.setSignal(x+" "*(20-len(x)))
        if position_performanceOld=="D" and robotSignalOld[15:19]=="0001" :
                possible=[0]
                direc=robotSignalOld[13:15]
                x=robotX
                y=robotY
                BX=int(base_signal[0:2])
                BY=int(base_signal[2:4])
                #robot.GetBasePosition() 
                distx=abs(BX-x)
                disty=abs(BY-y)
                if direc=="NE":
                        if distx<1 :
                                possible.append(2)
                        if disty<1:
                                possible.append(1)
                if direc=="NW":
                        if distx<1 :
                                possible.append(4)
                        if disty<1:
                                possible.append(1)                
                if direc=="SW":
                        if distx<1 :
                                possible.append(4)
                        if disty<1:
                                possible.append(3)                
                if direc=="SE":
                        if distx<1 :
                                possible.append(2)
                        if disty<1:
                                possible.append(3)
                if direc=="UP":
                        if disty<1:
                                possible.append(1)
                if direc=="DW":
                        if disty<1:
                                possible.append(3)
                if direc=="RT":
                        if distx<1:
                                possible.append(2)
                if direc=="LT":
                        if distx:
                                possible.append(4)                        
                next_pos= possible[randint(0,len(possible)-1)]     
                                        
                                
                       
        if position_performanceOld=="D" and not robotSignalOld[15:19]=="0001" :
                possible=[]
                direc=robotSignalOld[13:15]
                x=robotX
                y=robotY
                BX=int(base_signal[0:2])
                BY=int(base_signal[2:4]) 
                distx=abs(BX-x)
                disty=abs(BY-y)
                
                
                if direc=="NE":
                        if distx<2:
                                possible.append(2)
                        if disty<2:
                                possible.append(1)  
                        if 1<=distx<=2:
                                possible.append(4) 
                        if 1<=disty<=2:
                                possible.append(3)  

                if direc=="NW":
                        if distx<2:
                                possible.append(4)
                        if disty<2:
                                possible.append(1)  
                        if 1<=distx<=2:
                                possible.append(2) 
                        if 1<=disty<=2:
                                possible.append(3) 
                
                if direc=="SW":
                        if distx<2:
                                possible.append(4)
                        if disty<2:
                                possible.append(3)  
                        if 1<=distx<=2:
                                possible.append(2) 
                        if 1<=disty<=2:
                                possible.append(1) 
                if direc=="SE":
                        if distx<2:
                                possible.append(2)
                        if disty<2:
                                possible.append(3)  
                        if 1<=distx<=2:
                                possible.append(4) 
                        if 1<=disty<=2:
                                possible.append(1)                                                                     
                    
                next_pos= possible[randint(0,len(list(set(possible)))-1)]  
        not_possible=[]  
        canvas_y= robot.GetDimensionY()
        canvas_x= robot.GetDimensionX()
        x,y=robot.GetPosition()
        if x==1: 
                not_possible.append(4)
        if y==1:
                not_possible.append(1)    
        if  canvas_x-x==1:
                not_possible.append(2)
        if  canvas_y-y==1:
                not_possible.append(3)                    
        
        if next_pos in not_possible:
                poss=[]
                for i in range(1,4):
                        if i not in not_possible:
                                poss.append(i)
                next_pos=poss[randint(0,len(poss)-1)]          

                                        
        if position_performanceOld=="A" or position_performanceNew=="A":
                next_pos=nextmovement(robotXstrNew+robotYstrNew,enemyBaseX+enemyBaseY)
        if next_pos==-1:
                if targetYStrNew=="  ":
                        next_pos=randint(1,4)
                else:
                        next_pos=nextmovement(robotXstrNew+robotYstrNew,targetXStrNew+targetYStrNew)                      
        return next_pos

        # After checking for any enemy bots, move to target
        # Check ur previous designation if RC, enemy base found, A of friendly base less than threshold, dist less then chg ur status A
        ##Robot Signal="XXYYSPTXTYSSPTGRDDI"; for blank keep space

def generate(s,t):#s=robot position tuple t= direction
                a,b = s
                aN=0
                bN=0
                abstr=""
                if s=="UP":
                        aN=a
                        bN=b-1
                if s=="NE":
                        aN=a+1
                        bN=b-1
                if s=="RT":
                        aN=a+1
                        bN=b
                if s=="SE":
                        aN=a+1
                        bN=b+1
                if s=="DW":
                        aN=a
                        bN=b+1
                if s=="SW":
                        aN=a-1
                        bN=b+1
                if s=="LT":
                        aN=a-1
                        bN=b
                if s=="NW":
                        aN=a-1
                        bN=b-1
                if aN<10:
                        abstr+="0"+str(aN)
                if aN>9:
                        abstr+=str(aN)
                if bN<10:
                        abstr+="0"+str(bN)
                if bN>9:
                        abstr+=str(bN)
                return (aN,bN,abstr) 
#complete this Drashti & Suranjan
def isNear(s1,s2,r):#"XXYY"
        import math
        xs1=int(s1[0:2])
        ys1=int(s1[2:4])
        xs2=int(s2[0:2])
        ys2=int(s2[2:4])

        xdistance =abs(xs1-xs2)
        ydistance=abs(ys1-ys2)

        distance=max(xdistance,ydistance)
        
        
        if distance<=r :
                return True
        else:
                return False

def distancebtw(s1="0000",s2="0000"):#"XXYY"
        xs1=int(s1[0:2])
        ys1=int(s1[2:4])
        xs2=int(s2[0:2])
        ys2=int(s2[2:4])
        return max(abs(xs2-xs1),abs(ys1-ys2))

def nextmovement(s1,s2):#XXYY
                x=int(s1[0:2])
                y=int(s1[2:4])
                tx=int(s2[0:2])
                ty=int(s2[2:4])
                """
                distx1=tx-x
                disty1=ty-y
                distx = abs(tx-x) 
                disty = abs(ty-y)
                """
                poss=[0]
                

                if x < tx:
                        poss.append(2)
                if x > tx:
                        poss.append(4) 
                if y < ty:
                        poss.append(3)
                if y > ty:
                        poss.append(1)
                
                
                if len(poss)==1:
                        return poss[0]
                else:
                        return poss[randint(0,len(poss)-1)]
        #return 0

def createStr(i=0):
        s=""
        if i<10:
                s+="0"+str(i)
        if i>9:
                s+=str(i)
        return s

def ActBase(base):
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGCXCYT"; for blank keep space
                              01234567890123456789
                              t=reached yet? Y/N
                P=attacking or defense(A/D/Resorce collector)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''
        #creating signal for the first time
        
        canvasX=base.GetDimensionX()
        canvasY=base.GetDimensionY()
        canvaspartitions=[]
        istr=""
        jstr=""
        for i in range(3,canvasX,5):
                yrange=[]
                
                for j in range(3,canvasY,5):
                        if i<10:
                                istr="0"+str(i)
                        if i>9:
                                istr=str(i)
                        if j<10:
                                jstr="0"+str(j)
                        if j>9:
                                jstr=str(j)
                        yrange.append(istr+jstr)
                canvaspartitions.append(yrange)
        base_X_int,base_Y_int=base.GetPosition()
        base_X_str=""
        base_Y_str=""
        if base_X_int<10:
                base_X_str+="0"+str(base_X_int)
        if base_X_int>9:
                base_X_str+=str(base_X_int)
        if base_Y_int<10:
                base_Y_str+="0"+str(base_Y_int)
        if base_Y_int>9:
                base_Y_str+=str(base_Y_int)
        #creating signal
        if base.GetYourSignal()=="":
                base_X_int,base_Y_int=base.GetPosition()
                base_X_str=""
                base_Y_str=""
                if base_X_int<10:
                        base_X_str+="0"+str(base_X_int)
                if base_X_int>9:
                        base_X_str+=str(base_X_int)
                if base_Y_int<10:
                        base_Y_str+="0"+str(base_Y_int)
                if base_Y_int>9:
                        base_Y_str+=str(base_Y_int)
                base.SetYourSignal(base_X_str+base_Y_str+" "*10+"0"*4+"  ")
                #create initial bots under here
                elix=base.GetElixir()
                totalrobots=0
                t=1
                #Resource collectors
                if base_X_int>canvasX/2:
                        t=-1
                for i in range(0,len(canvaspartitions),t):
                        for j in range(0,len(canvaspartitions[i]),t):
                                if elix>500:
                                        base.create_robot(base_X_str+base_Y_str+"  "+canvaspartitions[i][j]+"  "+"R"+"  "+str(canvasX)+str(canvasY)+"N")
                                        #base.create_robot(base_X_str+base_Y_str+"  "+canvaspartitions[i][j]+"  "+"R"+"  "+"    "+"N")
                                        totalrobots+=1
                                        elix-=50
                '''
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"UP"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NW"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"LT"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SW"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"DW"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SE"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"RT"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NE"+"1510")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"UP"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NW"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"LT"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SW"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"DW"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"SE"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"RT"+"1005")
                base.create_robot(base_X_str+base_Y_str+"  "+" "*6+"R"+"NE"+"1005")               
                '''
                #DEFENSE
                #Review this with team
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"NW"+"0500"+"Y")
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"SW"+"0500"+"Y")
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"SE"+"0500"+"Y")
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"NE"+"0500"+"Y")
                
                totalrobots+=4
                
                
                 
                #creating signal
                base.SetYourSignal(base_X_str+base_Y_str+" "*10+"0"*4+str(totalrobots))
                
                #created bots
        
        #basic info recollection
        base_signal_Old=base.GetYourSignal()
        enemy_base_found=False
        if base_signal_Old[4:8]!=" "*4:
                enemy_base_found=True
        enemy_baseX=base_signal_Old[4:6]
        enemy_baseY=base_signal_Old[6:8]
        base_signal_New=""

        #timeframe renewal
        timestamp=base_signal_Old[14:18]
        timestamp_New=str(1+int(timestamp))
        

        robot_signal_list=base.GetListOfSignals()
        robot_signal_list_distance_enemybase=[]
        totalrobots=len(robot_signal_list)
        if enemy_base_found==False:
                for w in robot_signal_list:
                        if w[10:12]=="EB":
                                enemy_baseX=w[6:8]
                                enemy_baseY=w[8:10]
        
        #Recounting Status of Robots
        #Recounting Status of Robots
        #Recounting Status of Robots
        resource_collectors=0
        for i in robot_signal_list:
                if len(i)>13:
                        if i[12]=="R":
                                resource_collectors+=1
        defender=0
        for i in robot_signal_list:
                if len(i)>13:
                        if i[12]=="D":
                                defender+=1

        #attack strategy implementation
        #Review Pending
        attacking_no_old=base_signal_Old[8:10]
        attacking_no_New=""
        attack_counter=0
        
        #Calculating the distance between 
        if enemy_base_found:
                if enemy_baseX!="  ":
                        for w in robot_signal_list:
                                robot_signal_list_distance_enemybase.append(distancebtw(w[0:4],(enemy_baseX+enemy_baseY)))
        
        
                for i in range(0,len(robot_signal_list)):
                        if robot_signal_list[i][12]=="A" and robot_signal_list_distance_enemybase[i]<base.GetDimensionX()/2:
                                attack_counter+=1



        if attack_counter<10:
                attacking_no_New="0"+str(attack_counter)
        if attack_counter>9:
                attacking_no_New=str(attack_counter)
                
        
        #Resource must be collected
        if resource_collectors<12 and base.GetElixir()>500:
                togo=random.choice(random.choice(canvaspartitions))
                base.create_robot(base_X_str+base_Y_str+"  "+togo+"  "+"R"+"  "+str(canvasX)+str(canvasY)+"N")
        if int(timestamp)%50==0 and base.GetElixir()>500:
                togo=random.choice(random.choice(canvaspartitions))
                base.create_robot(base_X_str+base_Y_str+"  "+togo+"  "+"R"+"  "+str(canvasX)+str(canvasY)+"N")
        
        
        
        
        
        #searching for enemy robots near base
        st = "  "
        
        #enemy position
        
        if base.investigate_up()=="enemy":
                st="UP"                       
        if base.investigate_nw()=="enemy":
                st="NW"
        if base.investigate_left()=="enemy":
                st="LT"
        if base.investigate_sw()=="enemy":
                st="SW"
        if base.investigate_down()=="enemy":
                st="DW"
        if base.investigate_se()=="enemy":
                st="SE"
        if base.investigate_right()=="enemy":
                st="RT"
        if base.investigate_ne()=="enemy":
                st="NE"
        
        if st!="  ":
                base.DeployVirus(800)
        
        base_signal_New=base_signal_Old[0:4]+enemy_baseX+enemy_baseY+attacking_no_New+createStr(resource_collectors)+createStr(defender)+timestamp_New+createStr(totalrobots)
        #print(base_signal_New)
        base.SetYourSignal(base_signal_New)
        
        #apply defense
        #checking for defense in 4 corners
        corner=["NE","SW","SE","NW"]
        corner_now=[]
        for i in robot_signal_list:
                if len(i)>13:
                        if i[12]=="D":
                                for j in corner:
                                        if i[13:15]==j:
                                                corner_now.append(j)
                                                break
        for i in range(0,len(corner)):
                if corner[i] not in corner_now:
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+corner[i]+"0500"+"Y")
        
        defender=0
        for i in robot_signal_list:
                if len(i)>13:
                        if i[12]=="D":
                                defender+=1

        if st!="  ":
                base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+st+"0500"+"Y")
        """
        if int(timestamp)>500:
                if base.GetElixir()>600:
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"UP"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"NE"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"RT"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"SE"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"DW"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"SW"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"RT"+"0001"+"Y")
                        base.create_robot(base_X_str+base_Y_str+"  "+base_X_str+base_Y_str+"  "+"D"+"NW"+"0001"+"Y")
        """        
        
        #Defense applied


        #retur
        '''
        Add your code here
                Robot Signal="XXYYSPTXTYSSPTGURLRT"; for blank keep space
                              01234567890123456789
                              t=reached yet?
                P=attacking or defense(A/D/R)
                XXYY=coord SP= special position SS special Structure EB-enemy Base
                Base Signal="BXBYEXEYNANCND0001TR"
                             01234567890123456789
        '''
        return