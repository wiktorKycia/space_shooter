import pygame

class Button():
    def __init__(self, game, x:int, y:int, image:pygame.image, scale:float = 1.0):
        self.game = game
        self.x = x
        self.y = y
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
