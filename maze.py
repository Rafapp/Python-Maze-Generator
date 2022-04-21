import pygame as pg
mazeWidth = 500
mazeHeight = 500
cellSize = 1



class Maze():
    def __init__(self, width, height, cellSize, screen):
        self.width = width
        self.height = height
        self.cellSize = cellSize
        self.screen = screen
        print("Initialized maze")
        for i in range(500):
            for j in range(500):
                rect = pg.rect.Rect(i,j,cellSize,cellSize)
                pg.draw.rect(screen, "white", rect)
        print('Maze drawn')
                



    
    

class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        

