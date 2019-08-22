import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""a class to manage bullets fired from the ship"""
	def __init__(self, ai_game):
		#create a bullet object at the ship's current position

		'''To create a bullet instance, __init__() needs the current instance of 
		AlienInvasion, and we call super() to inherit properly from Sprite.'''
		super().__init__()
		self.screen=ai_game.screen
		self.settings=ai_game.settings
		self.color=self.settings.bullet_color

		#create a bullet rect at (0,0) and then set correctposition
		self.rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)

		'''we set the bullet’s midtop attribute to match the ship’s midtop attribute. 
		This will make the bullet emerge from the top of the ship, 
		making it look like the bullet is fired from the ship.'''
		self.rect.midtop=ai_game.ship.rect.midtop

		#store the bullet's position as a decimal value
		self.y=float(self.rect.y)

	def update(self):
		#move the bullet up the screen
		#update the decimal position of the bullet
		self.y-=self.settings.bullet_speed
		#update the rect position
		self.rect.y=self.y

	def draw_bullet(self):
		#draw the bullet to the screen
		pygame.draw.rect(self.screen,self.color,self.rect)