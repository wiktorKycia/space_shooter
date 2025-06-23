import pygame, sys
from mycode.levels import *
from mycode.UI import *
from pygame.locals import *
import json

pygame.init()
pygame.display.set_caption("Planet defender")

tps_max = 100.0
tps_clock = pygame.time.Clock()
dt = 0.0

running: bool = True

width, height = (750, 750)
screen = pygame.display.set_mode((width, height))

player = Player()

shipBuilder = PlayableShipBuilder()
shipDirector = PlayableShipBuilderDirector(shipBuilder, "Ship1")

with open("./gameData/playerShips.json") as f:
	for ship in json.load(f)['ships']:
		shipDirector.choose_ship(ship['name'])
		player.add_new_ship(shipDirector.build(width / 2, height / 2))

mouse = Mouse()

waveManager: WaveManager = WaveManager("./gameData/levels.json")
levelManager: LevelManager = LevelManager(waveManager)

while running:
	# Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# clock
	dt = tps_clock.get_time() / 1000
	tps_clock.tick(tps_max)

	# Draw the background
	screen.fill((0, 0, 0))

	# Do the next tick
	pygame.display.update()

# Exit
pygame.quit()
quit()
