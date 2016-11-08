import time
from ultrasonic import Ultrasonic
from irproximity_sensor import IRProximitySensor
from camera import Camera
from motors import Motors
from reflectance_sensors import ReflectanceSensors
from avoidobj import AvoidObj
from behavior_line_follower import Behavior_line_follower
from behaviour_avoid_blue import  Behaviour_avoid_blue
from arbitrator import Arbitrator

class BBCON():


    behaviours = []
    active_behaviours = []
    sensobs = []
    motobs = []
    arbitrator = None

    def __init__(self, arbitrator):
        self.arbitrator = arbitrator


    def add_behaviour(self, behaviour):
        self.behaviours.append(behaviour)

    def add_sensob(self, sensob):
        self.sensobs.append(sensob)

    def active_behaviour(self, behaviour):
        if behaviour not in self.active_behaviours:
            self.active_behaviours.append(behaviour)

    def deactivate_behaviour(self, behaviour):
        if behaviour in self.active_behaviours:
            self.active_behaviours.remove(behaviour)


    def run_one_timestep(self):
        self.update_all_sensobs()
        self.update_all_behaviours()
        motor_recc, halt_req = self.arbitrator.choose_action(Stochastic = True)
        self.update_motobs(motor_recc, halt_req)
        self.reset_all_sensobs()

    def update_all_sensobs(self):
        for sensors in sensobs:
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
                    motobs.stop()
            elif tuples[0] == "f":
                for motobs in self.motobs:
                    motobs.forward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "b":
                for motobs in self.motobs:
                    motobs.backward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "r":
                for motobs in self.motobs:
                    motobs.right(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "l":
                for motobs in self.motobs:
                    motobs.left(speed = tuples[1], dur = tuples[2])
            time.wait(tuples[2]/1000)



