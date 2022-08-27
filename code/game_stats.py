class GameStats:
    """
    A class to manage the statistics of the game.
    """
    def __init__(self) -> None:
        """
        Constructor for the GameStats class.
        """
        # Initialize scores for both players
        self.scores = [0, 0]

        # Initialize the game in an inactive state
        self.game_active = False
