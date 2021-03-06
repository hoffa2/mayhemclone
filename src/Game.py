""" A class to contain the game.
.. Authors: Helge Hoff & Oystein Tveito
"""
from config import Config
import pygame
from World import World
from Player import Player

class Game(object):
	""" This is the main class for the game Mayhem """
	def __init__(self):
		""" Initialize the game """
		self.cfg = Config()
		self.clock = pygame.time.Clock()
		self.screen = World()

		self.player1 = Player(1)
		self.player2 = Player(2)

		self.stats = pygame.sprite.Group()
		self.players = pygame.sprite.Group()

		self.all = pygame.sprite.Group()

		self.players.add(self.player1.spaceship)
		self.players.add(self.player2.spaceship)

		self.stats.add(self.player1.stats)
		self.stats.add(self.player2.stats)

		self.all.add(self.player1.spaceship)
		self.all.add(self.player2.spaceship)
		self.all.add(self.player1.stats)
		self.all.add(self.player2.stats)

	def update(self):
		""" Updating all parameters for objects on screen """
		self.blackhole()
		self.statscheck()
		self.all.update()
		self.player1.shots.update(self.player1.shots, self.screen)
		self.player2.shots.update(self.player2.shots, self.screen)
		self.collision()

	def collision(self):
		""" Checking for collisions between objects on screen """
		self.spaceshipcollide()
		self.collidepad()
		self.shotcolliion()

	def shotcolliion(self):
		""" Checking if spaceship is hit by bullet """
		sprites = self.player2.shots
		for sprite in sprites:
			if pygame.sprite.collide_mask(self.player1.spaceship, sprite):
				self.player1.Lives.value -= 2
				self.player2.shots.remove(sprite)
				self.player2.score.value += 1

		sprites = self.player1.shots
		for sprite in sprites:
			if pygame.sprite.collide_mask(self.player2.spaceship, sprite):
				self.player2.Lives.value -= 2
				self.player1.shots.remove(sprite)
				self.player1.score.value += 1

	def spaceshipcollide(self):
		""" Checking collision between spaceships """
		if pygame.sprite.collide_mask(self.player1.spaceship, self.player2.spaceship):
			self.player1.Lives.value -= 10
			self.player2.Lives.value -= 10

	def blackhole(self):
		""" Resets players position and stats if caught in black hole """
		if self.player1.spaceship.pos.diff(self.screen.blackhole.pos) < 50:
			self.player1.reset()
		if self.player2.spaceship.pos.diff(self.screen.blackhole.pos) < 50:
			self.player2.reset()

	def statscheck(self):
		""" Checks the status of fuel level and lives """
		#fuelcheck
		if self.player1.fuel.value < 1:
			self.player1.lockthrust = True
		if self.player2.fuel.value < 1:
			self.player2.lockthrust = True

		#livescheck
		if self.player1.Lives.value < 1:
			self.player1.reset()
		if self.player2.Lives.value < 1:
			self.player2.reset()

	def collidepad(self):
		""" Checking if spaceship is on its pad """
		if pygame.sprite.collide_mask(self.player1.spaceship, self.screen.platform1):
			self.player1.spaceship.on_pad = True
			if self.player1.fuel.value < 500:
				self.player1.fuel.value += 3
				self.player1.Bullets.value = 100
		else:
			self.player1.spaceship.on_pad = False
		if pygame.sprite.collide_mask(self.player2.spaceship, self.screen.platform2):
			self.player2.spaceship.on_pad = True
			if self.player2.fuel.value < 500:
				self.player2.fuel.value += 3
				self.player2.Bullets.value = 100
		else:
			self.player2.spaceship.on_pad = False



	def draw(self):
		""" Drawing all visible objects on screen """
		self.screen.draw()
		self.stats.draw(self.screen.screen)
		self.players.draw(self.screen.screen)
		self.player1.shots.draw(self.screen.screen)
		self.player2.shots.draw(self.screen.screen)
		pygame.display.flip()

	def handle_events(self):
		""" Handles all the events thrown by pygame """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
			elif event.type == pygame.USEREVENT+1:
				self.player1.lock = False
			elif event.type == pygame.USEREVENT+2:
				self.player2.lock = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.player1.thrust()
			if not self.player1.lockthrust:
				self.player1.fuel.value -= 1
		elif keys[pygame.K_DOWN]:
			self.player1.reverse()
			if not self.player1.lockthrust:
				self.player1.fuel.value -= 1
		if keys[pygame.K_LEFT]:
			self.player1.turn_left()
		elif keys[pygame.K_RIGHT]:
			self.player1.turn_right()
		if keys[pygame.K_RCTRL]:
			self.player1.fire()

		if keys[pygame.K_w]:
			self.player2.thrust()
			if not self.player2.lockthrust:
				self.player2.fuel.value -= 1
		elif keys[pygame.K_s]:
			self.player2.reverse()
			if not self.player2.lockthrust:
				self.player2.fuel.value -= 1
		if keys[pygame.K_a]:
			self.player2.turn_left()
		elif keys[pygame.K_d]:
			self.player2.turn_right()
		if keys[pygame.K_SPACE]:
			self.player2.fire()


	def run(self):
		""" Main run loop """
		self.draw()
		while(True):
			self.clock.tick(60)
			self.handle_events()

			self.update()
			self.draw()


def main():
    pygame.init()
    game = Game()
    game.run()



if __name__ == '__main__':
    main()
