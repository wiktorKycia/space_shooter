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


click: bool = False

def main_menu():
	global tps_clock
	global click
	global dt
	running: bool = True

	# objects
	# player = Player()
	#
	# shipBuilder = PlayableShipBuilder()
	# shipDirector = PlayableShipBuilderDirector(shipBuilder, "Ship1")
	#
	# with open("./gameData/playerShips.json") as f:
	# 	for ship in json.load(f)['ships']:
	# 		shipDirector.choose_ship(ship['name'])
	# 		player.add_new_ship(shipDirector.build(width / 2, height / 2))
	#
	# mouse = Mouse()
	#
	# waveManager: WaveManager = WaveManager("./gameData/levels.json")
	# levelManager: LevelManager = LevelManager(waveManager)

	# main loop
	while running:
		# clock
		dt:float = tps_clock.get_time() / 1000

		# Draw the background
		screen.fill((0, 0, 0))

		draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

		mx, my = pygame.mouse.get_pos()

		button_1 = pygame.Rect(50, 100, 200, 50)
		button_2 = pygame.Rect(50, 200, 200, 50)
		if button_1.collidepoint((mx, my)):
			if click:
				game()
		if button_2.collidepoint((mx, my)):
			if click:
				options()
		pygame.draw.rect(screen, (255, 0, 0), button_1)
		pygame.draw.rect(screen, (255, 0, 0), button_2)

		click = False

		# Events
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					pygame.quit()
					sys.exit()
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		# Do the next tick
		pygame.display.update()
		tps_clock.tick(tps_max)

	# Exit
	pygame.quit()
	quit()


def game():
	global tps_clock
	running = True
	while running:
		screen.fill((0, 0, 0))

		draw_text('game', font, (255, 255, 255), screen, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False

		pygame.display.update()
		tps_clock.tick(60)


def options():
	running = True
	while running:
		screen.fill((0, 0, 0))

		draw_text('options', font, (255, 255, 255), screen, 20, 20)
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False

		pygame.display.update()
		tps_clock.tick(60)


if __name__ == "__main__":
	main_menu()