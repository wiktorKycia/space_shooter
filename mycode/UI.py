from mycode.ships import *
from mycode.player import *
from mycode.utils import *
import pygame
from pygame.math import *
from pygame.locals import *
import json
from abc import abstractmethod, ABC
from typing import Optional

class ButtonDisplayer(ABC):
    @abstractmethod
    def get_rect(self) -> pygame.rect.Rect:
        """Returns the rect area of the button"""
        pass
    @abstractmethod
    def get_width(self) -> int:
        """Returns the width of the button"""
        pass
    @abstractmethod
    def get_height(self) -> int:
        """Returns the height of the button"""
        pass
    @abstractmethod
    def activate(self) -> None:
        """An action performed when a button goes active, for example when mouse hovers over it"""
        pass
    @abstractmethod
    def deactivate(self) -> None:
        """An action performed when a button goes inactive, for example when mouse leaves the object"""
        pass
    @abstractmethod
    def draw(self, screen: pygame.Surface, x:int , y:int) -> None:
        """Displays the button on the screen"""
        pass

class ImageButtonDisplayer(ButtonDisplayer):
    def __init__(self, path: str, path_hover: str = "", scale: float = 1.0):
        """
        Display manager for buttons, that have an image, that changes on hover
        :param path: path to the main image
        :param scale: scale of the image
        :param path_hover: path to image shown, when mouse is over the object
        """
        self.main_image: pygame.Surface = pygame.image.load(path).convert_alpha()
        self.hover_image: Optional[pygame.Surface] = None
        self.current_image: pygame.Surface = self.main_image

        if scale != 1.0:
            self.main_image = pygame.transform.scale_by(self.main_image, scale)

        if path_hover != "":
            self.hover_image = pygame.image.load(path_hover)

            if scale != 1.0:
                self.hover_image = pygame.transform.scale_by(self.hover_image, scale)

    def get_rect(self) -> pygame.rect.Rect:
        return self.current_image.get_rect()

    def get_width(self) -> int:
        return self.current_image.get_width()

    def get_height(self) -> int:
        return self.current_image.get_height()

    def activate(self):
        if self.hover_image:
            self.current_image = self.hover_image

    def deactivate(self):
        self.current_image = self.main_image

    def draw(self, screen: pygame.Surface, x:int, y:int):
        screen.blit(self.current_image, (x - self.current_image.get_width() / 2, y - self.current_image.get_height() / 2))

class TextButtonDisplayer(ButtonDisplayer):
    def __init__(self, width:int , height:int , text: str, color: tuple[int, int, int] = (30, 30, 30), hover_color: tuple[int, int, int] = (100, 100, 100)):
        """
        Display managers for buttons, that has dynamic or not-repetitive text inside of them
        :param width:
        :param height:
        :param text:
        """
        self.main_color: tuple[int, int, int] = color
        self.hover_color: tuple[int, int, int] = hover_color

        self.surf: pygame.Surface = pygame.Surface((width, height))
        self.surf.fill(color)

        self.text: str = text

    def get_rect(self) -> pygame.rect.Rect:
        return self.surf.get_rect()

    def get_width(self) -> int:
        return self.surf.get_width()

    def get_height(self) -> int:
        return self.surf.get_height()

    def activate(self) -> None:
        self.surf.fill(self.hover_color)
        write(self.surf, self.text, 0, 0, 28, (250, 250, 250), is_centered=True)

    def deactivate(self) -> None:
        self.surf.fill(self.main_color)
        write(self.surf, self.text, 0, 0, 28, (200, 200, 200), is_centered=True)

    def draw(self, screen, x, y):
        """
        Blits the button surface on the screen,
        draws the border of the button,
        writes the text of the button
        :return:
        """
        screen.blit(self.surf, (x - self.get_width() / 2, y - self.get_height() / 2))
        pygame.draw.rect(screen, (250, 250, 250), self.get_rect(), 1)
        write(self.surf, self.text, 0, 0, 28, (200, 200, 200), is_centered=True)

