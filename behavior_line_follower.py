
class Behaviour_line_follower():
	def __init__(self, bb, refSens, THRESHOLD = 0.8):
		self.bbqon = bb
		self.ref_sensors = refSens
		self.THRESHOLD = THRESHOLD
		self.sensobs = [self.ref_sensors]
		self.motor_recommandations = [('f',0,0)]
		self.active_flag = True
		self.halt_request = False
		self.priority = 1000000000
		self.match_degree = 0.0
		self.weight = self.priority*self.match_degree

	def get_weight(self):
		return self.weight

	def get_motor_recc(self):
		return self.motor_recommandations

	def update_weight(self):
		self.weight = self.priority*self.match_degree

	def consider_deactivation(self, reflactance_values):
		#If all sensors show dark, the zumo has driven
		#off the line and we can deactivate
		for value in reflactance_values:
			if value < 1 - self.THRESHOLD:
				return False
		return True

	def get_halt_request(self):
		return self.halt_request


	def consider_activation(self, reflactance_values):
		#Check if the zumo has driven back on the line
		for value in reflactance_values:
			if value > 1 - self.THRESHOLD:
				return True
		return False

	def sense_and_act(self, reflactance_values):
		#Check if the sensors is on the line based on a experimental
		#THRESHOLD value. Prioritizes higher the longer away from the middle
		#the line is and recomends turning towards the middle
		if self.active_flag:
			#Low Pri
			l = reflactance_values[2]
			r = reflactance_values[3]
			if l > self.THRESHOLD or r > self.THRESHOLD:
				self.match_degree = 0.33
				if l < self.THRESHOLD:
					self.motor_recommandations = [("f",0.1,0)]
				else:
					self.motor_recommandations = [("f",0.1,0)]
				return self.motor_recommandations

			#Medium Pri
			l = reflactance_values[1]
			r = reflactance_values[4]
			if l > self.THRESHOLD or r > self.THRESHOLD:
				self.match_degree = 0.66
				if l < self.THRESHOLD:
					self.motor_recommandations = [("l",0.1,0.5)]
				else:
					self.motor_recommandations = [("r",0.1,0.5)]
				return self.motor_recommandations

			#High Pri
			l = reflactance_values[0]
			r = reflactance_values[5]
			if l > self.THRESHOLD or r > self.THRESHOLD:
				self.match_degree = 1.00
				if l < self.THRESHOLD:
					self.motor_recommandations = [("l",0.2,0.5)]
				else:
					self.motor_recommandations = [("r",0.2,0.5)]
				return self.motor_recommandations
			#Not on line
			else: 
				self.match_degree = 0.00
			

	def update(self):
		reflactance_values = self.ref_sensors.get_value()

		if self.active_flag:
			self.consider_deactivation(reflactance_values)
		else:
			self.consider_activation(reflactance_values)
		self.sense_and_act(reflactance_values)
		self.update_weight()
