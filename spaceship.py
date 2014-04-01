import pygame
import os
import math
from vector import Vector
from Lazer import Lazer
from World import World
from config import Config
import vector

class Spaceship(pygame.sprite.Sprite):


    def __init__(self, x, y, num, speedx = 1, speedy = 1):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector(x, y)
        self.vel = Vector(speedx, speedy)
        self.angle = self.vel
        if num == 1:
            self.image = pygame.image.load(os.path.join("res", "Ship1.png"))
        elif num ==2:
            self.image = pygame.image.load(os.path.join("res", "Ship2.png"))
        self.Cimage = pygame.transform.scale(self.image, [80, 80])
        self.image = self.Cimage
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

    def update(self):
        self.pos += self.vel + self.blackhole()
        self.vel *= 0.9
        print "spaceship"
        self.image = pygame.transform.rotate(self.Cimage, math.degrees(self.angle.angle()) + 180)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def blackhole(self):
        print (self.pos - Config.middle_of_screen).magnitude()
        if (self.pos - Config.middle_of_screen).magnitude() < 250:
            return (Config.middle_of_screen - self.pos) / 60
        else:
            return vector.Vector(0,0)