class Button:
    def __init__(self, x: int, y:int, displayer: ButtonDisplayer, callback: Callable = lambda: None):
        """
        A class for the object, that can be clicked,
        it might have 2 images, as one will be shown only when mouse is hovering over the image rectangle
        :param x: x coordinate
        :param y: y coordinate
        :param callback: a function to call when the button is clicked
        """
        self.x: int = x
        self.y: int = y

        self.displayer: ButtonDisplayer = displayer

        # self.width = self.current_image.get_width()
        # self.height = self.current_image.get_height()

        self.rect: pygame.rect.Rect = self.displayer.get_rect()
        self.rect.center = (x, y)

        self.callback: Callable = callback

    def tick(self, click: bool):
        """
        sets action variable to False\n
        checks the mouse position,\n
        checks if mouse collides with rect,
         - if yes -> activates the button, checks if the mouse is clicked,
         * if yes -> calls the callback function
         - if no -> deactivates the button
        :return: action
        """
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            self.displayer.activate()

            if click:
                self.callback()

        else:
            self.displayer.deactivate()

    def draw(self, screen: pygame.Surface):
        self.displayer.draw(screen, self.x, self.y)


class LevelButton(Button):
    def __init__(self, x: int, y:int, width:int, height:int, level_id: int, callback: Callable):
        self.level_id = level_id
        self.displayer: ButtonDisplayer = TextButtonDisplayer(width, height, f"Level {str(level_id)}")
        super().__init__(x, y, self.displayer, callback)


# class Button(Clickable):
#     def __init__(self, x: float, y: float, path: str, scale: float = 1.0, path_hover: str = "", callback: Callable = lambda: None):
#         super().__init__(x, y, path, scale, path_hover, callback)
#
#     def tick(self, click: bool):
#         super().tick(click)

class MenuHandler:
    def __init__(self, mainmenu):
        self.currentMenuType = mainmenu
        self.currentMenu = self.currentMenuType()
        self.hiddenMenu = None

    def resetMenu(self, *args):
        self.currentMenu = self.currentMenuType(*args)

    def revealMenu(self):
        self.currentMenuType = type(self.hiddenMenu)
        self.currentMenu = self.hiddenMenu

    def changeMenu(self, menu, override: bool = False, *args):
        if override:
            self.hiddenMenu = self.currentMenu

        self.currentMenuType = menu
        self.resetMenu(args)

    def tick(self, *args):
        self.currentMenu.tick_menu(args)

    def draw(self, *args):
        self.currentMenu.draw_menu(args)

