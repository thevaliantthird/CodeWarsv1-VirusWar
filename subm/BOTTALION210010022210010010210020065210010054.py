from random import randint
import random
import math
import string

from random import randint
import random
import math
import string


def investigate_all(th):
    a = [th.investigate_up(),
         th.investigate_ne(),
         th.investigate_right(),
         th.investigate_se(),
         th.investigate_down(),
         th.investigate_sw(),
         th.investigate_left(),
         th.investigate_nw()]
    return a


def move_x(robot, signal):
    sig = signal

    coordinate = robot.GetPosition()
    x = coordinate[0]
    y = coordinate[1]
    sig = sig[0]+str(x).zfill(2) + str(y).zfill(2)+sig[5:]
    if sig[0] == '0' and x < 20:
        sig = '2'+sig[1:]

    elif sig[0] == '0' and x > 20:
        sig = '4'+sig[1:]

    elif x == 39:
        sig = '4'+sig[1:]

    elif x == 0:
        sig = '2'+sig[1:]

    robot.setSignal(sig)
    return int(sig[0])


def move_y(robot, signal):
    sig = signal

    coordinate = robot.GetPosition()
    x = coordinate[0]
    y = coordinate[1]
    sig = sig[0]+str(x).zfill(2) + str(y).zfill(2)+sig[5:]
    if sig[0] == '0' and y < 20:
        sig = '3'+sig[1:]

    elif sig[0] == '0' and y > 20:
        sig = '1'+sig[1:]

    elif y == 39:
        sig = '1'+sig[1:]

    elif y == 0:
        sig = '3'+sig[1:]

    robot.setSignal(sig)
    return int(sig[0])


def ActRobot(robot):

    ##
    # ATTACK
    # robot.GetVirus i the total virus of the team
    # 1st if statement is for attacking the enemy base
    # 2nd elif statement is for attacking other robots
    # ##
    invstgn = investigate_all(robot)
    if invstgn.count('enemy-base') > 0:
        robot.DeployVirus(robot.GetVirus())
    elif invstgn.count('enemy') > 0 and invstgn.count('enemy') <= 2:
        robot.DeployVirus(robot.GetVirus()/2)

    elif invstgn.count('enemy') > 2:
        robot.DeployVirus(robot.GetVirus())

    rob_sig = robot.GetYourSignal()
    if len(rob_sig) == 0:
        rob_sig = robot.GetInitialSignal()

    base_sig = robot.GetCurrentBaseSignal()
    set_x = ['2', '4']
    set_y = ['1', '3']

    if base_sig[2:5] == '100':

        if rob_sig[-1] == '0':
            rob_sig = set_y[randint(0, 1)]+rob_sig[1:18]+'1'
        else:
            rob_sig = set_x[randint(0, 1)]+rob_sig[1:18]+'0'

    if base_sig[0] == 'D':
        if rob_sig[-1] == '0':
            return move_x(robot, rob_sig)
        else:
            return move_y(robot, rob_sig)

    elif base_sig[0] == 'R':
        return randint(1, 4)


def ActBase(base):
    invstgn = investigate_all(base)
    if invstgn.count('enemy') > 0:
        base.DeployVirus(base.GetVirus())

    sig = base.GetYourSignal()
    if len(sig) == 0:
        sig = 'R0'+'000'+'000000000000000'

    base_count = int(sig[2:5])
    base_count += 1

    if base_count >= 50 and base_count < 100:
        sig = 'D0'+sig[2:]
    elif base_count > 100:
        sig = 'R0'+sig[2:]
        base_count = 0

    sig = sig[0:2]+str(base_count).zfill(3)+'000000000000000'

    base.SetYourSignal(sig)

    base_cor = base.GetPosition()
    x = base_cor[0]
    y = base_cor[1]
    d_type = ['1', '2', '3', '4', '5', '6', '7', '8']

    while base.GetElixir() > 1950:
        base.create_robot('0'+str(x).zfill(2) + str(y).zfill(2) +
                          '00000000000000' + str(randint(0, 1)))

    return
