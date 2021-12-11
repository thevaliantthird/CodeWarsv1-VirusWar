# CodeOmicron

WnCC's Freshie Orientation

Freshies find it simple

400 by 400 canvas!

Each robot deployed on the screen can put up a signal(which is an integer)

Each team has a un-movable base on the canvas, which runs the ```Operator``` script, the function of this is to deploy robots, it can also deploy every robot with a starting singal which is an integer!

The ```Robot``` script would have access to this integer signal and could accordingly decide which way it should go!
The Robot also has a signal which is an integer, which the Operator could read any time it wants to.

The Robot explores the map and also decides when and where to disperse the virus.

When it does so, the selected amount of virus will spread uniformly in all the eight directions (N,S,E,W,NE,NW,SE,SW).

Virus is a static variable associated with every team, the different robots of a team can explore the map to collect virus, but all the collected virus is stored on the base, BUT can be disperesd by any of the robots.

This virus can be deployed(any particular amount of it) by any other robot of the team, as and when it is deployed, it spreads in the 8 cells that surround the robot(i.e. N,S,E,W,NW,NE,SW,SE) by equal amounts.

When you disperse a virus, if the opponent team's robot is on that spot, then the virus would erode that particular robot's elixir (in a 1:1 ratio) (which is at most 50) if the robot's elixir becomes 0, then the robot is destroyed!

Every cell has an initial amount of virus/elixir(one of these) and whenever a robot comes there, it takes all of it, to enhance his own team's resources. Further after said amount of timeframes all the used-up cells(which have been already mined of resources) will have their resource renewed.

If two robots share the same position, then they shall be replaced by a single robot belonging to the team of the robot with a greater amount of elixir and elixir equal to the difference of the amounts (if both have same elixir, then both robots shall be destroyed!)


**Operator**

This can take some input from all your deployed robots(the signals they have up) and accordingly put up its own signal, which can be read by all the robots which it has deployed. Whenever it creates a robot, it passes another signal(integer to it).

To sum up the signal part : The operator puts up a signal which can be seen by all the robots it has deployed.Further every robot is also provided with a signal unique to it. All the robots also put up a signal. This signal can be seen by the operator/base, which can see the signal of all of it's deployed robots and make decisions accordingly!

**Functions which the Robots shall have access to**

MoveRobot(Robot r)
Robot class must have functions to:

1. moveUp, moveDown, moveLeft, moveRight
2. InvestigateUp, investigateDOwn, Inver.Left, invesRight, investigateNw, investigaeNw.... : int : 0 : ,1,2
3. DeployVirus(float v): (tells us the amount of virus, it must be less than the total stock)
4. setSignal(int i) : Sets the robot's signal
5. GetInitialSignal() : The signal which was used to initialize this robot by the base
6. GetYourSignal(): The signal which you have currently put up
7. GetCurrentOperatorSignal : Get the Operator/Base's Signal
8. GetTotalElixir : the team's total elixir stock
9. GetVirus : The team's total virus stock
10. GetElixir : The robot's stock of Elixir
11. GetPosition() : (x,y)
12. GetDimensionX()
13. GetDimensionY()

**Operator**

runOperator(Operator o)

The operator class must have the following functions!

1. GetListOfSignals() : Returns to us a list of integers containing the signals of all robots deployed!
2. CreateRobot(int signal) : create a robot with initial signal (integer)
3. GetYourSignal() : get your own signal
4. SetYourSignal() : Sets the operator signal
5. InvestigateUp, investigateDOwn, Inver.Left, invesRight, investigateNw, investigateNw.... : int : 0 : ,1,2
6. DeployVirus(float v): (tells us the amount of virus, it must be less than the total stock)
7. GetTotalElixir : the team's total elixir stock
8. GetVirus : The team's total virus stock
9. GetElixir : The robot's stock of Elixir
10. GetPosition() : (x,y)
11. GetDimensionX()
12. GetDimensionY()