from random import randint,choice


def ActRobot(robot):

        if (robot.investigate_down() == 'enemy-base' or robot.investigate_up() == 'enemy-base' or robot.investigate_right() == 'enemy-base' or robot.investigate_left() == 'enemy-base' or robot.investigate_ne() == 'enemy-base' or robot.investigate_nw() == 'enemy-base' or robot.investigate_se() == 'enemy-base' or robot.investigate_sw() == 'enemy-base'):
                
                robot.DeployVirus(robot.GetVirus())
                t = robot.GetPosition()
                
                if not robot.GetCurrentBaseSignal():
                        
                        if robot.investigate_up() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0], t[1]-1))
                                return 0
                        elif robot.investigate_right() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0]+1, t[1]))
                                return 0
                        elif robot.investigate_down() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0], t[1]+1))
                                return 0
                        elif robot.investigate_left() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0]-1, t[1]))
                                return 0
                        elif robot.investigate_ne() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0]+1, t[1]-1))
                                return 0
                        elif robot.investigate_nw() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0]-1, t[1]-1))
                                return 0
                        elif robot.investigate_se() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0]+1, t[1]+1))
                                return 0
                        elif robot.investigate_sw() == 'enemy-base':
                                robot.setSignal("E:{},{}".format(t[0]-1, t[1]+1))
                                return 0
                # return 0
        
        if (robot.investigate_down() == 'enemy' or robot.investigate_up() == 'enemy' or robot.investigate_right() == 'enemy' or robot.investigate_left() == 'enemy' or robot.investigate_ne() == 'enemy' or robot.investigate_nw() == 'enemy' or robot.investigate_se() == 'enemy' or robot.investigate_sw() == 'enemy'):
               
                if robot.GetYourSignal() == 'patrol_up' or robot.GetYourSignal() == 'patrol_right' or robot.GetYourSignal() == 'patrol_down' or robot.GetYourSignal() == 'patrol_left':
                        if (((robot.GetTotalElixir() / 26) * 8  + 400) >= robot.GetVirus()):
                                robot.DeployVirus(robot.GetVirus())
                        else:
                                robot.DeployVirus( ((robot.GetTotalElixir() / 26) * 8  + 600) )
                        # robot.DeployVirus( robot.GetVirus() * 0.4 )
                        return 0
                
                if not robot.GetCurrentBaseSignal():
                        
                        if robot.GetInitialSignal() == 'explore' or robot.GetYourSignal() == 'explore':
                                robot.DeployVirus( robot.GetVirus() * 0.1) 
                                if robot.investigate_up() == 'enemy':
                                        return choice([2, 3, 4])
                                elif robot.investigate_right() == 'enemy':
                                        return choice([1, 3, 4])
                                elif robot.investigate_down() == 'enemy':
                                        return choice([2, 1, 4])
                                elif robot.investigate_left() == 'enemy':
                                        return choice([2, 3, 1])
        
        if robot.GetCurrentBaseSignal() and (robot.GetInitialSignal() == 'explore' or robot.GetYourSignal() == 'explore'):
                
                ebase_pos = robot.GetCurrentBaseSignal()
                e = ebase_pos.split(":")[1].split(",")
                enemy_pos = (int(e[0]), int(e[1]))
                bot_pos = robot.GetPosition()
                
                if abs(enemy_pos[0] - bot_pos[0]) >= abs(enemy_pos[1] - bot_pos[1]):
                        
                        if (enemy_pos[0] - bot_pos[0]) > 0:
                                return 2
                        elif (enemy_pos[0] - bot_pos[0]) < 0:
                                return 4
                
                if abs(enemy_pos[0] - bot_pos[0]) < abs(enemy_pos[1] - bot_pos[1]):
                        
                        if (enemy_pos[1] - bot_pos[1]) > 0:
                                return 3
                        elif (enemy_pos[1] - bot_pos[1]) < 0:
                                return 1                               
                
        
        if robot.GetInitialSignal() == 'patrol':
                
                if (robot.investigate_down() == 'friend-base' or robot.investigate_up() == 'friend-base' or robot.investigate_right() == 'friend-base' or robot.investigate_left() == 'friend-base' or robot.investigate_ne() == 'friend-base' or robot.investigate_nw() == 'friend-base' or robot.investigate_se() == 'friend-base' or robot.investigate_sw() == 'friend-base'):
                        return 0
                elif robot.investigate_up() == 'blank':
                        robot.setSignal('patrol_up')
                        return 1
                elif robot.investigate_right() == 'blank':
                        robot.setSignal('patrol_right')
                        return 2
                elif robot.investigate_down() == 'blank':
                        robot.setSignal('patrol_down')
                        return 3
                elif robot.investigate_left() == 'blank':
                        robot.setSignal('patrol_left')
                        return 4
                else:
                        robot.setSignal('explore')
                        return randint(1,4)
        
        elif robot.GetInitialSignal() == 'patrol_up' and robot.GetYourSignal() == '':
                robot.setSignal('patrol_up')
                return 1
        elif robot.GetInitialSignal() == 'patrol_down' and robot.GetYourSignal() == '':
                robot.setSignal('patrol_down')
                return 3
        elif robot.GetInitialSignal() == 'patrol_right' and robot.GetYourSignal() == '':
                robot.setSignal('patrol_right')
                return 2
        elif robot.GetInitialSignal() == 'patrol_left' and robot.GetYourSignal() == '':
                robot.setSignal('patrol_left')
                return 4
        elif robot.GetYourSignal() == 'patrol_up' or robot.GetYourSignal() == 'patrol_right' or robot.GetYourSignal() == 'patrol_down' or robot.GetYourSignal() == 'patrol_left':
                return 0
        
        if robot.investigate_up() == 'wall':
                return choice([2, 3, 4])
        elif robot.investigate_right() == 'wall':
                return choice([1, 3, 4])
        elif robot.investigate_down() == 'wall':    
                return choice([2, 1, 4])
        elif robot.investigate_left() == 'wall':      
                return choice([2, 3, 1])
        else:
                return randint(1,4)
        

