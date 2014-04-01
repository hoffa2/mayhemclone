import pygame
from pygame.locals import *
from config import Config
import vector
from platform import Platform
from obstacle import *


class World:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((Config.width, Config.height))
        self.platforms = self.init_platforms()
        self.backgroundimage = pygame.transform.scale(self.loadimage("background3.jpg"), (Screen_Size[0], Screen_Size[1]))
        self.screen = pygame.display.get_surface()

    def loadimage(self, filename):
        return pygame.image.load(filename).convert()

    def init_platforms(self):
        platforms = pygame.sprite.Group()
        platforms.add(Platform(100, 600, self.loadimage("platform.jpeg")))
        platforms.add(Platform(1000, 600, self.loadimage("platform.jpeg")))
        return Platforms

    def init_obstacles(self):
        self.obstacles = pygame.sprite.Group()
        self.obstacles.add(Obstacle(Config.Screen_Size[0]/2, Config.Screen_Size[1]/2))

    def draw():
        self.screen.blit(self.background, (0,0))

