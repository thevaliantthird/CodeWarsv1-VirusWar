from random import randint
from robot import Robot
from base import Base
from collectible import Collectible
def investigateall(Robot): #this is a function to investigate in all direction together
   u=Robot.investigate_up()
   d=Robot.investigate_down()
   l=Robot.investigate_left()
   r=Robot.investigate_right()
   ne=Robot.investigate_ne()
   nw=Robot.investigate_nw()
   se=Robot.investigate_se()
   sw=Robot.investigate_sw()
   results={"up":u,"down":d,"right":r,"left":l,"ne":ne,"nw":nw,"se":se,"sw":sw}
   return results

def investigateall_Base(Base): #this is a function to investigate in all direction together
   u=Base.investigate_up()
   d=Base.investigate_down()
   l=Base.investigate_left()
   r=Base.investigate_right()
   ne=Base.investigate_ne()
   nw=Base.investigate_nw()
   se=Base.investigate_se()
   sw=Base.investigate_sw()
   results={"up":u,"down":d,"right":r,"left":l,"ne":ne,"nw":nw,"se":se,"sw":sw}
   return results
     
def ActRobot(robot): #this is a function which returns 0-4 value to make the move
   result=investigateall(robot)
   for direction in result:
      i=0
      if direction=="enemy":
         i=i+1
   if i>=3:
      robot.DeployVirus(base.GetVirus()/10)
   if investigateall=="enemy-base": #function to attack on enemy base after getting it's location
      robot.setSignal("enemy-base")
   if robot.GetCurrentBaseSignal()=="attack": #function to attack on enemy base after getting it's location
      return(randint(1,4))
                #send all robots to current base location
   if robot.setSignal=="enemy":
      robot.DeployViurs(base.GetVirus()/10)
   if robot.setSignal=="enemy_base":
      robot.DeployViurs(base.GetVirus())
   name=robot.GetInitialSignal()
   if name[0:8]=="defender":
      pass
   X=Base.GetDimensionX(Base)
   Y=Base.GetDimensionY(Base)
   for x in range(-1,-X-1,-1) and y in range(-1,-Y-1,-1):
      if (X,Y)==(0,0):
         robot.GetPosition()!=(x,y)
   for i in range(0,X):
      if True:
         robot.GetPosition()!=(i,Y)
   for j in range(0,Y):
      if True:
         robot.GetPosition()!=(X,j)
   
   return
   
def ActBase(base): #this is a function defining the move of the base
   a=base.GetListOfSignals()
   if a=="enemy-base":
      base.setYourSignal("attack")
   if base.GetElixir() > 500:
      base.create_robot('')
   result=base.investigateall_Base(Base)
   for direction in result:
      if direction=="enemy":
         base.DeployVirus(base.GetVirus()/10)

   return 