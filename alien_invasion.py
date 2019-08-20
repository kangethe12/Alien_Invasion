import sys
import pygame

from settings import Settings

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
		pygame.display.set_caption("Alien Invasion")

		#set the background color
		self.bg_color=(self.settings.bg_color)

	def run_game(self):
		#Start the main loop for the game
		while True:
			#watch for keyboard and mouse events
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					sys.exit()

			#redraw the screen during each pass through the loop
			self.screen.fill(self.bg_color)

			#make the most recently drawn screen visible		
			pygame.display.flip()

if __name__=='__main__':
	#make a game instance & run the game
	ai=AlienInvasion()
	ai.run_game()