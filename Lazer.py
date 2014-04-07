from pygame import *
import pygame
import math
from config import Config
import vector
from World import World

class Lazer(pygame.sprite.Sprite):
	def __init__(self, pos, vel):
                """ Inits the lazer object.
                pos is a vector giving the starting position
                vel is a vector giving the initial velosity"""
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.vel = vel.normalized()
		self.Cimage = pygame.Surface((10, 20))
		self.Cimage = self.Cimage.convert_alpha()
		pygame.draw.ellipse(self.Cimage, (255,0, 0), [0, 0, 10, 20], 2)
		self.image = self.Cimage
		#pygame.transform.rotate(self.Cimage, math.degrees(self.vel.angle()))
		self.rect = self.image.get_rect()
		self.rect.centerx = pos.x
		self.rect.centery = pos.y
		self.mask = pygame.mask.from_surface(self.image)
		print self.mask

	def update(self, shots,screen):
                WWW
		if self.outofbounds(screen):
			shots.remove(self)
			return
		self.vel = self.vel + (self.blackhole(shots) / 20)
		self.pos += self.vel * 20
		self.image = pygame.transform.rotate(self.Cimage, math.degrees(self.vel.angle()) + 180)
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos.x
		self.rect.centery = self.pos.y

	def blackhole(self, shots):
		length = (self.pos - Config.middle_of_screen).magnitude()
		if length < 250:
			if length < 40:
				shots.remove(self)

			#self.scale = length / 250
			v = Config.middle_of_screen - self.pos
			v = v.rotate(-math.pi/2) / (length)
			return ((Config.middle_of_screen - self.pos) /length *8) + v
		else:
			return vector.Vector(0,0)
	def outofbounds(self, screen):
		if screen.backgroundrect.contains(self.rect):
			return False
		else:
			return True
