import pygame
import os
import math
from vector import Vector
from Lazer import Lazer
from World import World
from config import Config
import vector

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, x, y, num, speedx = 0, speedy = 0):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector(x, y)
        self.vel = Vector(speedx, speedy)
        self.angle = self.vel
        self.lock = False
        self.platformpos = Vector(x,y)
        self.respawnpos = Vector(x, y)
        if num == 1:
            self.image = pygame.image.load(os.path.join("res", "Ship1.png"))
        elif num ==2:
            self.image = pygame.image.load(os.path.join("res", "Ship2.png"))
        self.Cimage = pygame.transform.scale(self.image, [80, 80])
        self.image = self.Cimage
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos += self.vel + self.blackhole()
        self.vel *= 0.9
        self.keepinside()
        self.image = pygame.transform.rotate(self.Cimage, math.degrees(self.angle.angle()) + 180)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def keepinside(self):
        if self.pos.x > Config.Screen_Size[0]:
            self.vel.x = -1
        elif self.pos.x < 0:
            self.vel.x = 1
        elif self.pos.y > Config.Screen_Size[1]:
            self.vel.y = -1
        elif self.pos.y < 0:
            self.vel.y = 1

    def blackhole(self):
        length = (self.pos - Config.middle_of_screen).magnitude()
        if length < 250:
            return (Config.middle_of_screen - self.pos) /length *4
        else:
            return (Config.middle_of_screen - self.pos) /(length )

    def set_pos(self):
        self.pos = self.respawnpos

    def reset(self):
        self.pos = self.respawnpos
        self.vel = Vector(0,0)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y













