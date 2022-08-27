from pygame.math import Vector2


class Settings:
    """
    A class to store all settings for Alien Invasion.
    """

    def __init__(self) -> None:
        """
        Initialize the game's static settings.
        """
        # Screen settings
        self.screen_width = 480
        self.screen_height = 234
        self.bg_color = 'black'
        self.window_name = 'Pong'
        self.score_offset = Vector2(100, 25)

        # Font settings
        self.score_font_size = 60
        self.msg_font_size = 30
        self.font_path = None
        self.msg_offset = Vector2(0, 100)

        # Player settings
        self.player_speed = 4
        self.player_width = 8
        self.player_height = 50
        self.player_offset = 20

        # Ball settings
        self.ball_speed = 2
        self.ball_size = 6

        # Clock settings
        self.fps = 60

        # Other settings
        self.debug_mode = False
