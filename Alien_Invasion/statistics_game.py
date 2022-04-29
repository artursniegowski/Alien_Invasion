class Statistics():
    """Tracking statistics of the game"""

    def __init__(self, my_settings) -> None:
        self.my_settings = my_settings
        self.init_statistics()
        # Main loop
        self.game_on = False
        # value to store the highest value
        self.high_score = 0

    def init_statistics(self):
        """Setting the initial values"""
        self.ships_lifes = self.my_settings.ship_lifes
        # value to store the total points 
        self.total_score = 0 
        # level
        self.level = 1
