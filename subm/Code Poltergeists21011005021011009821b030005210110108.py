import random


def ActRobot(robot):
        up = robot.investigate_up()
        down = robot.investigate_down()
        left = robot.investigate_left()
        right = robot.investigate_right()
        sw = robot.investigate_sw()
        se = robot.investigate_se()
        nw = robot.investigate_nw()
        ne = robot.investigate_ne()
        surroundings = [up, down, left, right, sw, se, nw, ne]
        enemy_base_dim = ()
        enemy_base_x = ''
        enemy_base_y = ''
        home_base_signal = robot.GetCurrentBaseSignal()
        print(robot.GetDimensionX())

        def check_surroundings():
                for dir in surroundings:
                        if dir == 'enemy':
                                return True
        

        def setting_signal():
                '''setting signal form specific bots containing coordinates of enemy base'''
                if enemy_base_dim != ():
                        if enemy_base_dim[0] and enemy_base_dim[1] < 10 :
                                enemy_base_x = '0' + str(enemy_base_dim[0])
                                enemy_base_y = '0' + str(enemy_base_dim[1])
                                enemy_base_string = 'enemy ' +  enemy_base_x + enemy_base_y
                                robot.setSignal(enemy_base_string)

                        elif enemy_base_dim[0] < 10 and enemy_base_dim[1] >= 10:
                                enemy_base_x = '0' + str(enemy_base_dim[0])
                                enemy_base_y = str(enemy_base_dim[1])
                                enemy_base_string = 'enemy ' +  enemy_base_x + enemy_base_y
                                robot.setSignal(enemy_base_string)

                        elif enemy_base_dim[0] >= 10 and enemy_base_dim[1] >= 10:
                                enemy_base_x = str(enemy_base_dim[0])
                                enemy_base_y = str(enemy_base_dim[1])
                                enemy_base_string = 'enemy ' +  enemy_base_x + enemy_base_y
                                robot.setSignal(enemy_base_string)

                        elif enemy_base_dim[0] >= 10 and enemy_base_dim[1] < 10:
                                enemy_base_x = str(enemy_base_dim[0])
                                enemy_base_y = '0' + str(enemy_base_dim[1])
                                enemy_base_string = 'enemy ' +  enemy_base_x + enemy_base_y
                                robot.setSignal(enemy_base_string)



        def attack_enemy_base():
                '''recieving signal from home base containing enemy base coordinates and making robots deploy virus on enemy base'''
                if home_base_signal[0:6] == 'enemy ' or home_base_signal[0:6] == 'enemyp' :
                        enemy_base_x_int = int(home_base_signal[6:8])
                        enemy_base_y_int = int(home_base_signal[8:10])
                        robot_x = robot.GetPosition()[0]
                        robot_y = robot.GetPosition()[1]

                        if enemy_base_x_int > robot_x :
                                move_x_right = enemy_base_x_int - robot_x

                                for i in range(move_x_right) :
                                        if check_surroundings() :
                                                robot.DeployVirus(150)
                                        return 2


                        elif enemy_base_x_int < robot_x :
                                move_x_left = robot_x - enemy_base_x_int

                                for i in range(move_x_left) :
                                        if check_surroundings():
                                                robot.DeployVirus(150)
                                        return 4


                        else:
                                pass

                        
                        if enemy_base_y_int > robot_y :
                                move_y_down = enemy_base_y_int - robot_y

                                for i in range(move_y_down) :
                                        if check_surroundings():
                                                robot.DeployVirus(150)
                                        return 3

                                robot.DeployVirus(int(robot.GetVirus()))


                        elif enemy_base_y_int < robot_y :
                                move_y_up = robot_y - enemy_base_y_int

                                for i in range(move_y_up) :
                                        if check_surroundings():
                                                robot.DeployVirus(150)
                                        return 1

                                robot.DeployVirus(int(robot.GetVirus()))


                        else :
                                pass
        
        attack_enemy_base()

        #Bots to find enemy base
        check_enemy_base = True

        while check_enemy_base:
                if robot.GetInitialSignal() == 'check-EB-up' and robot.GetYourSignal != 'stop' :
                        if (robot.GetDimensionY()) - (robot.GetPosition())[1] == (robot.GetDimensionY() - 1):
                                robot.setSignal('stop')

                        elif up == 'enemy-base':
                                robot.DeployVirus(robot.GetVirus())
                                enemy_base_dim = (robot.GetPosition()[0],( (robot.GetPosition()[1]) - 1) )
                                check_enemy_base = False
                                setting_signal()
                        
                        elif check_surroundings():
                                robot.DeployVirus(robot.GetVirus())
                                return 1

                        
                        
                        else:
                                return 1

                if robot.GetInitialSignal() == 'check-EB-right' and robot.GetYourSignal != 'stop' :
                        if robot.GetDimensionX() - robot.GetPosition()[0] == 1 or  robot.GetDimensionX() - robot.GetPosition()[0] == 0 :
                                robot.setSignal('stop')

                        elif right == 'enemy-base':
                                robot.DeployVirus(robot.GetVirus())
                                enemy_base_dim = (robot.GetPosition()[0] + 1,( (robot.GetPosition()[1])) )
                                check_enemy_base = False
                                setting_signal()

                                
                        
                        elif check_surroundings():
                                robot.DeployVirus(robot.GetVirus())
                                return 2

                        
                        
                        else:
                                return 2

                if robot.GetInitialSignal() == 'check-EB-down' and robot.GetYourSignal != 'stop' :
                        if robot.GetDimensionY() - robot.GetPosition()[1] == 1:
                                robot.setSignal('stop')

                        elif down == 'enemy-base':
                                robot.DeployVirus(robot.GetVirus())
                                enemy_base_dim = (robot.GetPosition()[0] ,( (robot.GetPosition()[1]) + 1 ) )
                                check_enemy_base = False
                                setting_signal()

                                
                        
                        elif check_surroundings():
                                robot.DeployVirus(robot.GetVirus())
                                return 3

                        
                        
                        else:
                                return 3

                if robot.GetInitialSignal() == 'check-EB-left' and robot.GetYourSignal != 'stop' :
                        if robot.GetDimensionX() - robot.GetPosition()[0] ==( robot.GetDimensionX() - 1) or robot.GetDimensionX() - robot.GetPosition()[0] == robot.GetDimensionX():
                                robot.setSignal('stop')

                        elif left == 'enemy-base':
                                robot.DeployVirus(robot.GetVirus())
                                enemy_base_dim = (robot.GetPosition()[0] - 1,( (robot.GetPosition()[1]) ) )
                                check_enemy_base = False
                                setting_signal()

                                
                        elif check_surroundings():
                                robot.DeployVirus(robot.GetVirus())
                                return 4

                        
                        
                        else:
                                return 4

        
        setting_signal()
        
        attack_enemy_base()
                        
        #deploying virus on enemy bots/enemy base and getting coordinates of enemy base if found
        if up == 'enemy' or up == 'enemy-base':
                robot.DeployVirus(int(robot.GetVirus())*0.85)

                if up == 'enemy-base' :
                        if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0],( (robot.GetPosition()[1]) - 1) )
                                setting_signal()
                
                
        else:
                pass

        if right == 'enemy' or up == 'enemy-base':
                robot.DeployVirus(int(robot.GetVirus())*0.85)

                if right == 'enemy-base' :
                        if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0] + 1, (robot.GetPosition()[1]))
                                setting_signal()
                        
                        

        else:
                pass

        if down == 'enemy' or up == 'enemy-base':
                robot.DeployVirus(int(robot.GetVirus())*0.85)

                if down == 'enemy-base':
                        if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0],( (robot.GetPosition()[1]) + 1) )
                                setting_signal()
                        
        else:
                pass


        
        if left == 'enemy' or up == 'enemy-base':
                robot.DeployVirus(int(robot.GetVirus())*0.85)

                if left == 'enemy-base' :
                        if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0] - 1,( (robot.GetPosition()[1])))
                                setting_signal()
        else:
                pass



        #getting coordinates of enemy base from surroundings
        if sw == 'enemy-base':
                if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0] - 1,( robot.GetPosition()[1] - 1))
                                setting_signal()
        
        elif se == 'enemy-base':
                if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0] + 1,( robot.GetPosition()[1] - 1))
                                setting_signal()
        
        elif nw == 'enemy-base':
                if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0] -1 ,( robot.GetPosition()[1] + 1))
                                setting_signal()

        elif se == 'enemy-base':
                if enemy_base_dim == ():
                                enemy_base_dim = (robot.GetPosition()[0] + 1,( robot.GetPosition()[1] + 1))
                                setting_signal()



        #making sure bot doesn't land on the enemy base
        if up == 'enemy-base':
                return random.choice([2,3,4])
        
        elif right == 'enemy-base':
                return random.choice([1,3,4])
        
        elif down == 'enemy-base':
                return random.choice([1,2,4])
        
        elif left == 'enemy-base':
                return random.choice([1,2,3])
        
        else:
                return random.randint(1,4)
              





