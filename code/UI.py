import pygame

class Button():
    def __init__(self, game, x, y, image, scale):
        self.game = game
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
