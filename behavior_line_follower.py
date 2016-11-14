
class Behaviour_line_follower():
	def __init__(self, bb, refSenss):
		self.bbqon = bb
		self.ref_sensors = refSens
		self.THRESHOLD = THRESHOLD
		self.sensobs = [self.ref_sensors]
		self.motor_recommandations = [('f',0,0)]
		self.active_flag = True
		self.halt_request = False
		self.priority = 2
		self.match_degree = 0.0
		self.weight = self.priority*self.match_degree

	def get_weight(self):
		return self.weight

	def get_motor_recc(self):
		return self.motor_recommandations

	def update_weight(self):
		self.weight = self.priority*self.match_degree

	def consider_deactivation(self, reflactance_values):
		#We always want to look for the line, and therfore not deactivate
		return True

	def consider_activation(self, reflactance_values):
		#We therfore dont have to consider activating
		return False

	def get_halt_request(self):
		return self.halt_request

	def sense_and_act(self, reflactance_values):
		#Checks all sensors and if we are above 50% of the max darkness limit we want to 
		#turn the zumo. If no turn recc has been given we dont want to give a rec
		#and lets the default behaviour(fob) win over this behaviour
		if self.active_flag:
			max_read = 0.5
			turn = False
			print(reflactance_values)
			for sensor in reflactance_values:
				if sensor < max_read:
					print('Sving!')
					self.match_degree = 1
					self.motor_recommandations = [('r',0.5, 1)]
					turn = True
			if not turn:
				self.match_degree = 0
				self.motor_recommandations = [('f',0,0)]

	def update(self):
		reflactance_values = self.ref_sensors.get_value()

		if self.active_flag:
			self.consider_deactivation(reflactance_values)
		else:
			self.consider_activation(reflactance_values)
		self.sense_and_act(reflactance_values)
		self.update_weight()
