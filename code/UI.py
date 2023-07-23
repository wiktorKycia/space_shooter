from code.ships import *
from code.player import *
from code.general import TextButton, Clickable
import pygame
from pygame.math import *

def write(game, text, x, y, font_size, color=(0, 0, 0), font_style="Arial", is_centered=False,):
    font = pygame.font.SysFont(font_style, font_size)
    rend = font.render(text, True, color)
    if is_centered is True:
        x = (game.width - rend.get_rect().width)/2
        y = (game.height - rend.get_rect().height)/2
    game.screen.blit(rend, (x, y))

def write_on_surface(surface, text, x, y, font_size, color=(0, 0, 0), is_centered=False, font_style='Arial'):
    font = pygame.font.SysFont(font_style, font_size)
    rend = font.render(text, True, color)
    if is_centered is True:
        x = (surface.get_rect().width - rend.get_rect().width) / 2
        y = (surface.get_rect().height - rend.get_rect().height) / 2
    surface.blit(rend, (x, y))

class LevelButton(TextButton):
    def __init__(self, game, x, y, width, height, level_id:int):
        self.level_id = level_id
        self.text = f"Level {str(level_id)}"
        super().__init__(game, x, y, width, height, self.text)

class Button(Clickable):
    def __init__(self, game, x:int, y:int, path:str, scale:float = 1.0, path2:str=""):
        super().__init__(game, x, y, path, scale, path2)

class MainMenu:
    def __init__(self, game):
        self.game = game
        size = game.screen.get_size()

        self.title_image = pygame.image.load("./images/Game_title.png")
        self.title_image = pygame.transform.scale(self.title_image, (int(self.title_image.get_width() * 2), int(self.title_image.get_height() * 2)))

        self.button_play = Button(game, size[0]/2, size[1]/2, "./images/buttons/button_play.png", 1.0, "./images/buttons/button_play_hover.png")
        self.button_exit = Button(game, 50, 700, "./images/buttons/button_exit.png", 1.0, "./images/buttons/button_exit_hover.png")
        self.buttons = [
            self.button_play,
            self.button_exit
        ]
        self.background = pygame.image.load("./images/background.png").convert_alpha()

    def tick_menu(self):
        if self.button_play.check_click():
            self.game.showing = "gamemenu"
        elif self.button_exit.check_click():
            self.game.isrun = False

    def draw_menu(self):
        self.game.screen.blit(self.background, (0, 0))
        self.game.screen.blit(self.title_image, (self.game.width/2 - self.title_image.get_width()/2, 150 - self.title_image.get_height()/2))
        for button in self.buttons:
            button.draw()