#
# class Menu:
#     def __init__(self):
#         pass
#
# class MainMenu:
#     def __init__(self, screen_size: tuple[int, int]):
#
#         # self.
#         self.buttons = [
#             self.button_play,
#             self.button_exit
#         ]
#         self.background = pygame.image.load("./images/background.png").convert_alpha()
#
#     def tick_menu(self, mouse: Mouse, menuHandler: MenuHandler, quit_game: Callable):
#         if self.button_play.check_click(mouse):
#             menuHandler.changeMenu(GameMenu)
#         elif self.button_exit.check_click(mouse):
#             quit_game()
#
#     def draw_menu(self, screen: pygame.Surface):
#         screen.blit(self.background, (0, 0))
#         screen.blit(
#             self.title_image,
#             (screen.get_width() / 2 - self.title_image.get_width() / 2, 150 - self.title_image.get_height() / 2)
#         )
#         for button in self.buttons:
#             button.draw(screen)
#
# class GameMenu:
#     def __init__(self, screen_size: tuple[int, int], ship: PlayableShip):
#         screen_size: tuple[int, int] = screen_size
#
#         # define the buttons
#         self.button_endless = Button(
#             screen_size[0] / 3, screen_size[1] / 5, "./images/buttons/button_endless.png", 1.0,
#             "./images/buttons/button_endless_hover.png"
#             )
#         self.button_levels = Button(
#             screen_size[0] * 2 / 3, screen_size[1] / 5, "./images/buttons/button_levels.png", 1.0,
#                                     "./images/buttons/button_levels_hover.png")
#         self.button_ship = Button(
#             screen_size[0] / 4, screen_size[1] - 50, "./images/buttons/button_ship.png", 1.0,
#             "./images/buttons/button_ship_hover.png"
#             )
#         self.button_hangar = Button(
#             screen_size[0] / 2, screen_size[1] - 50, "./images/buttons/button_hangar.png", 1.0,
#             "./images/buttons/button_hangar_hover.png"
#             )
#         self.button_shop = Button(
#             screen_size[0] * 3 / 4, screen_size[1] - 50, "./images/buttons/button_shop.png", 1.0,
#             "./images/buttons/button_shop_hover.png"
#             )
#         self.button_back = Button(
#             50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png"
#         )
#
#         # pack the buttons to the list
#         self.buttons = [
#             self.button_endless,
#             self.button_levels,
#             self.button_ship,
#             self.button_hangar,
#             self.button_shop,
#             self.button_back
#         ]
#         self.background = pygame.image.load("./images/background.png").convert_alpha()
#         ship.reset_stats(screen_size)
#
#
#         # self.game.menuHandler.currentMenu.other_bullets.clear()
#
#         # coin
#         self.coin: pygame.Surface = convert_path("./images/coin.png")
#         width = self.coin.get_width()
#         height = self.coin.get_height()
#         self.coin = pygame.transform.scale(self.coin, (int(width * 5), int(height * 5)))
#
#     def tick_menu(self, mouse: Mouse, menuHandler: MenuHandler):
#         if self.button_levels.check_click(mouse):
#             menuHandler.changeMenu(LevelsMenu)
#         elif self.button_back.check_click(mouse):
#             menuHandler.changeMenu(MainMenu)
#         elif self.button_hangar.check_click(mouse):
#             menuHandler.changeMenu(HangarMenu)
#         elif self.button_ship.check_click(mouse):
#             menuHandler.changeMenu(ShipMenu)
#
#     def draw_menu(self, screen: pygame.Surface, player_ship: PlayableShip, coins: int):
#         screen.blit(self.background, (0, 0))
#         for button in self.buttons:
#             button.draw(screen)
#         player_ship.draw(screen)
#         screen.blit(self.coin, (450, 300))
#         write(str(coins), 500, 300, 36, (200, 200, 200))
#
#         write(f"Health: {str(player_ship.hp.amount)}", 50, 300, 28, (200, 200, 200))
#         write(f"Force: {str(player_ship.physics.force)}", 50, 350, 28, (200, 200, 200))
#         write(f"Mass: {str(player_ship.physics.mass)}", 50, 400, 28, (200, 200, 200))
#

from mycode.levels import LevelManager
from mycode.enemies import BaseEnemy
class LevelGame:
    def __init__(
        self, level_number: int, levelManager: LevelManager, menuHandler: MenuHandler, player_ship: PlayableShip
    ):
        """
        Manages the situation on a concrete level
        :param level_number:
        :param levelManager:
        :param menuHandler:
        """
        self.enemies: list[BaseEnemy] = []
        self.other_bullets: list[Projectile] = []
        
        self.level_manager: LevelManager = levelManager
        self.level_number: int = level_number
        
        self.click_P_counter: int = 0
        self.menuHandler = menuHandler
        
        # reset player's ship's stats
        player_ship.refill_stats()
    
    def check_for_key_press(self, key: int = pygame.K_p):
        if pygame.key.get_pressed()[key] == 1 and self.click_P_counter == 0:
            self.click_P_counter += 1
            self.menuHandler.changeMenu(PauseMenu, True)
        elif pygame.key.get_pressed()[pygame.K_p] == 0:
            self.click_P_counter = 0
        else:
            self.click_P_counter += 1
    
    def tick_menu(self, dt: float, player_ship: PlayableShip):
        """
        Method tick contains instructions to run during every tick (frame).
        First, it calls every enemies' tick method,
        then calls every bullets' tick method, that doesn't have any superior object, for example a ship,
        then calls player's and level's tick method,
        lastly, checks for clicking p key in order to show pause menu.
        """
        for enemy in self.enemies:
            enemy.tick(dt)

        for bullet in self.other_bullets:
            if bullet.steered_by_menu:
                bullet.tick(dt)
            else:
                bullet.steered_by_menu = True
        
        player_ship.tick(dt)
        self.level_manager.tick(self.level_number, self.enemies)
        
        self.check_for_key_press()
    
    def draw_menu(self, screen, player_ship: PlayableShip):
        """
        Method draw usually is called after tick method, it displays object on the screen.
        First, it draws the enemies,
        then player and player's hp.
        """
        for enemy in self.enemies:
            enemy.draw(screen)

        for bullet in self.other_bullets:
            bullet.draw(screen)
        
        player_ship.draw(screen)

