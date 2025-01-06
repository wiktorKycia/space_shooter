import pygame

from abc import ABC, abstractmethod


# class AmmoBar:
#     def __init__(self, game, amount, width, height, x, y, color=(0, 0, 255)):
#         self.game = game
#         self.amount = amount
#         self.max_amount = amount
#
#         self.bar_length = width
#         self.height = height
#
#         self.x = x
#         self.y = y
#
#         self.color = color
#
#         self.ratio = self.max_amount / self.bar_length
#         self.bar = pygame.Rect(self.x - self.bar_length / 2, self.y - self.height / 2, self.bar_length, self.height)
#
#     def fill(self):
#         self.amount = self.max_amount
#
#     def decrease_by(self, amount):
#         if self.amount > 0:
#             self.amount -= amount
#         if self.amount < 0:
#             self.amount = 0
#
#     def increase_by(self, amount):
#         if self.amount < self.max_amount:
#             self.amount += amount
#         if self.amount > self.max_amount:
#             self.amount = self.max_amount
#
#     def tick(self):
#         bar_width = int(self.amount / self.ratio)
#         self.bar = pygame.Rect(self.x - self.bar_length/2, self.y - self.height/2, bar_width, self.height)
#
#     def draw(self):
#         pygame.draw.rect(self.game.screen, self.color, self.bar)
#         pygame.draw.rect(self.game.screen, (255, 255, 255),
#                          (self.x - self.bar_length / 2, self.y - self.height / 2, self.bar_length, self.height), 2)
@ABC
class RefillableBar:
    @abstractmethod
    def __init__(self, amount: int, x: int, y: int, width: int, height: int, color: tuple[int, int, int]):
        pass
    
    @abstractmethod
    def maximise(self):
        pass
    
    @abstractmethod
    def damage(self, amount: int):
        pass
    
    @abstractmethod
    def add_health(self, amount: int):
        pass
    
    @abstractmethod
    def tick(self, screen: pygame.Surface):
        pass


class HP(RefillableBar):
    def __init__(self, amount, x, y, width, height, color=(250, 250, 250)):
        self.amount = amount

        self.x = x
        self.y = y

        self.width = width
        self.height = height

        self.color = color
        self.bgcolor = (255, 0, 0)#(color[0] - 100, color[1] - 100, color[2] - 100)

        self.back = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)

        self.unit = self.width / self.amount

        self.block = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.unit * self.amount, self.height)
    
    def damage(self, amount):
        self.amount -= amount
        # self.tick()
        # self.draw()

    def tick(self):
        self.block = pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.unit * self.amount, self.height)
    
    def draw(self, screen: pygame.Surface):
        # self.game.screen.blit(self.surf, (self.x - self.width/2, self.y - self.height/2))
        pygame.draw.rect(screen, self.bgcolor, self.back)
        pygame.draw.rect(screen, self.color, self.block)


class DeluxeHP(RefillableBar):
    def __init__(self, amount, x, y, width, height, color=(250, 0, 0)):
        self.current_hp = amount
        self.max_hp = amount
        self.hp = amount

        self.bar_length = width
        self.health_ratio = self.max_hp / self.bar_length
        self.change_speed = 1

        self.height = height
        self.x = x
        self.y = y
        self.color = color
    
    def maximise(self):
        self.hp = self.max_hp
    
    def damage(self, amount):
        if self.hp > 0:
            self.hp -= amount
        if self.hp < 0:
            self.hp = 0
    
    def add_health(self, amount):
        if self.hp < self.max_hp:
            self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
    
    def tick(self, screen: pygame.Surface):
        transition_width = 0
        transition_color = (255, 0, 0)

        if self.current_hp < self.hp:
            self.current_hp += self.change_speed
            if self.current_hp > self.hp: self.current_hp = self.hp
            transition_width = int((self.hp - self.current_hp) / self.health_ratio)
            transition_color = (0, 255, 0)

            health_bar_width = int(self.current_hp / self.health_ratio)
            health_bar = pygame.Rect(self.x - self.bar_length/2, self.y - self.height/2, health_bar_width, self.height)
            transition_bar = pygame.Rect(health_bar.right, self.y - self.height/2, transition_width, self.height)
            
            pygame.draw.rect(screen, self.color, health_bar)
            pygame.draw.rect(screen, transition_color, transition_bar)
            pygame.draw.rect(
                screen, (255, 255, 255),
                (self.x - self.bar_length / 2, self.y - self.height / 2, self.bar_length, self.height), 2
            )


        elif self.current_hp > self.hp:
            self.current_hp -= self.change_speed
            if self.current_hp < self.hp: self.current_hp = self.hp
            transition_width = int((self.current_hp - self.hp) / self.health_ratio)
            transition_color = (255, 255, 0)

            health_bar_width = int(self.hp / self.health_ratio)
            health_bar = pygame.Rect(self.x - self.bar_length/2, self.y - self.height/2, health_bar_width, self.height)
            transition_bar = pygame.Rect(health_bar.right, self.y - self.height/2, transition_width, self.height)
            
            pygame.draw.rect(screen, self.color, health_bar)
            pygame.draw.rect(screen, transition_color, transition_bar)
            pygame.draw.rect(
                screen, (255, 255, 255),
                (self.x - self.bar_length / 2, self.y - self.height / 2, self.bar_length, self.height), 2
            )


        else:
            health_bar_width = int(self.current_hp / self.health_ratio)
            health_bar = pygame.Rect(self.x - self.bar_length/2, self.y - self.height/2, health_bar_width, self.height)
            # transition_bar = pygame.Rect(health_bar.right, self.y, transition_width, self.height)
            
            pygame.draw.rect(screen, self.color, health_bar)
            # pygame.draw.rect(self.game.screen, transition_color, transition_bar)
            pygame.draw.rect(
                screen, (255, 255, 255),
                (self.x - self.bar_length / 2, self.y - self.height / 2, self.bar_length, self.height), 2
            )


class Mouse:
    def __init__(self, game):
        self.game = game
        self.click_counter = 0
        self.surf = pygame.Surface((1, 1))
        self.surf.fill((0, 0, 0))
        self.mask = pygame.mask.from_surface(self.surf)

    def click(self, button=0):
        if pygame.mouse.get_pressed()[button] == 1 and self.click_counter == 0:
            self.click_counter += 1
            return True
        elif pygame.mouse.get_pressed()[button] == 0:
            self.click_counter = 0
        else:
            self.click_counter += 1
        return False