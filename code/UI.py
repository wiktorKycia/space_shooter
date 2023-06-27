import pygame
import os

class Button:
    def __init__(self, game, x:int, y:int, image:str, scale:float = 1.0, image2:str=""):
        self.game = game
        self.x = x
        self.y = y

        self.image = pygame.image.load(os.path.join(image)).convert_alpha()

        width = self.image.get_width()
        height = self.image.get_height()

        self.image = pygame.transform.scale(self.image, (int(width * scale), int(height * scale)))

        # create an image2 if the path is not empty
        if not image2 == "":
            self.image2 = pygame.image.load(os.path.join(image2)).convert_alpha()
            self.image2 = pygame.transform.scale(self.image2, (int(width * scale), int(height * scale)))

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

        self.img = self.image

    def check_click(self):
        pos = pygame.mouse.get_pos()
        # check if the rect collides with the mouse
        if self.rect.collidepoint(pos):
            self.img = self.image2
            # check if the mouse is clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return self.clicked

    def draw(self, surface):
        surface.blit(self.img, (self.x - self.width/2, self.y - self.height/2))

class MainMenu:
    def __init__(self, game):
        self.game = game
        size = game.screen.get_size()
        self.button_play = Button(game, size[0]/2, size[1]/2, "./images/button_play.png", 1.0, "./images/button_play_hover.png")
        self.buttons = [self.button_play]

    def tick_menu(self):
        for button in self.buttons:
            if button.check_click():
                print("I'm clicked!")

    def draw_menu(self):
        for button in self.buttons:
            button.draw(self.game.screen)

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