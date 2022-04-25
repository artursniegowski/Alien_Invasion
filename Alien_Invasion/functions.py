import sys
from tkinter.messagebox import NO
import pygame
from pygame.sprite import Group
from my_settings import MySettings
from space_ship import SpaceShip
from rocket import Rocket
from alien_ship import Alien_Ship

def check_events_keydown(event: pygame.event, my_settings : MySettings,\
     screen : pygame.Surface, space_ship: SpaceShip,\
          rockets :  Group ) -> None:
    """Events - key down"""
    if event.key == pygame.K_ESCAPE:
        # End the game
        pygame.quit()
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        # Start movig to the right
        space_ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        # Start movig to the left
        space_ship.moving_left = True 
    elif event.key == pygame.K_SPACE:
        # New rocket - hit spacebar
        if len(rockets) < my_settings.rocket_capacity:
            rocket = Rocket(my_settings,screen,space_ship)
            rockets.add(rocket)
        
def check_events_keyup(event: pygame.event, space_ship: SpaceShip) -> None:
    """Events - key up"""
    if event.key == pygame.K_RIGHT:
        # Stop movig to the right
        space_ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
        # Stop movig to the left
        space_ship.moving_left = False 

def check_events(my_settings : MySettings, screen : pygame.Surface, \
    space_ship : SpaceShip, rockets : Group) -> None:
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        # Exiting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Moving the ship
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(event, my_settings, screen, space_ship, \
                rockets)
        
        elif event.type == pygame.KEYUP:
            check_events_keyup(event, space_ship)


def update_rockets(rockets : Group) -> None:
    """Encapsulating the functions managing rockets"""
    rockets.update()

    # Erasing rockets that are out of reach
    #print(len(rockets))
    #print((rockets))
    for rocket in rockets:
        if rocket.rocket_image_rect.bottom <= 0:
            rockets.remove(rocket)

def position_alien_ships(my_settings : MySettings, screen :pygame.Surface, \
    alien_ships: Group) -> None:
    """Create and position all of the alien ships"""
    # Getting the dimensions from an alien ship
    alien_ship = Alien_Ship(my_settings,screen)
    Max_aliens_ships_x = max_alien_ships_x(my_settings,alien_ship)
    Max_aliens_ships_y = max_alien_ships_y(my_settings,alien_ship)

    # Positioning the alien ships
    for alien_ship_number_y in range(Max_aliens_ships_y):  
        for alien_ship_number_x in range(Max_aliens_ships_x):
            alien_ship = Alien_Ship(my_settings,screen)
            pos_x = alien_ship.alien_ship_rect.width/2 + my_settings.space_factor_x \
                * alien_ship.alien_ship_rect.width * alien_ship_number_x 
            alien_ship.alien_ship_rect.x = pos_x
            pos_y = alien_ship.alien_ship_rect.height/2 + my_settings.space_factor_y \
                * alien_ship.alien_ship_rect.height * alien_ship_number_y 
            alien_ship.alien_ship_rect.y = pos_y
            alien_ships.add(alien_ship)


def max_alien_ships_x(my_settings : MySettings, alien_ship: Alien_Ship) -> int:
    """Calculating max number of ships (horizontally)"""
    Max_aliens_ships_x = int((my_settings.screen_width / \
        alien_ship.alien_ship_rect.width) /my_settings.space_factor_x)

    return Max_aliens_ships_x

def max_alien_ships_y(my_settings : MySettings, alien_ship: Alien_Ship) -> int:
    """Calculating max number of ships (vertically) """
    Max_aliens_ships_y = int((my_settings.screen_height / \
        alien_ship.alien_ship_rect.height) /my_settings.space_factor_y * 0.4)

    return Max_aliens_ships_y

def update_alien_ships(alien_ships : Group) -> None :
    """Move all the allien ships"""
    alien_ships.update()

def update_view(my_settings : MySettings, screen : pygame.Surface, \
    space_ship : SpaceShip, rockets : Group, alien_ships : Group) -> None:
        """Update view on tha main screen"""
        # Changing surface color
        screen.fill(my_settings.background_color)
        space_ship.draw_ship()       
        # Draw all the rockets
        for rocket in rockets:
            rocket.draw_rocket()
        # Drawing Alien ships
        for alien_ship in alien_ships:
            alien_ship.draw_alien_ship()
        # Update the screen
        pygame.display.update()
        #pygame.display.flip()