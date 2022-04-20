import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, text : str, position : tuple[int, int]):
        super().__init__()
        self.image = font.render(text, True, 'white')
        self.rect = pygame.Rect(position[0], position[1], self.image.get_width(), self.image.get_height())
    