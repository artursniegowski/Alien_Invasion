import sys
import pygame
from my_settings import MySettings
from space_ship import SpaceShip

def check_events_keydown(ship: SpaceShip, event: pygame.event) -> None:
    """Events - key down"""
    if event.key == pygame.K_RIGHT:
        # Start movig to the right
        ship.moving_right = True 
    elif event.key == pygame.K_LEFT:
        # Start movig to the left
        ship.moving_left = True 

def check_events_keyup(ship: SpaceShip, event: pygame.event) -> None:
    """Events - key up"""
    if event.key == pygame.K_RIGHT:
        # Stop movig to the right
        ship.moving_right = False 
    elif event.key == pygame.K_LEFT:
        # Stop movig to the left
        ship.moving_left = False 

def check_events(ship: SpaceShip) -> None:
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        # Exiting the game
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Moving the ship
        elif event.type == pygame.KEYDOWN:
            check_events_keydown(ship, event)
        
        elif event.type == pygame.KEYUP:
            check_events_keyup(ship, event)


def update_view(my_settings : MySettings, screen : pygame.Surface, \
    space_ship : SpaceShip) -> None:
        """Update view on tha main screen"""
        # Changing surface color
        screen.fill(my_settings.background_color)
        space_ship.draw_ship()
        # Update the screen
        pygame.display.update()