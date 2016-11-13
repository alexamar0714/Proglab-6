from imager2 import Imager

class Behaviour_avoid_blue():

    def __init__(self, bb=None, cam=None, ultra=None):
        self.bbcon = bb
        self.cam = cam
        self.ultra = ultra
        self.sensobs = [cam]
        self.motor_recommandations = [('b', 1, 0.5),('f', 1, 0.5),('r', 1, 0.5),('r', 1, 0.5),('r', 1, 0.5)]
        self.active_flag = False
        self.halt_request = False
        self.priority = 100
        self.match_degree = 0.0
        self.weight = self.priority*self.match_degree
        
    def get_weight(self):
        return self.weight
    
    def get_halt_request(self):
        return self.halt_request
    
    def get_motor_recc(self):
        return self.motor_recommandations

    def update_weight(self):
        self.weight = self.priority*self.match_degree

        
    def consider_deactivation(self): #determines whether there is an object w. ultra, if not deactivates
        if self.ultra.get_value()>15:
            self.active_flag = False
            self.match_degree = 0.0
        
    def consider_activation(self): #determines whether there is an object w. ultra, if there is, activates
        if self.ultra.get_value()<=30:
            self.active_flag = True


    def sense_and_act(self):
        if self.active_flag:
            print("BLUE AVOID")
            im = self.cam.get_value() #loads image from camera
            im = Imager(image=im) #creates an Imager object
            rgb = im.most_frequent_colour() # gets th most frequent pixel
            most_rgb = max(rgb[1][0],rgb[1][1], rgb[1][2]) #gets th edominant RGB colour
            print("MOST_RGB: ", rgb[0], " vs ", im.xmax * im.ymax)
            if most_rgb != rgb[1][0]: #if the dominant colour is not red
                self.match_degree = 1
                self.active_flag = False
                

    def update(self):
        self.consider_activation()
        self.sense_and_act()
        self.update_weight()


        

        