class LevelsMenu:
    def __init__(self, screen_size: tuple[int, int], config_file: str = "../gameData/levels.json"):
        screen_size: tuple[int, int] = screen_size
        self.button_back = Button(
            50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png"
        )
        self.buttons = []
        with open(config_file, "r") as f:
            self.number_of_levels: int = len(json.load(f)['levels'])

        for i in range(self.number_of_levels):
            if (i+1) % 3 == 1:
                self.buttons.append(LevelButton(screen_size[0] / 5, self._calculate_level_y(i + 1), 200, 100, i + 1))
            elif (i+1) % 3 == 2:
                self.buttons.append(LevelButton(screen_size[0] / 2, self._calculate_level_y(i + 1), 200, 100, i + 1))
            elif (i+1) % 3 == 0:
                self.buttons.append(
                    LevelButton(screen_size[0] * 4 / 5, self._calculate_level_y(i + 1), 200, 100, i + 1)
                )
    
    def tick_menu(self, mouse: Mouse, menuHandler: MenuHandler):
        if self.button_back.check_click(mouse):
            menuHandler.changeMenu(GameMenu)
        for i, button in enumerate(self.buttons):
            # tu nie może być printa sprawdzającego check_click()
            if button.check_click(mouse):
                menuHandler.changeMenu(LevelGame)
                menuHandler.currentMenu.level_pointer = i
                menuHandler.currentMenu.reset_current_level()
        for event in pygame.event.get():
            if event.type == MOUSEWHEEL:
                if event.y == -1:
                    for button in self.buttons:
                        button.y -= 50
                        button.rect.center = (button.x, button.y)
                elif event.y == 1:
                    for button in self.buttons:
                        button.y += 50
                        button.rect.center = (button.x, button.y)

    @staticmethod
    def _calculate_level_y(level_id):
        a = level_id % 3
        if a == 0: a = 3
        b = level_id - a
        y = 80 + b * 40
        return y
    
    def draw_menu(self, screen: pygame.Surface):
        for button in self.buttons:
            button.draw(screen)
        self.button_back.draw(screen)
        #     if button.level_id % 3 == 1:
        #         button.draw(self.game.screen, self.game.width/5, self._calculate_level_y(button.level_id))
        #     if button.level_id % 3 == 2:
        #         button.draw(self.game.screen, self.game.width/2, self._calculate_level_y(button.level_id))
        #     if button.level_id % 3 == 0:
        #         button.draw(self.game.screen, self.game.width*4/5, self._calculate_level_y(button.level_id))

