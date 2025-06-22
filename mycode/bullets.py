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
    def __init__(self):
        super().__init__()
        self.sound: mixer.Sound | None = None
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

    def reset(self):
        self.bullet = Bullet()
        return self
    
    def buildPhysics(self, x: float, y: float, mass: int, force: int, is_player: bool = True, slip: float = 0.98):
        self.bullet.physics = PygamePhysics(x, y, mass, force, is_player, slip)
        return self
    
    def set_damage(self, damage: int):
        self.bullet.damage = damage
        return self

    def set_initial_rotation(self, rotation: float = 0.0):
        self.bullet.initial_rotation = rotation
        return self

    def buildDisplayer(self, path: str, scale: float = 1.0, is_player: bool = True):
        self.bullet.displayer = Displayer(
            pygame.transform.rotate(PathConverter(path).create(), 90),
            scale
        )
        if not is_player:
            self.bullet.displayer.image = pygame.transform.flip(self.bullet.displayer.image, False, True)
        return self

    def buildSound(self, path: str, volume: float = 0.1):
        self.bullet.sound = mixer.Sound(path)
        self.bullet.sound.set_volume(volume)
        return self
    
    def buildBullet(self):
        self.bullet.physics.add_force(Vector2(0, -self.bullet.physics.force).rotate(self.bullet.initial_rotation))
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
    
    def build(self, x: float, y: float, initial_force: int, rotation: float, is_player: bool = True) -> Bullet:
        bullet: Bullet = (
            self.builder
            .reset()
            .buildDisplayer(self.bullet_data['image_path'], self.bullet_data['scale'], is_player)
            .buildPhysics(x, y, self.bullet_data['mass'], initial_force, is_player)
            .set_initial_rotation(rotation)
            .set_damage(self.bullet_data['damage'])
            .buildSound(self.bullet_data['sound_path'])
            .buildBullet()
        )
        return bullet
