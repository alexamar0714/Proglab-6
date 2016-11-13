
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
        if self.ultra.get_value() > 17:
            self.active_flag = False
            self.bbcon.deactivate_behaviour(self)
            self.match_degree = 0.0
        else:
            self.update_weight()

    def consider_activation(self):
        if self.ultra.get_value() <= 17:
            self.update_weight()
            self.active_flag = True
            self.bbcon.deactivate_behaviour(self)

    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()


    def update_weight(self): ##behaviour specific method
        dist_cm = 17 #max detecting range
        #checks ultra several times, because there are times when it randomly inputs 0 value, even though
        #nothing is there
        temp_dist = self.ultra.get_value()
        self.ultra.update()
        temp_dist2 = self.ultra.get_value()
        self.ultra.update()
        temp_dist3 = self.ultra.get_value()
        temp_d = temp_dist + temp_dist2 + temp_dist3
        sides = self.ir_prox.get_value()
        if temp_d <= dist_cm * 3:
            self.bbcon.ultra_detected(True)
            if sides[0]:    #left detected
                self.motor_recc = [("r", 0.5, 0.5)]
            elif sides[1]:   #right detected
                self.motor_recc = [("l", 0.5, 0.5)]
            else:           #default, no sides detected
                self.motor_recc = [("r", 0.5, 0.5)]
            #has not implemented the case where both are detected
            self.match_degree = 1.0
