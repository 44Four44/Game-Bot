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
            direction = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.vy = self.speed
                direction = 5
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.vy = -self.speed
                direction = 1
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.vx = -self.speed
                if direction == 5:
                    direction = 6
                elif direction == 1:
                    direction = 8
                else:
                    direction = 7
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.vx = self.speed
                if direction == 5:
                    direction = 4
                elif direction == 1:
                    direction = 2
                else:
                    direction = 3

            with open(moves_path, 'a') as file:
                file.write(str(direction))

        elif control == 'random':
            # 0 - rest, 1 - up, 2 - up right ... 8 - up left
            direction = random.randint(0, 8)
            # Probability of changing directions
            change = random.randint(0, 10)

            if change == 0:
                self.vx = 0
                self.vy = 0
                if direction == 4 or direction == 5 or direction == 6:
                    self.vy = self.speed
                if direction == 8 or direction == 1 or direction == 2:
                    self.vy = -self.speed
                if direction == 6 or direction == 7 or direction == 8:
                    self.vx = -self.speed
                if direction == 2 or direction == 3 or direction == 4:
                    self.vx = self.speed

            if self.game.tick == 0:
                with open(moves_path, 'a') as file:
                    file.write(str(direction) + "\n")
            else:
                with open(moves_path, 'r') as file:
                    data = file.readlines()
                line = data[self.game.player_list.index(self)]
                data[self.game.player_list.index(self)] = line[:len(line)-1] + str(direction) + line[len(line):] + "\n"
                with open(moves_path, 'w') as file:
                    file.writelines(data)

        elif control == 'read':
            direction = 0
            # Read moves from moves file
            with open(moves_path, 'r') as file:
                data = file.readlines()
            if self.game.tick < len(data[0]):
                direction = int(list(data[0])[self.game.tick])

            self.vx = 0
            self.vy = 0
            if direction == 4 or direction == 5 or direction == 6:
                self.vy = self.speed
            if direction == 8 or direction == 1 or direction == 2:
                self.vy = -self.speed
            if direction == 6 or direction == 7 or direction == 8:
                self.vx = -self.speed
            if direction == 2 or direction == 3 or direction == 4:
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
