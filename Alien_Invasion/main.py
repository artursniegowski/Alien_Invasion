import pygame
from my_settings import MySettings
from space_ship import SpaceShip
import functions as game_func


def game_on():
    # Main thread - init Pygame , screen etc.
    pygame.init()
    my_settings = MySettings()
    screen = pygame.display.set_mode((my_settings.screen_width,\
        my_settings.screen_height))
    pygame.display.set_caption(my_settings.caption)
    
    # Make a spaceship
    space_ship = SpaceShip(my_settings,screen)

    # run window
    while True: 

        # Watch for keyboard and mouse events
        game_func.check_events(space_ship)
        space_ship.update_pos()
        # updatign screen 
        game_func.update_view(my_settings,screen,space_ship)

        
# Start the game
game_on()