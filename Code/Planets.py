import pygame
from math import sqrt, pow, sin, cos

class Planet:
    def __init__(self, Xpos, Ypos, Ratius, Color, Outline):
        self.Xpos = Xpos
        self.Ypos = Ypos
        self.Ratius = Ratius
        self.Color = Color

        self.Outline = Outline


    def Update(self, Screen):
        self.Rect = pygame.draw.circle(Screen, self.Color, (self.Xpos, self.Ypos), self.Ratius, self.Outline)


def GetDistance(Planet1, Planet2):

    return sqrt(pow((Planet2.Xpos - Planet1.Xpos), 2) + pow((Planet2.Ypos - Planet1.Ypos), 2))




