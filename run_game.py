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
resetMazeTxt = "Reset Maze"

# INIT
pg.init()
screen = pg.display.set_mode((1920, 1080), pg.FULLSCREEN)

width = screen.get_width()
height = screen.get_height()

size = (width, height)

buttonFont = pg.font.Font("Fonts/MINECRAFT.TTF", int(width / 40))

generateMazeRender = buttonFont.render(generateMazeTxt, True, (0,0,255))
randomMouseRender = buttonFont.render(randomMouseTxt, True, (0,0,255))
wallFollowerRender = buttonFont.render(wallFollowerTxt, True, (0,0,255))
pledgeAlgorithmRender = buttonFont.render(pledgeAlgorithmTxt, True, (0,0,255))
tremauxAlgorithmRender = buttonFont.render(tremauxAlgorithmTxt, True, (0,0,255))
resetMazeRender = buttonFont.render(resetMazeTxt, True, (0,0,255))

background = pg.Rect(0, 0, width, height)

widthButtonFactor = width / 7
heightButtonFactor = 100

#MAIN LOOP
while running:
    
    pg.display.set_caption("Maze Generator and Solver! : Press ESC to quit")
    screen.fill((0,0,0))
    pg.draw.rect(screen, (0,0,255), background, 50)

    
    def BlitText(widthFactor, heightFactor, text, font, render):
        screen.blit(render, (widthFactor - font.size(text)[0]/2), heightFactor - buttonFont.size(text)[1]/2)

# Generate maze button
    BlitText(widthButtonFactor * 1, heightButtonFactor, generateMazeTxt, buttonFont, generateMazeRender)

    # Random mouse solve button
    BlitText(widthButtonFactor * 2, heightButtonFactor, randomMouseTxt, buttonFont, randomMouseRender)

    # Wall follower solve button
    BlitText(widthButtonFactor * 3, heightButtonFactor, wallFollowerTxt, buttonFont, wallFollowerRender)
    
    # Pledge algorithm solve button
    BlitText(widthButtonFactor * 4, heightButtonFactor, pledgeAlgorithmTxt, buttonFont, pledgeAlgorithmRender)

    # Tremaux algorithm solve button
    BlitText(widthButtonFactor * 5, heightButtonFactor, tremauxAlgorithmTxt, buttonFont, tremauxAlgorithmRender)

    # Reset Maze button
    BlitText(widthButtonFactor * 6, heightButtonFactor, resetMazeTxt, buttonFont, resetMazeRender)

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







