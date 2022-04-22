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