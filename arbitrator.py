import random
class Arbitrator():
	def __init__(self, bb):
		self.bbcon = bb

	def choose_action(self, stochastic = True):
		#Chooses a winning behavior from bbqon stochastically(default) or deterministically
		#returns the behaviors motor recomandations and halt request
		behaviors = self.bbcon.get_behaviours()
		
		if not stochastic:													
			winning_behavior = max(behaviors, key=lambda x: x.get_weight())
		else:																	 
			i = 0
			_sum = sum(map(lambda x: x.get_weight(), behaviors))
			rand = random.uniform(0,_sum)
			for behavior in behaviors:
				i += behavior.get_weight()
				if rand < i:
					winning_behavior = behavior
		print(behavior)
		return behavior.get_motor_recc(), behavior.get_halt_request()
