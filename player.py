import pygame
from maze import Maze


class Player(pygame.sprite.Sprite):
    def __init__(self, maze: Maze, *groups: pygame.sprite.AbstractGroup) -> None:
        super().__init__(*groups)
        self.maze = maze
        self.x, self.y = maze.start
        self.font: pygame.font.Font = pygame.font.Font("Fonts/MINECRAFT.TTF", int(maze.cellSize / 2))
        self.image = pygame.Surface((maze.cellSize, maze.cellSize))
        self.image.fill('green')
        self.checked = {}
        
        self.turn = 1
        
    def handle_key(self, key, screen: pygame.Surface):        
        if key in {pygame.K_LEFT, pygame.K_a} and self.maze.grid[self.x - 1][self.y] == 'c':
            self.__handle_move(screen)
            self.x -= 1
        elif key in {pygame.K_RIGHT, pygame.K_d} and self.maze.grid[self.x + 1][self.y] == 'c':
            self.__handle_move(screen)
            self.x += 1
        elif key in {pygame.K_UP, pygame.K_w} and self.maze.grid[self.x][self.y - 1] == 'c':
            self.__handle_move(screen)
            self.y -= 1
        elif key in {pygame.K_DOWN, pygame.K_s} and self.maze.grid[self.x][self.y + 1] == 'c':
            self.__handle_move(screen)
            self.y += 1
            
    def solveDFS(self, screen):
        if (self.x, self.y) != self.maze.end:
            if self.x + 1 < len(self.maze.grid) and self.maze.grid[self.x + 1][self.y] == 'c' and (self.x + 1, self.y) not in self.checked: 
                self.__handle_move(screen)
                self.x += 1
                self.stack.append((self.x, self.y))
            elif self.x - 1 >= 0 and self.maze.grid[self.x - 1][self.y] == 'c' and (self.x - 1, self.y) not in self.checked: 
                self.__handle_move(screen)
                self.x -= 1
                self.stack.append((self.x, self.y))
            elif self.y + 1 < len(self.maze.grid[0]) and self.maze.grid[self.x][self.y + 1] == 'c' and (self.x, self.y + 1) not in self.checked:
                self.__handle_move(screen)
                self.y += 1
                self.stack.append((self.x, self.y))
            elif self.y - 1 >= 0 and self.maze.grid[self.x][self.y - 1] == 'c' and (self.x, self.y - 1) not in self.checked:
                self.__handle_move(screen)
                self.y -= 1
                self.stack.append((self.x, self.y))
            elif self.stack:
                self.__handle_move(screen)
                self.stack.pop(-1)
                self.x, self.y = self.stack[-1]
            
        
    def update(self, screen: pygame.Surface, *args, **kwargs) -> None:
        self.rect = pygame.rect.Rect(self.maze.xPosition + (self.x * self.maze.cellSize), self.maze.yPosition + (self.y * self.maze.cellSize), self.maze.cellSize, self.maze.cellSize)
        screen.blit(self.image, self.rect)
        return super().update(*args, **kwargs)
    
    
    def __handle_move(self, screen):
        if (self.x, self.y) not in self.checked:
            turn = self.turn
            self.turn += 1
        else:
            turn = self.checked[(self.x, self.y)]
        blank = pygame.Surface((self.maze.cellSize, self.maze.cellSize))
        blank.fill((35,39,42))
        num_text: pygame.Surface = self.font.render(str(turn), False, 'green')
        num_rect = num_text.get_rect()
        num_rect.center = blank.get_rect().center
        blank.blit(num_text, num_rect)
        blank_rect = pygame.rect.Rect(self.maze.xPosition + (self.x * self.maze.cellSize), self.maze.yPosition + (self.y * self.maze.cellSize), self.maze.cellSize, self.maze.cellSize)
        screen.blit(blank, blank_rect)
        self.checked[(self.x, self.y)] = turn