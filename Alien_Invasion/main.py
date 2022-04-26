import pygame
from my_settings import MySettings
from space_ship import SpaceShip
import functions as game_func
from rocket import Rocket
from alien_ship import Alien_Ship

def game_on():
    # Main thread - init Pygame , screen etc.
    pygame.init()
    my_settings = MySettings()
    screen = pygame.display.set_mode((my_settings.screen_width,\
        my_settings.screen_height))
    pygame.display.set_caption(my_settings.caption)
    
    # Make a spaceship
    space_ship = SpaceShip(my_settings,screen)
    # Creating a group of rockets
    rockets = pygame.sprite.Group()
    # Creating alien ships
    alien_ships = pygame.sprite.Group()
    # Position all the alien ships
    game_func.position_alien_ships(my_settings,screen,alien_ships)
    
    # run window
    while True: 

        # Watch for keyboard and mouse events
        game_func.check_events(my_settings,screen,space_ship,rockets)
        space_ship.update_pos()
        game_func.update_rockets(my_settings,screen,alien_ships,rockets)
        game_func.update_alien_ships(my_settings,space_ship,alien_ships)
        # updatign screen 
        game_func.update_view(my_settings,screen,space_ship,rockets,alien_ships)

        
# Start the game
game_on()