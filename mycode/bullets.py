import pygame
from pygame import mixer
from pygame.math import Vector2

import json

from mycode.physics import PygamePhysics
from mycode.displayable import Displayer, PathConverter
from mycode.projectile import Projectile
from mycode.spacecraft import Spacecraft

mixer.init()


class Bullet(Projectile):
    def __init__(
        self, physics: PygamePhysics, damage: int, rotation: float, image: pygame.Surface,
        sound_path: str | None = None,
        scale: float = 1.0
    ):
        super().__init__(physics, damage, rotation)
        
        self.displayer = Displayer(image, scale)
        self.displayer.image = pygame.transform.rotate(image, 90)
        
        if sound_path != "":
            self.sound = mixer.Sound(sound_path)
            self.sound.set_volume(0.1)

        self.line = None

        self.steered_by_menu = False
    
    def check_collision(self, ship: Spacecraft):
        if self.line is not None:
            if (ship.displayer.mask.overlap(
                    self.displayer.mask, (
                            (self.physics.pos.x - self.displayer.width / 2) - ship.displayer.hitbox.x,
                            (self.physics.pos.y - self.displayer.height / 2) - ship.displayer.hitbox.y)
            ) or ship.displayer.hitbox.clipline(self.line)):
                return True
            return False
        elif ship.displayer.mask.overlap(
                self.displayer.mask, (
                        (self.physics.pos.x - self.displayer.width / 2) - ship.displayer.hitbox.x,
                        (self.physics.pos.y - self.displayer.height / 2) - ship.displayer.hitbox.y)
        ):
            return True
        return False
    
    def tick(self, dt):
        # Checking if the target of a bullet is in between of last bullet position and new bullet position
        # making it too far jump per one frame

        # drawing a line
        # if self.vel.y * self.game.dt > self.height or self.vel.x * self.game.dt > self.width:
        new_pos: Vector2 = self.physics.pos + (((self.physics.vel * self.physics.current_slip) + self.physics.acc) * dt)
        self.line = ((self.physics.pos.x, self.physics.pos.y), (new_pos.x, new_pos.y))
        
        # TODO: check collision and position somewhere else
        '''
        
        # if self.physics.pos.y < 0:
        #     del self   <- This does not remove a Bullet from a list,
        #     return
        
        # if self.gun.is_player:
        #     for enemy in self.game.menuHandler.currentMenu.enemies:
        #         if self.check_collision(enemy):
        #             enemy.hp.get_damage(self.damage)
        #             try:
        #                 self.gun.bullets.remove(self)
        #             except ValueError:
        #                 pass
        # else:
        #     if self.check_collision(self.game.player.current_ship):
        #         self.game.player.current_ship.hp.get_damage(self.damage)
        #         try:
        #             if not self.steered_by_menu:
        #                 self.gun.bullets.remove(self)
        #             else:
        #                 self.game.menuHandler.currentMenu.other_bullets.remove(self)
        #         except ValueError:
        #             pass
        '''
        
        self.physics.tick(dt)
        self.displayer.tick(self.physics.pos.x, self.physics.pos.y)
    
    def draw(self, screen: pygame.Surface):
        self.displayer.draw(screen, self.physics.pos.x, self.physics.pos.y)


class BulletBuilder:
    def __init__(self):
        self.bullet: Bullet | None = None
        self.physics: PygamePhysics | None = None
        self.damage: int | None = None
        self.rotation: float = 0.0
        self.image: pygame.Surface | None = None
        self.sound_path: str | None = None
        self.scale: float | None = None
    
    def buildPhysics(self, x: int, y: int, mass: int, force: int, slip: float = 0.98):
        self.physics = PygamePhysics(x, y, mass, force, slip)
        return self
    
    def set_damage(self, damage: int):
        self.damage = damage
        return self
    
    def set_rotation(self, rotation: float = 0.0):
        self.rotation = rotation
        return self
    
    def buildImage(self, path: str, scale: float = 1.0):
        self.image = PathConverter(path).create()
        self.scale = scale
        return self
    
    def buildSound(self, path: str):
        self.sound_path = path
        return self
    
    def buildBullet(self):
        self.bullet = Bullet(self.physics, self.damage, self.rotation, self.image, self.sound_path, self.scale)
        return self.bullet


class BulletBuilderDirector:
    def __init__(self, builder: BulletBuilder, bullet_name: str):
        self.builder = builder
        self.bullet_name = bullet_name
        self.bullet_data: dir = { }
        self.__reload_data()
    
    def __reload_data(self):
        with open("./gameData/bullets.json") as f:
            self.config: dir = json.load(f)
            bullets = self.config['bullets']
            self.bullet_data = list(filter(lambda bullet: bullet == self.bullet_name, bullets))[0]
    
    def choose_bullet(self, bullet_name):
        self.bullet_name = bullet_name
        self.__reload_data()
    
    def build(self, x: int, y: int, initial_force: int, rotation: float) -> Bullet:
        bullet: Bullet = (
            self.builder
            .buildImage(self.bullet_data['image_path'], self.bullet_data['scale'])
            .buildPhysics(x, y, self.bullet_data['mass'], initial_force)
            .set_rotation(rotation)
            .set_damage(self.bullet_data['damage'])
            .buildSound(self.bullet_data['sound_path'])
            .buildBullet()
        )
        return bullet
