import pygame

class Button():
    def __init__(self, game, x:int, y:int, image:pygame.image, scale:float = 1.0):
        self.game = game
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
