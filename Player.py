from Enemy import *


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
        pygame.draw.rect(self.image, fill, [4, 4, 20, 20])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = 0
        self.vy = 0
        self.speed = speed
        self.size = size
        self.fill = fill
        self.border = border

    def key_pressed(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.vy = self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.vx = -self.speed
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.vy = -self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.vx = self.speed

    def update(self):
        self.key_pressed()
        self.x += self.vx
        self.y += self.vy
        self.wall_collision('y')
        self.wall_collision('y')

    def wall_collision(self, direction):
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
        if direction == 'x':
            wall_hit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if wall_hit:
                if self.vx > 0:
                    self.rect.x = wall_hit[0].rect.left - self.rect.width
                if self.vx < 0:
                    self.rect.x = wall_hit[0].rect.right
                self.vx = 0
        if direction == 'y':
            wall_hit = pygame.sprite.spritecollide(self, self.game.walls, False)
            if wall_hit:
                if self.vy > 0:
                    self.rect.y = wall_hit[0].rect.top - self.rect.height
                if self.vy < 0:
                    self.rect.y = wall_hit[0].rect.bottom
                self.vy = 0

    def respawn(self):
        self.x = 126
        self.y = 286
        self.rect.x = self.game.startx * tile_size + 6
        self.rect.y = self.game.starty * tile_size + 6
