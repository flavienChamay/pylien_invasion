"""
This module contains the description of the ship of the player in the Alien Invasion game.

:class Ship: This class is the ship of the player.
"""

import pygame


class Ship:
    """
    Class that manages all the functionalities of the ship of the player.

    :method: __init__(self)
    :method: blitme(self)
    :method: update(self)
    """

    def __init__(self, game):
        """
        Initialize the ship and set its starting position.

        :var screen Surface: The screen of the game var.
        :var screen_rect Rect: The rectangular coordinates of the ship.
        :var image Surface: Loads the image of the ship.
        :var rect Rect: The rectangular coordinates of the image of the ship.
        :var rect.midbottom Rect: The rectangular coordinates of the ship displayed at the bottom center of the screen.
        :var moving_left Bool: True if the ship is moving left, false if not. Default at False.
        :var moving_right Bool: True if the ship is moving right, false if not. Default at False.
        :var settings Settings: The settings of the game.
        :returns: None.
        """

        # Position of the ship set.
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        # Load the ship image and gettings its coordinates.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Display the ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flag.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Method that updates the ship's position based on the movement flag.

        :var rect.x int: The X coordinate of the ship.
        :returns: None.
        """

        # Update the ship's x value, not the rect.
        if self.moving_right and (self.rect.right < self.screen_rect.right):
            self.x += self.settings.ship_speed
        if self.moving_left and (self.rect.left > 0):
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """
        Function that draws the ship at its current location.

        :returns: None.
        """

        self.screen.blit(self.image, self.rect)