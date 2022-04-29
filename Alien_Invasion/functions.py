import sys
import pygame
from pygame.sprite import Group
from my_settings import MySettings
from space_ship import SpaceShip
from rocket import Rocket
from alien_ship import Alien_Ship
from statistics_game import Statistics
from controls import Control
from Display_score import Scores

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
        add_rocket(space_ship,rockets,screen,my_settings)
        #if len(rockets) < my_settings.rocket_capacity:
        #    rocket = Rocket(my_settings,screen,space_ship)
        #    rockets.add(rocket)

def add_rocket(space_ship : SpaceShip , rockets : Group , \
    screen : pygame.Surface, my_settings : MySettings) -> None :
    """Creating rockets"""
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

def check_events(display_scores : Scores ,my_settings : MySettings, screen : pygame.Surface, \
    game_stats : Statistics, start_button : Control, space_ship : SpaceShip, \
    rockets : Group, alien_ships : Group) -> None:
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
        
        # Start button
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            check_in_range_start_button(display_scores,game_stats,my_settings,\
                screen, start_button,space_ship,alien_ships,rockets,mouse_x,mouse_y)

        elif event.type == pygame.MOUSEMOTION:
            (mouse_x, mouse_y) = pygame.mouse.get_pos()
            check_if_mouse_above_button(start_button,mouse_x,mouse_y)

        elif event.type == pygame.KEYUP:
            check_events_keyup(event, space_ship)

def check_in_range_start_button(display_scores: Scores, game_stats : Statistics,\
    my_settings : MySettings, screen : pygame.Surface, start_button : Control,\
    space_ship : SpaceShip ,alien_ships : Group ,rockets : Group, \
        mouse_x : int, mouse_y : int) -> None :
    """checking if the usser pressed the button start"""
    if start_button.rect.collidepoint(mouse_x,mouse_y) and not game_stats.game_on:
        # reseting at the start of the game
        game_stats.init_statistics()
        # Reset the game settings
        my_settings.init_settings_start_game()
        game_stats.game_on = True

        # Empty everything
        alien_ships.empty()
        rockets.empty()
        
        # Display staring values scores
        display_scores.update_score()
        # update level
        display_scores.update_level()
        # update lives
        display_scores.update_lives()

        # Create the game 
        position_alien_ships(my_settings,screen,alien_ships)
        space_ship.starting_pos()


def check_if_mouse_above_button(start_button : Control, mouse_x : int,\
     mouse_y : int) -> None:
    """Managing the start button if the mouse hover above it"""
    if start_button.rect.collidepoint(mouse_x,mouse_y):
        start_button.hover = True
    else:
        start_button.hover = False

def update_rockets(my_settings : MySettings, screen :pygame.Surface, \
    alien_ships : Group ,rockets : Group, game_stats : Statistics, \
        display_score : Scores) -> None:
    """Encapsulating the functions managing rockets"""
    
    # Updating rockets position
    rockets.update()
    # checking for contact betwen rockets and alien_ships
    contact_alien_ship_rocket = pygame.sprite.groupcollide(rockets,alien_ships,\
        True,True)

    if contact_alien_ship_rocket:
        for alien_ships in contact_alien_ship_rocket.values():
            for alien in alien_ships:
                # addin points for destroying an alien ship
                game_stats.total_score += my_settings.alien_ship_points
                # updating main score
                display_score.update_score()
                # updating high score
                update_high_score(game_stats,display_score)

    # Erasing rockets that are out of reach
    #print(len(rockets))
    #print(len(alien_ships))
    # remove rockets that went pass the screen
    remove_all_rockets(rockets)
    
    # When all alien ships were shoot down we start over -nxt level
    if(len(alien_ships)==0):
        #remove_all_rockets(rockets,removing_all=True)
        rockets.empty()
        
        # addin points for finihsing the level
        game_stats.total_score += my_settings.nex_level_points
        display_score.update_score()
        
        # increasing the difficulty
        my_settings.next_level()

        position_alien_ships(my_settings,screen,alien_ships)

        # updating level
        game_stats.level += 1
        display_score.update_level()
    
