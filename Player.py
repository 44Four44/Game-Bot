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
    image : surface
        The pygame surface that the player will be drawn on
    rect : rect
        Pygame rectangle
    rect.x : float
        The x coordinate of the player
    rect.y : float
        The y coordinate of the player
    vx : float
        The velocity in the x direction
    vy : float
        The velocity in the y direction
    direction : int
        Direction of player's total velocity
    speed : float
        The speed of the player
    size : int
        The side length of the square player
    fill : int list
        The color of the player in RGB
    border : int list
        The border color of the player in RGB
    moves : str
        String of move history
    changes : int
        Number of directional changes in velocity
    change_limit : int
        The limit of directional changes before the player is killed off
    checkpoint : int
        The currently targetted checkpoint
    hit : bool
        True if the player collided with an enemy

    Methods
    -------
    move(control : str) -> None
        Moves the player based on its control
    read_move(direction : int -> None
        Manually moves player in the inputted direction
    update(None) -> None
        Updates player position
    wall_collision(None) -> None
        Checks for player collision with walls
    enemy_collision(direction : char) -> None
        Checks for player collision with enemies
    respawn(None) -> None
        Moves the player back to its original starting position
    die(None) -> None
        Removes the player from all sprite groups and lists
    end_moves(None) -> None
        Kills the player and writes its moves to the moves file along with it score

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
        speed : float
            The speed of the player
        size : int
            The side length of the square player
        fill : int list
            The color of the player in RGB
        border : int list
            The color of the player border in RGB
        moves : str
            String of move history
        changes : int
            Number of directional changes in velocity
        change_limit : int
            The limit of directional changes before the player is killed off
        checkpoint : int
            The currently targetted checkpoint
        hit : bool
            True if the player collided with an enemy

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
        self.direction = 0

        self.control = control
        self.speed = speed
        self.size = size
        self.fill = fill
        self.border = border

        # AI
        self.moves = ''
        self.changes = 0
        self.change_limit = 20
        # The nth targeted checkpoint
        self.checkpoint = self.game.checkpoint
        self.hit = False

    def move(self, control):
        """
        Moves the player in a direction based on ts control type

        Parameters
        ----------
        control : str


        Returns
        -------
        None

        """

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
                # Adjust direction
                if direction == 5:
                    direction = 6
                elif direction == 1:
                    direction = 8
                else:
                    direction = 7
            if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.vx = self.speed
                #Adjust direction
                if direction == 5:
                    direction = 4
                elif direction == 1:
                    direction = 2
                else:
                    direction = 3
            # Update direction and add to moves list
            self.direction = direction
            self.moves += str(self.direction)

        elif control == 'random':
            # 0 - rest, 1 - up, 2 - up right ... 8 - up left
            direction = random.randint(0, 8)
            # Probability of changing directions
            change = random.randint(0, 10)

            if change == 0:
                # Another directional change
                self.changes += 1
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
                self.direction = direction

            # Update moves list
            self.moves += str(self.direction)

    def read_move(self, direction):
        """
        Manually moves player in the inputted direction

        Parameters
        ----------
        direction : int
            Direction of move


        Returns
        -------
        None

        """

        # Move in inputted direction
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
        """
        Updates player position

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # Check if direction change limit is reached
        if self.changes > self.change_limit:
            self.end_moves()

        # Rewind moves
        if self.game.rewind:
            if self.game.tick < self.game.best_moves_num:
                self.read_move(int(self.game.best_moves[self.game.tick]))
                self.game.tick += 1
            else:
                self.game.rewind = False
                self.game.tick = 0

                # New starting position for next generation
                self.game.checkx = self.rect.x
                self.game.checky = self.rect.y
                self.game.new_player('random', self.game.player_count)


                self.die()
        else:
            # Move normally
            self.move(self.control)

        self.rect.x += self.vx
        self.wall_collision('x')
        self.rect.y += self.vy
        self.wall_collision('y')
        self.enemy_collision()

        # Check for if a checkpoint has been reached
        if not self.game.rewind:
            coordinates = self.game.checkpoints_list[self.checkpoint]

            if math.hypot(float(coordinates[0] + tile_size / 2) - float(self.rect.x + self.size / 2),
                          float(coordinates[1] + tile_size / 2) - float(self.rect.y + self.size / 2)) <= 1.5*tile_size:
                if len(self.game.checkpoints_list[self.checkpoint + 1]) == 0:
                    # Remove from sprite lists
                    self.game.all_sprites.remove(self)
                    self.game.players.remove(self)
                    # Remove from player list and clears index
                else:
                    self.checkpoint += 1
                    if self.checkpoint > self.game.checkpoint:
                        self.game.checkpoint = self.checkpoint

            # print(checkpoint_score(self.game, self))

    def wall_collision(self, direction):
        """
        Checks for player collision with walls

        Parameters
        ----------
        direction : char
            The direction the player is hitting the wall in, x or y

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
        """
        Checks for player collision with enemies

        Parameters
        ----------
        None

        Return
        ------
        None

        """

        enemy_hit = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if enemy_hit:
            self.hit = True
            self.end_moves()


    def respawn(self):
        """
        Moves the player back to its original starting position

        Parameters
        ----------
        None

        Return
        ------
        None

        """

        self.x = self.game.startx * tile_size + 6
        self.y = self.game.starty * tile_size + 6
        self.rect.x = self.game.startx * tile_size + 6
        self.rect.y = self.game.starty * tile_size + 6

    def die(self):
        """
        Removes the player from all sprite groups and lists

        Parameters
        ----------
        None

        Return
        ------
        None

        """

        # Remove from sprite lists
        self.game.all_sprites.remove(self)
        self.game.players.remove(self)
        # Remove from player list and clears index
        # TODO: fix
        if self in self.game.player_list:
            self.game.player_list.pop(self.game.player_list.index(self))

    def end_moves(self):
        """
        Kills the player and writes its moves to the moves file along with it score

        Parameters
        ----------
        None

        Return
        ------
        None

        """

        self.die()
        # Writes moves pre death into moves file to be scored and sorted
        with open(moves_path, 'a') as file:
            file.write("Score: " + str(checkpoint_score(self.game, self)) + " Moves: " + self.moves + "\n")
