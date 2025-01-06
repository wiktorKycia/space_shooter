import pygame


class Displayable:
    def __init__(self, image: pygame.Surface, scale: float = 1.0):
        self.image = image if not scale != 1.0 else pygame.transform.scale_by(image, scale)
        
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        
        self.hitbox = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
    
    def tick(self, x: float, y: float):
        self.hitbox.center = (x, y)
    
    def draw(self, screen: pygame.Surface, x: float, y: float):
        """
        blits the image in the current position
        :return:
        """
        screen.blit(self.image, (x - self.width / 2, y - self.height / 2))


class PathConverter:
    def __init__(self, path: str):
        self.__image: pygame.Surface = pygame.image.load(path).convert_alpha()
    
    def create(self):
        return self.__image
