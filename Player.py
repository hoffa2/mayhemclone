from spaceship import Spaceship
import math
from Lazer import Lazer
import pygame
from pygame import *
import math
from config import Config

class Player():
	def __init__(self, num, shotGroup):
		self.num = num
		if num == 1:
			self.spaceship = Spaceship(Config.platform1[0] + 100, Config.platform1[1], num, -1, -1)
		else:
			self.spaceship = Spaceship(Config.platform2[0] + 100, Config.platform2[1], num, -1, -1)
		self.shots = shotGroup
		self.lock = False
		#self.stats = Status()

	def update(self):
		self.spaceship.pos += self.spaceship.vel
		self.spaceship.vel *= 0.3

	def force(self, v):
		self.spaceship.vel += v

	def fire(self):
		if(self.lock):
			return
		shot = Lazer(self.spaceship.pos, self.spaceship.angle)
		self.shots.add(shot)
		self.lock = True
		pygame.time.set_timer(USEREVENT+self.num, 200)
		print "player", self.num, "fire"


	def thrust(self):
		print "player", self.num, "thrust"
		self.spaceship.vel += (self.spaceship.vel + self.spaceship.angle).normalized()

	def turn_right(self):
		print "player", self.num, "right"
		self.spaceship.vel = self.spaceship.vel.rotate(math.radians(4))
		self.spaceship.angle = self.spaceship.angle.rotate(math.radians(4))
		#self.spaceship.vel = Vector(math.cos(tmp.angle()),-math.sin(tmp.angle()))

	def turn_left(self):
		print "player", self.num, "left"
		self.spaceship.vel = self.spaceship.vel.rotate(math.radians(-4))
		self.spaceship.angle = self.spaceship.angle.rotate(math.radians(-4))
		# = Vector(math.cos(tmp.angle()),-math.sin(tmp.angle()))
