"""
Manages an alien in the game.

:class: Alien(Sprite)
"""

import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Manage an alien.

    :method: __init__(self, game)
    :mehtod: update(self)
    :method: check_edges(self)
    """

    def __init__(self, game):
        """
        Initialize the alien and set its starting position.

        :var screen Surface: The screen object.
        :var image Surface: The image of the alien.
        :var rect Rect: The rectangular position of the alien.
        :var x float: The horizontal position of the alien on the screen.
        :var settings Settings: The settings of the game.
        :retuns Alien: Instance of an alien object.
        """
        super().__init__()
        self.screen = game.screen

        # Load settings of the game.
        self.settings = game.settings

        # load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self):
        """
        Move the alien to the right.

        :returns: None.
        """
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        """
        Check if an alien touches the edge of the screen.

        :returns bool: True if it touches the edge, false if not.
        """
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right or self.rect.left <= 0)
