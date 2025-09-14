import pygame


def write(surf: pygame.Surface, text, x, y, font_size, color=(0, 0, 0), font_style="Arial", is_centered=False):
    font = pygame.font.SysFont(font_style, font_size)
    rend = font.render(text, True, color)
    if is_centered:
        x = (surf.get_width() - rend.get_rect().width)/2
        y = (surf.get_height() - rend.get_rect().height)/2
    surf.blit(rend, (x, y))


def create_image_with_alpha_conversion(path: str) -> pygame.Surface:
    return pygame.image.load(path).convert_alpha()
