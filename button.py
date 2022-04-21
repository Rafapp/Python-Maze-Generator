import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, text : str, position : "tuple[int, int]"):
        super().__init__()
        self.set_image(font, text)
        self.rect = pygame.Rect(position[0], position[1], self.image.get_width(), self.image.get_height())

    def update(self):
        return

    def set_image(self, font : pygame.font.Font, text):
        text_render = font.render(text, True, 'white')
        bg = pygame.Surface((text_render.get_width(), text_render.get_height()))
        bg.fill('black')
        bg.blit(text_render, (0,0))
        canvas = pygame.Surface((text_render.get_width() + 4, text_render.get_height() + 4))
        canvas.fill('white')
        canvas.blit(bg, (2,2))
        self.image = canvas