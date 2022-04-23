import sys
import pygame
from my_settings import MySettings
from space_ship import SpaceShip

def check_events():
    """Watch for keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def update_view(my_settings : MySettings, screen : pygame.Surface, \
    space_ship : SpaceShip) -> None:
        """Update view on tha main screen"""
        # Changing surface color
        screen.fill(my_settings.background_color)
        space_ship.draw_ship()
        # Update the screen
        pygame.display.update()