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
        self.make_maze()
        print('Maze drawn')

    def make_maze(self):
        for i in range(self.width):
            for j in range(self.height):
                rect = pg.rect.Rect(i,j,cellSize,cellSize)
                pg.draw.rect(self.screen, "white", rect)



    
    

class Cell():
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        

