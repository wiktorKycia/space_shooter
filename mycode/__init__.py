import pygame
from pygame.math import Vector2
from mycode.other import *
from mycode.utils import *
import math
from typing import Callable


# class StaticObject:
#     """
#     Static Object is the parent class for every object in the game, that does not move.
#     It has general use in user interface.
#     It has only the x, y as coordinates and game parameters.
#     """
#
#     def __init__(self, x, y):
#         """
#         Static Object is the parent class for every object in the game, that does not move.
#         It has general use in user interface.
#         It has only the x, y as coordinates and game parameters.
#         :param x: x coordinate
#         :param y: y coordinate
#         """
#         super().__init__()
#         self.x = x
#         self.y = y

#
# class UnClickable(StaticObject): # TODO: to usunąć, bo nikt tego nie używa, klasy pochodne też
#     """
#     The class that is a parent of static objects, that cannot be clicked.
#     (They can be clicked, but there will be no reaction from the program).
#     it takes the same parameters as parent class (StaticObject), plus one more: surf.
#     """
#
#     def __init__(self, x, y, surf):
#         """
#         The class that is a parent of static objects, that cannot be clicked.
#         (They can be clicked, but there will be no reaction from the program).
#         it takes the same parameters as parent class (StaticObject), plus one more: surf.
#         :param x: x coordinate
#         :param y: y coordinate
#         :param surf: the surface, that will be displayed on the screen
#         """
#         super().__init__(x, y)
#         self.surf = surf
#
#     def draw(self, screen: pygame.Surface):
#         """
#         Blits the (given in init) surface on the screen
#         """
#         screen.blit(self.surf, (self.x, self.y))
#
# class TextObject(UnClickable):
#     """
#     The class certainly for displaying text on the screen
#     """
#
#     def __init__(
#         self, screen: pygame.Surface, x, y, text, font_size, color=(255, 255, 255), font_style="Arial",
#         is_centered=False
#     ):
#         """
#         initializes the text and calls 'write' method
#         :param x: x coordinate
#         :param y: y coordinate
#         :param text: the text that will be displayed on the screen, can have a fstring
#         :param font_size: the size of the font in pixels
#         :param color: the rgb tuple of integer values defining the color, default: white
#         :param font_style: the font of the given text, default: Arial
#         :param is_centered: a boolean value, that determines if the text will be placed in the center or not, when True value is given, the x and y coordinates will be omitted and the text will be centered
#         """
#         self.text = self.write(screen, text, font_size, color, font_style, is_centered)
#         super().__init__(x, y, self.text)
#
#     def write(
#         self, screen: pygame.Surface, text: str, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False
#     ):
#         """
#         renders the text, returns pygame.Surface type
#         :param screen:
#         :param text: the text displayed
#         :param font_size: size of the text
#         :param color: color of the text in rgb
#         :param font_style: font of the text ex.Arial
#         :param is_centered: defines whether the text is centered or not, default: False -> text not centered
#         :return:
#         """
#         font = pygame.font.SysFont(font_style, font_size)
#         rend = font.render(text, True, color)
#         if is_centered is True:
#             self.x = (screen.get_width() - rend.get_rect().width) / 2
#             self.y = (screen.get_height() - rend.get_rect().height) / 2
#         return rend
#
#     def draw(self, screen: pygame.Surface):
#         """
#         blits the text on the screen
#         :return:
#         """
#         screen.blit(self.text, (self.x - self.text.get_width() / 2, self.y - self.text.get_height() / 2))
#
# class ImageObject(UnClickable):
#     def __init__(self, x: float, y: float, path: str, scale=1.0):
#         """
#         Represent an image in game with specified path to an image and scale, that can be omitted
#         :param x: x coordinate
#         :param y: y coordinate
#         :param path: string, path to the image
#         :param scale: can be omitted, default value: 1.0
#         """
#         self.image = pygame.image.load(path).convert_alpha()
#         if scale != 1.0:
#             self.image = pygame.transform.scale_by(self.image, scale)
#         super().__init__(x, y, self.image)
#
#     def draw(self, screen: pygame.Surface):
#         """
#         Blits the image on the screen
#         :return:
#         """
#         screen.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))


# class TextButton(StaticObject):
#     def __init__(self, x, y, width, height, text):
#         """
#         Represents a button, that has text in it
#         by default it has background color of rgb(30, 30, 30),
#         but when hovering it has color of rgb(100, 100, 100)
#         :param x: x coordinate
#         :param y: y coordinate
#         :param width: width of the button
#         :param height: height of the button
#         :param text: text displayed in the button
#         """
#         super().__init__(x, y)
#         self.width = width
#         self.height = height
#
#         self.surf = pygame.Surface((width, height))
#         self.surf.fill((30, 30, 30))
#         self.rect = self.surf.get_rect()
#         # self.rect.topleft = (x - width/2, y - height/2)
#         self.rect.center = (x,y)
#
#         self.text = text
#
#     def check_click(self):
#         """
#         sets action variable to False\n
#         checks the mouse position,\n
#         checks if mouse collides with rect,
#          - if yes -> lightens the background and the text, checks if the mouse is clicked,
#          * if yes -> sets action variable to True
#          - if no -> changes the text and background to previous values
#         :return: action
#         """
#         action = False
#         pos = pygame.mouse.get_pos()
#         # check if the rect collides with the mouse
#         if self.rect.collidepoint(pos):
#             self.surf.fill((100, 100, 100))
#             write_on_surface(self.surf, self.text, 0, 0, 28, (250, 250, 250), True)
#
#             # check if the mouse is clicked
#             if mouse.click():
#                 action = True
#                 # return action
#         elif not self.rect.collidepoint(pos):
#             self.surf.fill((30, 30, 30))
#             write_on_surface(self.surf, self.text, 0, 0, 28, (200, 200, 200), True)
#         return action
#
#     def draw(self, screen: pygame.Surface):
#         """
#         Blits the button surface on the screen,
#         draws the border of the button,
#         writes the text of the button
#         :return:
#         """
#         screen.blit(self.surf, (self.x - self.width / 2, self.y - self.height / 2))
#         pygame.draw.rect(screen, (250, 250, 250), self.rect, 1)
#         write_on_surface(self.surf, self.text, 0, 0, 28, (200, 200, 200), True)

