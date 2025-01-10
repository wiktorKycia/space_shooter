import pygame
from pygame import mixer
from mycode.other import RefillableBar
from mycode.weapons import *
from mycode.physics import PygamePhysics
from mycode.slot import Slot
from mycode.enemies import BaseEnemy
from mycode.displayable import Displayer, PathConverter
from mycode.spacecraft import Spacecraft
mixer.init()


class PlayableShip(Spacecraft):
    def __init__(
        self, physics: PygamePhysics, healthBar: RefillableBar, image: pygame.Surface, scale: float = 1.0
    ):
        self.displayer = Displayer(image, scale)
        self.physics: PygamePhysics = physics
        self.hp = healthBar
        
        self.slots = []

    def refill_stats(self):
        self.hp.maximise()
        for slot in self.slots:
            try:
                slot.weapon.clip.maximise_ammo()
            except AttributeError:
                pass

    def getClosestEnemy(self, enemies: list[BaseEnemy]):
        e = None
        d = math.inf
        for enemy in enemies:
            distance = math.sqrt(
                math.pow(abs(enemy.pos.x - self.physics.x), 2) + math.pow(abs(self.physics.y - enemy.pos.y), 2)
            )
            if e is None or distance < d:
                d = distance
                e = enemy
        try:
            return e.pos.x, e.pos.y
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
            slot.tick()
        
        self.displayer.tick(self.physics.x, self.physics.y)
        self.physics.tick(dt)
    
    def draw(self, screen: pygame.Surface):
        self.displayer.draw(screen, self.physics.x, self.physics.y)
        for slot in self.slots:
            slot.draw()


class PlayableShipBuilder:
    def __init__(self):
        self.ship: PlayableShip | None = None
        self.image: pygame.Surface | None = None
        self.scale: float | None = None
        self.displayer: Displayer | None = None
        self.healthBar = None  # :RefillableBar
        self.physics: PygamePhysics | None = None
    
    def createImage(self, path: str, scale: float = 1.0):
        self.image = PathConverter(path).create()
        self.scale = scale
        return self
    
    def createHealthBar(
        self, barType, amount: int, x: int, y: int, width: int, height: int, color: tuple[int, int, int] = (250, 0, 0)
    ):
        self.healthBar = barType(amount, x, y, width, height, color)
        return self
    
    def createPhysics(self, x: int, y: int, mass: int, force: int, slip: float = 0.98):
        self.physics = PygamePhysics(x, y, mass, force, slip)
        return self
    
    def createShip(self) -> PlayableShip:
        self.ship = PlayableShip(self.physics, self.healthBar, self.image, self.scale)
        return self.ship
    # TODO: dodać metody createSlot i addWeapons


class Ship1:
    def __init__(self):
        
        self.slots.extend(
            [
                Slot(game, self, Vector2(20, -20), pygame.K_KP_0, KineticLight),
                Slot(game, self, Vector2(-20, -20), pygame.K_KP_0, KineticLight)
            ]
        )


class Ship2:
    def __init__(self):
        
        self.slots.extend([
            Slot(game, self, Vector2(0, -20), pygame.K_KP_0, ShotGun1)
        ])


class Ship3:
    def __init__(self):
        
        self.slots.extend([
            Slot(game, self, Vector2(-10, -20), pygame.K_KP_0, Flamethrower1),
            Slot(game, self, Vector2(10, -20), pygame.K_KP_0, Flamethrower1)
        ])


class Ship4:
    def __init__(self):
        
        self.slots.extend([
            Slot(game, self, Vector2(3, -15), pygame.K_KP_0, Laser1),
            Slot(game, self, Vector2(-4, -15), pygame.K_KP_0, Laser1),
            Slot(game, self, Vector2(13, 6), pygame.K_KP_0, Laser1),
            Slot(game, self, Vector2(-14, 6), pygame.K_KP_0, Laser1)
        ])


class Ship5:
    def __init__(self): pass
