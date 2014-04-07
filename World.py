import pygame
from pygame.locals import *
from config import Config
import vector
from platform import Platform
from obstacle import *
import os


class World:
    def __init__(self):
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
        return pygame.image.load(filename)

    def get_rect(self):
        return self.backgroundrect

    def add_platforms(self):
        platforms = pygame.sprite.Group()
        platforms.add(self.platform1)
        platforms.add(self.platform2)
        return platforms


    def draw(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.platforms.draw(self.screen)

