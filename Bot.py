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

    def bubble_sort(self):
        with open(map_path, 'r') as file:
            data = file.readlines()
        for i in range (0, 100):
            for j in range (0,100):
                if data[j][300] > data[j + 1][300]:
                    x = data[j][300]
                    data[j][300] = data[j + 1][300]
                    data[j + 1][300] = x

    def checkpoint_score(self, Player):
        return 1