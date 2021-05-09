"""
This module manages the entire Alien Invasion game.

:class AlienInvasion: Main class of the game, managing all functionalities.
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class AlienInvasion:
    """
    Class that manages the game assets and its behavior.

    :method: __init__(self)
    :method: run_game(self)
    :method: _check_keydown_events(self, event)
    :method: _check_keyup_events(self, event)
    :method: _check_events(self)
    :method: _fire_bullet(self)
    :method: _update_screen(self)
    """

    def __init__(self):
        """
        Initialize the game and create game resources.

        :var screen Surface: The screen of the game.
        :var ship Ship: The ship of the player.
        :var bullets Group: The bullets of the ship of the player.
        :var bg_color (int, int, int): The background of the game.
        :returns: None.
        """

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Ship and bullets initialized.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Set background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """
        Function that starts the main loop for the game and displays the game.

        :returns: None.
        """

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        """
        Helper method that responds to keypresses and mouse events.

        :var event Event: An event on the game.
        :returns: None.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        Helper method of _check_events that responds to key presses. And if q is pressed then the game exits.

        :returns: None.
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _fire_bullet(self):
        """
        Method that create a new bullet and add it to the bullets group.

        :var new_bullet Bullet: A new bullet shoot from the ship.
        :returns: None.
        """

        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """
        Helper method of _check_events that responds to key releases.

        :returns: None.
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """
        Helper method that update images on the screen, and flip to the new screen.

        :returns: None.
        """

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    # Create a game instance and run it.
    game = AlienInvasion()
    game.run_game()