def ActBase(base):
        up = base.investigate_up()
        down = base.investigate_down()
        left = base.investigate_left()
        right = base.investigate_right()
        sw = base.investigate_sw()
        se = base.investigate_se()
        nw = base.investigate_nw()
        ne = base.investigate_ne()
        prob_enemy_base_dim = ()
        (base_x, base_y) = base.GetPosition()
        bot_signals = base.GetListOfSignals()


        def setting_signal():
                '''setting signal form specific bots containing coordinates of enemy base'''
                if prob_enemy_base_dim != ():
                        if prob_enemy_base_dim[0] and prob_enemy_base_dim[1] < 10 :
                                enemy_base_x = '0' + str(prob_enemy_base_dim[0])
                                enemy_base_y = '0' + str(prob_enemy_base_dim[1])
                                base.SetYourSignal(f'enemyp{enemy_base_x}{enemy_base_y}')

                        elif prob_enemy_base_dim[0] < 10 and prob_enemy_base_dim[1] >= 10:
                                enemy_base_x = '0' + str(prob_enemy_base_dim[0])
                                enemy_base_y = str(prob_enemy_base_dim[1])
                                base.SetYourSignal(f'enemyp{enemy_base_x}{enemy_base_y}')
                                

                        elif prob_enemy_base_dim[0] >= 10 and prob_enemy_base_dim[1] >= 10:
                                enemy_base_x = str(prob_enemy_base_dim[0])
                                enemy_base_y = str(prob_enemy_base_dim[1])
                                base.SetYourSignal(f'enemyp{enemy_base_x}{enemy_base_y}')
                                

                        elif prob_enemy_base_dim[0] >= 10 and prob_enemy_base_dim[1] < 10:
                                enemy_base_x = str(prob_enemy_base_dim[0])
                                enemy_base_y = '0' + str(prob_enemy_base_dim[1])
                                base.SetYourSignal(f'enemyp{enemy_base_x}{enemy_base_y}')
                                
        

        if base_x == 9 and base_y == 19:
                prob_enemy_base_dim = (base_x + 20, base_y)
                setting_signal()

        elif base_x == 29 and base_y == 19:
                prob_enemy_base_dim = (base_x - 20, base_y)
                setting_signal()

        elif base_x == 19:
                if base_y == 9:
                        prob_enemy_base_dim = (base_x, base_y + 20)
                        base.SetYourSignal(f'enemyp{prob_enemy_base_dim[0]}{prob_enemy_base_dim[1]}')
                        setting_signal()

                elif base_y == 29:
                        prob_enemy_base_dim = (base_x, base_y - 20)
                        base.SetYourSignal(f'enemyp{prob_enemy_base_dim[0]}{prob_enemy_base_dim[1]}')
                        setting_signal()

                else:
                        pass

        elif base_x <= 19 and base_y <= 19:
                prob_enemy_base_dim = (base_x + 20, base_y + 20)
                setting_signal()
                
        elif base_x <= 19 and base_y >= 19:
                prob_enemy_base_dim = (base_x + 20, base_y - 20)
                setting_signal()


        else:
                pass



        if len(bot_signals) > 0:
                for signal in bot_signals:
                        if signal[0:6] == 'enemy ':
                                base.SetYourSignal(signal)

        if up == 'enemy'  or down == 'enemy' or right == 'enemy'or left == 'enemy'or sw == 'enemy'or se == 'enemy'or nw == 'enemy'or ne == 'enemy' :
                base.DeployVirus(500)

        if base.GetElixir() > 700:
                base.create_robot('')
        
        if base.GetElixir() >500 and base.GetElixir() <= 700:
                base.create_robot('check-EB-up')
                base.create_robot('check-EB-right')
                base.create_robot('check-EB-down')
                base.create_robot('check-EB-left')
                

    