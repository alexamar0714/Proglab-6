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
    reflect_sens = ReflectanceSensors(True)
    cam = Camera()
    motor = Motors()
    ir = IR()
    ultra = Ultrasonic()

    bbcon.set_arb(arb)
    bbcon.add_behaviour(AvoidObj(bbcon, ultra, ir))
    bbcon.add_behaviour(Behaviour_line_follower(bbcon, reflect_sens))
    bbcon.add_behaviour(Behaviour_avoid_blue(bb=bbcon, cam=cam, ultra=ultra))
    bbcon.add_behaviour(fub(bb=bbcon))
    bbcon.add_sensob(reflect_sens)
    bbcon.add_sensob(cam)
    bbcon.add_sensob(ir)
    bbcon.add_sensob(ultra)
    bbcon.add_motobs(motor)

    butt = ZumoButton()
    butt.wait_for_press()
    print("bug")

    while True:
        bbcon.run_one_timestep()
