from typing import Type

import pygame

from mycode import DeluxeHP
from mycode.other import RefillableBar
from mycode.weapons import *
from mycode.physics import PygamePhysics
from mycode.slot import Slot
from mycode.enemies import BaseEnemy
from mycode.displayable import Displayer, PathConverter
from mycode.spacecraft import Spacecraft
import json
import math

class PlayableShip(Spacecraft):
    def __init__(self):
        super().__init__()
    
    def reset_stats(self, screen: pygame.Surface):
        # center ship's position
        self.physics.pos = Vector2(screen.get_width() / 2, screen.get_height() / 2)
        self.physics.vel = Vector2(0, 0)
        self.physics.acc = Vector2(0, 0)
        
        # maximise ship's stats
        self.refill_stats()
        
        # clear bullets
        for slot in self.slots:
            try:
                slot.weapon.bullets.clear()
            except AttributeError:
                pass

    def refill_stats(self):
        self.hp.maximise()
        for slot in self.slots:
            try:
                slot.weapon.clip.maximise_ammo()
            except AttributeError:
                pass
    
    def add_weapon(self, weapon: Weapon, slot_index: int):
        self.slots[slot_index].weapon = weapon

    def getClosestEnemy(self, enemies: list[BaseEnemy]):
        e = None
        d = math.inf
        for enemy in enemies:
            distance = math.sqrt(
                math.pow(abs(enemy.physics.pos.x - self.physics.x), 2) + math.pow(
                    abs(self.physics.y - enemy.physics.pos.y), 2
                )
            )
            if e is None or distance < d:
                d = distance
                e = enemy
        try:
            return e.physics.pos.x, e.physics.pos.y
        except AttributeError:
            return None
    
    def tick(self, dt: float):
        # Input
        pressed = pygame.key.get_pressed()
        force = Vector2(0, 0)
        if pressed[pygame.K_w]:
            force.y = -self.physics.force
        if pressed[pygame.K_s]:
            force.y = self.physics.force
        if pressed[pygame.K_d]:
            force.x = self.physics.force
        if pressed[pygame.K_a]:
            force.x = -self.physics.force
        if pressed[pygame.K_LSHIFT]:
            self.physics.current_slip = 0.8
        else:
            self.physics.current_slip = self.physics.slip

        if force != [0, 0]:
            self.physics.add_force(force.clamp_magnitude(self.physics.force))
        else:
            self.physics.add_force(force)

        for slot in self.slots:
            slot.tick(dt, self.physics.pos)
        
        self.displayer.tick(self.physics.x, self.physics.y)
        self.physics.tick(dt)
    
    def draw(self, screen: pygame.Surface):
        self.hp.tick(screen)
        self.displayer.draw(screen, self.physics.x, self.physics.y)
        for slot in self.slots:
            slot.draw(screen)


class PlayableShipBuilder:
    def __init__(self):
        self.ship: PlayableShip|None = None

    def reset(self):
        self.ship = PlayableShip()
        return self
    
    def buildImage(self, path: str, scale: float = 1.0):
        self.ship.displayer = Displayer(
            PathConverter(path).create(),
            scale
        )
        return self
    
    def buildHealthBar(
        self, barType: Type[RefillableBar], amount: int, x: float, y: float, width: int, height: int,
        color: tuple[int, int, int] = (250, 0, 0)
    ):
        self.ship.hp = barType(amount, x, y, width, height, color)
        return self
    
    def buildPhysics(self, x: float, y: float, mass: int, force: int, slip: float = 0.98):
        self.ship.physics = PygamePhysics(x, y, mass, force, True, slip)
        return self

    def buildSlot(self, translation: Vector2, trigger: Callable):
        self.ship.slots.append(Slot(translation, trigger))
        return self

    def buildShip(self) -> PlayableShip:
        return self.ship



keys = {
    "numpad_0": pygame.K_KP_0
}

class PlayableShipBuilderDirector:
    def __init__(self, builder: PlayableShipBuilder, ship_type: str | None = None):
        self.ship_type: str | None = ship_type
        self.ship_data: dict = { }
        self.slots: list = []
        self.builder: PlayableShipBuilder = builder
        self.__reload_file()
    
    def __reload_file(self):
        with open('./gameData/playerShips.json', 'r') as f:
            self.config: dict = json.load(f)
            ships = self.config["ships"]
            self.ship_data = list(filter(lambda ship: ship['name'] == self.ship_type, ships))[0]
            self.slots: list = self.ship_data['slots']
    
    def choose_ship(self, ship_type: str):
        self.ship_type = ship_type
        self.__reload_file()
    
    def build(self, x: float, y: float) -> PlayableShip:
        h: dict = self.config['shipsDefaultHealthBar']
        ship = (
            self.builder
            .buildImage(self.ship_data['path'], self.ship_data['scale'])
            .buildPhysics(x, y, self.ship_data['mass'], self.ship_data['force'])
            .buildHealthBar(
                DeluxeHP, self.ship_data['hp_amount'], h['x'], h['y'], h['width'], h['height']
            )
        )
        for slot in self.slots:
            ship.buildSlot(Vector2(slot['x'], slot['y']), lambda: pygame.key.get_pressed()[keys[slot['key']]])
        return ship.buildShip()
#
# class Ship1:
#     def __init__(self):
#
#         self.slots.extend(
#             [
#                 Slot(game, self, Vector2(20, -20), pygame.K_KP_0, KineticLight),
#                 Slot(game, self, Vector2(-20, -20), pygame.K_KP_0, KineticLight)
#             ]
#         )
#
#
# class Ship2:
#     def __init__(self):
#
#         self.slots.extend([
#             Slot(game, self, Vector2(0, -20), pygame.K_KP_0, ShotGun1)
#         ])
#
#
# class Ship3:
#     def __init__(self):
#
#         self.slots.extend([
#             Slot(game, self, Vector2(-10, -20), pygame.K_KP_0, Flamethrower1),
#             Slot(game, self, Vector2(10, -20), pygame.K_KP_0, Flamethrower1)
#         ])
#
#
# class Ship4:
#     def __init__(self):
#
#         self.slots.extend([
#             Slot(game, self, Vector2(3, -15), pygame.K_KP_0, Laser1),
#             Slot(game, self, Vector2(-4, -15), pygame.K_KP_0, Laser1),
#             Slot(game, self, Vector2(13, 6), pygame.K_KP_0, Laser1),
#             Slot(game, self, Vector2(-14, 6), pygame.K_KP_0, Laser1)
#         ])
#
#
# class Ship5:
#     def __init__(self): pass
