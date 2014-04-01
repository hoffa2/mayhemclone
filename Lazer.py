from pygame import *
import pygame

class Lazer(pygame.sprite.Sprite):
	def __init__(self, pos, vel):
		pygame.sprite.Sprite.__init__(self)
		self.pos = pos
		self.vel = vel.normalized()

		self.Cimage = pygame.Surface((10, 20))
		self.Cimage = self.Cimage.convert_alpha()
		pygame.draw.ellipse(self.Cimage, (255,0, 0), [0, 0, 10, 20], 2)


		self.image = self.Cimage #pygame.transform.rotate(self.Cimage, math.degrees(self.vel.angle()))
		self.rect = self.image.get_rect()
		self.rect.centerx = pos.x
		self.rect.centery = pos.y

	def update(self):
		self.pos += self.vel * 20
		self.image = pygame.transform.rotate(self.Cimage, math.degrees(self.vel.angle()) + 180)
		self.rect = self.image.get_rect()
		self.rect.centerx = self.pos.x
		self.rect.centery = self.pos.y
