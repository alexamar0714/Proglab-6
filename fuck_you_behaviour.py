class Fuck_you_behaviour():
	
    def __init__(self, bb=None):
        self.bbcon = bb
        self.motor_recommandations = [('f',1,1000)]
        self.active_flag = True
        self.halt_request = False
        self.priority = 2
        self.match_degree = 1
        self.weight = self.priority*self.match_degree

    def get_weight(self):
        return self.weight

    def get_motor_recc(self):
        return self.motor_recommandations   

    def update(self):
        pass


        