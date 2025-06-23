import pygame, sys
from mycode.levels import *
from mycode.UI import *
from pygame.locals import *
import json

# initialization
pygame.init()
pygame.display.set_caption("Planet defender")

# screen
width, height = (750, 750)
screen = pygame.display.set_mode((width, height))

# text
font = pygame.font.SysFont(None, 20)

def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

# clocks
tps_max = 100.0
tps_clock = pygame.time.Clock()
dt = 0.0

running: bool = True

# objects
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

# main loop
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

	# logic here

	# Do the next tick
	pygame.display.update()

# Exit
pygame.quit()
quit()
