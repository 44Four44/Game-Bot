from EnemyCircular import *

class EnemyLinear(pygame.sprite.Sprite):
    """
    Enemies

    Attributes
    ----------
    game : Game
        The game this enemy is in
    groups : sprite group
        All sprite groups this sprite belongs in
    size : int
        The diameter of the circular enemy
    speed : float
        The speed of the enemy
    x : float
        x coordinate of the centre of the circle
    y : float
        y coordinate of the centre of the circle
    xint : float
        The starting x coordinate
    yint : float
        The starting y coordinate
    rect.x : float
        The left bound coordinate of the circle
    rect.y : float
        The upper bound coordinate of the circle
    criticals : float list list
        A list of coordinates that the enemy will loop around
    prevx : float
        The x coordinate of the previous path point
    prevy : float
        The y coordinate of the previous path point
    nextx : float
        The x coordinate of the next path point
    nexty : float
        The y coordinate of the previous path point
    step : int
        The stage in the loop between critical points that the enemy is on
    fill : int list
        The color of the enemy
    border : int list
            The color of the enemy's border

    Methods
    -------
    die(None) -> None
        Deletes the player
    reset(None) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

    """

    def __init__(self, game, size, speed, x, y, criticals, fill, border):
        """
        Constructor to build a player

        Parameters
        ----------
        game : Game
            The game this enemy is in
        size : int
            The diameter of the circular enemy
        speed : float
            The speed of the enemy
        x : float
            Starting x coordinate
        y : float
            Starting y coordinate
        criticals : float list list
            A list of coordinates that the enemy will loop around
        fill : int list
            The color of the enemy
        border : int list
            The color of the enemy's border

	    Returns
        -------
        None

        """

        self.groups = game.all_sprites, game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((size, size), pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, border, [int(size/2), int(size/2)], int(size/2))
        pygame.draw.circle(self.image, fill, [int(size/2), int(size/2)], int(size/2) - 4)
        self.rect = self.image.get_rect()
        self.rect.x = x - size/2
        self.rect.y = y - size/2
        self.size = size
        self.speed = speed
        self.x = x
        self.y = y
        self.prevx = x
        self.prevy = y
        self.nextx = criticals[0][0]
        self.nexty = criticals[0][1]
        self.criticals = criticals
        self.step = 0
        self.fill = fill
        self.border = border

    def move(self):
        if math.hypot(self.nextx - self.x, self.nexty - self.y) <= self.speed:
            self.x = self.nextx
            self.y = self.nexty
            self.prevx = self.nextx
            self.prevy = self.nexty
            if self.step + 1 == len(self.criticals):
                # Loop back to the beginning
                self.step = 0
            else:
                self.step += 1
            self.nextx = self.criticals[self.step][0]
            self.nexty = self.criticals[self.step][1]
        else:
            hyp = math.hypot(self.nextx - self.prevx, self.nexty - self.prevy)
            self.x += (self.nextx - self.prevx) * (self.speed / hyp)
            self.y += (self.nexty - self.prevy) * (self.speed / hyp)

    def update(self):
        self.move()
        self.rect.x = self.x - self.size/2
        self.rect.y = self.y - self.size/2
