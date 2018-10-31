from EnemyLinear import *


class Player(pygame.sprite.Sprite):
    """
    The player that moves to complete levels

    Attributes
    ----------
    game : Game
        The game that this player is in
    groups : sprite group
        All sprite groups this sprite belongs in
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

    def __init__(self, game, control, x, y, speed, size, fill, border):
        """
        Constructor to build a player

        Parameters
        ----------
        game : Game
            The game that this player is in
        control : str
            The type of control that this player will move to, 'keys' or 'random'
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
        self.control = control
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

        # AI
        self.moves = []

    def move(self, control):
        if control == 'keys':
            self.vx = 0
            self.vy = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.vy = self.speed
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.vy = -self.speed
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.vx = -self.speed
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.vx = self.speed

        elif control == 'random':
            change = random.randint(0, 10)
            if change == 0:
                self.vx = 0
                self.vy = 0
                xprob = random.randint(0, 2)
                yprob = random.randint(0, 2)
                if yprob == 0:
                    self.vy = self.speed
                if yprob == 1:
                    self.vy = -self.speed
                if xprob == 0:
                    self.vx = -self.speed
                if xprob == 1:
                    self.vx = self.speed

    def update(self):
        self.move(self.control)
        self.rect.x += self.vx
        self.wall_collision('x')
        self.rect.y += self.vy
        self.wall_collision('y')
        self.enemy_collision()

    def wall_collision(self, direction):
        """
        Checks for player collision with walls

        Parameters
        ----------
        direction : char
            The direction te player is hitting the wall in, x or y

        Return
        ------
        None

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

    def enemy_collision(self):
        enemy_hit = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if enemy_hit:
            self.respawn()

    def respawn(self):
        self.x = self.game.startx * tile_size + 6
        self.y = self.game.starty * tile_size + 6
        self.rect.x = self.game.startx * tile_size + 6
        self.rect.y = self.game.starty * tile_size + 6
