from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from mycode.projectile import Projectile
	from mycode.spacecraft import Spacecraft


def check_collision(spacecraft: Spacecraft, projectile: Projectile) -> bool:
	if projectile.line is not None:
		if (spacecraft.displayer.mask.overlap(
				projectile.displayer.mask, (
						(projectile.physics.pos.x - projectile.displayer.width / 2) - spacecraft.displayer.hitbox.x,
						(projectile.physics.pos.y - projectile.displayer.height / 2) - spacecraft.displayer.hitbox.y
				)
		) or spacecraft.displayer.hitbox.clipline(projectile.line)):
			return True
		return False
	elif spacecraft.displayer.mask.overlap(
			projectile.displayer.mask, (
					(projectile.physics.pos.x - projectile.displayer.width / 2) - spacecraft.displayer.hitbox.x,
					(projectile.physics.pos.y - projectile.displayer.height / 2) - spacecraft.displayer.hitbox.y
			)
	):
		return True
	return False
