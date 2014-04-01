from config import Config
import pygame
from World import World
class Game(object):
	def __init__(self):
		self.cfg = Config()
		self.clock = pygame.time.Clock()
		self.screen = World()

		self.shots = pygame.sprite.Group()

		self.player1 = Player(1, self.shots);
		self.player2 = Player(2, self.shots);

		self.players = pygame.sprite.Group()
		self.players.add(self.player1.spaceship)
		self.players.add(self.player2.spaceship)

	def update(self):
		self.players.update()
		self.shots.update()

	def draw(self):
		self.screen.draw()
		self.players.draw(self.screen.screen)
		self.shots.draw(self.screen.screen)
		pygame.display.flip()

	def handle_events(self):
		""" Handles all the events thrown by pygame """
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.on_exit()
				exit()
			elif event.type == pygame.USEREVENT+1:
				self.player1.lock = False
			elif event.type == pygame.USEREVENT+2:
				self.player2.lock = False

		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.player1.thrust()
		if keys[pygame.K_LEFT]:
			self.player1.turn_left()
		elif keys[pygame.K_RIGHT]:
			self.player1.turn_right()
		if keys[pygame.K_RCTRL]:
			self.player1.fire()

		if keys[pygame.K_w]:
			self.player2.thrust()
		if keys[pygame.K_a]:
			self.player2.turn_left()
		elif keys[pygame.K_d]:
			self.player2.turn_right()
		if keys[pygame.K_SPACE]:
			self.player2.fire()



	def on_exit(self):
		pass

	def run(self):
		""" Main run loop """
		self.draw()
		while(True):
			self.clock.tick(60)
			self.handle_events()

			self.update()
			self.draw()