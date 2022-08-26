import pygame
from settings import Settings


class Player(pygame.sprite.Sprite):
    """
    A class to manage the player(s).
    """
    def __init__(self, x: int, y: int, game):
        """
        Constructor for the Player class.

        :param x: The x position of the player at creation.
        :param y: The y position of the player at creation.
        :param game: An instance of the Game class defined in main.py.
        """
        super().__init__()
        self.screen = game.screen
        self.settings = Settings()

        self.player_rect = pygame.rect.Rect(0, 0,
                                            self.settings.player_width,
                                            self.settings.player_height)
        self.player_rect.left = x
        self.player_rect.centery = y

    def draw_player(self) -> None:
        """
        Draw the player on the screen.
        """
        pygame.draw.rect(self.screen, 'white', self.player_rect)

    def move_up(self) -> None:
        """
        This method moves the player rect up.
        """
        if self.player_rect.top > 0:
            self.player_rect.y -= self.settings.player_speed

    def move_down(self) -> None:
        """
        This methods moves the player down.
        """
        if self.player_rect.bottom < self.screen.get_rect().height:
            self.player_rect.y += self.settings.player_speed
