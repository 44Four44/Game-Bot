from enemies import *


class Player(pygame.sprite.Sprite):
    """
    The player that moves to complete levels

    Attributes
    ----------
    game : Game
        The game that this player is in
    x : float
        The x coordinate of the player
    y : float
        The y coordinate of the player
    speed : float
        The speed of the player
    size : int
        The side length of the square player
    fill : int list
        The color of the player in RGB
    border : int list
        The border color of the player in RGB


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
        fill : int list
            The color of the player in RGB
        border : int list
            The color of the player border in RGB

	    Returns
        -------
        None

        """

        self.groups = game.all_sprites, game.players
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((size, size))
        self.image.fill(border)
        pygame.draw.rect(self.image, fill, [4, 4, 22, 22])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.fill = fill
        self.border = border

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
        if not self.wall_collision(dx, dy):
            self.x += dx
            self.y += dy
            self.rect.x = self.x
            self.rect.y = self.y

    def wall_collision(self, dx=0, dy=0):
        """
        Checks for player collision with walls

        Parameters
        ----------
        dx : int
            Change in x position
        dy : int
            Change in y position

        Return
        ------
        True : bool
            True if the player will collide with a wall on its next move
        False : bool
            False if the player will not collide with a wall on its next move

        """
        for wall in self.game.walls:
            if wall.rect.x - self.size < self.x + dx and self.x + dx < wall.rect.x + wall.size \
                    and wall.rect.y - self.size < self.y + dy and self.y + dy < wall.rect.y + wall.size:
                return True
        return False
