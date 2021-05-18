"""
Manage and tracks the statistics of the game.

:class: GameStats()
"""


class GameStats:
    """
    Tracks the statistics of the game.

    :method: __init__(self, game)
    :method: reset_stats(self)
    """

    def __init__(self, game):
        """
        Initialize the GameStats class.

        :param game AlienInvasion: The current game.
        :var settings Settings: The settings of the game.
        :var game_active bool: True if the game is still active, false if not. 
        By default, false because the game waits for the player to click the play button.
        :var high_score int: The highest score of the Alien Invasion in this computer. 
        High score should never be reset.
        :returns GameStats: Generates an instance of GameStats class.
        """
        self.settings = game.settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        """
        Reset all statistics when a new game is created.

        :var ships_left int: The number of lives of the ship.
        :var score int: The score of the current game. Default is at 0 because we begin the game.
        :var level int: The level of the game. By default, it is at 1 (for the first level).
        :returns: None.
        """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
