import os
import pygame


class SpaceShip():

    def __init__(self, screen) -> None:
        """Initialize the ship and set its starting position"""
        self.screen = screen

        # Load the ship
        self.image = pygame.image.load(os.path.join("Alien_Invasion","images",\
            "space_ship.png"))
        self.image.convert()
        #self.image = pygame.transform.rotozoom(self.image, 0, 0.8)

        self.image_rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.image_rect.centerx = self.screen_rect.centerx
        self.image_rect.bottom = self.screen_rect.bottom

    def draw_ship(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.image_rect)