def ActBase(base):
        
        patrol_spots = ['patrol_up', 'patrol_right', 'patrol_down', 'patrol_left']
       
        for i in base.GetListOfSignals():
                if i.startswith('E:'):
                        base.SetYourSignal(i)

        if (base.investigate_down() == 'enemy' or base.investigate_up() == 'enemy' or base.investigate_right() == 'enemy' or base.investigate_left() == 'enemy' or base.investigate_ne() == 'enemy' or base.investigate_nw() == 'enemy' or base.investigate_se() == 'enemy' or base.investigate_sw() == 'enemy') or (base.investigate_down() == 'enemy-base' or base.investigate_up() == 'enemy-base' or base.investigate_right() == 'enemy-base' or base.investigate_left() == 'enemy-base' or base.investigate_ne() == 'enemy-base' or base.investigate_nw() == 'enemy-base' or base.investigate_se() == 'enemy-base' or base.investigate_sw() == 'enemy-base'):
                if (((base.GetTotalElixir() / 26) * 8  + 400) >= base.GetVirus()):
                        base.DeployVirus(base.GetVirus())
                else:
                        base.DeployVirus( ((base.GetTotalElixir() / 26) * 8  + 600) )

                # base.DeployVirus( base.GetVirus() * 0.4 )
                
                
        # format is -> ( elixir we will be allocated at start ) - ( num of robots we want ) * ( cost of robot= 50 )
        if base.GetElixir() > (2000 - 4*50): # we want 4 patrol robots  
                
                base.create_robot('patrol')     
        
        elif base.GetElixir() > (2000 - 30*50):
                
                for i in patrol_spots:
                        if i not in base.GetListOfSignals() and base.GetElixir() > (2000 - 30*50): # we can adjust upto 30 - 26 = 4 extra robots
                                base.create_robot(i)
                                
                if base.GetElixir() > (2000 - 26*50):       
                        base.create_robot('explore')

        return