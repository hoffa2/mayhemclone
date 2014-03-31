import pygame
from pygame.locals import *
from config import *
import vector

class Obstacle(pygame.sprite.Sprite):

    defaultradius = 100

    def __init__(self, cx, cy):
        pygame.sprite.Sprite.__init__(self)
        radius = Obstacle.defaultradius
        diameter = radius * 2
        self.pos = vector.Vector2D(cx,cy)
        self.image = pygame.Surface((diameter, diameter))
        self.rect = pygame.Rect(int(cx) - radius, int(cy) - radius, diameter, diameter)

class circle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.pos = vector.Vector2D(x, y)


        class Game:
            def __init__(self):
                self.obstacles = pygame.sprite.Group()
                self.obstacles.add(Obstacle(Screen_Size[0]/2, Screen_Size[1]/2))

                def run(self):
                    while True:
                        for event in pygame.event.get():
                            if event.type == QUIT:
                                exit()
                                surface.blit(image,(0,0))
                                pygame.display.update()


def main():
    game = Game()
    pygame.init()
    game.run()

if __name__ == '__main__':
    main()
