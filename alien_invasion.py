import sys

import pygame

from settings import Settings 
from ship import Ship
from snoopy import Snoopy

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()

		self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.ship = Ship(self)

		self.snoopy = Snoopy(self)

		# Set the background color.
		self.bg_color = (135,206,250)

	# goal of method below: we’re looking for new events and updat- ing the screen on each pass through the loop.
	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watch for keyboard and mouse events.
			self._check_events()
			#Note about statement above: To call a method from within a class, use dot notation with the variable self and the name of the method. We call the method from inside the while loop in run_game().

			# Redraw the screen during each pass through the loop. 
			self._update_screen()

	# Helper methods below - indicated with the initial underscore!! Cannot call them on an instance. 
	# Note about the new method below: We make a new _check_events() method and move the lines that check whether the player has clicked to close the window into this new method.
	def _check_events(self):
		"""Respond to keypresses and mlouse events."""
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
	def _update_screen(self):
		"""Update images on the screen, and flip to the new screen."""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		self.snoopy.blitme()

		# Make the most recently drawn screen visible.
		pygame.display.flip()
		
if __name__ == '__main__':
	# Make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()

