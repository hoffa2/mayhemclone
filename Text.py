import pygame
from config import Config
from World import World

class Text(pygame.sprite.Sprite):
    def __init__(self, num, pos,name, value):
        pygame.sprite.Sprite.__init__(self)
        self.value = value
        self.initialvalue = value
        self.name = name
        self.text = str(self.name) + str(self.value)
        self.center = pos
        self.font = pygame.font.SysFont("None", 25)
        self.num = num
        self.update()

    def update(self):
        """ Rendering text """
        self.text = str(self.name) + " "+ str(self.value)
        self.image = self.font.render(self.text, 1, pygame.Color("yellow"))
        self.rect = self.image.get_rect()
        self.rect.center = self.center
