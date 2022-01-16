from random import randint
#new bots wrt elix avail
'''
##  ##  #####  ##  #####  #####  ###   ##  #####   #####  #####    ######
##  ##  ##     ##  ##     ##     ## #  ##  ##  ##  ##     ##  ##   ##
######  #####  ##  #####  #####  ##  # ##  #####   #####  #####    ## ####
##  ##  ##     ##     ##  ##     ##   ###  ##  ##  ##     ##  ##   ##    #
##  ##  #####  ##  #####  #####  ##    ##  #####   #####  ##   ##  #######
'''
def aptsignal(head,x,y):
		if x<10:
				msg_x='0'+str(x)
		else: 
				msg_x=str(x)
		if y<10:
				msg_y='0'+str(y)
		else:
				msg_y=str(y)
		return head+msg_x+msg_y
def corner():
		pass 
def ActRobot(robot):
		temp=['u','r','d','l']
		v=600
		if robot.GetVirus()>25000:
			v=1200
		initial_signal=robot.GetInitialSignal()
		investegs=(robot.investigate_nw(),robot.investigate_up(),robot.investigate_ne(),robot.investigate_left(),robot.investigate_right(),robot.investigate_sw(),robot.investigate_down(),robot.investigate_se())
		if robot.GetCurrentBaseSignal()!='':
				init=robot.GetCurrentBaseSignal()
		elif robot.GetYourSignal()!='':
				init=robot.GetYourSignal()
				if init[:2]=='eu' or init[:2]=='ed':
					if init[2]!=robot.GetInitialSignal()[14]:
						initial_signal=robot.GetInitialSignal()[:12]+init[:3]+robot.GetInitialSignal()[15:]
					
		else:
				init=robot.GetInitialSignal()
		rx,ry=robot.GetPosition()
		if init[0]=='e' :
				if init[1]=='u':
						move=1
						surr=[0 for i in range(8)]
						for case in range(8):
								
								if investegs[case]=='enemy':
										surr[case]=1
								elif investegs[case]=='enemy-base':
										
										if case==0:
												robot.setSignal(aptsignal('eb',rx-1,ry-1))
										elif case==1:
												robot.setSignal(aptsignal('eb',rx,ry-1))
										elif case==2:
												robot.setSignal(aptsignal('eb',rx+1,ry-1))
										elif case==3:
												robot.setSignal(aptsignal('eb',rx-1,ry))
										elif case==4:
												robot.setSignal(aptsignal('eb',rx+1,ry))
										elif case==5:
												robot.setSignal(aptsignal('eb',rx-1,ry+1))
										elif case==6:
												robot.setSignal(aptsignal('eb',rx,ry+1))
										elif case==7:
												robot.setSignal(aptsignal('eb',rx+1,ry+1))
										v=5000
										surr[case]=3
								elif investegs[case]=='wall' and case==1 and case!=2 and not (investegs[3]=='wall' or investegs[4]=='wall'):
										if rx>3:
												robot.setSignal('es'+(3*str(temp.index(init[2])+1))+'3'+init)
										else:
												robot.setSignal('es'+(rx*str(temp.index(init[2])+1))+'3'+init)
										break 
								elif investegs[case]=='wall' and case ==1:
										robot.setSignal('gr'+init[3:])

						decision=sum(surr)
						if decision>0:
								if robot.GetVirus()>=v:
										robot.DeployVirus(v)
										
								else:
										robot.DeployVirus(robot.GetVirus())
										
				elif init[1]=='d':
						move=3
						surr=[0 for i in range(8)]
						for case in range(8):
								
								if investegs[case]=='enemy':
										surr[case]=1
								elif investegs[case]=='enemy-base':
										
										if case==0:
												robot.setSignal(aptsignal('eb',rx-1,ry-1))
										elif case==1:
												robot.setSignal(aptsignal('eb',rx,ry-1))
										elif case==2:
												robot.setSignal(aptsignal('eb',rx+1,ry-1))
										elif case==3:
												robot.setSignal(aptsignal('eb',rx-1,ry))
										elif case==4:
												robot.setSignal(aptsignal('eb',rx+1,ry))
										elif case==5:
												robot.setSignal(aptsignal('eb',rx-1,ry+1))
										elif case==6:
												robot.setSignal(aptsignal('eb',rx,ry+1))
										elif case==7:
												robot.setSignal(aptsignal('eb',rx+1,ry+1))
										v=5000
										surr[case]=3
										
								elif investegs[case]=='wall' and case ==6 and case !=7 and not (investegs[3]=='wall' or investegs[4]=='wall'):
										if rx>3:
												robot.setSignal('es'+(3*str(temp.index(init[2])+1))+'1'+init)
										else:
												robot.setSignal('es'+(rx*str(temp.index(init[2])+1))+'1'+init)
										break 
								
								elif investegs[case]=='wall' and case ==6:
										robot.setSignal('gr'+init[3:])

						decision=sum(surr)
						if decision>0:
								if robot.GetVirus()>=v:
										robot.DeployVirus(v)
								else:
										robot.DeployVirus(robot.GetVirus())
				elif init[1]=='s':
						
						if len(init)>10:
								move=int(init[2])
								robot.setSignal('es'+init[3:])
						elif len(init)==10:
								move=int(init[2])
								
								robot.setSignal('e'+str(temp[int(init[2])-1])+init[-5]+initial_signal[15:])

		elif init[0]=='g':
				if init[1]=='d':
					sx=int(init[-4:-2])
					sy=int(init[-2:])
					sig=init[1:]
					defddist=0
				elif init[1]=='r':
					sx = int(init[2:4])
					sy = int(init[4:6])
					decider=randint(0,2)
					
					if decider>=1:
						initsig=robot.GetInitialSignal()
						if initsig[14]=='l':
							tempchr='r'
						else:
							tempchr='l'
						sig=initsig[12:14]+tempchr+initsig[15:]
						
					elif decider==0:
						decider2=randint(0,2)
						initsig=robot.GetInitialSignal()
						if decider2==0:
							sig='rm'+initsig[15:]
						elif decider2>=1:
							sig='r'
					defddist=1
				elif init[1]=='b':
					sx=int(init[2:4])
					sy=int(init[2:4])
					defddist=1
					sig='rm'+init[2:]
				dist = abs(sx-rx) + abs(sy-ry)
				if dist==defddist:
						robot.setSignal(sig)
						return 0
				if rx < sx:
						return 2
				if rx > sx:
						return 4
				if ry < sy :
						return 3
				if ry > sy:
						return 1
					

		elif init[0]=='a':
				sx = int(init[1:3])
				sy = int(init[3:5])
				dist = abs(sx-rx) + abs(sy-ry)
				if dist==1:
						robot.DeployVirus(robot.GetVirus()*0.75)
						return 0
				if rx < sx:
						return 2
				if rx > sx:
						return 4
				if ry < sy :
						return 3
				if ry > sy:
						return 1
		elif init[0]=='r':
			if len(init)>1 and init[1]=='m':
				
				if 'enemy' in investegs:
						robot.DeployVirus(500)
				if 'enemy-base' in investegs:
						robot.DeployVirus(robot.GetVirus()*0.75)
				if rx>int(init[2:4])+4 or rx<int(init[2:4])-4 or ry>int(init[4:6])+4 or ry<int(init[4:6])-4:
					robot.setSignal('gr'+init[2:])
				return randint(1,4)
			else:
				if 'enemy' in investegs:
						robot.DeployVirus(500)
				if 'enemy-base' in investegs:
						robot.DeployVirus(robot.GetVirus()*0.75)
				if len(init)>1:
					robot.setSignal(init[1:])
					
				return randint(1,4)
		elif init[0]=='d':
				if init[1]=='u':
						move=1
						robot.setSignal('d01')
				elif init[1]=='l':
						move=2
						robot.setSignal('d02')
				elif init[1]=='d':
						move=3
						robot.setSignal('d03')
				elif init[1]=='r':
						move=4
						robot.setSignal('d04')
				elif init[1]=='0':
						if 'enemy' in investegs:
								
								robot.DeployVirus(2000)

						move=int(init[2])
						if init[2] in ('1','2'):
								robot.setSignal('d0'+str(int(init[2])+2))
						else:
								robot.setSignal('d0'+str(int(init[2])-2))
		return move


