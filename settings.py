class Settings:
	'''a class to store all settings for alien invasion'''
	def __init__(self):
		'''initialize game settings'''
		#screen settings
		self.screen_width=1200
		self.screen_height=800
		self.bg_color=(230,230,230)

		#ship settings
		self.ship_speed=1.5
		self.ship_limit=3


		#bullet settings
		self.bullet_speed=1.0
		self.bullet_width=3
		self.bullet_height=15
		self.bullets_allowed=3
		self.bullet_color=(60,60,60)

		#alien's settings
		self.alien_speed=1.0
		self.fleet_drop_speed=10
		#fleet_direction of 1 rep right; -1 rep left
		self.fleet_direction=1