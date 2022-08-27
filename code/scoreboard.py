import pygame
from settings import Settings
from pygame.math import Vector2


class Scoreboard:
    """
    A class to manage the scores on screen.
    """
    def __init__(self):
        """
        A constructor for the Scoreboard class.
        """
        self.settings = Settings()

        self.screen = pygame.display.get_surface()
        self.font = pygame.font.Font(self.settings.score_font_path,
                                     self.settings.score_font_size)

    def draw(self, scores: list) -> None:
        """
        Draw the scores on the screen.

        :param scores: A list of two elements with the scores of each player.
        """
        p1_score_surf = self.font.render(f'{scores[0]}', False, 'White')
        p1_score_rect = p1_score_surf.get_rect(
            topleft=self.settings.score_offset)
        self.screen.blit(p1_score_surf, p1_score_rect)

        p2_score_surf = self.font.render(f'{scores[1]}', False, 'White')
        p2_score_pos = self.screen.get_rect().topright \
                       - self.settings.score_offset.reflect(Vector2(0, 1))
        p2_score_rect = p2_score_surf.get_rect(
            topright=p2_score_pos)
        self.screen.blit(p2_score_surf, p2_score_rect)
