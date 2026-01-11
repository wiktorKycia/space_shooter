from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from mycode.projectile import Projectile
    from mycode.spacecraft import Spacecraft

from mycode.ships import PlayableShip
from mycode.enemies import BaseEnemy

class CollisionManager:
    def __init__(self):
        self.player_projectiles: list[Projectile] = []
        self.enemy_projectiles: list[Projectile] = []
        self.ships: list[Spacecraft] = []

    def register_projectile(self, projectile: Projectile):
        """Add a projectile based on the is_player flag"""
        if projectile.is_player:
            self.player_projectiles.append(projectile)
        else:
            self.enemy_projectiles.append(projectile)

    def register_projectiles(self, projectiles: list[Projectile]):
        """
        Allows to register more projectiles at once

        To avoid bugs, all projectiles must have the same value of 'is_player'
        """
        # if len(projectiles) == 0:
        #     raise ArgumentError("The length of 'projectiles' parameter should not be zero")

        if projectiles[0].is_player:
            self.player_projectiles.extend(projectiles)
        else:
            self.enemy_projectiles.extend(projectiles)

    def register_ship(self, ship: Spacecraft):
        """Adds a ship to the list of ships"""
        self.ships.append(ship)

    def check_collisions(self) -> list[tuple[Projectile, Spacecraft]]:
        """Main collision detection - call this every frame"""
        collisions: list[tuple[Projectile, Spacecraft]] = []

        for p in self.player_projectiles:
            for enemy in list(filter(lambda s: isinstance(s, BaseEnemy), self.ships)):
                print(enemy)
                if self._check_collision(p, enemy):
                    print('enemy got hit')
                    collisions.append((p, enemy))

        for p in self.enemy_projectiles:
            for ship in list(filter(lambda s: isinstance(s, PlayableShip), self.ships)):
                if self._check_collision(p, ship):
                    collisions.append((p, ship))

        return collisions

    def _check_collision(self, projectile: Projectile, ship: Spacecraft):
        if projectile.line is not None:
            if (ship.displayer.mask.overlap(
                    projectile.displayer.mask, (
                            (projectile.physics.pos.x - projectile.displayer.width / 2) - ship.displayer.hitbox.x,
                            (projectile.physics.pos.y - projectile.displayer.height / 2) - ship.displayer.hitbox.y
                    )
            ) or ship.displayer.hitbox.clipline(projectile.line)):
                return True
            return False
        elif ship.displayer.mask.overlap(
                projectile.displayer.mask, (
                        (projectile.physics.pos.x - projectile.displayer.width / 2) - ship.displayer.hitbox.x,
                        (projectile.physics.pos.y - projectile.displayer.height / 2) - ship.displayer.hitbox.y
                )
        ):
            return True
        return False

    def cleanup_dead_objects(self):
        """Removed flagged instances"""
        self.player_projectiles = [p for p in self.player_projectiles if p.alive]
        self.enemy_projectiles = [p for p in self.enemy_projectiles if p.alive]
        self.ships = [s for s in self.ships if s.alive]