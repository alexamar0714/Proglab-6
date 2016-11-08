
class AvoidObj():

    bbcon = None
    ir_prox = None
    ultra = None
    priority = 0
    active_flag = None
    match_degree = 0
    motor_recc = None

    def __init__(self, bbcon, ultra, ir_prox):
        self.bbcon = bbcon
        self.ultra = ultra
        self.ir_prox = ir_prox
        self.priority = 8
        self.active_flag = False
        self.match_degree = 0.0

    def get_weight(self):
        x = priority * match_degree
        return x

    def get_motor_recc(self):
        return self.motor_recc

    def consider_deactivation(self):
        if self.ultra.get_value() > 30:
            self.active_flag = False
            self.bbcon.deactivate_behaviour(self)
            self.match_degree = 0.0

    def consider_activation(self):
        if self.ultra.get_value() <= 30:
            self.update_weight()
            self.active_flag = True
            self.bbcon.deactivate_behaviour(self)

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()


    def update_weight(self): ##behaviour specific method
        dist_cm = 30
        temp_dist = self.ultra.get_value()
        sides = ir_prox.get_value()
        if temp_dist <= dist_cm:
            if sides[0]:    #left detected
                motor_recc = [("r",1, 1000)]
            elif side[1]:   #right detected
                motor_recc = [("l", 1, 1000)]
            else:           #default, no sides detected
                motor_recc = [("r", 1, 1000)]
            self.match_degree = 1.0
