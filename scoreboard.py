"""
This module manages the scoring informations of the game.

:class Scoreboard: Class of the scoreboard.
"""

import pygame.font


class Scoreboard:
    """
    Class that manages the displaying of the score on the screen.

    :method: __init__(self, game)
    """

    def __init__(self, game):
        """
        Method initializing the scrorekeeping attributes and creates an instance of Scoreboard.

        :var screen Surface: The screen of the game.
        :var screen_rect Rect: The dimensions of the screen.
        :var settings Settings: The settings of the game.
        :var stats GameStats: The statistics of the game.
        :var text_color (int, int, int): The color of the text of the scoring.
        :var font Font: The font of the scoring.
        :returns: Scoreboard.
        """
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Font settings for scoring information
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        # Prepare the initial score image.
        self.prep_score()

    def prep_score(self):
        """
        Method that turns the score into a rendered image.

        :var score_str str: The string of text containing the score.
        :var score_image Surface: The image rendered of the scoring.
        :var :
        :returns: None.
        """

        score_str = str(self.stats.score)
        self.score_image = self.font.render(
            score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """
        Method that draw the score to the screen.

        :returns: None.
        """
        self.screen.blit(self.score_image, self.score_rect)
