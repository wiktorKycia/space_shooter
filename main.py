from typing import TYPE_CHECKING

import pygame, sys
from mycode.levels import *
from mycode.UI import *
from pygame.locals import *
import json

from pygame.font import Font

# initialization
pygame.init()
pygame.display.set_caption("Planet defender")

# screen
width, height = (750, 750)
screen = pygame.display.set_mode((width, height))

# text
font = pygame.font.SysFont(None, 20)

def draw_text(text: str, font: Font, color: tuple[int, int, int], surface: pygame.Surface, x: int, y: int):
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
	global width, height
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
		dt = tps_clock.get_time() / 1000

		# Loading objects
		# load title image
		title_image = pygame.image.load("./images/Game_title.png")
		title_image = pygame.transform.scale(
			title_image, (int(title_image.get_width() * 2), int(title_image.get_height() * 2))
		)

		# load background image
		bg = pygame.image.load("./images/background.png").convert_alpha()

		# get the mouse position
		# mx, my = pygame.mouse.get_pos()

		# load buttons
		button_play = Button(
			width/2, height/2, "./images/buttons/button_play.png", 1.0, "./images/buttons/button_play_hover.png",
			callback=lambda: game()
		)
		button_exit = Button(
			50, 700, "./images/buttons/button_exit.png", 1.0, "./images/buttons/button_exit_hover.png",
			callback=lambda: (pygame.quit(), sys.exit())
		)
		buttons = [button_play, button_exit]


		# Draw the background
		screen.fill((0, 0, 0))

		# play the buttons
		for button in buttons:
			button.tick(click)

		# display objects
		screen.blit(bg, (0,0))
		screen.blit(
			title_image,
			(screen.get_width() / 2 - title_image.get_width() / 2, 150 - title_image.get_height() / 2)
		)
		for button in buttons:
			button.draw(screen)

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