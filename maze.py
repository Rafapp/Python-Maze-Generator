from fileinput import close
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

        cell = "c"
        wall = "w"
        unvisited = "u"

        # Initialize an empty maze with all cells unvisited
        maze = []
        for y in range(0,height):
            row = []
            for x in range(0, width):
                row.append(unvisited)
            maze.append(row)

        
        def GenerateMaze():

            cell = "c"
            wall = "w"

            # Choose random point to start, and make sure we are not at edges of maze
            startY = int(random.random()*height)
            startX = int(random.random()*width)

            if (startY == 0): startY += 1
            if (startY == height-1): startY -= 1
            if (startX == 0): startX += 1
            if (startX == width-1): startX -= 1

            # Mark this starting point as a cell, add all four walls to list
            maze[startY][startX] = cell
            walls = []
            walls.append([startY - 1, startX])
            walls.append([startY, startX - 1])
            walls.append([startY, startX + 1])
            walls.append([startY + 1, startX])

            # Set these four walls from unvisited, to "wall"
            maze[startY-1][startX] = wall
            maze[startY + 1][startX] = wall

            maze[startY][startX - 1] = wall
            maze[startY][startX + 1] = wall
            
            # Helper function, check number of surrounding cells
            def surroundingCells(rand_wall):
                s_cells = 0
                if (maze[rand_wall[0]-1][rand_wall[1]] == cell or maze[rand_wall[0]+1][rand_wall[1]] == cell
                 or maze[rand_wall[0]][rand_wall[1]-1] == cell or maze[rand_wall[0]][rand_wall[1]+1] == cell):
                    s_cells += 1
                return s_cells

            # Algorithm:
            # - While there are walls, pick a random wall
            # - If only one of the two cells divided by a wall is visted, add them to the list, and
            # - make that wall a passage, and mark any unvisited cells as part of the maze

            while (walls):
                # Choose any random wall from the four-wall array
                rand_wall = walls[int(random.random()*len(walls))-1]

            # Check the wall at the bottom
                if (rand_wall[0] != height-1):
                    if (maze[rand_wall[0]+1][rand_wall[1]] == unvisited and maze[rand_wall[0]-1][rand_wall[1]] == cell):
                        s_cells = surroundingCells(rand_wall)

                        # If one max cell, mark new random wall as cell, and make a new set of walls
                        if (s_cells < 2):
                            maze[rand_wall[0]][rand_wall[1]] = cell

                            # Change the value of the cells to walls to repeat the loop
                            # Bottom
                            if (rand_wall[0] != height-1):
                                if (maze[rand_wall[0]+1][rand_wall[1]] != cell) : maze[rand_wall[0]+1][rand_wall[1]] = wall
                                if ([rand_wall[0]+1, rand_wall[1]] not in walls) : walls.append([rand_wall[0]+1, rand_wall[1]])
                            # Right
                            if (rand_wall[1] != 0):
                                if (maze[rand_wall[0]][rand_wall[1]-1] != cell) : maze[rand_wall[0]][rand_wall[1]-1] = wall
                                if ([rand_wall[0], rand_wall[1]-1] not in walls) : walls.append([rand_wall[0], rand_wall[1]-1])
                            # Left
                            if (rand_wall[1] != width-1):
                                if (maze[rand_wall[0]][rand_wall[1]+1] != cell) : maze[rand_wall[0]][rand_wall[1]+1] = wall
                                if ([rand_wall[0], rand_wall[1]+1] not in walls) : walls.append([rand_wall[0], rand_wall[1]+1])

                        # Delete walls from the list, and repeat the loop
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]) : walls.remove(wall)
                        continue

                # Check the wall at the top
                if (rand_wall[0] != 0):
                    if (maze[rand_wall[0]-1][rand_wall[1]] == unvisited and maze[rand_wall[0]+1][rand_wall[1]] == cell):
                        s_cells = surroundingCells(rand_wall)

                        # If one max cell, mark new random wall as cell, and make a new set of walls
                        if (s_cells < 2):
                            maze[rand_wall[0]][rand_wall[1]] = cell

                            # Change the value of the cells to walls to repeat the loop
                            # Top
                            if (rand_wall[0] != 0):
                                if (maze[rand_wall[0]-1][rand_wall[1]] != cell) : maze[rand_wall[0]-1][rand_wall[1]] = wall
                                if ([rand_wall[0]-1, rand_wall[1]] not in walls) : walls.append([rand_wall[0]-1, rand_wall[1]])

                            # Left
                            if (rand_wall[1] != 0):
                                if (maze[rand_wall[0]][rand_wall[1]-1] != cell) : maze[rand_wall[0]][rand_wall[1]-1] = wall
                                if ([rand_wall[0], rand_wall[1]-1] not in walls) : walls.append([rand_wall[0], rand_wall[1]-1])

                            # Right
                            if (rand_wall[1] != width-1):
                                if (maze[rand_wall[0]][rand_wall[1]+1] != cell) : maze[rand_wall[0]][rand_wall[1]+1] = wall
                                if ([rand_wall[0], rand_wall[1]+1] not in walls) : walls.append([rand_wall[0], rand_wall[1]+1])

                        # Delete walls from the list, and repeat the loop
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)
                        continue

                # Check the wall at the right
                if (rand_wall[1] != width-1):
                    if (maze[rand_wall[0]][rand_wall[1]+1] == unvisited and maze[rand_wall[0]][rand_wall[1]-1] == cell):
                        s_cells = surroundingCells(rand_wall)

                        # If one max cell, mark new random wall as cell, and make a new set of walls
                        if (s_cells < 2):
                            maze[rand_wall[0]][rand_wall[1]] = cell

                            # Change the value of the cells to walls to repeat the loop
                            if (rand_wall[1] != width-1):
                                if (maze[rand_wall[0]][rand_wall[1]+1] != cell) : maze[rand_wall[0]][rand_wall[1]+1] = wall
                                if ([rand_wall[0], rand_wall[1]+1] not in walls) : walls.append([rand_wall[0], rand_wall[1]+1])
                            if (rand_wall[0] != height-1):
                                if (maze[rand_wall[0]+1][rand_wall[1]] != cell) : maze[rand_wall[0]+1][rand_wall[1]] = wall
                                if ([rand_wall[0]+1, rand_wall[1]] not in walls) : walls.append([rand_wall[0]+1, rand_wall[1]])
                            if (rand_wall[0] != 0):	
                                if (maze[rand_wall[0]-1][rand_wall[1]] != cell) : maze[rand_wall[0]-1][rand_wall[1]] = wall
                                if ([rand_wall[0]-1, rand_wall[1]] not in walls) : walls.append([rand_wall[0]-1, rand_wall[1]])

                        # Delete walls from the list, and repeat the loop
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]) : walls.remove(wall)
                        continue

                # Check the wall at the left
                if (rand_wall[1] != 0):
                    if (maze[rand_wall[0]][rand_wall[1]-1] == unvisited and maze[rand_wall[0]][rand_wall[1]+1] == cell):
                        s_cells = surroundingCells(rand_wall)

                        # If one max cell, mark new random wall as cell, and make a new set of walls
                        if (s_cells < 2):
                            maze[rand_wall[0]][rand_wall[1]] = cell

                            # Change the value of the cells to walls to repeat the loop
                            # Top
                            if (rand_wall[0] != 0):
                                if (maze[rand_wall[0]-1][rand_wall[1]] != cell): maze[rand_wall[0]-1][rand_wall[1]] = wall
                                if ([rand_wall[0]-1, rand_wall[1]] not in walls): walls.append([rand_wall[0]-1, rand_wall[1]])
                            # Bottom
                            if (rand_wall[0] != height-1):
                                if (maze[rand_wall[0]+1][rand_wall[1]] != cell) : maze[rand_wall[0]+1][rand_wall[1]] = wall
                                if ([rand_wall[0]+1, rand_wall[1]] not in walls):  walls.append([rand_wall[0]+1, rand_wall[1]])
                            # Left
                            if (rand_wall[1] != 0):	
                                if (maze[rand_wall[0]][rand_wall[1]-1] != cell): maze[rand_wall[0]][rand_wall[1]-1] = wall
                                if ([rand_wall[0], rand_wall[1]-1] not in walls): walls.append([rand_wall[0], rand_wall[1]-1])
                        
                        # Delete walls from the list, and repeat the loop
                        for wall in walls:
                            if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                                walls.remove(wall)
                        continue

                # Remove the wall
                for wall in walls:
                    if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]) : walls.remove(wall)

        # Make any unvisited cells into walls
        def FillUnvisitedAsWalls():
            for i in range(0, height):
                for j in range(0, width):
                    if (maze[i][j] == unvisited):
                        maze[i][j] = wall

        # Create an entrance and an exit to make the maze solvable
        def EnsureSolvability():
            # Create bottom right entrance
            for i in range(width-1, 0, -1):
                if (maze[height-2][i] == cell):
                    maze[height-1][i] = cell
                    break
            # Create top left entry path
            for i in range(0, width):
                if (maze[1][i] == cell):
                    maze[0][i] = cell
                    break
                
        def RenderMaze():
            for x in range(0, len(maze)):
                for y in range(0, len(maze[0])):
                    # If unvisited draw in red
                    if(maze[x][y] == unvisited):
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, "red", cellRect)

                    # If path, draw in background color
                    elif(maze[x][y] == cell):
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, (35,39,42), cellRect)

                    # If wall, draw in white
                    else:
                        cellRect = pg.rect.Rect(xPosition + (x * cellSize), yPosition + (y * cellSize), cellSize, cellSize)
                        pg.draw.rect(screen, "white", cellRect)
                    pg.display.update()

        
        # Render unvisited maze
        RenderMaze()

        # Generate and render maze
        GenerateMaze()
        RenderMaze()

        # Render wall filling
        FillUnvisitedAsWalls()
        RenderMaze()

        # Render adding the entrance and exit paths
        EnsureSolvability()
        RenderMaze()
        


