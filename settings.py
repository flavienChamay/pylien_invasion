"""
This module contains all the settings for the Alien Invasion game.

:class Settings: Class containing all settings of the game.
"""


class Settings:
    """
    This class stores all settings for Alien Invasion.

    :method: __init__(self)
    """

    def __init__(self):
        """
        Initialize the game's settings like the screen.

        :var screen_width int: The width of the screen.
        :var screen_height int: The height of the screen.
        :var bg_color (int, int, int): The color of the background of the game.
        :var ship_speed int: The speed of the ship.
        :var bullet_speed float: The speed of the bullet.
        :var bullet_width int: The width of a bullet.
        :var bullet_height int: The height of a bullet.
        :var bullet_color (int, int, int): The color of the bullet.
        :var bullets_allowed int: The number of bullets allowed in the screen.
        """

        self.screen_width = 960
        self.screen_height = 540
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
