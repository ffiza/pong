import pygame
from settings import Settings
import random
import os


class Background(pygame.sprite.Sprite):
    """
    A class to manage the background images of the game.
    """
    def __init__(self) -> None:
        """
        Constructor for the Background class.
        """
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.settings = Settings()

        bg_imgs = os.listdir('../graphics/backgrounds/')
        self.bg_img = pygame.image.load(
            f'../graphics/backgrounds/{random.choice(bg_imgs)}')
        self.bg_img.convert_alpha()
        self.bg_rect = self.bg_img.get_rect()
        self.bg_rect.top = 0
        self.bg_rect.left = 0

    def blit_bg(self) -> None:
        """
        This function puts the background image on the game.
        """
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.bg_img, self.bg_rect)
