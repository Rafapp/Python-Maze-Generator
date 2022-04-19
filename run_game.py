from string import whitespace
import pygame as pg
import sys
from pygame.locals import *
import time
import random

running = True

generateMazeTxt = "Generate Maze"
randomMouseTxt = "Random Mouse Solve"
wallFollowerTxt = "Wall Follower Solve"
pledgeAlgorithmTxt = "Pledge Algorithm Solve"
tremauxAlgorithmTxt = "Tremaux Algorithm Solve"

# INIT
pg.init()
screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

size = (width, height)

buttonFont = pg.font.Font("Fonts/MINECRAFT.TTF", int(width / 40))

generateMazeRender = buttonFont.render(generateMazeTxt, True, 'white')
randomMouseRender = buttonFont.render(randomMouseTxt, True, 'white')
wallFollowerRender = buttonFont.render(wallFollowerTxt, True, 'white')
pledgeAlgorithmRender = buttonFont.render(pledgeAlgorithmTxt, True, 'white')
tremauxAlgorithmRender = buttonFont.render(tremauxAlgorithmTxt, True, 'white')

background = pg.Rect(0, 0, width, height)

widthButtonFactor = width / 7
heightButtonFactor = 100

def blit_text():
    texts = [generateMazeRender, randomMouseRender, wallFollowerRender, pledgeAlgorithmRender, tremauxAlgorithmRender]
    
    for i in range(len(texts)):
        button_width = widthButtonFactor - buttonFont.size(generateMazeTxt)[0] / 2
        button_height = heightButtonFactor - buttonFont.size(generateMazeTxt)[1] / 2
        screen.blit(generateMazeRender, (button_width, button_height * (i + 1)))
        
screen.fill('black')
blit_text()
#MAIN LOOP
while running:
    
    pg.display.set_caption("Maze Generator and Solver! : Press ESC to quit")
    pg.draw.rect(screen, 'white', background, 50)    

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







