import pygame
from settings import Settings


class Player(pygame.sprite.Sprite):
    """
    A class to manage the player(s).
    """
    def __init__(self, x: int, y: int):
        """
        Constructor for the Player class.

        :param x: The x position of the player at creation.
        :param y: The y position of the player at creation.
        """
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.settings = Settings()

        self.rect = pygame.rect.Rect(0, 0,
                                     self.settings.player_width,
                                     self.settings.player_height)
        self.rect.left = x
        self.rect.centery = y

    def draw_player(self) -> None:
        """
        Draw the player on the screen.
        """
        pygame.draw.rect(self.screen, 'white', self.rect)

    def move_up(self) -> None:
        """
        This method moves the player rect up.
        """
        if self.rect.top > 0:
            self.rect.y -= self.settings.player_speed

    def move_down(self) -> None:
        """
        This methods moves the player down.
        """
        if self.rect.bottom < self.screen.get_rect().height:
            self.rect.y += self.settings.player_speed
