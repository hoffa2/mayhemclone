import pygame



Screen_Size = (1300,700)
surface = pygame.display.set_mode(Screen_Size)
img = pygame.image.load("back.jpeg").convert()
image = pygame.transform.scale(img, (Screen_Size[0], Screen_Size[1]))
imagerect = image.get_rect()



