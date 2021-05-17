"""
This module manages the scoring informations of the game.

:class Scoreboard: Class of the scoreboard.
"""

import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard:
    """
    Class that manages the displaying of the score on the screen.

    :method: __init__(self, game)
    :method: check_high_score(self)
    :method: prep_score(self)
    :method: show_score(self)
    :method: prep_high_score(self)
    :method: prep_level(self)
    :method: prep_ships(self)
    """

    def __init__(self, game):
        """
        Method initializing the scrorekeeping attributes and creates an instance of Scoreboard.

        :param game AlienInvasion: The current game of Alien Invasion.
        :var game AlienInvasion: The current game of Alien Invasion as an attribute.
        :var screen Surface: The screen of the game.
        :var screen_rect Rect: The dimensions of the screen.
        :var settings Settings: The settings of the game.
        :var stats GameStats: The statistics of the game.
        :var text_color (int, int, int): The color of the text of the scoring.
        :var font Font: The font of the scoring.
        :returns Scoreboard: Generates an instance of the Scoreboard class.
        """

        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        """
        Method that turns the score into a rendered image.

        :var rounded_score int: The score rounded.
        :var score_str str: The string of text containing the score.
        :var score_image Surface: The image rendered of the scoring.
        :var score_rect Rect: The rectangle dimension of the scoring.
        :returns: None.
        """

        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        Method that draw the score, the level and the ships (lifes of the player) to the screen.

        :returns: None.
        """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """
        Method that turns the high score into a rendered image.

        :var high_score int: Highest score in the game on this computer.
        :var high_score_str: Highest score converted into an image.
        :var high_score_image Surface: Image of the highest score rendered.
        :var high_score_rect Rect: Dimension of the var high_score_image.
        :returns: None.
        """

        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(
            high_score_str, True, self.text_color, self.settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """
        Method that checks to see if there's a new high score.
        And updates the value of the highest score if there is one.

        :var stats.high_score int: The highest score of the game on this computer.
        :returns: None.
        """

        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def prep_level(self):
        """
        Method that turns the level into a rendered image.

        :var level_str str: The current level of the user in the game.       
        :var level_image Surface: Rendered image of level_str var.
        :var level_rect Rect: Rectangular dimensions of level_image var.
        :returns: None.
        """

        level_str = str(self.stats.level)
        self.level_image = self.font.render(
            level_str, True, self.text_color, self.settings.bg_color)

        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        """
        Method that show how many ships are left.

        :var ships Group: Group of ships indicating lifes of the player.
        :var ship_number int: The number of each ship to be displayed.
        :var ship Ship: A ship to be displayed.
        :returns: None.
        """

        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
