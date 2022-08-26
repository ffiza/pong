import pygame

pygame.init()

font = pygame.font.Font(None, 30)


def debug(info: str, x: int = 10, y: int = 10) -> None:
    """
    Prints custom information on the game screen.

    :param info: String with info to be printed in screen.
    :param x: x position of the text rectangle.
    :param y: y position of the text rectangle.
    """
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info), True, 'white')
    debug_rect = debug_surf.get_rect(topleft=(x, y))
    pygame.draw.rect(display_surface, 'black', debug_rect)
    display_surface.blit(debug_surf, debug_rect)
