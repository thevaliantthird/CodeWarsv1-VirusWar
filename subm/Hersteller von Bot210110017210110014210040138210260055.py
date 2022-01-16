from random import randint
from numpy import sign
import timeit

start = timeit.default_timer()

def ActRobot(robot):
        h_mov=0
        v_mov=0
        my_sig=robot.GetInitialSignal()
        if robot.GetYourSignal()!=my_sig and robot.GetYourSignal()!="":
              my_sig=robot.GetYourSignal()
              
        bas_sig=robot.GetCurrentBaseSignal() #Base Signal is originally ''
        pos=list(robot.GetPosition())

        if (bas_sig=="") and my_sig[my_sig.index("_")+1]=="1": #When target base not given
            Detect_Enemy(robot,pos)       
            return randint(1,4)
        
        elif (bas_sig=="") and my_sig[my_sig.index("_")+1]=="2":
            Detect_Enemy(robot,pos)
            
            '''Taking co-ordinates of both robot and target'''        
            pos=robot.GetPosition()
            trg_pos=eval(my_sig[my_sig.index("_(")+1:])

            '''Taking the current time'''
            stop = timeit.default_timer()
            execution_time = stop - start

            '''Changing the target position of robots'''
            if execution_time>15:
                    return randint(1,4) 
            if pos==trg_pos and robot.GetYourSignal()!=robot.GetInitialSignal() and 6<execution_time<15:
                    trg_x=New_Target(robot.GetDimensionX(),pos[0])
                    robot.setSignal(my_sig[:my_sig.index("_(")+1]+f"({trg_x},"+\
                                    my_sig[my_sig.index(",")+1:])
            mov_val=Move(pos,trg_pos,robot)
            return mov_val
                    
        else: #When target base given  
            trg_pos=eval(bas_sig)
            mov_val=Move(pos,trg_pos,robot,"enemy")
            return mov_val

def Detect_Enemy(robot,pos):
        '''Inspecting all 8 directions'''    
        w_a=[robot.investigate_up(),robot.investigate_down(),\
             robot.investigate_left(),robot.investigate_right(),\
             robot.investigate_ne(),robot.investigate_nw(),\
             robot.investigate_se(),robot.investigate_sw()]
            
        '''Dictionary for Correcting Co-ordinates
           This dictionary is used when enemy base is found,
           and we have to calculate its co-ordinates.'''
        dr_cr={0:(0,-1),1:(0,1),2:(-1,0),3:(1,0),\
               4:(1,-1),5:(-1,-1),6:(1,1),7:(-1,1)}
            
        '''Checking what each cell holds'''
        for i in range(len(w_a)):
            if w_a[i]=="enemy":
                if robot.GetVirus() > 1000:
                        robot.DeployVirus(200)
                        
            elif w_a[i]=="enemy-base":
                if robot.GetVirus() > 1000:
                    robot.DeployVirus(robot.GetVirus()*0.80) #Adjust Virus Amount

                    '''Correcting Co-ordinates'''    
                    pos[0],pos[1]=pos[0]+dr_cr[i][0],pos[1]+dr_cr[i][1]
                    pos=tuple(pos)
                    robot.setSignal(f"{pos}")
        
def Move(curr_pos, trg_pos,robot,trg="init"):
        if (trg_pos[0]-curr_pos[0])!=0:
                if abs(trg_pos[0]-curr_pos[0])==1 and trg=="enemy":
                        if robot.GetVirus() > 1000:
                            robot.DeployVirus(200)    
                h_mov=3-sign(trg_pos[0]-curr_pos[0])
                return h_mov
        
        if (trg_pos[1]-curr_pos[1])!=0:
                if abs(trg_pos[1]-curr_pos[1])==1 and trg=="enemy":
                        if robot.GetVirus() > 1000:
                            robot.DeployVirus(200) 
                v_mov=2+sign(trg_pos[1]-curr_pos[1])
                return v_mov
        
def New_Target(width,x):
        '''Gives the robots a new target'''
        if x<width/2:
                return width-1
        else:
                return 0
        
def Quad_Decide(width,x):
        '''Decides the orientation of robots'''
        if x<width/2:
                return 0
        else:
                return width-1
        
def ActBase(base):
        '''
        Add your code here
    
        '''
        if base.GetVirus()>1000:
                base.DeployVirus(20)
                
        L=base.GetListOfSignals()
        trg_x=Quad_Decide(base.GetDimensionX(),base.GetPosition()[0])
        if base.GetElixir() > 500: 
            n=len(L)
            pur=1
            if (n+1)%2==0 and n<27:
                pur=2
                base.create_robot(f'{n+1}_{pur}_({trg_x},{((n*3+1)/2)-1})')
            else:
                base.create_robot(f'{n+1}_{pur}')
        for i in range(len(L)):
            if L[i]!="" and L[i][0]=="(": 
                base.SetYourSignal(L[i])
                break  

