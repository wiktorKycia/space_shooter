from pygame import mixer
from mycode.other import RefillableBar
from mycode.cannons import *
from mycode.physics import PygamePhysics
from mycode.slot import Slot
from mycode.enemies import BaseEnemy
from mycode.displayable import Displayer

mixer.init()


class PlayableShip:
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

    def tick(self):
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
    
    def draw(self, screen: pygame.Surface):
        self.displayer.draw(screen, self.physics.x, self.physics.y)
        for slot in self.slots:
            slot.draw()



class Ship1(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_1.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.slots.extend(
            [
                Slot(game, self, Vector2(20, -20), pygame.K_KP_0, KineticLight),
                Slot(game, self, Vector2(-20, -20), pygame.K_KP_0, KineticLight)
            ]
        )

class Ship2(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_2.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.slots.extend([
            Slot(game, self, Vector2(0, -20), pygame.K_KP_0, ShotGun1)
        ])
        # self.guns.extend(
        #     [
        #         KineticMedium(game, self, Vector2(0, -20), key=pygame.K_KP_1)
        #     ]
        # )

class Ship3(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_3.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.slots.extend([
            Slot(game, self, Vector2(-10, -20), pygame.K_KP_0, Flamethrower1),
            Slot(game, self, Vector2(10, -20), pygame.K_KP_0, Flamethrower1)
        ])
        # self.guns.extend(
        #     [
        #         # KineticLight(game, self, Vector2(0, -20), key=pygame.K_KP_1)
        #         # ShotGun1(game, self, Vector2(0, -20), key=pygame.K_KP_1)
        #         Flamethrower1(game, self, Vector2(-10, -20), key=pygame.K_KP_0),
        #         Flamethrower1(game, self, Vector2(10, -20), key=pygame.K_KP_0)
        #     ]
        # )

class Ship4(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_4.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
        self.slots.extend([
            Slot(game, self, Vector2(3, -15), pygame.K_KP_0, Laser1),
            Slot(game, self, Vector2(-4, -15), pygame.K_KP_0, Laser1),
            Slot(game, self, Vector2(13, 6), pygame.K_KP_0, Laser1),
            Slot(game, self, Vector2(-14, 6), pygame.K_KP_0, Laser1)
        ])

class Ship5(PlayableShip):
    def __init__(self, game):
        super().__init__(
            game, "./images/SpaceShips/Ship_5.png",
            mass=300,
            max_speed=275,
            force=1500,
            hp_amount=200,
            hp_height=25, hp_width=300,
            hp_x=165, hp_y=710,
            scale=2.0
        )
