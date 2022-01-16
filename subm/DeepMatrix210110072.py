from random import randint


def ActRobot(robot):

    #investigate
    up = robot.investigate_up()
    down = robot.investigate_down()
    left = robot.investigate_left()
    right = robot.investigate_right()
    se = robot.investigate_se()
    sw = robot.investigate_sw()
    ne = robot.investigate_ne()
    nw = robot.investigate_nw()
    # robot.setSignal('')
    x, y = robot.GetPosition()
    Status = [up, right, down, left, se, sw, ne, nw]

    #attack and defend
    c = 1
    for i in Status:
        if i == 'enemy' and len(robot.GetInitialSignal()) == 0:
            robot.DeployVirus(robot.GetVirus()*0.3)
        elif i == 'enemy' and ('base' in robot.GetInitialSignal()):
            robot.DeployVirus(robot.GetVirus()*0.9)
        elif i == 'enemy-base':
            if c == 1:
                y -= 1
            elif c == 2:
                x += 1
            elif c == 3:
                y += 1
            elif c == 4:
                x -= 1
            elif c == 5:
                x += 1
                y += 1
            elif c == 6:
                x -= 1
                y += 1
            elif c == 7:
                x += 1
                y -= 1
            elif c == 8:
                x -= 1
                y -= 1
            robot.DeployVirus(robot.GetVirus() * 0.6)
            msg = "base" + "{:02d}".format(x) + "{:02d}".format(y)
            robot.setSignal(msg)
            return 0
        c += 1

    if 'base' in robot.GetInitialSignal():
        s = robot.GetInitialSignal()[4:]
        dx = int(s[0:2]) - x
        dy = y - int(s[2:4])
        if dx > 0:
            return 2
        elif dx < 0:
            return 4
        if dy > 0:
            return 1
        elif dy < 0:
            return 3
        if dx == 0 and dy == 0:
            return 0

    return randint(1,4)


def ActBase(base):

    u1 = base.investigate_up()
    d1 = base.investigate_down()
    r1 = base.investigate_right()
    l1 = base.investigate_left()
    se1 = base.investigate_se()
    sw1 = base.investigate_sw()
    ne1 = base.investigate_ne()
    nw1 = base.investigate_nw()
    base_status = [u1, r1, d1, l1, se1, sw1, ne1, nw1]

    (x1, y1) = base.GetPosition()
#guard bots
    if base.GetElixir() == 800:
        base.create_robot('base'+'{:02d}'.format(x1+1)+'{:02d}'.format(y1+1))
        base.create_robot('base'+'{:02d}'.format(x1+1)+'{:02d}'.format(y1-1))
        base.create_robot('base'+'{:02d}'.format(x1-1)+'{:02d}'.format(y1+1))
        base.create_robot('base'+'{:02d}'.format(x1-1)+'{:02d}'.format(y1-1))

    if "enemy" in base_status:
        vi = base.GetVirus()
        base.DeployVirus(vi*0.7)

    if base.GetElixir() > 800:
        base.create_robot('')

    L = base.GetListOfSignals()
    for l in L:
        if "base" in l and base.GetElixir() == 600:
            # print(l)
            base.create_robot(l)
            base.create_robot(l)
            return
