import pygame
from pygame.locals import *
from config import *
import vector
from platform import *
from obstacle import *


class World:
    def __init__(self):
        self.obstacles = pygame.sprite.Group()
        self.background = image
        self.obstacles.add(Obstacle(Screen_Size[0]/2, Screen_Size[1]/2))
        self.platforms = pygame.sprite.Group()
        self.platforms.add(Platform(100, 600))
        self.platforms.add(Platform(1000, 600))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
            surface.blit(self.background, (0,0))
            self.platforms.draw(surface)
            pygame.display.update()




def main():
    world = World()
    pygame.init()
    world.run()

if __name__ == '__main__':
    main()