class GameMenu:
    def __init__(self, game):
        self.game = game
        size = game.screen.get_size()
        self.button_endless = Button(game, size[0]/5, size[1]/5, "./images/buttons/button_endless.png", 1.0, "./images/buttons/button_endless_hover.png")
        self.button_levels = Button(game, size[0]/2, size[1]/5, "./images/buttons/button_levels.png", 1.0, "./images/buttons/button_levels_hover.png")
        self.button_two_players = Button(game, size[0]*4/5, size[1]/5, "./images/buttons/button_two_players.png", 1.0, "./images/buttons/button_two_players_hover.png")
        self.button_ship = Button(game, size[0]/4, self.game.height-50, "./images/buttons/button_ship.png", 1.0, "./images/buttons/button_ship_hover.png")
        self.button_hangar = Button(game, size[0]/2, self.game.height-50, "./images/buttons/button_hangar.png", 1.0, "./images/buttons/button_hangar_hover.png")
        self.button_shop = Button(game, size[0]*3/4, self.game.height-50, "./images/buttons/button_shop.png", 1.0, "./images/buttons/button_shop_hover.png")
        self.button_back = Button(game, 50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png")
        self.buttons = [
                        self.button_endless,
                        self.button_levels,
                        self.button_two_players,
                        self.button_ship,
                        self.button_hangar,
                        self.button_shop,
                        self.button_back
                        ]
        self.background = pygame.image.load("./images/background.png").convert_alpha()
        self.ship = self.game.player.current_ship
        self.ship.pos = Vector2(self.game.width/2, self.game.height/2)
        self.ship.vel = Vector2(0, 0)
        self.ship.acc = Vector2(0, 0)
        self.ship.bullets.clear()
        self.ship.hp.maximise_hp()
        self.game.other_bullets.clear()

        # coin
        self.coin = pygame.image.load("./images/coin.png").convert_alpha()
        width = self.coin.get_width()
        height = self.coin.get_height()
        self.coin = pygame.transform.scale(self.coin, (int(width * 5), int(height * 5)))


    def tick_menu(self):
        if self.button_levels.check_click():
            self.game.showing = "levelsmenu"
        elif self.button_back.check_click():
            self.game.showing = "mainmenu"
        elif self.button_hangar.check_click():
            self.game.showing = "hangar"
        elif self.button_two_players.check_click():
            self.game.showing = "twoplayers"

    def draw_menu(self):
        self.game.screen.blit(self.background, (0, 0))
        for button in self.buttons:
            button.draw()
        self.ship.pos = Vector2(self.game.width / 2, self.game.height / 2)
        self.ship.draw()
        self.game.screen.blit(self.coin, (450, 300))
        write(self.game, str(self.game.player.coins), 500, 300, 36, (200, 200, 200))

        write(self.game, f"Health points: {str(self.game.player.current_ship.hp.max_hp)}", 50, 300, 28, (200, 200, 200))
        write(self.game, f"Force: {str(self.game.player.current_ship.force)}", 50, 350, 28, (200, 200, 200))
        write(self.game, f"Mass: {str(self.game.player.current_ship.mass)}", 50, 400, 28, (200, 200, 200))

class LevelsMenu:
    def __init__(self, game):
        self.game = game
        self.button_back = Button(game, 50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png")
        self.buttons = []

        for i, level in enumerate(self.game.levels):
            if (i+1) % 3 == 1:
                self.buttons.append(LevelButton(self.game, self.game.width/5, self._calculate_level_y(i+1), 200, 100, i+1))
            elif (i+1) % 3 == 2:
                self.buttons.append(LevelButton(self.game, self.game.width/2, self._calculate_level_y(i+1), 200, 100, i+1))
            elif (i+1) % 3 == 0:
                self.buttons.append(LevelButton(self.game, self.game.width*4/5, self._calculate_level_y(i+1), 200, 100, i+1))

    def tick_menu(self):
        if self.button_back.check_click():
            self.game.showing = "gamemenu"
        for i, button in enumerate(self.buttons):
            # tu nie może być printa sprawdzającego check_click()
            if button.check_click():
                self.game.level_pointer = i
                self.game.levels[self.game.level_pointer-1].__init__(self.game)
                self.game.showing = "game"

    def _calculate_level_y(self, level_id):
        a = level_id % 3
        if a == 0: a = 3
        b = level_id - a
        y = 80 + b * 40
        return y

    def draw_menu(self):
        self.button_back.draw()
        for button in self.buttons:
            button.draw()
        #     if button.level_id % 3 == 1:
        #         button.draw(self.game.screen, self.game.width/5, self._calculate_level_y(button.level_id))
        #     if button.level_id % 3 == 2:
        #         button.draw(self.game.screen, self.game.width/2, self._calculate_level_y(button.level_id))
        #     if button.level_id % 3 == 0:
        #         button.draw(self.game.screen, self.game.width*4/5, self._calculate_level_y(button.level_id))

class HangarMenu:
    def __init__(self, game):
        self.game = game
        self.button_back = Button(game, 50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png")
        self.button_next = Button(game, 720, 250, "./images/buttons/button_next.png", 1.0, "./images/buttons/button_next_hover.png")
        self.button_prev = Button(game, 30, 250, "./images/buttons/button_prev.png", 1.0, "./images/buttons/button_prev_hover.png")
        self.translation = 0

    def tick_menu(self):
        if self.button_back.check_click():
            # self.game.player.current_ship.pos = Vector2(self.game.width / 2, self.game.height / 2)
            self.game.showing = "gamemenu"
            self.game.gamemenu.__init__(self.game)
        elif self.button_next.check_click():
            self.translation -= 50
        elif self.button_prev.check_click():
            self.translation += 50

        for i, ship in enumerate(self.game.player.ships):
            action = False
            pos = pygame.mouse.get_pos()
            # check if the ship collides with the mouse
            if ship.mask.overlap(self.game.mouse.mask, (pos[0] - ship.hitbox.x, pos[1] - ship.hitbox.y)):
                # check if the mouse is clicked
                if self.game.mouse.click():
                    action = True
            if action:
                self.game.player.current_ship = self.game.player.ships[i]

    def draw_menu(self):
        for i, ship in enumerate(self.game.player.ships):
            ship.pos.x = 100 + 150 * i + self.translation
            ship.pos.y = 150
            ship.hitbox.center = (ship.pos.x, ship.pos.y)
            ship.draw()
        self.game.player.current_ship.hitbox.center = (self.game.player.current_ship.pos.x, self.game.player.current_ship.pos.y)
        pygame.draw.rect(self.game.screen, (255, 255, 255), self.game.player.current_ship.hitbox, 1)
        self.button_back.draw()
        self.button_next.draw()
        self.button_prev.draw()

class PauseMenu:
    def __init__(self, game, resume_button_menu="game", exit_button_menu="levelsmenu"):
        self.game = game
        self.resume_button_menu = resume_button_menu
        self.exit_button_menu = exit_button_menu
        self.button_exit = Button(self.game, self.game.width/2, self.game.height/2-100, "./images/buttons/button_exit2.png", 2.0, "./images/buttons/button_exit2_hover.png")
        self.button_resume = Button(self.game, self.game.width/2, self.game.height/2+100, "./images/buttons/button_resume.png", 2.0, "./images/buttons/button_resume_hover.png")
    def tick_menu(self):
        if self.button_exit.check_click():
            self.game.showing = self.exit_button_menu
        elif self.button_resume.check_click():
            self.game.showing = self.resume_button_menu
    def draw_menu(self):
       self.button_exit.draw()
       self.button_resume.draw()

class SettingsMenu:
    def __init__(self, game):
        self.game = game
        self.buttons = []

    def tick_menu(self):
        pass
    def draw_menu(self):
        pass