"""
This module manages an alien of the game.

:class Alien: This class manages an alien in the game.
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Class inheriting from Sprite and managing an alien.

    :method: __init__(self, game)
    """

    def __init__(self, game):
        """
        Initialize the alien and set its starting position.

        :var screen Surface:
        :var image Surface:
        :var rect Rect:
        :var rect.x int:
        :var rect.y int:
        """

        super().__init__()

        self.screen = game.screen

        # load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
