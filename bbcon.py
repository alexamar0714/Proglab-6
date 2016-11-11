import time

class BBCON():


    behaviours = []
    active_behaviours = []
    sensobs = []
    motobs = []
    arbitrator = None

    def __init__(self):
        pass

    def set_arb(self,arb):
        self.arbitrator = arb
        
    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)
        
    def add_motobs(self, motob):
        self.motobs.append(motob)

    def get_behaviours(self):
        return self.behaviours
    def active_behaviour(self, behaviour):
        if behaviour not in self.active_behaviours:
            self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        if behaviour in self.active_behaviours:
            self.active_behaviours.remove(behaviour)


    def run_one_timestep(self):
        self.update_all_sensobs()
        self.update_all_behaviours()
        motor_recc, halt_req = self.arbitrator.choose_action(stochastic = False)
        print('motor_recc:', motor_recc)
        self.update_motobs(motor_recc, halt_req)
        print(self.active_behaviours)
        self.reset_all_sensobs()

    def update_all_sensobs(self):
        for sensors in self.sensobs:
            sensors.update()

    def update_all_behaviours(self):
        for behaviour in self.behaviours:
            behaviour.update()

    def reset_all_sensobs(self):
        for sensors in self.sensobs:
            sensors.reset()

    def update_motobs(self, motor_recc, halt_req):
        for tuples in motor_recc:
            if halt_req or motor_recc[0] == None:
                for motobs in self.motobs:
                    print("STOPPING")
                    motobs.stop()
            elif tuples[0] == "f":
                print('f-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.forward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "b":
                print('b-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.backward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "r":
                print('r-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.right(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "l":
                print('l-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.left(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "base":
                for motobs in self.motobs:
                    motobs.base(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "inc_r":
                for motobs in self.motobs:
                    motobs.inc_r(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "inc_l":
                for motobs in self.motobs:
                    motobs.inc_l(speed = tuples[1], dur = tuples[2])
            print("sleepend")
            time.sleep(tuples[2]/10)
            



