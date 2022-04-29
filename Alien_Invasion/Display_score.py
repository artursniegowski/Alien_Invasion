import pygame
from my_settings import MySettings
from statistics_game import Statistics

class Scores():
    """A class to show all the scores"""

    def __init__(self, my_settings : MySettings, screen : pygame.Surface, \
        game_stats : Statistics) -> None:
        """initialize all the scoring atributes"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.my_settings = my_settings
        self.game_stats = game_stats
        self.tex_color_RGB = my_settings.score_text_color_RGB
        self.font = pygame.font.SysFont(None,self.my_settings.score_text_size)

        # changing the score to a imgage
        self.score_text_image = self.font.render(str(self.game_stats.total_score),\
            True,self.tex_color_RGB)

        #  position of the score
        self.score_rect = self.score_text_image.get_rect()
        self.score_rect.topright = self.screen_rect.topright
        self.score_rect.x -= 20
        self.score_rect.y += 20

    def draw_score(self) -> None:
        """drawing the score"""
        self.screen.blit(self.score_text_image,self.score_rect)