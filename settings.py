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
        """

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
