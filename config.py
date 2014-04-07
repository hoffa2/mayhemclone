""" A class to contain the configuration of the game.
.. Authors: Helge Hoff & Øystein Tveito
"""
import pygame
import vector

class Config(object):
        """This class holds the config for the game mayhem"""
        Screen_Size = (1300, 700)
        height = Screen_Size[0]
        width = Screen_Size[1]
        platform1 = (height/1.1, width/2)
        platform2 = (width/20 ,width/2)
        middle_of_screen = vector.Vector(Screen_Size[0]/2, Screen_Size[1]/2)
        score = 0
        defaultlives = 100
        defaultfuel  = 500
        bulletcount = 100
