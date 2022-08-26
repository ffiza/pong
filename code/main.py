import pygame
import sys
from settings import Settings
from background import Background
from player import Player


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
                                               self.settings.screen_height),
                                              pygame.FULLSCREEN)
        pygame.display.set_caption(self.settings.window_name)

        self.background = Background()
        self.p1 = Player(x=self.settings.player_offset,
                         y=self.screen.get_size()[1]//2)
        self.p2 = Player(x=self.screen.get_size()[0]
                           - self.settings.player_offset
                           - self.settings.player_width,
                         y=self.screen.get_size()[1]//2)

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

        self._check_movement_events()

    def _update_screen(self) -> None:
        """
        Update elements on the screen and flip to the new screen.
        """
        self.background.blit_bg()  # Background should be draw first
        self.p1.draw_player()
        self.p2.draw_player()

        pygame.display.flip()

    @staticmethod
    def _quit_game() -> None:
        """
        This method quits the game.
        """
        pygame.quit()
        sys.exit()

    def _check_movement_events(self) -> None:
        """
        This method checks the inputs for the movement of the players.
        """
        keys = pygame.key.get_pressed()

        if keys[pygame.K_q]:
            self.p1.move_up()
        if keys[pygame.K_a]:
            self.p1.move_down()
        if keys[pygame.K_UP]:
            self.p2.move_up()
        if keys[pygame.K_DOWN]:
            self.p2.move_down()

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
