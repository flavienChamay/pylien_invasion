"""
Manages the entire Alien Invasion game.

:class: AlienInvasion
"""

import sys
import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


class AlienInvasion:
    """
    Manages the game assets and its behavior.

    :method: __init__(self)
    :method: run_game(self)
    :method: _check_keydown_events(self, event)
    :method: _check_keyup_events(self, event)
    :method: _check_events(self)
    :method: _fire_bullet(self)
    :method: _update_bullets(self)
    :method: _screen(self)
    :method: _create_fleet(self)
    :method: _update_aliens(self)
    :method: _ship_hit(self)
    :method: _check_aliens_bottom(self)
    :method: _check_bullet_alien_collisions(self)
    :method: _check_fleet_edges(self)
    :method: _check_play_button(self, mouse_pos)
    :method: _ship_hit(self)
    """

    def __init__(self):
        """
        Initialize the game and create game resources.

        :var settings Settings: The settings of the game.
        :var screen Surface: The screen of the game.
        :var ship Ship: The ship of the player.
        :var bullets Group: The bullets of the ship of the player.
        :var bg_color (int, int, int): The background of the game.
        :var stats GameStats: The stats of the current game.
        :var play_button Button: The play button to trigger the beginning of the game.
        :var sb Scoreboard: The scoreboard of the current game.
        :var aliens Group: The aliens in the game.
        :returns AlienInvasion: Generates an instance of AlienInvasion.
        """
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create stats of the game.
        self.stats = GameStats(self)

        # Create a scoreboard.
        self.sb = Scoreboard(self)

        # Ship, bullets and aliens initialized.
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # Set background color.
        self.bg_color = (230, 230, 230)

        # Make the play button.
        self.play_button = Button(self, "Play")

    def run_game(self):
        """
        Start the main loop for the game and displays the game.

        :returns: None.
        """
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _check_events(self):
        """
        Respond to keypresses and mouse events.

        :var event Event: An event on the game.
        :var mouse_pos (int, int): The position of the mouse in (x, y) coordinates.
        :returns: None.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """
        Respond to key presses. And if q is pressed then the game exits.

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
        Create a new bullet and add it to the bullets group.

        :var new_bullet Bullet: A new bullet shoot from the ship.
        :returns: None.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_keyup_events(self, event):
        """
        Respond to key releases.

        :param event Event: An event in the game.
        :returns: None.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_bullets(self):
        """
        Update the position of the bullets and get rid of old bullets.

        :returns: None.
        """
        # Udate bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        """
        Check alien-bullet collision.

        If any bullet hits an alien then it gets rid of the bullets and of the alien.
        And if no more aliens are there then destroys existing bullets and repopulate the fleet of aliens.

        :var collisions Sprite_dict: Dictionnary of the collisions between an alien and bullets.
        :returns: None.
        """
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        # If a collision is detected then update score.
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase level
            self.stats.level += 1
            self.sb.prep_level()

    def _update_screen(self):
        """
        Update images on the screen and flip to the new screen.

        :returns: None.
        """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

    def _create_fleet(self):
        """
        Create a fleet of aliens.

        :var alien Alien: An alien of the fleet.
        :var alien_width int: The width of an alien.
        :var available_space_x int: The available horizontal space on the screen for the fleet.
        :var number_aliens_x int: The number of aliens in a row.
        :var alien_number int: The number of the alien in the fleet.
        :var ship_height int: The height of an alien.
        :var available_space_y int: Vertical available space between aliens.
        :var available_space_x int: Horizontal available space between aliens.
        :var number_rows int: Number of rows of aliens.
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
        Create an alien and place it on the row.

        :parma alien_number int: The number of the alien in the fleet.    
        :param row_number int: The row number of the alien fleet.
        :var alien Alien: The alien to be created.
        :var alien_width int: The width of an alien.
        :var alien_height int: The height of an alien.      
        :returns: None.
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        """
        Check if the fleet is at an edge and updates the positions of all aliens in the fleet.

        :returns: None.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

    def _check_fleet_edges(self):
        """
        Manage the appropriate respond if any aliens have reached an edge.

        :var alien Alien: An alien in the sprite of the fleet.
        :returns: None.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Change the entire fleet's direction.

        :var alien Alien: An alien in the sprite.
        :returns: None.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        """
        Manage the response of the ship to an alien ship.

        :returns: None.
        """
        if self.stats.ships_left > 0:
            # Decrement the number of ships left and update scoreboard.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause the game for the player to recover.
            sleep(1)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """
        Check if an alien hits the bottom of the screen.

        :var screen_rect Rect: Rectangular dimensions of the screen.
        :returns: None.
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this action the same as if the ship got hit.
                self._ship_hit()
                break

    def _check_play_button(self, mouse_pos):
        """
        Start the game when the play button is clicked.

        :param mouse_pos (int, int): Coordinates of the mouse on the screen.
        :var button_clicked bool: True if the button is clicked, false if not.
        :returns: None.
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the game statistics.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)


if __name__ == '__main__':
    # Create a game instance and run it.
    game = AlienInvasion()
    game.run_game()
