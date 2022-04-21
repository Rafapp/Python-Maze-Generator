from string import whitespace
import pygame as pg
import sys
from pygame.locals import *
import time
import random
from button import Button
from RafaMaze import Maze

running = True

# INIT
pg.init()
screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

size = (width, height)

buttonFont = pg.font.Font("Fonts/MINECRAFT.TTF", int(width / 80))

generateMazeTxt = "Generate Maze"
randomMouseTxt = "Random Mouse Solve"
wallFollowerTxt = "Wall Follower Solve"
pledgeAlgorithmTxt = "Pledge Algorithm Solve"
tremauxAlgorithmTxt = "Tremaux Algorithm Solve"

generateMazeButton = Button(buttonFont, generateMazeTxt, (0, 0))
randomMouseButton = Button(buttonFont, randomMouseTxt, (generateMazeButton.rect.right + 50, 0))
wallFollowerButton = Button(buttonFont, wallFollowerTxt, (randomMouseButton.rect.right + 50, 0))
pledgeAlgorithmButton = Button(buttonFont, pledgeAlgorithmTxt, (wallFollowerButton.rect.right + 50, 0))
tremauxAlgorithmButton = Button(buttonFont, tremauxAlgorithmTxt, (pledgeAlgorithmButton.rect.right + 50, 0))

buttons = pg.sprite.Group(generateMazeButton,  randomMouseButton, wallFollowerButton, pledgeAlgorithmButton, tremauxAlgorithmButton)

def GenerateMaze():
    # FOR SOME REASON HAS TO BE EQUILATERAL, FIX LATER
    maze_width = 50
    maze_height = 50

    # self, width, height, xPosition, yPosition, cellSize, screen
    rafamaze = Maze(maze_width, maze_height, int(width / 2) - int(maze_width / 2), int(height / 2) - int(maze_height / 2), 10, screen)
    

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

dict = {generateMazeButton: GenerateMaze, randomMouseButton: RandomMouseSolve, wallFollowerButton: WallFollowerSolve, pledgeAlgorithmButton:PledgeAlgorithmSolve,tremauxAlgorithmButton:TremauxAlgorithmSolve}

screen.fill((35,39,42))

# Draw navbar background
navBar = pg.rect.Rect(0,0, screen.get_width(), screen.get_height() / 15)
pg.draw.rect(screen, (88,101,242), navBar)
pg.display.update()

# Render buttons
buttons.draw(screen)
buttons.update()

#MAIN LOOP
while running:
    
    pg.display.set_caption("Maze Generator and Solver! : Press ESC to quit")
    pg.display.update()

# Quit game on esc key
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            pg.quit()
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                for button in buttons:
                    if button.rect.collidepoint(x, y):
                        dict[button]()
                        
pg.quit()
