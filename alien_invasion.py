import sys
import pygame

from settings import Settings
from ship import Ship

from bullet import Bullet
from aliens import Alien

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

		'''We’ll create a group in AlienInvasion to store all the live bullets
		 so we can manage the bullets that have already been fired. 
		 This group will be an instance of the pygame.sprite.Group class, 
		 which behaves like a list with some extra functionality that’s helpful when building games. 
		 We’ll use this group to draw bullets to the screen on each pass through the main loop and to update each bullet’s position.'''
		self.bullets=pygame.sprite.Group()
		self.aliens=pygame.sprite.Group()

		self._create_fleet()


	def run_game(self):
		#Start the main loop for the game
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()
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

		#shooting bullets
		elif event.key==pygame.K_SPACE:
			self._fire_bullet()
	
	#when the player releases the arrow
	def _check_keyup_events(self,event):
		#when the player releases the arrow
		if event.key==pygame.K_RIGHT:
			self.ship.moving_right=False
		elif event.key==pygame.K_LEFT:
			self.ship.moving_left=False

	def _fire_bullet(self):
		#checking if number of bullets is less than allowed
		if len(self.bullets)<=self.settings.bullets_allowed:

			#create a new bullet and add it to the bullets group
			new_bullet=Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		#the method update position of bullets and delete old bullets

		#update bullet positions
		self.bullets.update()

		#get rid of bullets that have disapeared
		for bullet in self.bullets.copy():
			if bullet.rect.bottom<=0:
				self.bullets.remove(bullet)


	def _create_fleet(self):
		'''create the fleet of aliens'''
		#create an alien & find the number of aliens in a row.
		#spacing between alien is equal to one alien
		alien=Alien(self)
		alien_width=alien.rect.width
		#we find the available space by subtracting margins on either side
		available_space_x=self.settings.screen_width-(2*alien_width)
		#finding aliens which can fit on the available space
		number_aliens_x=available_space_x//(2*alien_width)

		#create the first row of aliens
		for alien_number in range(number_aliens_x):
			self._create_alien(alien_number)
			
	def _create_alien(self,alien_number):
		#create an alien and place it in the row
		alien=Alien(self)
		alien_width=alien.rect.width
		'''we create a new alien and then set its x-coordinate value 
		to place it in the row'''
		'''Each alien is pushed to the right one alien width from the left margin. 
		Next, we multiply the alien width by 2 to account for the space each alien 
		takes up,including the empty space to its right, 
		and we multiply this amount by the alien’s position in the row.'''
		alien.x=alien_width+2*alien_width*alien_number

		#We use the alien’s x attribute to set the position of its rect.
		alien.rect.x=alien.x


		self.aliens.add(alien)

	def _update_screen(self):
		#redraw the screen during each pass through the loop
		self.screen.fill(self.settings.bg_color)
#after filling the background we draw the ship on the screen 
		self.ship.blitme()

		'''The bullets.sprites() method returns a list of all sprites
		 in the group bullets.To draw all fired bullets to the screen, 
		 we loop through the sprites in bullets and call draw_bullet() on each one '''
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		'''The draw() method requires one argument: 
		a surface on which to draw the elements from the group.'''
		self.aliens.draw(self.screen)

		#make the most recently drawn screen visible		
		pygame.display.flip()

if __name__=='__main__':
	#make a game instance & run the game
	ai=AlienInvasion()
	ai.run_game()