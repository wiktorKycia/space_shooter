from code.ships import *
from code.player import *
import pygame
import os

def write(game, text, x, y, font_size, color=(0, 0, 0), font_style="Arial", is_centered=False,):
    font = pygame.font.SysFont(font_style, font_size)
    rend = font.render(text, True, color)
    if is_centered is True:
        x = (game.width - rend.get_rect().width)/2
        y = (game.height - rend.get_rect().height)/2
    game.screen.blit(rend, (x, y))

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
        action = False
        pos = pygame.mouse.get_pos()
        # check if the rect collides with the mouse
        if self.rect.collidepoint(pos):
            self.img = self.image2
            # check if the mouse is clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        else:
            self.img = self.image
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

    def draw(self, surface):
        surface.blit(self.img, (self.x - self.width/2, self.y - self.height/2))

class MainMenu:
    def __init__(self, game):
        self.game = game
        size = game.screen.get_size()
        self.button_play = Button(game, size[0]/2, size[1]/2, "./images/button_play.png", 1.0, "./images/button_play_hover.png")
        self.buttons = [self.button_play]
        self.background = pygame.image.load("./images/background.png").convert_alpha()

    def tick_menu(self):
        for button in self.buttons:
            if button.check_click():
                self.game.showing = "gamemenu"

    def draw_menu(self):
        self.game.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(self.game.screen)

class GameMenu:
    def __init__(self, game):
        self.game = game
        size = game.screen.get_size()
        self.button_endless = Button(game, size[0]/5, size[1]/5, "./images/button_endless.png", 1.0, "./images/button_endless_hover.png")
        self.button_levels = Button(game, size[0]/2, size[1]/5, "./images/button_levels.png", 1.0, "./images/button_levels_hover.png")
        self.button_two_players = Button(game, size[0]*4/5, size[1]/5, "./images/button_two_players.png", 1.0, "./images/button_two_players_hover.png")
        self.button_ship = Button(game, size[0]/4, self.game.height-50, "./images/button_ship.png", 1.0, "./images/button_ship_hover.png")
        self.button_hangar = Button(game, size[0]/2, self.game.height-50, "./images/button_hangar.png", 1.0, "./images/button_hangar_hover.png")
        self.button_shop = Button(game, size[0]*3/4, self.game.height-50, "./images/button_shop.png", 1.0, "./images/button_shop_hover.png")
        self.buttons = [self.button_endless,
                        self.button_levels,
                        self.button_two_players,
                        self.button_ship,
                        self.button_hangar,
                        self.button_shop
                        ]
        self.background = pygame.image.load("./images/background.png").convert_alpha()
        self.ship = Ship1(self.game)

        # coin
        self.coin = pygame.image.load("./images/coin.png").convert_alpha()
        width = self.coin.get_width()
        height = self.coin.get_height()
        self.coin = pygame.transform.scale(self.coin, (int(width * 5), int(height * 5)))


    def tick_menu(self):
        for button in self.buttons:
            if button.check_click():
                print("click")
                # self.game.showing = "game"
    def draw_menu(self):
        self.game.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw(self.game.screen)
        self.ship.draw()
        self.game.screen.blit(self.coin, (450, 300))
        write(self.game, self.game.player.coins, 500, 300, 36, (200, 200, 200))

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