class MySettings():
    """This class represents all settings for the game"""

    def __init__(self) -> None:
        """Init"""
        # Size of the Screen 
        self.screen_width = 800
        self.screen_height = 600
        # Background color
        self.background_color = (125,125,125)
        # Name of the window
        self.caption = "ALIEN INVASION V1.0"
        # Ship settings - speed
        self.ship_speed = 0.2
        # Rockets settings
        self.rocket_speed = 0.6
        self.rocket_width = 2
        self.rocket_height = 12
        self.rocket_color_RGB = (255,10,10)
        self.rocket_capacity = 4
        # alien settins
        self.space_factor_x = 2.5
        self.space_factor_y = 1.5
        # Max speed is 1.0 
        self.alien_ships_speed = 0.2
        # in pixels !
        self.alien_ships_speed_droping = 1
        # setting default direction for alien space ships
        self.direction_alien_RIGHT = True
