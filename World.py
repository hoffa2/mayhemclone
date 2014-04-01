import pygame
from pygame.locals import *
from config import Config
import vector
from platform import Platform
from obstacle import *


class World:
    def __init__(self):
        pygame.init()
        pygame.display.set_mode((1300, 700))
        self.platforms = self.init_platforms()
        self.background = pygame.transform.scale(self.loadimage("back.jpeg"), (Config.Screen_Size[0], Config.Screen_Size[1]))
        self.screen = pygame.display.get_surface()

    def loadimage(self, filename):
        return pygame.image.load(filename)

    def init_platforms(self):
        platforms = pygame.sprite.Group()
        platforms.add(Platform(Config.platform1[0], Config.platform1[1], self.loadimage("platform.png")))
        platforms.add(Platform(Config.platform2[0], Config.platform2[1], self.loadimage("platform.png")))
        return platforms

    def init_obstacles(self):
        self.obstacles = pygame.sprite.Group()
        self.obstacles.add(Obstacle(Config.Screen_Size[0]/2, Config.Screen_Size[1]/2))

    def draw(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.platforms.draw(self.screen)

