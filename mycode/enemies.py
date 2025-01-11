import pygame.time

from mycode.weapons import *
from mycode.Behaviors import *
from mycode.slot import Slot
import random
import json

from mycode.other import RefillableBar, DeluxeHP
from mycode.physics import PygamePhysics
from mycode.displayable import Displayer
from mycode.spacecraft import Spacecraft


class BaseEnemy(Spacecraft):
    def __init__(self, physics: PygamePhysics, healthBar: RefillableBar, image: pygame.Surface, scale: float = 1.0):
        self.displayer = Displayer(image, scale)
        self.physics: PygamePhysics = physics
        self.hp = healthBar
        
        self.physics.force *= -1
        
        self.move_clock = 0
        self.slots = []
        self.is_shooting = True
    
    def tick(self, dt: float):
        self.displayer.tick(self.physics.x, self.physics.y)
        self.physics.tick(dt)

        for slot in self.slots:
            slot.tick()
    
    def _move_bullets_after_die(self, bullet_list: list):
        for slot in self.slots:
            bullet_list.extend(slot.weapon.bullets)
    
    def draw(self, screen: pygame.Surface):
        self.displayer.draw(screen)
        
        for slot in self.slots:
            slot.draw()


class BaseEnemyBuilder:
    def __init__(self):
        self.enemy: BaseEnemy | None = None
        self.image: pygame.Surface | None = None
        self.scale: float | None = None
        self.displayer: Displayer | None = None
        self.healthBar = None  # :RefillableBar
        self.physics: PygamePhysics | None = None
    
    def buildImage(self, path: str, scale: float = 1.0):
        self.image = PathConverter(path).create()
        self.scale = scale
        return self
    
    def buildHealthBar(
        self, barType, amount: int, x: int, y: int, width: int, height: int, color: tuple[int, int, int] = (250, 0, 0)
    ):
        self.healthBar = barType(amount, x, y, width, height, color)
        return self
    
    def buildPhysics(self, x: int, y: int, mass: int, force: int, slip: float = 0.98):
        self.physics = PygamePhysics(x, y, mass, force, slip)
        return self
    
    def buildEnemy(self) -> BaseEnemy:
        self.enemy = BaseEnemy(self.physics, self.healthBar, self.image, self.scale)
        return self.enemy
    # TODO: add methods buildSlot and addWeapon


class BaseEnemyBuilderDirector:
    def __init__(self, builder: BaseEnemyBuilder, enemy_type: str | None = None):
        self.enemy_type: str | None = enemy_type
        self.builder: BaseEnemyBuilder = builder
        with open('./gameData/enemies.json', 'r') as f:
            self.config: dir = json.load(f)
            enemies = self.config["enemies"]
            self.enemy_data = list(filter(lambda enemy: enemy['name'] == self.enemy_type, enemies))[0]
    
    def choose_enemy(self, enemy_type: str):
        self.enemy_type = enemy_type
    
    def build(self, x: int, y: int) -> BaseEnemy:
        h: dir = self.config['enemiesDefaultHealthBar']
        enemy: BaseEnemy = (
            self.builder
            .buildImage(self.enemy_data['path'], self.enemy_data['scale'])
            .buildPhysics(x, y, self.enemy_data['mass'], self.enemy_data['force'])
            .buildHealthBar(
                DeluxeHP, self.enemy_data['hp_amount'], h['x'], h['y'], h['width'], h['height']
            )
            .buildEnemy()
        )
        return enemy

class Enemy1(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        super().__init__(
            game, x, y,
            path="./enemies/Enemy1.png",
            mass=50,
            max_speed=50,
            force=500,
            hp_amount=20
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 10), self.is_shooting, KineticLight)
            ]
        )

class Enemy2(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        super().__init__(
            game, x, y,
            path="./enemies/Enemy2.png",
            mass=75,
            max_speed=120,
            force=350,
            hp_amount=45
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 10), self.is_shooting, KineticLight)
            ]
        )

class Enemy3(BaseEnemy):
    def __init__(self, game, x, y):
        self.game = game
        super().__init__(
            game, x, y,
            path="./enemies/Enemy3.png",
            mass=250,
            max_speed=100,
            force=1000,
            hp_amount=100
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(-22, 10), self.is_shooting, KineticMedium),
                Slot(game, self, Vector2(22, 10), self.is_shooting, KineticMedium)
            ]
        )


class Bouncer1(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(
            game, x, y,
            "./enemies/bouncer1.png",
            mass=2,
            max_speed=200,
            force=1500,
            hp_amount=15,
            scale=3.0
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 0), self.is_shooting, KineticLight)
            ]
        )

    def do_move(self):
        angle = 0
        if self.pos.x < 350 and self.pos.y < 150: # top left
            angle = random.randint(91, 180)
        if self.pos.x > 350 and self.pos.y < 150: # top right
            angle = random.randint(180, 270)
        if self.pos.x < 350 and self.pos.y > 150: # bottom left
            angle = random.randint(1, 90)
        if self.pos.x > 350 and self.pos.y > 150: # bottom right
            angle = random.randint(270, 360)
        if angle > 180:
            angle = -angle
        if angle < -180:
            angle = -angle
        self.add_force(Vector2(0, self.force))
        self.acc.rotate_ip(angle)

    def tick(self):
        self.hp.x = self.pos.x
        self.hp.y = self.pos.y - 50
        self.move_clock += self.game.dt
        if self.move_clock > 0.5:
            self.move_clock = 0
            self.do_move()
        super().tick()


class Bouncer2(BaseEnemy):
    def __init__(self, game, x, y):
        super().__init__(
            game, x, y,
            "./enemies/bouncer2.png",
            mass=6,
            max_speed=200,
            force=2500,
            hp_amount=35,
            scale=3.0
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(0, 10), self.is_shooting, KineticLight)
            ]
        )
        self.destination_x = random.randint(0, 750)
        self.destination_y = random.randint(0, 350)
        self.dest_clock = 0

        self.behavior = Behavior(self.game, self)

    def reset_destination_points(self):
        self.destination_x = random.randint(0, 750)
        self.destination_y = random.randint(0, 350)

    def do_move(self, x, y):
        angle = 0
        if self.pos.x < x and self.pos.y < y:  # top left
            angle = random.randint(91, 180)
        if self.pos.x > x and self.pos.y < y:  # top right
            angle = random.randint(180, 270)
        if self.pos.x < x and self.pos.y > y:  # bottom left
            angle = random.randint(1, 90)
        if self.pos.x > x and self.pos.y > y:  # bottom right
            angle = random.randint(270, 360)
        if angle > 180:
            angle = -angle
        if angle < -180:
            angle = -angle
        self.add_force(Vector2(0, self.force))
        self.acc.rotate_ip(angle)

    def tick(self):
        self.hp.x = self.pos.x
        self.hp.y = self.pos.y - 50
        self.move_clock += self.game.dt
        # self.dest_clock += self.game.dt
        # if self.dest_clock > 5.0:
        #     self.reset_destination_points()
        self.behavior.tick()

        if self.move_clock > 0.5:
            self.move_clock = 0
            self.do_move(self.destination_x, self.destination_y)
        super().tick()
