import pygame

def write(game, text, x, y, font_size, color=(0, 0, 0), font_style="Arial", is_centered=False,):
    font = pygame.font.SysFont(font_style, font_size)
    rend = font.render(text, True, color)
    if is_centered is True:
        x = (game.width - rend.get_rect().width)/2
        y = (game.height - rend.get_rect().height)/2
    game.screen.blit(rend, (x, y))

def write_on_surface(surface, text, x, y, font_size, color=(0, 0, 0), is_centered=False, font_style='Arial'):
    font = pygame.font.SysFont(font_style, font_size)
    rend = font.render(text, True, color)
    if is_centered is True:
        x = (surface.get_rect().width - rend.get_rect().width) / 2
        y = (surface.get_rect().height - rend.get_rect().height) / 2
    surface.blit(rend, (x, y))


def convert_path(path: str) -> pygame.Surface:
    return pygame.image.load(path).convert_alpha()
