""" A class to contain the configuration of the game.
.. Authors: Helge Hoff & Oystein Tveito
"""
import pygame
import os
import math
from vector import Vector
from Lazer import Lazer
from World import World
from config import Config
import vector

class Spaceship(pygame.sprite.Sprite):
    """ loads and controlls the spaceship sprite. Functionallity to manage its behaviure is also included in this class """
    def __init__(self, x, y, num, speedx = 0, speedy = 0):
        """ initializes the spaceship """ 
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector(x, y)
        self.vel = Vector(speedx, speedy)
        self.angle = self.vel
        self.lock = False
        self.on_pad = True
        self.platformpos = Vector(x,y)
        self.respawnpos = Vector(x, y)
        if num == 1:
            self.image = pygame.image.load(os.path.join("res", "Ship1.png"))
        elif num ==2:
            self.image = pygame.image.load(os.path.join("res", "Ship2.png"))
        self.Cimage = pygame.transform.scale(self.image, [60, 60])
        self.image = self.Cimage
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.mask = pygame.mask.from_surface(self.image)
        self.scale = 1

    def update(self):
        """ Updates spaceship position"""
        #self.vel += self.blackhole()
        self.pos += self.vel + self.blackhole()
        self.vel *= 0.9
        self.keepinside()
        self.image = pygame.transform.rotozoom(self.Cimage, math.degrees(self.angle.angle()) + 180, self.scale)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def keepinside(self):
        """ Keeping ship from wandering outside of the screen bounds"""
        if self.pos.x > Config.Screen_Size[0]:
            self.vel.x = -1
        elif self.pos.x < 0:
            self.vel.x = 1
        elif self.pos.y > Config.Screen_Size[1]:
            self.vel.y = -1
        elif self.pos.y < 0:
            self.vel.y = 1

    def blackhole(self):
        """ Attraction towards the black hole"""
        if self.on_pad:
            return Vector(0,0)
        length = (self.pos - Config.middle_of_screen).magnitude()
        if length < 250:
            self.scale = length / 250
            v = Config.middle_of_screen - self.pos
            v = v.rotate(-math.pi/2) / (length / 20 + 10)
            return ((Config.middle_of_screen - self.pos) /length *2) + v
        else:
            self.scale = 1
            return (Config.middle_of_screen - self.pos) /(length )

    def set_pos(self):
        """ Resetting the position of the spaceship """
        self.pos = self.respawnpos

    def reset(self):
        """ Resets the spaceship to inital position """
        self.pos = self.respawnpos
        self.vel = Vector(0,0)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y












