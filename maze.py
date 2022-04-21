from turtle import update
import pygame as pg
import random

class Maze():
    def __init__(self, width, height, xPosition, yPosition, cellSize, screen):
        clock = pg.time.Clock()

        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.screen = screen
        self.xPosition = xPosition
        self.yPosition = yPosition

        def drawWalls():
            clock.tick(1)
            for i in range(int(xPosition / cellSize), int((xPosition +  width) / cellSize)):
                for j in range(int(yPosition / cellSize), int((yPosition + height) / cellSize)):
                    rect = pg.rect.Rect(i * cellSize, j * cellSize, cellSize, cellSize)
                    rand = random.randrange(0,2)
                    if(rand):
                        pg.draw.rect(screen, "white", rect)
                        pg.display.update()
                    else:
                        pg.draw.rect(screen, (35,39,42), rect)
                    pg.display.update()
                    
        drawWalls()
                
class MazeTwo():
    def __init__(self, cellSize, maze_width, maze_height):
        self.width = maze_width - (maze_width % cellSize)
        self.height = maze_height - (maze_height % cellSize)
        self.rows = int(self.width / cellSize)
        self.cols = int(self.height / cellSize)
        self.grid = ([None] * self.rows) * self.cols
    
    def draw(self, screen):
        clock = pg.time.Clock()
        clock.tick(1)
        
        
class Cell():
    def __init__(self, x, y, cellSize):
        self.x = x
        self.y = y
        self.cellSize = cellSize
        self.walls = {"left": False, "right": False, "top": False, "bottom": False}
        self.set_image()
    
    def set_image(self):
        canvas = pg.Surface((self.cellSize, self.cellSize))
        canvas.fill('white')
        if self.walls["left"]:
            pg.draw.line(canvas, 'black', (0, 0), (0, self.cellSize))
        if self.walls["right"]:
            pg.draw.line(canvas, 'black', (self.cellSize, 0), (self.cellSize, self.cellSize))
        if self.walls["top"]:
            pg.draw.line(canvas, 'black', (0,0), (self.cellSize, 0))
        if self.walls["bottom"]:
            pg.draw.line(canvas, 'black', (0, self.cellSize), (self.cellSize, self.cellSize))
        
        

