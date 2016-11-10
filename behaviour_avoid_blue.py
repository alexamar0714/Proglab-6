from imager2 import Imager

class Behaviour_avoid_blue():

    def __init__(self, bb=None, cam=None, ultra=None):
        self.bbcon = bb
        self.cam = cam
        self.ultra = ultra
        self.sensobs = [cam]
        self.motor_recommandations = [('b',1,1000),('f',1,1000),('r',1,1000),('r',1,1000),('r',1,1000)]
        self.active_flag = False
        self.halt_request = False
        self.priority = 1
        self.match_degree = 0.0
        self.weight = self.priority*self.match_degree

    def get_weight(self):
        return self.weight

    def get_motor_recc(self):
        return self.motor_recommandations

    def update_weight(self):
        self.weight = self.priority*self.match_degree

        
    def consider_deactivation(self):
        if self.ultra.get_value()>30:
            self.active_flag = False
            self.match_degree = 0.0
        
    def consider_activation(self):
        if self.ultra.get_value()<=30:
            self.active_flag = True


    def sense_and_act(self):
        #if blue < 50% of image, urgency low
        #after, urgency very high

        if self.active_flag:
            im = self.cam.get_value() #fra Image.open(....)
            im = Imager(image=im)
            im.display()
            rgb = im.most_frequent_colour()
            most_rgb = max(rgb[1][0], rgb[1][1], rgb[1][2])
            
            if most_rgb == rgb[1][2]: #if the dominant colour is blue
                tot_size = im.xmax * im.ymax
                if rgb[0]*2>=tot_size: #if blue is more than half the image
                    self.match_degree = 1.0
                    self.priority = 16
                else:
                    self.match_degree = (rgb[0]*2)/tot_size
            
            
        


    def update(self):
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        self.sense_and_act()
        self.update_weight()

#b = Behaviour_avoid_blue()
#b.active_flag = True
#b.sense_and_act()
        

        
