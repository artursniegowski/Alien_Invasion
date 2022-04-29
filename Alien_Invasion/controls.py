import pygame, sys
from my_settings import MySettings

class Control():
    """class to manage buttons"""

    def __init__(self, my_settings : MySettings, screen: pygame.Surface ,\
        info : str) -> None:

        self.screen = screen 
        self.screen_rect = screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (0,255,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)

        # Build the buttons react object and center it
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center

        # The buttom message needs to be prepped only once
        self.prep_info(info)

    def prep_info(self, info : str) -> None :
        """Turn info into a render image and center text on the button"""
        self.info_image = self.font.render(info,True,self.text_color,self.button_color)
        self.info_image_rect = self.info_image.get_rect()
        self.info_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and ten draw message
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.info_image,self.info_image_rect)