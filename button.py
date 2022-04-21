import pygame

class Button(pygame.sprite.Sprite):
    def __init__(self, font: pygame.font.Font, text : str, position : "tuple[int, int]"):
        super().__init__()
        self.set_image(font, text)
        self.rect = pygame.Rect(position[0] + 10, position[1] + 10, self.image.get_width(), self.image.get_height())

    def update(self):
        return

    def set_image(self, font : pygame.font.Font, text):
        # Text color
        text_render = font.render(text, True, 'white')
        bg = pygame.Surface((text_render.get_width(), text_render.get_height()))

        # Text background
        bg.fill((64, 78, 237))
        bg.blit(text_render, (0,0))

        # Render
        canvas = pygame.Surface((text_render.get_width() + 20, text_render.get_height() + 20))

        # Button border
        canvas.fill((64, 78, 237))
        canvas.blit(bg, (10,10))
        self.image = canvas