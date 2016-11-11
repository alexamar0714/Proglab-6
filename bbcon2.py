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
            if halt_req:
                for motobs in self.motobs:
                    print("STOPPING")
                    motobs.stop()
            elif tuples[0] == "f":
                print('f-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.forward(speed = tuples[1], dur = tuples[2])
                old_l_speed = tuples[1]; old_r_speed = tuples[1]
            elif tuples[0] == "b":
                print('b-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.backward(speed = tuples[1], dur = tuples[2])
                old_l_speed = -tuples[1]; old_r_speed = -tuples[1]
            elif tuples[0] == "r":
                print('r-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.right(speed = tuples[1], dur = tuples[2])
                    old_l_speed = 0; old_r_speed = tuples[1]
            elif tuples[0] == "l":
                print('l-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.left(speed = tuples[1], dur = tuples[2])
                old_l_speed = tuples[1]; old_r_speed = 0
            elif tuples[0] == "inc_r":
                print('inc_r:', motor_recc)
                for motobs in self.motobs:
                    motobs.right(speed = old_r_speed + tuples[1], dur = old_dur)
                    motobs.left(speed = old_l_speed, dur = old_dur)
                old_r_speed = old_r_speed + tuples[1]
                old_l_speed = old_l_speed

            elif tuples[0] == "inc_l":
                print('inc_l:', motor_recc)
                for motobs in self.motobs:
                    motobs.right(speed = old_r_speed, dur = old_dur)
                    motobs.left(speed = old_l_speed + tuples[1], dur = old_dur)
                old_r_speed = old_r_speed
                old_l_speed = old_l_speed + tuples[1]





            print("sleepend")
            time.sleep(tuples[2])
            



