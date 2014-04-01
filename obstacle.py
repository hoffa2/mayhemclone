import pygame
from pygame.locals import *
from config import *
import vector
pygame.init()

class Obstacle(pygame.sprite.Sprite):

    defaultradius = 100

    def __init__(self, cx, cy):
        pygame.sprite.Sprite.__init__(self)
        radius = Obstacle.defaultradius
        diameter = radius * 2
        self.pos = vector.Vector(cx,cy)
        self.image = pygame.Surface((diameter, diameter))
        self.rect = pygame.Rect(int(cx) - radius, int(cy) - radius, diameter, diameter)
