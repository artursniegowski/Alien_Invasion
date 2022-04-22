import pygame
from my_settings import MySettings
from space_ship import SpaceShip
import sys


def game_on():
    # Main thread - init Pygame , screen etc.
    pygame.init()
    my_settings = MySettings()
    screen = pygame.display.set_mode((my_settings.screen_width,\
        my_settings.screen_height),pygame.RESIZABLE)
    pygame.display.set_caption(my_settings.caption)
    
    # Make a spaceship
    space_ship = SpaceShip(screen)

    # run window
    while True:

        # Watch for keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Changing surface color
        screen.fill(my_settings.background_color)
        space_ship.draw_ship()

        # Update the screen
        pygame.display.update()

        
# Start the game
game_on()