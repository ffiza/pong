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
        self.screen_width = 640
        self.screen_height = 350
        self.bg_color = 'black'
        self.window_name = 'Pong'
        self.score_offset = Vector2(100, 25)

        # Font settings
        self.score_font_size = 40
        self.msg_font_size = 50
        self.title_font_size = 80
        self.title_font_path = '../fonts/Round9x13.ttf'
        self.msg_font_path = '../fonts/Volt5x5.ttf'
        self.score_font_path = '../fonts/Scoreboard9x13.ttf'
        self.msg_offset = Vector2(self.screen_width/2,
                                  self.screen_height*3/4)
        self.title_offset = Vector2(self.screen_width/2,
                                    self.screen_height/6)

        # Player settings
        self.player_speed = 4
        self.player_width = 8
        self.player_height = 50
        self.player_offset = 20

        # Ball settings
        self.ball_speed = 2
        # self.ball_size = 6
        self.ball_speed_increase_fact = 1.1

        # Collision settings
        self.col_tolerance = self.ball_speed + self.player_speed

        # Clock settings
        self.fps = 60

        # Other settings
        self.debug_mode = False
