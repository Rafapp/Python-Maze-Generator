from string import whitespace
import pygame as pg
import sys
from pygame.locals import *
import time
import random

# VARIABLES
BLACK   =(35, 39, 42)
WHITE   =(255,255,255)
RED     =(255,0,0)
GREEN   =(0,255,0)
BLUE    =(0,0,255)

running = True

generateMazeText = "Generate Maze"

# INIT
pg.init()
screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

size = (width, height)

buttonFont = pg.font.Font("Fonts/MINECRAFT.TTF", int(width / 40))
renderedText = buttonFont.render(generateMazeText, True, WHITE)

background = pg.Rect(0, 0, width, height)

widthButtonFactor = width / 7
heightButtonFactor = 100

#MAIN LOOP
while running:
    
    pg.display.set_caption("Rafa's Maze Generator and Solver! : Press ESC to quit")
    screen.fill(BLACK)
    pg.draw.rect(screen, WHITE, background, 50)

    # Generate maze button
    screen.blit(renderedText, (widthButtonFactor - buttonFont.size(generateMazeText)[0]/2, heightButtonFactor - buttonFont.size(generateMazeText)[1]/2))
    pg.display.update()

# Quit game on esc key
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            running = False
pg.quit()

def GenerateMaze():
    print()

def RandomMouseSolve():
    print()

def WallFollowerSolve():
    print()

def PledgeAlgorithmSolve():
    print()

def TremauxAlgorithmSolve():
    print()

def Reset():
    print()





