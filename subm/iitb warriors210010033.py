from random import randint 


def actrobot(robot):
    if robot.getvirus() >1000:
        robot.deployvirus(200)
        init_signal =robot.getinitialsignal()
        if init_signal.find ('defender')!=1:
            base_x=int(init_signal[8;10])
            base_y=int(init_signal[10;1])
            x,y=robot.getposition()
            if x>base_x:
                return 4
            if x<base_x:
                return 2
            if y>base_y:
                return 1 
            if y<base_y:
                return 3
            if x== base x and y== base y:
                return randint(1,4)
            
            def actbase (base);
            if base. getelixir() >500:
                p=randint(0,5)
         if p!=0:
             base.creat_robot('attacker')
         else:
             x,y= base.getposition()
             msg_x=str(x)
             msg_y=str(y)
             if x<10:
                 msg_x='0'+msg_x 
                 if y<10:
                     msg_y='0'+msg_y
                     base.creat_robot('defender'+msg_x+msg_y)   
                     return     
