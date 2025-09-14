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
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)

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

# mouse
click: bool = False

# player
player = Player()

shipBuilder = PlayableShipBuilder()
shipDirector = PlayableShipBuilderDirector(shipBuilder, "Ship1")

with open("./gameData/playerShips.json") as f:
	for ship in json.load(f)['ships']:
		shipDirector.choose_ship(ship['name'])
		player.add_new_ship(shipDirector.build(width / 2, height / 2))

# waveManager: WaveManager = WaveManager("./gameData/levels.json")
# levelManager: LevelManager = LevelManager(waveManager)

def main_menu():
	global tps_clock
	global click
	global dt
	global width, height
	running: bool = True

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

	def menu_quit():
		nonlocal running
		running = False

	# load buttons
	button_play = Button(
		width / 2, height / 2, "./images/buttons/button_play.png", 1.0, "./images/buttons/button_play_hover.png",
		callback=lambda: game()
	)
	button_exit = Button(
		50, 700, "./images/buttons/button_exit.png", 1.0, "./images/buttons/button_exit_hover.png",
		callback=lambda: menu_quit()
	)
	buttons = [button_play, button_exit]

	# main loop
	while running:
		# clock
		dt = tps_clock.get_time() / 1000

		# Draw
		screen.fill((0, 0, 0))

		# display objects
		screen.blit(bg, (0,0))
		screen.blit(
			title_image,
			(screen.get_width() / 2 - title_image.get_width() / 2, 150 - title_image.get_height() / 2)
		)
		for button in buttons:
			button.draw(screen)

		# Tick
		for button in buttons:
			button.tick(click)

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
	global click
	running: bool = True

	def menu_quit():
		nonlocal running
		running = False

	# define the buttons
	button_endless = Button(
		screen_size[0] / 3, screen_size[1] / 5, "./images/buttons/button_endless.png", 1.0,
		"./images/buttons/button_endless_hover.png"
	)
	button_levels = Button(
		screen_size[0] * 2 / 3, screen_size[1] / 5, "./images/buttons/button_levels.png", 1.0,
		"./images/buttons/button_levels_hover.png"
	)
	button_ship = Button(
		screen_size[0] / 4, screen_size[1] - 50, "./images/buttons/button_ship.png", 1.0,
		"./images/buttons/button_ship_hover.png"
	)
	button_hangar = Button(
		screen_size[0] / 2, screen_size[1] - 50, "./images/buttons/button_hangar.png", 1.0,
		"./images/buttons/button_hangar_hover.png"
	)
	button_shop = Button(
		screen_size[0] * 3 / 4, screen_size[1] - 50, "./images/buttons/button_shop.png", 1.0,
		"./images/buttons/button_shop_hover.png"
	)
	button_back = Button(
		50, 700, "./images/buttons/button_back.png", 1.0, "./images/buttons/button_back_hover.png",
		callback=menu_quit
	)

	# pack the buttons to the list
	buttons = [
		button_endless,
		button_levels,
		button_ship,
		button_hangar,
		button_shop,
		button_back
	]
	bg = pygame.image.load("./images/background.png").convert_alpha()
	ship = player.current_ship
	ship.reset_stats(screen_size)

	# coin
	coin: pygame.Surface = create_image_with_alpha_conversion("./images/coin.png")
	coin = pygame.transform.scale(coin, (int(coin.get_width() * 5), int(coin.get_height() * 5)))

	while running:
		screen.fill((0, 0, 0))

		screen.blit(bg, (0,0))
		for button in buttons:
			button.draw(screen)

		ship.draw_for_menu(screen)
		screen.blit(coin, (450, 300))
		write(screen, str(player.coins), 500, 300, 36, (200, 200, 200))

		write(screen, f"Health: {str(ship.hp.amount)}", 50, 300, 28, (200, 200, 200))
		write(screen, f"Force: {str(-ship.physics.force)}", 50, 350, 28, (200, 200, 200))
		write(screen, f"Mass: {str(ship.physics.mass)}", 50, 400, 28, (200, 200, 200))

		for button in buttons:
			button.tick(click)

		click = False

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE:
					running = False
			if event.type == MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True

		pygame.display.update()
		tps_clock.tick(tps_max)


if __name__ == "__main__":
	main_menu()