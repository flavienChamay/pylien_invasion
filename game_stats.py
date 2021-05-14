"""
This module manages and tracks the statistics of the game.

:class GameStats: The class that manages statistics.
"""


class GameStats:
    """
    Class that tracks statistics for Alien Invasion game.

    :method: __init__(self, game)
    :method: reset_stats(self)
    """

    def __init__(self, game):
        """
        Method that initialize the GameStats class.

        :param game AlienInvasion: The current game.
        :var settings Settings: The settings of the game.
        :var game_active bool: True if the game is still active, false if not. 
        By default, false because the game waits for the player to click the play button.
        :returns: None.
        """

        self.settings = game.settings
        self.reset_stats()
        self.game_active = False

    def reset_stats(self):
        """
        Method that reset all statistics when a new game is created.

        :var ships_left :
        :returns: None.
        """

        self.ships_left = self.settings.ship_limit
