from Wall import *


class Player(pygame.sprite.Sprite):
    """
    The player that moves to complete levels

    Attributes
    ----------
    x : float
        The x coordinate of the player
    y : float
        The y coordinate of the player
    speed : float
        The speed of the player
    size : int
        The side length of the square player
    color : int list
        The color of the player in RGB


    Methods
    -------
    die(None) -> None
        Deletes the player
    reset(None) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

    """

    def __init__(self, game, x, y, speed, size, fill, border):
        """
        Constructor to build a player

        Parameters
        ----------
        x : float
            The x coordinate of the player
        y : float
            The y coordinate of the player
        speed : flot
            The speed of the player
        size : int
            The side length of the square player
        color : int list
            The color of the player in RGB

	    Returns
        -------
        None

        """

        self.groups = game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((size, size))
        self.image.fill(border)
        pygame.draw.rect(self.image, fill, [4, 4, 22, 22])
        self.rect = self.image.get_rect()

        self.x = x
        self.y = y
        self.speed = speed

    def move(self, dx=0, dy=0):
        """
        Checks for player movement, then updates position

        Parameters
        ----------
        dx : int
            Change in x position
        dy : int
            Change in y position

        Return
        ------
        None

        """

        # checks for which keys are pressed and moves the player
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y
