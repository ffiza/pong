import pygame
import numpy as np


def get_rect_sides(rect: pygame.rect.Rect) -> np.ndarray:
    """
    Gets all the sides of an instrance of the pygame.rect.Rect class and
    returns a NumPy array with the values.

    :param rect: An instance of the pygame.rect.Rect class for which to
                 calculate the sides.
    :return sides: A NumPy array with the sides on the following order:
                   (left, top, right, bottom).
    """
    sides = np.array([rect.left, rect.top, rect.right, rect.bottom])
    return sides
