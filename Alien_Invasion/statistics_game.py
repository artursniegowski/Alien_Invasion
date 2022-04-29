class Statistics():
    """Tracking statistics of the game"""

    def __init__(self, my_settings) -> None:
        self.my_settings = my_settings
        self.init_statistics()
        # Main loop
        self.game_on = False

    def init_statistics(self):
        """Setting the initial values"""
        self.ships_lifes = self.my_settings.ship_lifes
        self.total_score = 0 