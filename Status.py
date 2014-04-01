import pyame
from config import Config



class Status(pygame.sprite.Sprite):
    def __init__(self):
        self.score = Config.score
        self.lives = Config.defaultlives
        self.fuel  = Config.defaultfuel

    def draw(self):

