import pygame
from my_settings import MySettings
from space_ship import SpaceShip
import functions as game_func
from rocket import Rocket
from alien_ship import Alien_Ship
from statistics_game import Statistics
from controls import Control

def game_on():
    # Main thread - init Pygame , screen etc.
    pygame.init()
    my_settings = MySettings()
    screen = pygame.display.set_mode((my_settings.screen_width,\
        my_settings.screen_height))
    pygame.display.set_caption(my_settings.caption)
    
    # Creating the play button
    play_button = Control(my_settings,screen,"START")
    # Instance to store game statistics
    game_stats = Statistics(my_settings)
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
        game_func.check_events(my_settings,screen,game_stats,play_button, \
            space_ship,rockets)
       # new
        # Checking if the players has still lives left
        if game_stats.game_on:
            space_ship.update_pos()
            game_func.update_rockets(my_settings,screen,alien_ships,rockets)
            game_func.update_alien_ships(my_settings,game_stats,screen,space_ship,\
                alien_ships,rockets)

        # updatign screen 
        game_func.update_view(my_settings,game_stats,screen,space_ship,rockets,\
            alien_ships,play_button)

        
# Start the game
game_on()