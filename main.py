from ultrasonic import Ultrasonic
from irproximity_sensor import IRProximitySensor as IR
from camera import Camera
from motors import Motors
from reflectance_sensors import ReflectanceSensors
from avoidobj import AvoidObj
from behavior_line_follower import Behaviour_line_follower
from behaviour_avoid_blue import  Behaviour_avoid_blue
from arbitrator import Arbitrator
from fuck_you_behaviour import Fuck_you_behaviour as fub
from zumo_button import ZumoButton
from bbcon import BBCON


def start():
    bbcon = BBCON()
    arb = Arbitrator(bbcon)
    motor = Motors()
    reflect_sens = ReflectanceSensors(False)
    cam = Camera()
    ir = IR()
    ultra = Ultrasonic()

    bbcon.add_motobs(motor)
    bbcon.set_arb(arb)
    bbcon.add_behaviour(AvoidObj(bbcon, ultra, ir))
    bbcon.add_behaviour(Behaviour_line_follower(bbcon, reflect_sens))
    bbcon.add_behaviour(fub(bb=bbcon))
    #behaviour avoid blue, has to be added last, do not change this, will screw up bbcon code
    bbcon.add_behaviour(Behaviour_avoid_blue(bb=bbcon, cam=cam, ultra=ultra))
    bbcon.add_sensob(reflect_sens)
    bbcon.add_sensob(ir)
    bbcon.add_sensob(ultra)
    #cam has to be added last, will screw up bbcon code if not
    bbcon.add_sensob(cam)

    butt = ZumoButton()
    butt.wait_for_press()
    print("Start zumo")

    while True:
        bbcon.run_one_timestep()
