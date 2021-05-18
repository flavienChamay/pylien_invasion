"""
Contain all the settings for the Alien Invasion game.

:class: Settings()
"""


class Settings:
    """
    Stores all the settings of the game.

    :method: __init__(self)
    :method: initialize_dynamic_settings(self)
    :method: increase_speed(self)
    """

    def __init__(self):
        """
        Initialize the game's settings like the screen, etc...

        :var screen_width int: The width of the screen.
        :var screen_height int: The height of the screen.
        :var bg_color (int, int, int): The color of the background of the game.
        :var ship_speed int: The speed of the ship.
        :var bullet_speed float: The speed of the bullet.
        :var bullet_width int: The width of a bullet.
        :var bullet_height int: The height of a bullet.
        :var bullet_color (int, int, int): The color of the bullet.
        :var bullets_allowed int: The number of bullets allowed in the screen.
        :var score_scale float: How quickly the alien point values increase.
        :var speedup_scale float: How quickly the game speeds up.
        :returns: Settings instance.
        """
        self.screen_width = 960
        self.screen_height = 540
        self.bg_color = (230, 230, 230)

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # Ship settings
        self.ship_limit = 3

        self.speedup_scale = 1.1

        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """
        Initialize the settings that change throughout the game.

        :var ship_speed float: The speed of the ship.
        :var bullet_speed float: The speed of the bullets.
        :var alien_speed float: The speed of an alien.
        :var fleet_direction int: 1 represents right, -1 represents left.
        :var alien_points int: The number of points earned by alien eliminated.
        :returns: None.
        """
        self.alien_speed = 1.0
        self.bullet_speed = 1.0
        self.ship_speed = 1.5
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """
        Inscreases the speed of the game and alien point values.

        :var ship_speed float: The speed of the ship being increased.
        :var bullet_speed float: The speed of the bullet being increased.
        :var alien_speed float: The speed of the aliens being increased.
        :var alien_points int: The points given to the player each time an alien is hit.
        :returns: None.
        """
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
