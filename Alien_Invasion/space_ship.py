import os
import pygame
from my_settings import MySettings


class SpaceShip():

    def __init__(self, my_settings: MySettings , screen: pygame.Surface ) \
        -> None:
        """Initialize the ship and set its starting position"""
        self.screen = screen
        self.my_settings = my_settings
        # Load the ship
        self.ship = pygame.image.load(os.path.join("Alien_Invasion","images",\
            "space_ship_2.png"))
        self.ship.convert()
        self.ship = pygame.transform.rotozoom(self.ship, 0, 0.2)

        self.ship_rect = self.ship.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # Initial position
        self.center = (self.ship_rect.centerx)

        # Directions to move
        self.moving_right = False
        self.moving_left = False

    def update_pos(self):
        """Update the spaceship's position based on the flag"""
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.center += (self.my_settings.ship_speed)
        if self.moving_left and self.ship_rect.left > 0:
            self.center -= (self.my_settings.ship_speed)
        
        # Updating the position
        self.ship_rect.centerx = self.center 

    def draw_ship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.ship, self.ship_rect)