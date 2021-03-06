""" A class to contain the configuration of the game.
.. Authors: Helge Hoff & Oystein Tveito
"""
import pygame
from pygame.locals import *
from config import Config
import vector
from platform import Platform
from obstacle import *
import os


class World:
    """ Holds the surface to be drawn on and all obects that is contained in the world that is not spawned or controlled by the player """
    def __init__(self):
        """ Initializing pygame, background and attributes in the game inviroment"""
        pygame.init()
        pygame.display.set_mode((Config.Screen_Size[0], Config.Screen_Size[1]))
        self.platform1 = Platform(Config.platform1[0] , Config.platform1[1], self.loadimage(os.path.join("res", "platform.png")))
        self.platform2 = Platform(Config.platform2[0] , Config.platform2[1], self.loadimage(os.path.join("res", "platform.png")))
        self.platforms = self.add_platforms()
        self.background = pygame.transform.scale(self.loadimage(os.path.join("res", "back.jpeg")), (Config.Screen_Size[0], Config.Screen_Size[1]))
        self.backgroundrect = self.background.get_rect()
        self.screen = pygame.display.get_surface()
        self.blackhole = Obstacle((Config.Screen_Size[0]/2 - 30), Config.Screen_Size[1]/2 - 30)

    def loadimage(self, filename):
        """ loading image """
        return pygame.image.load(filename)

    def get_rect(self):
        """ Returns the rect of the background """
        return self.backgroundrect

    def add_platforms(self):
        """ adding platforms to spritegroup """
        platforms = pygame.sprite.Group()
        platforms.add(self.platform1)
        platforms.add(self.platform2)
        return platforms


    def draw(self):
        """ Drawing background and platform """
        self.screen.blit(self.background, self.background.get_rect())
        self.platforms.draw(self.screen)

