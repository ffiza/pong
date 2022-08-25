import pygame
import sys
from settings import Settings


class Game:
    """
    Overall class to manage the game.
    """

    def __init__(self) -> None:
        """
        Constructor for the Game class.
        """
        pygame.init()

        self.settings = Settings()
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode((self.settings.screen_width,
                                               self.settings.screen_height))
        pygame.display.set_caption(self.settings.window_name)

    def run(self) -> None:
        """
        Run the main game loop.
        """
        while True:
            self._check_events()
            self._update_screen()

            self.clock.tick(self.settings.fps)

    def _check_events(self) -> None:
        """
        This function checks for user events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _update_screen(self) -> None:
        """
        Update elements on the screen and flip to the new screen.
        """
        self.screen.fill(self.settings.bg_color)
        pygame.display.flip()

    def _quit_game(self) -> None:
        """
        This method quits the game.
        """
        pygame.quit()
        sys.exit()

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """
        Checks for keydown events.

        :param event: An instance of the Event class.
        """
        if event.key == pygame.K_ESCAPE:
            self._quit_game()


if __name__ == '__main__':
    game = Game()
    game.run()
