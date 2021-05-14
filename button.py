"""
This module manages a button in the game.

:class Button: Class that manages the button.
"""

import pygame.font


class Button:
    """
    Class managing a click button in the game.

    :method: __init__(self, game, msg)
    :method: _prep_msg(self, msg)
    :method: draw_button(self)
    """

    def __init__(self, game, msg):
        """
        Initialize button attributes and generates an instance of Button class.

        :returns: None.
        """

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 30)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """
        Helper method that turns msg into a rendered image and center text on the button.

        :param msg str: String of text in the button.
        :returns: None.
        """

        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """
        Method that draw a blank button and draw the message in it.

        :returns: None.
        """

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
