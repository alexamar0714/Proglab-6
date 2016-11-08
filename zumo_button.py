__author__ = 'keithd'
import wiringpi as wp
import time
class ZumoButton():

    def __init__(self):
        wp.wiringPiSetupGpio()
        wp.pinMode(22, 0)
        wp.pullUpDnControl(22, 2)

    def wait_for_press(self):
        read_val = wp.digitalRead(22)
        while read_val:
            print("in loop") 
            read_val = wp.digitalRead(22)
            time.sleep(2)
        print("Button pressed!!")

