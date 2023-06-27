import pygame
import os

class Button:
    def __init__(self, game, x:int, y:int, image:str, scale:float = 1.0):
        self.game = game
        self.x = x
        self.y = y
        self.image = pygame.image.load(os.path.join(image)).convert_alpha()
        width = self.image.get_width()
        height = self.image.get_height()
        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def check_click(self):
        pos = pygame.mouse.get_pos()
        # check if the rect collides with the mouse
        if self.rect.collidepoint(pos):
            # check if the mouse is clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return self.clicked

    def draw(self, surface):
        surface.blit(self.image, (self.x - self.width/2, self.y - self.height/2))

class MainMenu:
    def __init__(self, game):
        self.game = game
        # TODO: create more buttons, for example: play_button
        self.buttons = []

    def tick_menu(self):
        pass
    def draw_menu(self):
        pass

class GameMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = []

    def tick_menu(self):
        pass
    def draw_menu(self):
        pass

class ResumeMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = []

    def tick_menu(self):
        pass
    def draw_menu(self):
        pass

class SettingsMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = []

    def tick_menu(self):
        pass
    def draw_menu(self):
        pass