from string import whitespace
import pygame as pg
import sys
from pygame.locals import *
import time
import random
from button import Button
from maze import Maze
from player import Player

running = True
player = maze = solve = None
# INIT
pg.init()
screen = pg.display.set_mode((1800, 900))#, pg.FULLSCREEN)
width = screen.get_width()
height = screen.get_height()

buttonFont = pg.font.Font("Fonts/MINECRAFT.TTF", int(width / 80))

generateMazeTxt = "Generate Maze"
dfsText = 'Solve DFS'
bfsText = 'Solve BFS'
# randomMouseTxt = "Random Mouse Solve"
# wallFollowerTxt = "Wall Follower Solve"
# pledgeAlgorithmTxt = "Pledge Algorithm Solve"
# tremauxAlgorithmTxt = "Tremaux Algorithm Solve"
showPath = 'Show Path'

generateMazeButton = Button(buttonFont, generateMazeTxt, (0, 0))
dfsButton = Button(buttonFont, dfsText, (generateMazeButton.rect.right + 50, 0))
bfsButton = Button(buttonFont, bfsText, (dfsButton.rect.right + 50, 0))
# randomMouseButton = Button(buttonFont, randomMouseTxt, (generateMazeButton.rect.right + 50, 0))
# wallFollowerButton = Button(buttonFont, wallFollowerTxt, (randomMouseButton.rect.right + 50, 0))
# pledgeAlgorithmButton = Button(buttonFont, pledgeAlgorithmTxt, (wallFollowerButton.rect.right + 50, 0))
# tremauxAlgorithmButton = Button(buttonFont, tremauxAlgorithmTxt, (pledgeAlgorithmButton.rect.right + 50, 0))
showPathButton = Button(buttonFont, showPath, (0, 0))
showPathButton.rect.right = width

buttons = pg.sprite.Group(generateMazeButton)#,  randomMouseButton, wallFollowerButton, pledgeAlgorithmButton, tremauxAlgorithmButton)

def GenerateMaze():
    global maze, player, solves, solve
    # NOT CENTERING IF NOT EQUILATERAL, DIMENSIONS ARE FLIPPED, FIX LATER
    maze_width = 50
    maze_height = 50
    maze_cellsize = 15

    # self, width, height, xPosition, yPosition, cellSize, screen
    maze = Maze(maze_width, maze_height, int(width / 2) - int((maze_width * maze_cellsize)/2),  int(height / 2) - int((maze_height * maze_cellsize)/2), maze_cellsize, screen)
    player = Player(maze)
    solves = {
        'dfs': player.solveDFS,
        'bfs': player.solveBFS
    }
    buttons.add(dfsButton, bfsButton)
    solve = None
    
# To be added soon! ...
def DfsSolve():
    global player, solve
    player.checked = {}
    player.stack = []
    player.turn = 0
    player.x, player.y = maze.start
    solve = 'dfs'
    
def BfsSolve():
    global player, solve
    player.checked = {}
    player.turn = 0
    player.x, player.y = maze.start
    player.queue = [[(player.x, player.y)]]
    solve = 'bfs'

def RandomMouseSolve():
    print()

def WallFollowerSolve():
    print()

def PledgeAlgorithmSolve():
    print()

def TremauxAlgorithmSolve():
    print()
    
def DrawPath():
    player.draw_path(screen)

dict = {generateMazeButton: GenerateMaze, dfsButton: DfsSolve, bfsButton: BfsSolve, showPathButton: DrawPath}#, randomMouseButton: RandomMouseSolve, wallFollowerButton: WallFollowerSolve, pledgeAlgorithmButton:PledgeAlgorithmSolve,tremauxAlgorithmButton:TremauxAlgorithmSolve}

screen.fill((35,39,42))

# Draw navbar background
navBar = pg.rect.Rect(0,0, screen.get_width(), screen.get_height() / 15)
pg.draw.rect(screen, (88,101,242), navBar)
pg.display.update()

# Render buttons
buttons.draw(screen)
buttons.update()
pg.display.update()
pg.display.set_caption("Maze Generator and Solver! : Press ESC to quit")
clock = pg.time.Clock()
#MAIN LOOP
while running:
    # Quit game on esc key
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                pg.quit()
                quit()
            else:
                player.handle_key(event.key, screen)
        elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = event.pos
                for button in buttons:
                    if button.rect.collidepoint(x, y):
                        dict[button]()
    if player:
        player.update(screen)
        if solve:
            solves[solve](screen)
        if (player.x, player.y) == maze.end:
            solve = None
            buttons.add(showPathButton)
    buttons.draw(screen)
    pg.display.update()
    clock.tick(60)
        
pg.quit()
