import pygame
from pygame.math import Vector2
from mycode.other import *
from mycode.general import *
import math

class MainObject(object):
    """
    This is the main class,
    it basically is an abstract class for every object in the game.
    """
    def __init__(self):
        pass

    def tick(self):
        """
        Method tick contains instructions to run during every tick (frame).
        """
        pass

    def draw(self):
        """
        Method draw usually is called after tick method, it displays object on the screen.
        """
        pass

class StaticObject(MainObject):
    """
    Static Object is the parent class for every object in the game, that does not move.
    It has general use in user interface.
    It has only the x, y as coordinates and game parameters.
    """
    def __init__(self, game, x, y):
        """
        Static Object is the parent class for every object in the game, that does not move.
        It has general use in user interface.
        It has only the x, y as coordinates and game parameters.
        :param game: pass here the instance of Game class from main.py
        :param x: x coordinate
        :param y: y coordinate
        """
        super().__init__()
        self.game = game
        self.x = x
        self.y = y


class UnClickable(StaticObject):
    """
    The class that is a parent of static objects, that cannot be clicked.
    (They can be clicked, but there will be no reaction from the program).
    it takes the same parameters as parent class (StaticObject), plus one more: surf.
    """
    def __init__(self, game, x, y, surf):
        """
        The class that is a parent of static objects, that cannot be clicked.
        (They can be clicked, but there will be no reaction from the program).
        it takes the same parameters as parent class (StaticObject), plus one more: surf.
        :param game: pass here the instance of Game class from main.py
        :param x: x coordinate
        :param y: y coordinate
        :param surf: the surface, that will be displayed on the screen
        """
        super().__init__(game, x, y)
        self.surf = surf

    def draw(self):
        """
        Blits the (given in init) surface on the screen
        """
        self.game.screen.blit(self.surf, (self.x, self.y))

class TextObject(UnClickable):
    """
    The class certainly for displaying text on the screen
    """
    def __init__(self, game, x, y, text, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False):
        """
        initializes the text and calls 'write' method
        :param game: pass here the instance of Game class from main.py
        :param x: x coordinate
        :param y: y coordinate
        :param text: the text that will be displayed on the screen, can have a fstring
        :param font_size: the size of the font in pixels
        :param color: the rgb tuple of integer values defining the color, default: white
        :param font_style: the font of the given text, default: Arial
        :param is_centered: a boolean value, that determines if the text will be placed in the center or not, when True value is given, the x and y coordinates will be omitted and the text will be centered
        """
        self.text = self.write(text, font_size, color, font_style, is_centered)
        super().__init__(game, x, y, self.text)

    def write(self, text:str, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False):
        """
        renders the text, returns pygame.Surface type
        :param text: the text displayed
        :param font_size: size of the text
        :param color: color of the text in rgb
        :param font_style: font of the text ex.Arial
        :param is_centered: defines whether the text is centered or not, default: False -> text not centered
        :return:
        """
        font = pygame.font.SysFont(font_style, font_size)
        rend = font.render(text, True, color)
        if is_centered is True:
            self.x = (self.game.width - rend.get_rect().width) / 2
            self.y = (self.game.height - rend.get_rect().height) / 2
        return rend

    def draw(self):
        """
        blits the text on the screen
        :return:
        """
        self.game.screen.blit(self.text, (self.x - self.text.get_width()/2, self.y - self.text.get_height()/2))

class ImageObject(UnClickable):
    def __init__(self, game, x:float, y:float, path:str, scale=1.0):
        """
        Represent an image in game with specified path to an image and scale, that can be omitted
        :param game:
        :param x: x coordinate
        :param y: y coordinate
        :param path: string, path to the image
        :param scale: can be omitted, default value: 1.0
        """
        self.image = pygame.image.load(path).convert_alpha()
        if scale != 1.0:
            self.image = pygame.transform.scale_by(self.image, scale)
        super().__init__(game, x, y, self.image)

    def draw(self):
        """
        Blits the image on the screen
        :return:
        """
        self.game.screen.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))


class Clickable(StaticObject):
    def __init__(self, game, x, y, path, scale=1.0, path2=""):
        """
        A class for the object, that can be clicked,
        it might have 2 images, as one will be shown only when mouse is hovering over the image rectangle
        :param game: game object
        :param x: x coordinate
        :param y: y coordinate
        :param path: path to the main image
        :param scale: scale of the image
        :param path2: path to image shown, when mouse is over the object
        """
        super().__init__(game, x, y)
        self.image = pygame.image.load(path).convert_alpha()
        if scale != 1.0: self.image = pygame.transform.scale_by(self.image, scale)
        if path2 != "":
            self.image2 = pygame.image.load(path2)
            if scale != 1.0: self.image2 = pygame.transform.scale_by(self.image2, scale)

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # current image
        self.img = self.image

    def check_click(self):
        """
        sets action variable to False\n
        checks the mouse position,\n
        checks if mouse collides with rect,
         - if yes -> changes the image, checks if the mouse is clicked,
         * if yes -> sets action variable to True
         - if no -> changes the image to the first image
        :return: action
        """
        action = False
        pos = pygame.mouse.get_pos()
        # check if the rect collides with the mouse
        if self.rect.collidepoint(pos):
            self.img = self.image2
            # check if the mouse is clicked
            if self.game.mouse.click():
                action = True
        elif not self.rect.collidepoint(pos):
            self.img = self.image

        return action

    def draw(self):
        self.game.screen.blit(self.img, (self.x - self.width/2, self.y - self.height/2))

class TextButton(StaticObject):
    def __init__(self, game, x, y, width, height, text):
        """
        Represents a button, that has text in it
        by default it has background color of rgb(30, 30, 30),
        but when hovering it has color of rgb(100, 100, 100)
        :param game:
        :param x: x coordinate
        :param y: y coordinate
        :param width: width of the button
        :param height: height of the button
        :param text: text displayed in the button
        """
        super().__init__(game, x, y)
        self.width = width
        self.height = height

        self.surf = pygame.Surface((width, height))
        self.surf.fill((30, 30, 30))
        self.rect = self.surf.get_rect()
        # self.rect.topleft = (x - width/2, y - height/2)
        self.rect.center = (x,y)

        self.text = text

    def check_click(self):
        """
        sets action variable to False\n
        checks the mouse position,\n
        checks if mouse collides with rect,
         - if yes -> lightens the background and the text, checks if the mouse is clicked,
         * if yes -> sets action variable to True
         - if no -> changes the text and background to previous values
        :return: action
        """
        action = False
        pos = pygame.mouse.get_pos()
        # check if the rect collides with the mouse
        if self.rect.collidepoint(pos):
            self.surf.fill((100, 100, 100))
            write_on_surface(self.surf, self.text, 0, 0, 28, (250, 250, 250), True)

            # check if the mouse is clicked
            if self.game.mouse.click():
                action = True
                # return action
        elif not self.rect.collidepoint(pos):
            self.surf.fill((30, 30, 30))
            write_on_surface(self.surf, self.text, 0, 0, 28, (200, 200, 200), True)
        return action

    def draw(self):
        """
        Blits the button surface on the screen,
        draws the border of the button,
        writes the text of the button
        :return:
        """
        self.game.screen.blit(self.surf, (self.x - self.width / 2, self.y - self.height / 2))
        pygame.draw.rect(self.game.screen, (250, 250, 250), self.rect, 1)
        write_on_surface(self.surf, self.text, 0, 0, 28, (200, 200, 200), True)