def remove_all_rockets(rockets : Group , removing_all : bool = False) -> None:
    """Removing all existing rockets"""
    for rocket in rockets:
        if rocket.rocket_image_rect.bottom <= 0 or removing_all:
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
    filling_density = 0.4
    Max_aliens_ships_y = int((my_settings.screen_height / \
        alien_ship.alien_ship_rect.height) /my_settings.space_factor_y * \
            filling_density)

    return Max_aliens_ships_y

def if_allien_ship_reached_bottom(my_settings : MySettings, game_stats : Statistics, \
    display_score : Scores, screen : pygame.Surface, space_ship : SpaceShip, \
    alien_ships : Group, rockets : Group) -> None :
        """Checking if any alien ships reached the bottom of the screen"""
        screen_rect = screen.get_rect()
        for alien in alien_ships:
            if alien.rect.bottom >= screen_rect.bottom:
                # same as palyer loosing
                ending_life_ship(my_settings,game_stats,display_score,screen,\
                    space_ship,alien_ships,rockets)
                #ending the game
                break

def update_alien_ships(my_settings : MySettings, game_stats : Statistics, \
    display_score : Scores, screen : pygame.Surface, space_ship : SpaceShip,\
    alien_ships : Group, rockets : Group) -> None :
    """Move all the allien ships"""
    alien_ships.update()

    # Chcking if the alien ships reached the our ship
    if pygame.sprite.spritecollideany(space_ship,alien_ships):
        ending_life_ship(my_settings,game_stats,display_score,screen,space_ship,\
            alien_ships,rockets)

    if_allien_ship_reached_bottom(my_settings,game_stats,display_score,screen,\
        space_ship,alien_ships,rockets)

def ending_life_ship(my_settings : MySettings, game_stats : Statistics, \
    display_score : Scores, screen : pygame.Surface, space_ship : SpaceShip, \
    alien_ships : Group, rockets : Group) -> None :
    """Logic when collison wiht an alien ship occurs"""
    # Decreassing lifes of eh player
    game_stats.ships_lives -= 1

    # updating lives on the screen
    display_score.update_lives()

    if game_stats.ships_lives > 0:
        # restart the game 
        alien_ships.empty()
        rockets.empty()

        # create alien ships from starting possiton
        position_alien_ships(my_settings,screen,alien_ships)
        # initila position for the space ship
        space_ship.starting_pos()
    else:
        # updating high score if the current score is higher that the actual 
        # high score
        update_high_score(game_stats,display_score)
        game_stats.game_on = False

def update_high_score(game_stats : Statistics, display_score : Scores) -> None:
    """Methode used for updating the high score"""

    if game_stats.total_score > game_stats.high_score:
        game_stats.high_score = game_stats.total_score
        # updateing the score on the main view
        display_score.update_high_score()

def check_alien_ship_on_the_edege(my_settings : MySettings, \
    alien_ships : Group) -> None:
    """Checking if a alien ship is on the edge and changing the \
        direction they move"""
    for alien_ship in alien_ships:
        if alien_ship.check_vertical_right_border():
            my_settings.direction_alien_RIGHT = False
            drop_alien_ships(my_settings,alien_ships)
            break
        if alien_ship.check_vertical_left_border():
            my_settings.direction_alien_RIGHT = True
            drop_alien_ships(my_settings,alien_ships)
            break

def drop_alien_ships(my_settings : MySettings, \
    alien_ships : Group) -> None:
    """Droping the alien ships"""
    for alien_ship in alien_ships:
        alien_ship.alien_ship_rect.y += my_settings.alien_ships_speed_droping

def update_view(my_settings : MySettings, game_stats : Statistics, screen : pygame.Surface, \
    display_score : Scores, space_ship : SpaceShip, rockets : Group, alien_ships : Group, \
        button : Control) -> None:
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
        # changing the sites the alien ships are moving
        check_alien_ship_on_the_edege(my_settings,alien_ships)
        # drawing the score on the mian view
        display_score.draw_score()
        # Draw the start button if the game is not active
        if not game_stats.game_on:
            button.draw_button()
        # Update the screen
        pygame.display.update()
        #pygame.display.flip()