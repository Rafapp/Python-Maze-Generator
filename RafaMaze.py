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
        
        def GenerateMaze():
            # Pick a random starting point
            startX = int(random.random() * height)
            startY = int(random.random() * width)

            # Make sure we don't start at the edge of the maze
            if startY == 0:
                startY += 1
            if startY == height-1:
                startY -= 1

            if startX == 0:
                startX += 1
            if startX == width-1:
                startX -= 1

            # Mark this point as path, add all 4 surrounding walls (+x, +y, -x, -y)
            maze[startX][startY] = False
            walls = []
            walls.append([startY, startX - 1])
            walls.append([startY, startX + 1])
            walls.append([startY - 1, startX])
            walls.append([startY + 1, startX])

            # Make sure surrounding blocks are walls
            maze[startY, startX - 1] = True
            maze[startY, startX + 1] = True
            maze[startY - 1, startX] = True
            maze[startY + 1, startX] = True

            # While there are still walls, pick a random one
            while walls:
                rand_wall = walls[int(random.random()*len(walls))-1]
                
            

        def RenderMaze():
            for x in range(0, len(maze)):
                for y in range(0, len(maze[0])):
                    if(maze[x][y] == True):
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, "white", cellRect)
                    else:
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, (35,39,42), cellRect)
                    pg.display.update()
        RenderMaze()


