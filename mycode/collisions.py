from __future__ import annotations
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
	from mycode.projectile import Projectile
	from mycode.spacecraft import Spacecraft
	from mycode.ships import PlayableShip
	from mycode.enemies import BaseEnemy

class CollisionManager:
    def __init__(self):
        self.player_projectiles: Optional[set[Projectile]] = None
        self.enemy_projectiles: Optional[set[Projectile]] = None
        self.ships: Optional[set[Spacecraft]] = None

    def register_projectile(self, projectile: Projectile):
        """Add a projectile based on the is_player flag"""
        if projectile.is_player:
            self.player_projectiles.add(projectile)
        else:
            self.enemy_projectiles.add(projectile)

    def register_projectiles(self, projectiles: list[Projectile]):
        """
        Allows to register more projectiles at once

        To avoid bugs, all projectiles must have the same value of 'is_player'
        """
        # if len(projectiles) == 0:
        #     raise ArgumentError("The length of 'projectiles' parameter should not be zero")

        if projectiles[0].is_player:
            self.player_projectiles |= projectiles
        else:
            self.enemy_projectiles |= projectiles

    def register_ship(self, ship: Spacecraft):
        """Adds a ship to the list of ships"""
        self.ships.add(ship)

    def check_collisions(self) -> list[tuple[bool, Projectile, Spacecraft]]:
        """Main collision detection - call this every frame"""
        collisions: list[tuple[bool, Projectile, Spacecraft]] = [] # bool: player-friendly, bullet object, ship object

        for p in self.player_projectiles:
            for enemy in list(filter(lambda s: isinstance(s, BaseEnemy), self.ships)):
                if self._check_collision(p, enemy):
                    collisions.append((True, p, enemy))

        for p in self.enemy_projectiles:
            for ship in list(filter(lambda s: isinstance(s, PlayableShip), self.ships)):
                if self._check_collision(p, ship):
                    collisions.append((False, p, ship))

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