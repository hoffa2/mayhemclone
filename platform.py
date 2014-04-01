import pygame
from pygame.locals import *
from config import *
import vector
pygame.init()

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.position = vector.Vector2D(x,y)
        self.image = platform
        self.imagerect = self.image.get_rect()
        self.rect  = pygame.Rect(int(x), int(y), self.imagerect[2], self.imagerect[3])
