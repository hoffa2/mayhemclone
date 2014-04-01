import pygame
import vector

class Config(object):
        Screen_Size = (1300,700)
        height = Screen_Size[0]
        width = Screen_Size[1]
        platform1 = (height/15, 650)
        platform2 = (height/1.3 ,650)
        middle_of_screen = vector.Vector(Screen_Size[0]/2, Screen_Size[1]/2)
        score = 0
        defaultlives = 100
        defaultfuel  = 500
