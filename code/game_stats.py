import pygame


class GameStats:
    """
    A class to manage the statistics of the game.
    """
    def __init__(self) -> None:
        """
        Constructor for the GameStats class.
        """
        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(None, 40)

        self.scores = [0, 0]

        # Initialize the game in an inactive state
        self.game_active = False
