import pygame
from pygame.math import Vector2
# from code.bullets import *
# from code.bullets2 import *
# from code.cannons import *
# from code.enemies import *
# from code.levels import *
# from code.maneuvering_cannons import *
from code.other import *
# from code.player import *
# from code.ships import *
# from code.two_players import *
# from code.UI import *
from code.general import *

class MainObject(object):
    def __init__(self):
        pass

    def tick(self):
        pass

    def draw(self):
        pass

class StaticObject(MainObject):
    def __init__(self, game, x, y):
        super().__init__()
        self.game = game
        self.x = x
        self.y = y


class UnClickable(StaticObject):
    def __init__(self, game, x, y, surf):
        super().__init__(game, x, y)
        self.surf = surf

    def draw(self):
        self.game.screen.blit(self.surf, (self.x, self.y))

class TextObject(UnClickable):
    def __init__(self, game, x, y, text, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False):
        self.text = self.write(text, font_size, color, font_style, is_centered)
        super().__init__(game, x, y, self.text)

    def write(self, text, font_size, color=(255, 255, 255), font_style="Arial", is_centered=False):
        font = pygame.font.SysFont(font_style, font_size)
        rend = font.render(text, True, color)
        if is_centered is True:
            self.x = (self.game.width - rend.get_rect().width) / 2
            self.y = (self.game.height - rend.get_rect().height) / 2
        return rend

    def draw(self):
        self.game.screen.blit(self.text, (self.x - self.text.get_width()/2, self.y - self.text.get_height()/2))

class ImageObject(UnClickable):
    def __init__(self, game, x, y, path, scale=1.0):
        self.image = pygame.image.load(path).convert_alpha()
        if scale != 1.0:
            self.image = pygame.transform.scale_by(self.image, scale)
        super().__init__(game, x, y, self.image)

    def draw(self):
        self.game.screen.blit(self.image, (self.x - self.image.get_width() / 2, self.y - self.image.get_height() / 2))


class Clickable(StaticObject):
    def __init__(self, game, x, y, path, scale=1.0, path2=""):
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
        super().__init__(game, x, y)
        self.width = width
        self.height = height

        self.surf = pygame.Surface((width, height))
        self.surf.fill((30, 30, 30))
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x - width/2, y - height/2)

        self.text = text

    def check_click(self):
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
        self.game.screen.blit(self.surf, (self.x - self.width / 2, self.y - self.height / 2))
        pygame.draw.rect(self.game.screen, (250, 250, 250), self.rect, 1)
        write_on_surface(self.surf, self.text, 0, 0, 28, (200, 200, 200), True)


class DynamicObject(MainObject):
    def __init__(self, game, x, y, path):
        super().__init__()
        self.game = game
        self.pos = Vector2(x, y)
        self.image = pygame.image.load(path).convert_alpha()

        self.width = self.image.get_width()
        self.height = self.image.get_height()

        self.hitbox = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def tick(self):
        self.hitbox.center = (self.pos.x, self.pos.y)

    def draw(self):
        self.game.screen.blit(self.image, (self.pos.x - self.width/2, self.pos.y - self.height/2))

class HasHealth:
    def __init__(self, game, hp_amount, hp_x, hp_y, hp_width, hp_height):
        self.hp = DeluxeHP(game, amount=hp_amount, x=hp_x, y=hp_y, width=hp_width, height=hp_height)
        self.game = game
        self.bullets = []
        self.clock = 0

    def tick(self):
        self.clock += self.game.dt
        self.hp.tick()
        for bullet in self.bullets:
            bullet.tick()

    def draw(self):
        for bullet in self.bullets:
            bullet.draw()

class NoMoving(DynamicObject):
    def __init__(self, game, x, y, path):
        super().__init__(game, x, y, path)

class Moving(DynamicObject):
    def __init__(self, game, x, y, path, mass, max_speed, slip=0.98):
        super().__init__(game, x, y, path)
        self.vel = Vector2(0, 0)
        self.acc = Vector2(0, 0)

        self.mass = mass

        self.slip = slip
        self.max_speed = max_speed

    def add_force(self, force):
        self.acc += force / self.mass

    def tick(self):
        # Physics
        self.vel *= self.slip
        self.vel += self.acc

        # Limiting speed
        if self.vel.x > self.max_speed:  # right
            self.vel = Vector2(self.max_speed, self.vel.y)
        elif self.vel.x < -self.max_speed:  # left
            self.vel = Vector2(-self.max_speed, self.vel.y)
        if self.vel.y > self.max_speed:  # up
            self.vel = Vector2(self.vel.x, self.max_speed)
        elif self.vel.y < -self.max_speed:  # down
            self.vel = Vector2(self.vel.x, -self.max_speed)

        self.pos += self.vel * self.game.dt
        self.acc *= 0
        super().tick()

class ShootingDownNoMove(HasHealth, NoMoving):
    def __init__(self, game, x, y, path, shot_force, hp_amount, hp_width, hp_height, hp_x=0, hp_y=-50):
        NoMoving.__init__(self, game, x, y, path)
        hp_x = self.pos.x + hp_x
        hp_y = self.pos.y + hp_y

        self.shot_force = -shot_force

        super().__init__(hp_amount, hp_x, hp_y, hp_width, hp_height)

class ShootingDown(Moving, HasHealth):
    def __init__(self, game, x, y, path, mass, max_speed, shot_force, hp_amount, hp_width, hp_height, hp_x=0, hp_y=-50, slip=0.98):
        super().__init__(game, x, y, path, mass, max_speed, slip)
        hp_x = self.pos.x + hp_x
        hp_y = self.pos.y + hp_y

        self.shot_force = -shot_force
        HasHealth.__init__(self, game, hp_amount, hp_x, hp_y, hp_width, hp_height)

    def tick(self):
        super().tick()
        HasHealth.tick(self)

    def draw(self):
        super().draw()
        HasHealth.draw(self)

class ShootingUp(Moving, HasHealth):
    def __init__(self, game, x, y, path, mass, max_speed, shot_force, hp_amount, hp_width, hp_height, hp_x, hp_y, hp_relative=False, slip=0.98):
        super().__init__(game, x, y, path, mass, max_speed, slip)
        self.shot_force = shot_force
        if hp_relative: # ! może być błąd z hp_x i hp_y
            hp_x = self.pos.x + hp_x
            hp_y = self.pos.y + hp_y
        HasHealth.__init__(self, game, hp_amount, hp_x, hp_y, hp_width, hp_height)

