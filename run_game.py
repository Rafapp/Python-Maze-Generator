from string import whitespace
import pygame as pg
import sys
from pygame.locals import *
import time
import random
from button import Button

running = True

# INIT
pg.init()
screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

size = (width, height)

buttonFont = pg.font.Font("Fonts/MINECRAFT.TTF", int(width / 40))

generateMazeTxt = "Generate Maze"
randomMouseTxt = "Random Mouse Solve"
wallFollowerTxt = "Wall Follower Solve"
pledgeAlgorithmTxt = "Pledge Algorithm Solve"
tremauxAlgorithmTxt = "Tremaux Algorithm Solve"

generateMazeButton = Button(buttonFont, generateMazeTxt, (0, 0))
randomMouseButton = Button(buttonFont, randomMouseTxt, (0, generateMazeButton.rect.bottom))
wallFollowerButton = Button(buttonFont, wallFollowerTxt, (0, randomMouseButton.rect.bottom))
pledgeAlgorithmButton = Button(buttonFont, pledgeAlgorithmTxt, (0, wallFollowerButton.rect.bottom))
tremauxAlgorithmButton = Button(buttonFont, tremauxAlgorithmTxt, (0, pledgeAlgorithmButton.rect.bottom))

buttons = pg.sprite.Group(generateMazeButton,  randomMouseButton, wallFollowerButton, pledgeAlgorithmButton, tremauxAlgorithmButton)

screen.fill('black')
buttons.draw(screen)
#MAIN LOOP
while running:
    
    pg.display.set_caption("Maze Generator and Solver! : Press ESC to quit")

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
    pg.display.update()

# Quit game on esc key
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            running = False
pg.quit()







