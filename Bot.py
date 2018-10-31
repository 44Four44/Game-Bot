from Player import *
class Bot:
    """
    An AI that learns to play the game

    Attributes
    ----------
    game : Game
        The game that this AI is playing

    Methods
    -------
    die(None) -> None
        Deletes the player
    """

    def __init__(self, game):
        """
        Constructor to build a player

        Parameters
        ----------
        game : Game
            The game that this AI is playing
        -------
        None

        """

        self.game = game


