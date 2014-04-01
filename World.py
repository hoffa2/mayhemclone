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
        return pygame.image.load(filename).convert()

    def init_platforms(self):
        platforms = pygame.sprite.Group()
        platforms.add(Platform(100, 600, self.loadimage("platform.jpeg")))
        platforms.add(Platform(1000, 600, self.loadimage("platform.jpeg")))
        return platforms

    def init_obstacles(self):
        self.obstacles = pygame.sprite.Group()
        self.obstacles.add(Obstacle(Config.Screen_Size[0]/2, Config.Screen_Size[1]/2))

    def draw(self):
        self.screen.blit(self.background, self.background.get_rect())
        self.platforms.draw(self.screen)

