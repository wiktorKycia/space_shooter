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
		width // 2, height // 2,
		ImageButtonDisplayer("./images/buttons/button_play.png", "./images/buttons/button_play_hover.png"),
		callback=lambda: game()
	)

	button_exit = Button(
		50, 700,
		ImageButtonDisplayer("./images/buttons/button_exit.png", "./images/buttons/button_exit_hover.png"),
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
	global dt
	global width, height
	global player
	running: bool = True

	def menu_quit():
		nonlocal running
		running = False

	# define the buttons
	button_endless = Button(
		width // 3, height // 5,
		ImageButtonDisplayer("./images/buttons/button_endless.png", "./images/buttons/button_endless_hover.png")
	)
	button_levels = Button(
		width * 2 // 3, height // 5,
		ImageButtonDisplayer("./images/buttons/button_levels.png", "./images/buttons/button_levels_hover.png"),
		callback=lambda: levels()
	)
	button_ship = Button(
		width // 4, height - 50,
		ImageButtonDisplayer("./images/buttons/button_ship.png", "./images/buttons/button_ship_hover.png")
	)
	button_hangar = Button(
		width // 2, height - 50,
		ImageButtonDisplayer("./images/buttons/button_hangar.png", "./images/buttons/button_hangar_hover.png")
	)
	button_shop = Button(
		width * 3 // 4, height - 50,
		ImageButtonDisplayer("./images/buttons/button_shop.png", "./images/buttons/button_shop_hover.png")
	)
	button_back = Button(
		50, 700, ImageButtonDisplayer("./images/buttons/button_back.png", "./images/buttons/button_back_hover.png"),
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
	ship.reset_stats((width, height))

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
		write(surf=screen, text=str(player.coins), x=500, y=300, font_size=36, color=(200, 200, 200))

		write(surf=screen, text=f"Health: {str(ship.hp.amount)}", x=50, y=300, font_size=28, color=(200, 200, 200))
		write(surf=screen, text=f"Force: {str(-ship.physics.force)}", x=50, y=350, font_size=28, color=(200, 200, 200))
		write(surf=screen, text=f"Mass: {str(ship.physics.mass)}", x=50, y=400, font_size=28, color=(200, 200, 200))

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

def levels():
	global tps_clock
	global click
	global dt
	global width, height
	running: bool = True

	config_file: str = "./gameData/levels.json"
	number_of_levels: int = 0

	def menu_quit():
		nonlocal running
		running = False

	def calculate_level_y(level_id):
		a = level_id % 3
		if a == 0: a = 3
		b = level_id - a
		y = 80 + b * 40
		return y

	button_back = Button(
		50, 700, ImageButtonDisplayer("./images/buttons/button_back.png", "./images/buttons/button_back_hover.png"),
		callback=menu_quit
	)
	level_buttons = []
	with open(config_file, "r") as f:
		number_of_levels = len(json.load(f)['levels'])

	for i in range(number_of_levels):
		if (i + 1) % 3 == 1:
			level_buttons.append(LevelButton(width // 5, calculate_level_y(i + 1), 200, 100, i + 1, lambda: level(i+1, config_file)))
		elif (i + 1) % 3 == 2:
			level_buttons.append(LevelButton(width // 2, calculate_level_y(i + 1), 200, 100, i + 1, lambda: level(i+1, config_file)))
		elif (i + 1) % 3 == 0:
			level_buttons.append(
				LevelButton(width * 4 // 5, calculate_level_y(i + 1), 200, 100, i + 1, lambda: level(i+1, config_file))
			)

	while running:
		screen.fill((0, 0, 0))

		button_back.tick(click)
		button_back.draw(screen)

		for button in level_buttons:
			button.tick(click)
			button.draw(screen)


		# for i, button in enumerate(level_buttons):
		# 	# tu nie może być printa sprawdzającego check_click()
		# 	if button.check_click(mouse):
		# 		menuHandler.changeMenu(LevelGame)
		# 		menuHandler.currentMenu.level_pointer = i
		# 		menuHandler.currentMenu.reset_current_level()


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
			if event.type == MOUSEWHEEL:
				if event.y == -1:
					for button in level_buttons:
						button.y -= 50
						button.rect.center = (button.x, button.y)
				elif event.y == 1:
					for button in level_buttons:
						button.y += 50
						button.rect.center = (button.x, button.y)

		pygame.display.update()
		tps_clock.tick(tps_max)

def level(level_number: int, config_file: str):
	global tps_clock
	global click
	global dt
	global width, height
	global player
	running: bool = True

	player_ship = player.current_ship

	enemies: list[BaseEnemy] = []
	other_projectiles: list[Projectile] = []

	wave_manager: WaveManager = WaveManager(config_file)
	level_manager: LevelManager = LevelManager(wave_manager)

	# reset player's ship's stats
	player_ship.refill_stats()

	while running:
		screen.fill((0, 0, 0))

		player_ship.tick(dt)
		for enemy in enemies:
			enemy.tick(dt)

		for bullet in other_projectiles:
			if bullet.steered_by_menu:
				bullet.tick(dt)
			else:
				bullet.steered_by_menu = True

		level_manager.tick(level_number, enemies)

		for enemy in enemies:
			enemy.draw(screen)

		for bullet in other_projectiles:
			bullet.draw(screen)

		player_ship.draw(screen)


		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				if event.key == K_ESCAPE or event.key == K_p:
					# running = False
					pass # tu zrobić takie coś, żeby się pokazywało manu pauzy

		pygame.display.update()
		tps_clock.tick(tps_max)

if __name__ == "__main__":
	main_menu()