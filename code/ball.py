import pygame
from settings import Settings
import random


class Ball(pygame.sprite.Sprite):
    """
    A class to manage the ball.
    """
    def __init__(self) -> None:
        """
        Constructor for the Ball class.
        """
        super().__init__()
        # General setup
        self.screen = pygame.display.get_surface()
        self.settings = Settings()

        # Ball setup
        self.rect = pygame.rect.Rect(0, 0,
                                     self.settings.ball_size,
                                     self.settings.ball_size)
        self.rect.center = self.screen.get_rect().center
        self.speed = self.settings.ball_speed
        # Use a random initial direction
        self.direction = pygame.math.Vector2(random.choices([1, -1], k=2))

    def draw_ball(self) -> None:
        """
        Draw the ball on screen.
        """
        pygame.draw.rect(self.screen, 'white', self.rect)

    def move_ball(self) -> None:
        """
        Move the ball
        """
        self.rect.center += self.speed * self.direction

    def reset(self) -> None:
        """
        Reset the ball position and select new initial direction.
        """
        self.rect.center = self.screen.get_rect().center
        self.direction = pygame.math.Vector2(random.choices([1, -1], k=2))

    def check_border_collisions(self) -> None:
        """
        Check is the ball collides with the screen borders and change direction.
        """
        has_collided = self.rect.bottom >= self.screen.get_rect().bottom \
                       or self.rect.top <= self.screen.get_rect().top
        if has_collided:
            self.direction.y *= -1

    def increase_speed(self, factor: float) -> None:
        """
        This method increases the ball of the speed by a given factor.

        :param factor: The multiplicative factor the speed is multiplied by
                       each time this method is called.
        """
        self.speed *= factor