class HangarMenu:
    def __init__(self, screen_size: tuple[int, int]):
        self.screen_size = screen_size
        self.button_back = Button(
            50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png"
        )
        self.button_next = Button(
            720, 250, "./images/buttons/button_next.png", 1.0, "./images/buttons/button_next_hover.png"
        )
        self.button_prev = Button(
            30, 250, "./images/buttons/button_prev.png", 1.0, "./images/buttons/button_prev_hover.png"
        )
        self.translation = 0
    
    def tick_menu(self, mouse: Mouse, menuHandler: MenuHandler, player: Player):
        if self.button_back.check_click(mouse):
            menuHandler.changeMenu(GameMenu)
        elif self.button_next.check_click(mouse):
            self.translation -= 50
        elif self.button_prev.check_click(mouse):
            self.translation += 50
        
        for i, ship in enumerate(player.ships):
            action = False
            pos = pygame.mouse.get_pos()
            if ship.displayer.mask.overlap(
                    mouse.mask, (pos[0] - ship.displayer.hitbox.x, pos[1] - ship.displayer.hitbox.y)
            ):
                if mouse.click():
                    action = True
            if action:
                player.set_current_ship(player.ships[i])
    
    def draw_menu(self, screen: pygame.Surface, player: Player):
        for i, ship in enumerate(player.ships):
            ship.physics.pos.x = 100 + 150 * i + self.translation
            ship.physics.pos.y = 150
            ship.displayer.hitbox.center = (ship.physics.pos.x, ship.physics.pos.y)
            ship.draw(screen)
        player.current_ship.hitbox.center = (player.current_ship.pos.x, player.current_ship.pos.y)
        pygame.draw.rect(screen, (255, 255, 255), player.current_ship.hitbox, 1)
        self.button_back.draw(screen)
        self.button_next.draw(screen)
        self.button_prev.draw(screen)

class PauseMenu:
    def __init__(self, screen_size: tuple[int, int], resume_button_menu: type, exit_button_menu: type):
        self.screen_size = screen_size
        self.resume_button_menu = resume_button_menu
        self.exit_button_menu = exit_button_menu
        self.button_exit = Button(
            screen_size[0] / 2, screen_size[1] / 2 - 100, "./images/buttons/button_exit2.png", 2.0,
            "./images/buttons/button_exit2_hover.png"
        )
        self.button_resume = Button(
            screen_size[0] / 2, screen_size[1] / 2 + 100, "./images/buttons/button_resume.png", 2.0,
            "./images/buttons/button_resume_hover.png"
        )
    
    def tick_menu(self, mouse: Mouse, menuHandler: MenuHandler):
        if self.button_exit.check_click(mouse):
            menuHandler.changeMenu(self.exit_button_menu)
        elif self.button_resume.check_click(mouse):
            menuHandler.revealMenu()
    
    def draw_menu(self, screen: pygame.Surface):
        self.button_exit.draw(screen)
        self.button_resume.draw(screen)

class ShipMenu:
    def __init__(self, ship: PlayableShip, screen: pygame.Surface):
        self.button_back = Button(
            50, 700, "./images/buttons/button_back.png", 1.0,
                                  "./images/buttons/button_back_hover.png")

        # Ship
        ship.reset_stats(screen)
        ship.physics.pos.y = 50

        # Coin
        self.coin = pygame.image.load("./images/coin.png").convert_alpha()
        width = self.coin.get_width()
        height = self.coin.get_height()
        self.coin = pygame.transform.scale(self.coin, (int(width * 5), int(height * 5)))
    
    def tick_menu(self, mouse: Mouse, menuHandler: MenuHandler):
        if self.button_back.check_click(mouse):
            menuHandler.changeMenu(GameMenu)
    
    def draw_menu(self, screen: pygame.Surface):
        write_on_surface(screen, "This feature is not yet added to the game", 0, 0, 24, is_centered=True)
        # write(self.game, f"Current level: {self.game.player.current_ship.level}", 10, 10, 28, (255, 255, 255))
        # write(self.game, f"Next level: {self.game.player.current_ship.level + 1}", 10, 40, 28, (255, 255, 255))
        # write(self.game, f"Coins: {str(self.game.player.coins)}", 10, 70, 28, (255, 255, 255))
        # self.ship.pos = Vector2(self.game.width / 2, 50)
        # self.ship.draw()
        self.button_back.draw(screen)
