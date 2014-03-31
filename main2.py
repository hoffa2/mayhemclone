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
            self.gravity = vector.Vector2D()



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

                grav_x = 0 grav_y = 0 for center in self.gravcenters:
                dis = math.sqrt(abs(center.centerx - self.x)**2 + abs(center.centery - self.y)**2)
                max_dis = center.radius * PLANET_GRAVETY_WELL if(max_dis > dis):
                norm_ang = ((center.centerx - self.x)/ dis, (center.centery - self.y) /dis) if dis < center.radius:
                grav_x = 40 * -norm_ang[0]
                grav_y = 40 * -norm_ang[1]
                self.hp -= COLL_DMG break else:
                gravety = (1-( dis - center.radius) / (max_dis - center.radius)) * (MAX_GRAVITY - MIN_GRAVITY) + MIN_GRAVITY
                grav_x += gravety * norm_ang[0]
                grav_y += gravety * norm_ang[1]
                self.x += self.inertia[0] + grav_x
                self.y += self.inertia[1] + grav_y
                for station in self.space_stations:
                    if station.radius > math.sqrt((station.x - self.x)**2 + (station.y - self.y)**2):
                        if self.hp < MAX_HP: self.hp +=1





    def main():
        game = Game()
        pygame.init()
        game.run()

    if __name__ == '__main__':
        main()
