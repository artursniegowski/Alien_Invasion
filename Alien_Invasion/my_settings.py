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
        self.rocket_speed = 0.1
        self.rocket_width = 2
        self.rocket_height = 12
        self.rocket_color_RGB = (255,10,10)