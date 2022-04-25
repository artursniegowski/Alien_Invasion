import os
import pygame
from pygame.sprite import Sprite
from my_settings import MySettings

class Alien_Ship(Sprite):
    """Class for the alien spaceship"""

    def __init__(self,  my_settings: MySettings , screen: pygame.Surface ) \
        -> None:
        super().__init__()

        self.screen = screen
        self.my_settings = my_settings

        # Load the alien ship
        self.alien_ship = pygame.image.load(os.path.join("Alien_Invasion",\
            "images","alien_ship_2.png"))
        self.alien_ship.convert()
        self.alien_ship = pygame.transform.rotozoom(self.alien_ship, 0, 0.1)

        self.alien_ship_rect = self.alien_ship.get_rect()

    def draw_alien_ship(self):
        """Draw the alien ship at its current location"""
        self.screen.blit(self.alien_ship, self.alien_ship_rect)