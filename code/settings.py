class Settings:
    """
    A class to store all settings for Alien Invasion.
    """

    def __init__(self) -> None:
        """
        Initialize the game's static settings.
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = '#122620'
        self.window_name = 'Pong'

        # Clock settings
        self.fps = 60
