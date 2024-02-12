# Code made by troolvo

import pygame
from math import sin, cos
from sys import exit

# Custom libraries 
import Planets

# Pygame init
pygame.init()

Width = 800
Height = 500
Screen = pygame.display.set_mode((Width, Height))
Title = pygame.display.set_caption("Planet Rotation")

Image_Icon = pygame.image.load("Assets\\Icon.png")
Icon = pygame.display.set_icon(Image_Icon)

Font = pygame.font.Font("Assets\\Pixelify.ttf", 20)

# Planets models

Planet1 = Planets.Planet(400, 250, 50, (247, 152, 100), 0)
Planet2 = Planets.Planet(400, 250, 20, (23, 220, 100), 200)
Planet3 = Planets.Planet(400, 250, 20, (106, 13, 173), 120)

IsRunnning = True
while IsRunnning:

    Screen.fill((10, 52, 99))

    # Planet rotation

    ticks = pygame.time.get_ticks()
    Planet2.MovePlanet(ticks)
    Planet3.MovePlanet(-ticks)

    # Texts
    
    Planet_1 = "({0}, {1})".format(round(Planet2.Xpos, 1), round(Planet2.Ypos, 1))
    Planet_2 = "({0}, {1})".format(round(Planet3.Xpos, 1), round(Planet3.Ypos, 1))

    XText = Font.render("Planet[0] Pos: " + Planet_1, False, (255, 255, 255))
    YText = Font.render("Planet[1] Pos: " + Planet_2 , False, (255, 255, 255))

    # Keybinds events

    Events = pygame.event.get()
    for event in Events:
        if event.type == pygame.QUIT:
            IsRunnning = False
            exit()

    # Update Planets
        
    Planet1.Update(Screen, False)
    Planet2.Update(Screen, True)
    Planet3.Update(Screen, True)

    Screen.blit(XText, (10, 10))
    Screen.blit(YText, (10, 40))

    pygame.display.update()

pygame.quit()

