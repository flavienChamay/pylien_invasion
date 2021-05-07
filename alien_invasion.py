"""
This module manages the entire Alien Invasion game.

:class AlienInvasion: Main class of the game, managing all functionalities.
"""

import sys
import pygame


class AlienInvasion:
    """
    Class that manages the game assets and its behavior.

    :method: __init__(self)
    :method: 
    """

    def __init__(self):
        """
        Initialize the game and create game resources.

        :var screen Surface: The screen of the game.
        :returns: None.
        """

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        # Set background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """
        Function that starts the main loop for the game and displays the game.

        :var event Eventlist: An event in the game.
        :returns: None.
        """

        while True:
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run it.
    game = AlienInvasion()
    game.run_game()
