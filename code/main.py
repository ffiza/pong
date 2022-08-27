import pygame
import sys
from settings import Settings
from background import Background
from player import Player
from ball import Ball
from game_stats import GameStats
from scoreboard import Scoreboard
from debug import debug


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

        # Window and background
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height),
            pygame.FULLSCREEN)
        pygame.display.set_caption(self.settings.window_name)
        self.background = Background()

        self.clock = pygame.time.Clock()
        self.scoreboard = Scoreboard()
        self.stats = GameStats()

        # Players and ball
        self.p1 = Player(x=self.settings.player_offset,
                         y=self.screen.get_size()[1]//2)
        self.p2 = Player(x=self.screen.get_size()[0]
                           - self.settings.player_offset
                           - self.settings.player_width,
                         y=self.screen.get_size()[1]//2)
        self.ball = Ball()

    def run(self) -> None:
        """
        Run the main game loop.
        """
        while True:
            self._draw_background()
            self._check_pasive_events()

            if self.stats.game_active:
                self._check_active_events()

            self._update_screen()
            pygame.display.flip()
            self.clock.tick(self.settings.fps)

    def _check_pasive_events(self) -> None:
        """
        Monitor events that should run always.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_active_events(self) -> None:
        """
        Monitor events that should run when the game is active.
        """
        self._check_movement_events()

    def _check_score(self) -> None:
        """
        Check if the ball leaves the screen and update score.
        """
        if self.ball.rect.right >= self.screen.get_rect().right:
            # Score for player 1
            self.stats.scores[0] += 1
            self.ball.reset()
        if self.ball.rect.left <= self.screen.get_rect().left:
            self.stats.scores[1] += 1
            self.ball.reset()

    def _draw_background(self) -> None:
        """
        Draw the background.
        """
        self.background.blit_bg()

    def _update_screen(self) -> None:
        """
        Update elements on the screen and flip to the new screen.
        """
        if self.settings.debug_mode:
            debug(str(int(self.clock.get_fps())) + ' FPS')
            debug(str(self.ball.rect.center), y=20)
            debug(str(self.p1.rect.center), y=35)
            debug(str(self.p2.rect.center), y=50)

        self.scoreboard.draw(self.stats.scores)
        self.p1.draw_player()
        self.p2.draw_player()
        self.ball.draw_ball()
        self._check_collisions()
        self._check_score()

        if not self.stats.game_active:
            self._show_start_msg()

    def _show_start_msg(self) -> None:
        """
        Show start message and wait for play input to start game.
        """
        self.font = pygame.font.Font(self.settings.font_path,
                                     self.settings.msg_font_size)
        msg = 'Press SPACE to start the game!'
        msg_surf = self.font.render(msg, False, 'White')
        msg_pos = self.screen.get_rect().midtop + self.settings.msg_offset
        msg_rect = msg_surf.get_rect(midtop=msg_pos)
        self.screen.blit(msg_surf, msg_rect)

        # Check if space is pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.stats.game_active = True

    def _check_ball_player_collision(self) -> None:
        """
        Check if the ball collides with a player and change direction
        accordingly.
        """
        has_collided = self.ball.rect.colliderect(self.p1.rect) \
                       or self.ball.rect.colliderect(self.p2.rect)
        if has_collided:
            self.ball.direction.x *= -1

    @staticmethod
    def _quit_game() -> None:
        """
        This method quits the game.
        """
        pygame.quit()
        sys.exit()

    def _check_collisions(self) -> None:
        """
        Check collision for the ball.
        """
        self.ball.check_border_collisions()
        self._check_ball_player_collision()

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

        self.ball.move_ball()

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
