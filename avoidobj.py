
class AvoidObj():

    bbcon = None
    ir_prox = None
    ultra = None
    priority = 0
    halt_request = False
    active_flag = None
    match_degree = 0
    motor_recc = [(None,0,0)]

    def __init__(self, bbcon, ultra, ir_prox):
        self.bbcon = bbcon
        self.ultra = ultra
        self.ir_prox = ir_prox
        self.priority = 4
        self.active_flag = False
        self.match_degree = 0.0
    
    def get_halt_request(self):
        return self.halt_request
    
    def get_weight(self):
        x = self.priority * self.match_degree
        return x

    def get_motor_recc(self):
        return self.motor_recc

    def consider_deactivation(self):
        print(self.ultra.get_value())
        if self.ultra.get_value() > 20:
            self.active_flag = False
            self.bbcon.deactivate_behaviour(self)
            self.match_degree = 0.0
        else:
            self.update_weight()

    def consider_activation(self):
        print(self.ultra.get_value())
        if self.ultra.get_value() <= 20:
            self.update_weight()
            self.active_flag = True
            self.bbcon.deactivate_behaviour(self)

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()


    def update_weight(self): ##behaviour specific method
        dist_cm = 20
        temp_dist = self.ultra.get_value()
        self.ultra.update()
        temp_dist2 = self.ultra.get_value()
        self.ultra.update()
        temp_dist3 = self.ultra.get_value()
        temp_d = temp_dist + temp_dist2 + temp_dist3
        sides = self.ir_prox.get_value()
        print('sides:',sides)
        if temp_d <= dist_cm * 3:
            if sides[0]:    #left detected
                self.motor_recc = [("r", 0.5, 1)]
            elif sides[1]:   #right detected
                self.motor_recc = [("l", 0.5, 1)]
            else:           #default, no sides detected
                self.motor_recc = [("r", 0.5, 1)]
            self.match_degree = 1.0
