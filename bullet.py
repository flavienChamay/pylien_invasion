"""
This module manages the bullets of the ship of the player.

:class Bullet(Sprite): Class that manages the bullets.
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Class inheriting of the Sprite class that manages the bullets.

    :method: __init__(self, game)
    :method: update(self)
    :method: draw_bullet(self)
    """

    def __init__(self, game):
        """
        Initialize a bullet object at the ship's current position.

        :param game AlienInvasion: The current game of Alien Invasion.
        :var screen Surface: The screen of the game.
        :var settings Settings: The current settings of the game.
        :var color (int, int, int): Color of the bullet.
        :var rect Rect: The rectangular dimension of the bullet.
        :var y int: The vertical coordinate of the bullet on the screen.
        :returns Bullet: Generates an instance of the Bullet class.
        """

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rectangle at (0,0) and then set correct position.
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = game.ship.rect.midtop

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self):
        """
        Method that moves the bullet up the screen.

        :var y float: The y coordinates of the bullet.
        :returns: None.
        """

        # Update the decimal position of the bullet
        self.y -= self.settings.bullet_speed
        # Update the rec position of the bullet.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Method that draws the bullet to the screen.

        :returns: None.
        """

        pygame.draw.rect(self.screen, self.color, self.rect)
