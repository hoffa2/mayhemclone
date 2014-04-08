""" A class to contain the game.
.. Authors: Helge Hoff & Oystein Tveito
"""
import pygame
from pygame.locals import *
from config import *
import vector

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        """initializig platform object"""
        pygame.sprite.Sprite.__init__(self)
        self.position = vector.Vector(x,y)
        self.cimage = image
        self.image = pygame.transform.scale(self.cimage, [120,40])
        self.imagerect = self.image.get_rect()
        self.rect  = pygame.Rect(int(x), int(y), self.imagerect[2], self.imagerect[3])
