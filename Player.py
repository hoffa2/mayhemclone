from spaceship import Spaceship
import math
from Lazer import Lazer
import pygame
from pygame import *
import math
from config import Config
from World import World
from Status import Status

class Player():
	def __init__(self, num):
		self.num = num
		if num == 1:
			self.textpos = (100, 50)
			self.spaceship = Spaceship(Config.platform1[0] + 100, Config.platform1[1], num, -1, -1)
		else:
			self.textpos = (Config.height - 100, 50)
			self.spaceship = Spaceship(Config.platform2[0] + 100, Config.platform2[1], num, -1, -1)
		self.shots = pygame.sprite.Group()
		self.lock = False
		self.lockthrust = False
		self.stats = self.init_stats()


	def init_stats(self):
		status = pygame.sprite.Group()
		self.fuel = Status(self.num, (self.textpos[0],self.textpos[1] + 20), "Fuel", Config.defaultfuel)
		self.Bullets = Status(self.num, (self.textpos[0], self.textpos[1] + 40), "Bullets",Config.bulletcount )
		self.Lives = Status(self.num, (self.textpos[0],self.textpos[1] + 60),  "Lives", Config.defaultlives)
		self.score = Status(self.num, (self.textpos[0],self.textpos[1]), "Score", Config.score)
		status.add(self.fuel)
		status.add(self.score)
		status.add(self.Lives)
		status.add(self.Bullets)
		return status


	def force(self, v):
		self.spaceship.vel += v

	def fire(self):
		if(self.lock or self.Bullets.value <1):
			return
		shot = Lazer(self.spaceship.pos, self.spaceship.angle)
		self.Bullets.value -= 1
		self.shots.add(shot)
		self.lock = True
		pygame.time.set_timer(USEREVENT+self.num, 200)
		#print "player", self.num, "fire"


	def thrust(self):
		if self.lockthrust:
			return
		#print "player", self.num, "thrust"
		self.spaceship.vel += (self.spaceship.vel + self.spaceship.angle).normalized()

	def turn_right(self):
		#print "player", self.num, "right"
		self.spaceship.vel = self.spaceship.vel.rotate(math.radians(4))
		self.spaceship.angle = self.spaceship.angle.rotate(math.radians(4))
		#self.spaceship.vel = Vector(math.cos(tmp.angle()),-math.sin(tmp.angle()))

	def turn_left(self):
		#print "player", self.num, "left"
		self.spaceship.vel = self.spaceship.vel.rotate(math.radians(-4))
		self.spaceship.angle = self.spaceship.angle.rotate(math.radians(-4))
		# = Vector(math.cos(tmp.angle()),-math.sin(tmp.angle()))

	def reset(self):
		self.reset_stats()
		self.lockthrust = False
		self.spaceship.reset()

	def reset_stats(self):
		list = self.stats.sprites()
		for stats in list:
			stats.value = stats.initialvalue







