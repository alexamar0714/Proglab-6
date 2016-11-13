import time
from camera import Camera

class BBCON():


    behaviours = []
    active_behaviours = []
    sensobs = []
    motobs = []
    ultra_detect = False
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
    
    #this method is mainly for class AvoidObj, to tell bbcon that ultrasonic has detected something
    def ultra_detected(self, booly):
        self.ultra_detect = booly
        
    def run_one_timestep(self):
        self.update_all_sensobs()
        self.update_all_behaviours()
        #since ultra has detected something, start code to activate camera and avoid_blue behaviour
        #this is done like this because the camera and avoid_blue_behaviour takes a lot of resources(time)
        if self.ultra_detect:
            print("camera is on")
            last_sens = len(self.sensobs) - 1
            last_beh = len(self.behaviours) - 1
            time.sleep(0.2)
            self.sensobs[last_sens].update()
            self.behaviours[last_beh].update()
            self.ultra_detect = False
            motor_recc, halt_req = self.arbitrator.choose_action(stochastic = False)
            self.behaviours[last_beh].weight = 0
            self.behaviours[last_beh].match_degree = 0
        else:
            motor_recc, halt_req = self.arbitrator.choose_action(stochastic = False)
        self.update_motobs(motor_recc, halt_req)
        self.reset_all_sensobs()
        

    def update_all_sensobs(self):
        #update all sensobs except for the last one, if you see in main.py, the last obj, is camera
        for ind, sensob in enumerate(self.sensobs):
            if ind == len(self.sensobs) - 1:
                continue
            else:
                sensob.update()
                
    def update_all_behaviours(self):
        #update all behaviours except for the last one, if you see in main.py, the last obj is avoid_blue
        for ind, behave in enumerate(self.behaviours):
            if ind == len(self.behaviours) - 1:
                continue
            else:
                behave.update()

    def reset_all_sensobs(self):
        for sensors in self.sensobs:
            sensors.reset()

    def update_motobs(self, motor_recc, halt_req):
        #motor_recc is a list of tuples with 3 variables = ("direction", speed, duration)
        for tuples in motor_recc:
            if halt_req or motor_recc[0] == None:
                for motobs in self.motobs:
                    #print("STOPPING")
                    motobs.stop()
            elif tuples[0] == "f":
                #print('f-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.forward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "b":
                #print('b-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.backward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "r":
                #print('r-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.right(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "l":
                #print('l-drive:', motor_recc)
                for motobs in self.motobs:
                    motobs.stop()
                    motobs.left(speed = tuples[1], dur = tuples[2])
            time.sleep(tuples[2]/10)
            



