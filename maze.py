import pygame as pg
import random

class Maze():
    def __init__(self, width, height, xPosition, yPosition, cellSize, screen):
        clock = pg.time.Clock()
        clock.tick(1)
        
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.screen = screen
        self.xPosition = xPosition
        self.yPosition = yPosition

        def drawWalls():
            for i in range(int(xPosition / cellSize), int((xPosition +  width) / cellSize)):
                for j in range(int(yPosition / cellSize), int((yPosition + height) / cellSize)):
                    rect = pg.rect.Rect(i * cellSize, j * cellSize, cellSize, cellSize)
                    rand = random.randrange(0,2)
                    if(rand):
                        pg.draw.rect(screen, "white", rect)
                    else:
                        pg.draw.rect(screen, "black", rect)
                    
        drawWalls()
                



    
    

class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        

