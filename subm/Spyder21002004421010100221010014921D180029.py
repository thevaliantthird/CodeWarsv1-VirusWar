from random import randint
def ActRobot(robot):
        #global flag
        st=robot.GetCurrentBaseSignal()
        dimx=robot.GetDimensionX()
        dimy=robot.GetDimensionY()
        if st[3]=="r":
                #print("QQQQ")
                #fr=["friend","friend-robot"]
                en=["enemy","enemy-robot"]
                up=robot.investigate_up()
                do=robot.investigate_down()
                lf=robot.investigate_left()
                rh=robot.investigate_right()
                nw=robot.investigate_nw()
                ne=robot.investigate_ne()
                sw=robot.investigate_sw()
                se=robot.investigate_se()
                l1=[up,do,lf,rh,nw,ne,sw,se]
                fr="friend-base"
                x,y=robot.GetPosition()
                #print((st))
                if st[4]=="u":
                        if 5<int(st[5:9])<10:
                                return 3
                else:
                        if 5<int(st[5:9])<10:
                                return 1

                
                if st[:2]=="go":
                        #flag=0
                        #print("#")
                        if "enemy" in l1:     
                                #print("K")
                                robot.DeployVirus(robot.GetVirus()/2)
                        if "enemy-base" in l1:
                                #if "enemy-base" in l1:
                                #robot.setSignal("enemybase"+","+str(x)+","+str(y))
                                if robot.investigate_up()==('enemy-base'):
                                        return 1
                                elif robot.investigate_down()==('enemy-base'):
                                        return 3
                                elif robot.investigate_left()==('enemy-base'):
                                        return 4
                                elif robot.investigate_right()==('enemy-base'):
                                        return 2
                                                
                                elif robot.investigate_nw()==('enemy-base'):
                                        return 1
                                                
                                elif robot.investigate_ne()==('enemy-base'):
                                        return 1
                                                
                                elif robot.investigate_sw()==('enemy-base'):
                                        return 3                           
                                elif robot.investigate_se()==('enemy-base'):
                                        return 3
                                robot.DeployVirus(robot.GetVirus())
                                if robot.GetVirus()<1:
                                        robot.setSignal("go_"+st[3:])
                                return 0
                         
                                
                        elif robot.GetInitialSignal()!="":
                                #print("Y")
                                xbf,ybf=int(robot.GetInitialSignal().split(",")[0]),int(robot.GetInitialSignal().split(",")[1])
                                delx=xbf-x
                                dely=ybf-y
                                if "enemy" in l1:     
                                        #print("K")
                                        robot.DeployVirus(robot.GetVirus()/2)
                                elif "enemy-base" in l1:
                                        #if "enemy-base" in l1:
                                        #robot.setSignal("enemybase"+","+str(x)+","+str(y))
                                        robot.DeployVirus(robot.GetVirus())
                                        if robot.GetVirus()<1:
                                                robot.setSignal("go_ru"+st[5:])
                                        return 0
                                #print(xbf,ybf)
                                if st[4]=="u":
                                                if 12<int(st[5:9])<17:
                                                        return 1
                                else:
                                                if 12<int(st[5:9])<17:
                                                        return 3
                                
                                   
                                        
                                        
                                if delx>0:
                                        for i in range(0,delx):
                                                return 2
                                

                                else:
                                        for i in range(0,-delx):
                                                return 4
                                
                                if dely>0:
                                        for i in range(0,dely):
                                                return 3
                                

                                else:
                                        for i in range(0,-dely):
                                                return 1
                                
                                
                        

                        if (50<int(st[5:9])<60) or (140 <int(st[5:9])<160):
                                if x!=0:
                                        return 2
                                else:
                                        return 4
                        elif (60<int(st[5:9])<140):
                                if x<5:
                                        return 2
                                elif x<dimx//3:
                                        return randint(1,4)
                                else:
                                        return 4
                              

                        else:
                                return randint(1,4)
                        

                else:               
                        l3=st.split(",")
                        print(l3)
                        
                        if l3[0]=="ebase":
                                #x,y=robot.GetPosition()
                                print("##")
                                xbf,ybf=int(l3[1]),int(l3[2])
                                #robot.setSignal("ebase"+","+str(xbf)+","+str(ybf))
        
                                delx=xbf-x
                                dely=ybf-y
                                if delx>0:
                                        for i in range(0,delx):
                                                return 2
                                else:
                                        for i in range(0,-delx):
                                                return 4
                                
                                if dely>0:
                                        for i in range(0,dely):
                                                return 3
                                else:
                                        for i in range(0,-dely):
                                                return 1
                                robot.DeployVirus(robot.GetVirus())
                                #robot.setSignal("go")
                                #flag=1
        else:
                #print("QQQQ")
                #fr=["friend","friend-robot"]
                en=["enemy","enemy-robot"]
                up=robot.investigate_up()
                do=robot.investigate_down()
                lf=robot.investigate_left()
                rh=robot.investigate_right()
                nw=robot.investigate_nw()
                ne=robot.investigate_ne()
                sw=robot.investigate_sw()
                se=robot.investigate_se()
                l1=[up,do,lf,rh,nw,ne,sw,se]
                fr="friend-base"
                x,y=robot.GetPosition()
                #print((st))
                if st[4]=="u":
                        if 5<int(st[5:9])<10:
                                return 3
                else:
                        if 5<int(st[5:9])<10:
                                return 1

                
                if st[:2]=="go":
                        #flag=0
                        #print("#")
                        if "enemy" in l1:     
                                #print("K")
                                robot.DeployVirus(robot.GetVirus()/2)
                        if "enemy-base" in l1:
                                #if "enemy-base" in l1:
                                #robot.setSignal("enemybase"+","+str(x)+","+str(y))
                                if robot.investigate_up()==('enemy-base'):
                                        return 1
                                elif robot.investigate_down()==('enemy-base'):
                                        return 3
                                elif robot.investigate_left()==('enemy-base'):
                                        return 4
                                elif robot.investigate_right()==('enemy-base'):
                                        return 2
                                                
                                elif robot.investigate_nw()==('enemy-base'):
                                        return 1
                                                
                                elif robot.investigate_ne()==('enemy-base'):
                                        return 1
                                                
                                elif robot.investigate_sw()==('enemy-base'):
                                        return 3                           
                                elif robot.investigate_se()==('enemy-base'):
                                        return 3
                                robot.DeployVirus(robot.GetVirus())
                                if robot.GetVirus()<1:
                                        robot.setSignal("go_"+st[3:])
                                return 0
                                
                        elif robot.GetInitialSignal()!="":
                                #print("Y")
                                xbf,ybf=int(robot.GetInitialSignal().split(",")[0]),int(robot.GetInitialSignal().split(",")[1])
                                delx=xbf-x
                                dely=ybf-y
                                if "enemy" in l1:     
                                        #print("K")
                                        robot.DeployVirus(robot.GetVirus()/2)
                                elif "enemy-base" in l1:
                                        #if "enemy-base" in l1:
                                        #robot.setSignal("enemybase"+","+str(x)+","+str(y))
                                        if robot.investigate_up()==('enemy-base'):
                                                return 1
                                        elif robot.investigate_down()==('enemy-base'):
                                                return 3
                                        elif robot.investigate_left()==('enemy-base'):
                                                return 4
                                        elif robot.investigate_right()==('enemy-base'):
                                                return 2
                                                        
                                        elif robot.investigate_nw()==('enemy-base'):
                                                return 1
                                                        
                                        elif robot.investigate_ne()==('enemy-base'):
                                                return 1
                                                        
                                        elif robot.investigate_sw()==('enemy-base'):
                                                return 3                           
                                        elif robot.investigate_se()==('enemy-base'):
                                                return 3
                                        robot.DeployVirus(robot.GetVirus())
                                        if robot.GetVirus()<1:
                                                robot.setSignal("go_ru"+st[5:])
                                        return 0
                                #print(xbf,ybf)
                                if st[4]=="u":
                                                if 12<int(st[5:9])<17:
                                                        return 1
                                else:
                                                if 12<int(st[5:9])<17:
                                                        return 3
                                #c
                                   
                                        
                                        
                                if delx>0:
                                        for i in range(0,delx):
                                                return 2    #c
                                

                                else:
                                        for i in range(0,-delx):
                                                return 4       #c
                                
                                if dely>0:
                                        for i in range(0,dely):
                                                return 3        #c
                                

                                else:
                                        for i in range(0,-dely):
                                                return 1     #c
                                
                                
                        

                        if (50<int(st[5:9])<60) or (140 <int(st[5:9])<150):
                                if x!=dimx-1:
                                        return 2   #c
                                else:
                                        return 4    #c
                        elif (60<int(st[5:9])<140) or (200<int(st[5:9])<205):
                                if x>dimx-5:
                                        return 4    #c
                                elif (dimx//3)<x:
                                        return 2 #c
                                else:
                                        return randint(1,4)
                                   

                        else:
                                return randint(1,4)

                else:               
                        l3=st.split(",")
                        print(l3)
                        
                        if l3[0]=="ebase":
                                #x,y=robot.GetPosition()
                                print("##")
                                xbf,ybf=int(l3[1]),int(l3[2])
                                #robot.setSignal("ebase"+","+str(xbf)+","+str(ybf))
        
                                delx=xbf-x
                                dely=ybf-y
                                if delx>0:
                                        for i in range(0,delx):
                                                return 4        #c
                                else:
                                        for i in range(0,-delx):
                                                return 2        #c
                                
                                if dely>0:
                                        for i in range(0,dely):
                                                return 3
                                else:
                                        for i in range(0,-dely):
                                                return 1
                                robot.DeployVirus(robot.GetVirus())
                                #robot.setSignal("go")
                                #flag=1
                
def ActBase(base):
        
        dimbx=base.GetDimensionX()
        dimby=base.GetDimensionY()
       
        #global flag
        #fr=["friend","friend-base"]
        en=["enemy","enemy-base"]
        up=base.investigate_up()
        do=base.investigate_down()
        lf=base.investigate_left()
        rh=base.investigate_right()
        nw=base.investigate_nw()
        ne=base.investigate_ne()
        sw=base.investigate_sw()
        se=base.investigate_se()
        xb,yb=base.GetPosition()
        sig=""
        si=""
        if xb>(dimbx//2):
                sig="r"
                #print("Detects right")
        elif xb<=(dimbx//2):
                sig="l"
                #print("detects left")
        if yb>(dimby//2):
                si="d"
        elif yb<=(dimby//2):
                si="u"
        s1=0
        if base.GetYourSignal()=="":
                s="###"+sig+si+"0000"
                base.SetYourSignal(s)
        else:
                s=base.GetYourSignal()
                s1=int(s[5:9])
                #print(s1)
                
                s1+=1
                
                s=s[0:3]+sig+si + (4-len(str(s1)))*"0"+ str(s1)
                base.SetYourSignal(s)
                #print(s)
        l=base.GetListOfSignals()
        #base.SetYourSignal("go")
        #base.create_robot("")
        
        while base.GetElixir()>950:
                base.create_robot("")
                b=base.GetYourSignal()
                base.SetYourSignal("go_"+sig+si+b[5:])
               
        while base.GetElixir()>800:
                base.create_robot(str(dimbx-base.GetPosition()[0])+","+str(dimby-base.GetPosition()[1]))
        while base.GetElixir()>650:
                base.create_robot(str(base.GetPosition()[0])+","+str(dimby-base.GetPosition()[1]))
        while base.GetElixir()>500:
                base.create_robot(str(dimbx-base.GetPosition()[0])+","+str(base.GetPosition()[1]))
        while base.GetElixir()>200:
                base.create_robot(str(base.GetPosition()[0])+","+str(base.GetPosition()[1]))                     
        
        if up and do in en:
                #if base.GetVirus()>300:
                base.DeployVirus(base.GetVirus()/2)
        
        elif lf and rh in en:
                #if base.GetVirus()>300:
                base.DeployVirus(base.GetVirus()/2)
        elif nw and ne in en:
                #if base.GetVirus()>300:
                base.DeployVirus(base.GetVirus()/2)

        elif se and sw in en:
                #if base.GetVirus()>300:
                base.DeployVirus(base.GetVirus()/2)
        return
        


