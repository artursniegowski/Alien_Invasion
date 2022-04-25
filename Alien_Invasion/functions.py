import sys
import pygame
from pygame.sprite import Group
from my_settings import MySettings
from space_ship import SpaceShip
from rocket import Rocket

def check_events_keydown(event: pygame.event, my_settings : MySettings,\
     screen : pygame.Surface, space_ship: SpaceShip,\
          rockets :  Group ) -> None:
    """Events - key down"""
    if event.key == pygame.K_RIGHT:
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

def update_view(my_settings : MySettings, screen : pygame.Surface, \
    space_ship : SpaceShip, rockets : Group) -> None:
        """Update view on tha main screen"""
        # Changing surface color
        screen.fill(my_settings.background_color)
        space_ship.draw_ship()       
        # Draw all the rockets
        for rocket in rockets:
            rocket.draw_rocket()
        # Update the screen
        pygame.display.update()
        #pygame.display.flip()