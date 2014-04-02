import pygame
from config import Config
from World import World

class Status(pygame.sprite.Sprite):
    def __init__(self, num, pos):
        pygame.sprite.Sprite.__init__(self)
        self.score = Config.score
        self.lives = Config.defaultlives
        self.fuel  = Config.defaultfuel
        self.text = "Fuel " + str(self.fuel)
        self.center = pos
        self.bulletcount = 100
        self.font = pygame.font.SysFont("None", 15)
        self.num = num
        self.update()

    def update(self):
        self.text = "Fuel " + str(self.fuel)
        self.image = self.font.render(self.text, 1, pygame.Color("yellow"))
        self.rect = self.image.get_rect()
        self.rect.center = self.center


