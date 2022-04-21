from turtle import width
import pygame as pg
import random

class Maze():
    def __init__(self, width, height, xPosition, yPosition, cellSize, screen):
        self.width = width
        self.height = height
        self.xPosition = xPosition
        self.yPosition = yPosition
        self.cellSize = cellSize
        self.screen = screen
        
        maze = [[True for x in range(width)] for y in range(height)]
        
        def RenderMaze():
            for x in range(0, width):
                for y in range(0, height):
                    if(maze[x][y] == True):
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, "white", cellRect)
                    else:
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, (35,39,42), cellRect)
                    pg.display.update()
        RenderMaze()


