import pygame
from math import sqrt, pow, sin, cos

class Planet:
    def __init__(self, Xpos, Ypos, Ratius, Color, Distance):
        self.Xpos = Xpos
        self.Ypos = Ypos

        self.Ratius = Ratius
        self.Distance = Distance
        self.Speed = 0.0002

        self.Color = Color

    def MovePlanet(self, tick):
        self.Xmove = sin(tick * self.Speed)
        self.Ymove = cos(tick * self.Speed)

        self.Xpos = 400 + (self.Xmove * self.Distance)
        self.Ypos = 250 + (self.Ymove * self.Distance)

    def Update(self, Screen, orbit):
        if orbit:
            self.Graph = pygame.draw.circle(Screen, (255, 255, 255), (400, 250), self.Distance, 3)

        self.Rect = pygame.draw.circle(Screen, self.Color, (self.Xpos, self.Ypos), self.Ratius)

