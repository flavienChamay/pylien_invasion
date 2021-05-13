"""
This module manages the entire Alien Invasion game.

:class AlienInvasion: Main class of the game, managing all functionalities.
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    """
    Class that manages the game assets and its behavior.

    :method: __init__(self)
    :method: run_game(self)
    :method: _check_keydown_events(self, event)
    :method: _check_keyup_events(self, event)
    :method: _check_events(self)
    :method: _fire_bullet(self)
    :method: _update_bullets(self)
    :method: _update_screen(self)
    :method: _create_fleet(self)
    :method: _update_aliens(self)
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

        # Ship, bullets and aliens initialized.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

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
            self._update_bullets()
            self._update_aliens()
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

        :param event Event: An event in the game.
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
        Method that creates a new bullet and add it to the bullets group.

        :var new_bullet Bullet: A new bullet shoot from the ship.
        :returns: None.
        """

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """
        Helper method of _check_events that responds to key releases.

        :param event Event: An event in the game.
        :returns: None.
        """

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """
        Helper method that updates the position of the bullets 
        and get rid of old bullets.

        :returns: None.
        """

        # Udate bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullets_alien_collisions()

    def _check_bullets_alien_collisions(self):
        """
        Helper method that checks alien-bullet collision. 
        If any bullet hits an alien then it gets rid of the bullets and of the alien.
        And if no more aliens are there then destroys existing bullets and repopulate the fleet of aliens.

        :returns: None.
        """

        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

    def _update_screen(self):
        """
        Helper method that update images on the screen, 
        and flip to the new screen.

        :returns: None.
        """

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

    def _create_fleet(self):
        """
        Method that creates a fleet of aliens.

        :var alien Alien: An alien of the fleet.
        :var alien_width int: The width of an alien.
        :var available_space_x int: The available horizontal space on the screen for the fleet.
        :var number_aliens_x int: The number of aliens in a row.
        :var alien_number int: The number of the alien in the fleet.
        :returns: None.
        """

        # Making an alien and finding the number of aliens in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
                             (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """
        This helper method creates an alien and place it on the row.

        :parma alien_number int: The number of the alien in the fleet.    
        :retunrs: None.
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        Helper method that checks if the fleet is at an edge and updates the positions of all aliens in the fleet.

        :returns: None.
        """

        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """
        Helper method that manages the appropriate respond if any aliens have reached an edge.

        :returns: None.
        """

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Helper method that changes the entire fleet's direction.

        :returns: None.
        """

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


if __name__ == '__main__':
    # Create a game instance and run it.
    game = AlienInvasion()
    game.run_game()
