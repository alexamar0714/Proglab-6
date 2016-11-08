__author__ = 'keithd'

from time import sleep
import random
import imager2 as IMR
from reflectance_sensors import ReflectanceSensors
from camera import Camera
from motors import Motors
from ultrasonic import Ultrasonic
from zumo_button import ZumoButton


## BE SURE TO RUN THESE DEMOS ON THE FLOOR or to have plenty of people guarding
## #  the edges of a table if it is run there.

# This just moves the robot around in a fixed dance pattern.  It uses no sensors.

def dancer():
    ZumoButton().wait_for_press()
    m = Motors()
    m.forward(.2,3)
    m.backward(.2,3)
    m.right(.5,3)
    m.left(.5,3)
    m.backward(.3,2.5)
    m.set_value([.5,.1],10)
    m.set_value([-.5,-.1],10)


# This tests the UV (distance) sensors.  The robot moves forward to within 10 cm of the nearest obstacle.  It
# then does a little dancing before backing up to approximately 50 cm from the nearest obstacle.

def explorer(dist=10):
    ZumoButton().wait_for_press()
    m = Motors(); u = Ultrasonic()
    while u.update() > dist:
        m.forward(.2,0.2)
    m.backward(.1,.5)
    m.left(.5,3)
    m.right(.5,3.5)
    sleep(2)
    while u.update() < dist*5:
        m.backward(.2,0.2)
    m.left(.75,5)



def random_step(motors,speed=0.25,duration=1):
    dir = random.choice(['forward','backward','left','right'])
    eval('Motors.'+ dir)(motors,speed,duration)

# This moves around randomly until it gets to a dark spot on the floor (detected with the infrared belly sensors).
# It then rotates around, snapping pictures as it goes.  It then pastes all the pictures together into a
# panoramo view, many of which may be created per "vacation".

def tourist(steps=25,shots=5,speed=.25):
    ZumoButton().wait_for_press()
    rs = ReflectanceSensors(); m = Motors(); c = Camera()
    for i in range(steps):
        random_step(m,speed=speed,duration=0.5)
        vals = rs.update()
        if sum(vals) < 1:  # very dark area
            im = shoot_panorama(c,m,shots)
            im.dump_image('vacation_pic'+str(i)+'.jpeg')

def shoot_panorama(camera,motors,shots=5):
    s = 1
    im = IMR.Imager(image=camera.update()).scale(s,s)
    rotation_time = 3/shots # At a speed of 0.5(of max), it takes about 3 seconds to rotate 360 degrees
    for i in range(shots-1):
        motors.right(0.5,rotation_time)
        im = im.concat_horiz(IMR.Imager(image=camera.update()))
    return im

def get_recc(reflactance_values):
    THRESHOLD = 0.9
    motor_recommandations = None
    l = reflactance_values[2]
    r = reflactance_values[3]
    if l > THRESHOLD or r > THRESHOLD:
        if l < THRESHOLD:
            motor_recommandations = [("l",1,100)]
        else:
            motor_recommandations = [("r",1,100)]
        return motor_recommandations
    l = reflactance_values[1]
    r = reflactance_values[4]
    if l > THRESHOLD or r > THRESHOLD:
        if l < THRESHOLD:
            motor_recommandations = [("l",1,500)]
        else:
            motor_recommandations = [("r",1,500)]
        return motor_recommandations
    l = reflactance_values[0]
    r = reflactance_values[5]
    if l > THRESHOLD or r > THRESHOLD:
        if l < THRESHOLD:
            motor_recommandations = [("l",1,1000)]
        else:
            motor_recommandations = [("r",1,1000)]
        return motor_recommandations
    else: 
        motor_recommandations = [("f",1,1000)]
   

def update_motobs(self, motor_recc, motobs):
        for tuples in motor_recc:
            if halt_req:
                for motobs in motobs:
                    motobs.stop()
            elif tuples[0] == "f":
                for motobs in motobs:
                    motobs.forward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "b":
                for motobs in motobs:
                    motobs.backward(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "r":
                for motobs in motobs:
                    motobs.right(speed = tuples[1], dur = tuples[2])
            elif tuples[0] == "l":
                for motobs in motobs:
                    motobs.left(speed = tuples[1], dur = tuples[2])
            time.wait(tuples[2]/1000)

def tourist(steps=25,shots=5,speed=.25):
    ZumoButton().wait_for_press()
    rs = ReflectanceSensors(); m = Motors();
    mr = get_recc(rs.get_value()) 
    update_motobs(mr, m)