def ActBase(base):
	L=base.GetListOfSignals()
	initel=base.GetElixir()
	
	if initel>=2000 :
		if base.GetElixir()>600:
			while base.GetElixir()>600:
					base.create_robot(aptsignal('r'*12+'edr',base.GetPosition()[0],base.GetPosition()[1]))
					base.create_robot(aptsignal('r'*12+'eul',base.GetPosition()[0],base.GetPosition()[1]))
		if base.GetElixir()>400:
			base.create_robot(aptsignal('r'*12+'gdu',base.GetPosition()[0],base.GetPosition()[1]))
			base.create_robot(aptsignal('r'*12+'gdl',base.GetPosition()[0],base.GetPosition()[1]))
			base.create_robot(aptsignal('r'*12+'gdr',base.GetPosition()[0],base.GetPosition()[1]))
			base.create_robot(aptsignal('r'*12+'gdd',base.GetPosition()[0],base.GetPosition()[1]))
	elif initel>=1000 and len(L)<1:
		while base.GetElixir()>250:
					base.create_robot(aptsignal('r'*12+'edr',base.GetPosition()[0],base.GetPosition()[1]))
					base.create_robot(aptsignal('r'*12+'eul',base.GetPosition()[0],base.GetPosition()[1]))
	elif initel>100 and len(L)<1:
		while base.GetElixir()>150:
					base.create_robot(aptsignal('r'*12+'edr',base.GetPosition()[0],base.GetPosition()[1]))
					base.create_robot(aptsignal('r'*12+'eul',base.GetPosition()[0],base.GetPosition()[1]))
	elif initel>50 and len(L)<1:
		base.create_robot(aptsignal('r'*12+'edr',base.GetPosition()[0],base.GetPosition()[1]))
	


	investegs=(base.investigate_nw(),base.investigate_up(),base.investigate_ne(),base.investigate_left(),base.investigate_right(),base.investigate_sw(),base.investigate_down(),base.investigate_se())
	if 'enemy' in investegs:
			base.DeployVirus(4000)
	for i in L:
		if i[:2]=='eb':
			base.SetYourSignal('a'+i[2:6])
	return