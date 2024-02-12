# Code made by troolvo

import pygame

from math import sin, cos
from sys import exit

# Custom events
import Planets

pygame.init()

Width = 800
Height = 500
Screen = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("Planet Rotation")

Image_Icon = pygame.image.load("Assets\\Icon.png")
Icon = pygame.display.set_icon(Image_Icon)

Font = pygame.font.Font("Assets\\Pixelify.ttf", 20)

# Planets and planet constants

Distance1, Distance2 = 200, 120
Speed = 0.0005
Direction = 1

Planet1 = Planets.Planet(400, 250, 50, (247, 152, 100), 0)
Planet2 = Planets.Planet(Planet1.Xpos + Distance1, 250, 20, (23, 220, 100), 0)
Planet3 = Planets.Planet(Planet1.Xpos + 120, 250, 20, (106, 13, 173), 0)

Planet_Distance = Planets.GetDistance(Planet1, Planet2)
Planet_Distance1 = Planets.GetDistance(Planet1, Planet3)

Graph = Planets.Planet(400, 250, Planet_Distance, (255, 255, 255), 3)
Graph1 = Planets.Planet(400, 250, Planet_Distance1, (255, 255, 255), 3)


IsRunnning = True
while IsRunnning:
    Screen.fill((10, 52, 99))

    # Planet rotation
    
    ticks = pygame.time.get_ticks()
    Xmove = sin(ticks * Speed)
    Ymove = cos(ticks * Speed)

    Planet2.Xpos = Planet1.Xpos + (Xmove * Distance1)
    Planet2.Ypos = Planet1.Ypos + (Ymove * Distance1)

    Planet3.Xpos = Planet1.Xpos + (-Xmove * Distance2)
    Planet3.Ypos = Planet1.Ypos + (Ymove * Distance2)

    # Texts
    XText = Font.render("X Pos: " + str(round(Xmove, 2)), False, (255, 255, 255))
    YText = Font.render("Y Pos: " + str(round(Ymove, 2)), False, (255, 255, 255))

    # Keybinds events
    Events = pygame.event.get()
    for event in Events:
        if event.type == pygame.QUIT:
            IsRunnning = False
            exit()

        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                Direction *= -1
        """

    # Update Planets
    Graph.Update(Screen)
    Graph1.Update(Screen)

    Planet1.Update(Screen)
    Planet2.Update(Screen)
    Planet3.Update(Screen)

    Screen.blit(XText, (10, 10))
    Screen.blit(YText, (10, 40))

    pygame.display.update()

pygame.quit()
