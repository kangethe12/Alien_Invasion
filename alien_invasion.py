import sys
import pygame

from settings import Settings
from ship import Ship

class AlienInvasion:
	#Class to manage game assets and behavior
	def __init__(self):
		'''pygame.init() function initializes the background settings 
		that pygame needs to work properly'''
		pygame.init()

		self.settings=Settings()

		'''we call pygame.display to create a display window on which
		we will draw all the graphical elements'''
		self.screen=pygame.display.set_mode((self.settings.screen_width,
			self.settings.screen_height))

		#the code below makes the game fullscreen
		'''self.screen=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
		self.settings.screen_width=self.screen.get_rect().width
		self.settings.screen_height=self.screen.get_rect().height'''


		pygame.display.set_caption("Alien Invasion")
		#calling Ship class after the screen have been created
		#argument self here gives Ship access to the game's resources
		self.ship=Ship(self)


	def run_game(self):
		#Start the main loop for the game
		while True:
			self._check_events()
			self.ship.update()
			self._update_screen()

	def _check_events(self):
	#watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				sys.exit()
			#moving the ship to the right
			elif event.type==pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type==pygame.KEYUP:
				self._check_keyup_events(event)

	#refactoring check events
	def _check_keydown_events(self,event):
		if event.key==pygame.K_RIGHT:
			#Move the ship to the right
			self.ship.moving_right=True
			#moving the ship to the left
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=True

		#pressing Q to quit
		elif event.key==pygame.K_q:
			sys.exit()
	
	#when the player releases the arrow
	def _check_keyup_events(self,event):
		#when the player releases the arrow
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=False
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=False
	def _update_screen(self):
		#redraw the screen during each pass through the loop
		self.screen.fill(self.settings.bg_color)
#after filling the background we draw the ship on the screen 
		self.ship.blitme()

		#make the most recently drawn screen visible		
		pygame.display.flip()

if __name__=='__main__':
	#make a game instance & run the game
	ai=AlienInvasion()
	ai.run_game()