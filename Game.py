from Player import *

class Game:
    """
    The game and functions for setting up

    Attributes
    ----------
    screen : surface
        The Pygame window that displays this game
    clock : Clock
        Pygame clock
    all_sprites : sprite group
        A group for all sprites in this game
    players : sprite group
        All players in this game
    player_list : Player list
        List of all players
    player_count : int
        Fixed number of players spawned each generation
    walls : sprite group
        All walls in this game
    zones : sprite group
        All green spaces such as starting/ending and checkpoints in this game
    borders : sprite group
        All bordered lines in this game
    enemies : sprite group
        All enemies in this game
    startx : float
        The x coordinate of the starting tile for this game
    starty : float
        The y coordinate of the starting tile for this game
    checkx : float
        The x coordinate of the ending position of the most recent generation
    checky : float
        The y coordinate of the ending position of the most recent generation
    level : int
        The level of the game, used to find level data in map file
    checkpoints_list : float list list
        Stores the checkpoints' x and y coordinates
    checkpoint : int
        Index of currently targetted checkpoint in 'checkpoints_list'
    generation : int
        Current generation starting from 0
    best_moves : str
        A string of all the highest scored moves from each generation combined
    best_moves_num : int
        Length of 'best_moves'
    rewind : bool
        True if the game is rewinding its best moves from each generation. Occurs at the end of each generation

    Methods
    -------
    new(level : int) -> None
        Reads from the map file and creates all objects relating to the map
    new_player(control : str, number : int) -> None
        Creates multiple new players at a time
    end_gen(None) -> None
        Sorts the ended generation's moves, begins rewind phase and then makes the next generation
    run(None) -> None
        Primary loop to update and draw game contents
    update(None) -> None
        Updates all game sprites
    draw_map(None) -> None
        Draws map grid and squares
    draw(None) -> None
        Draws all game sprites
    events(None) -> None
        Listens for any events such as keypresses
    quit(None) ->
        Closes the Pygame window and quits the program

    """

    def __init__(self):
        """
        Constructor to build a new Game

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(Title)

        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)

        # Counter for generation rewinding
        self.tick = 0

    def new(self, level):
        """
        Reads from the map file and creates all objects relating to the map

        Parameters
        ----------
        level : int
            The level of this game with its specific map data in the map file

        Returns
        -------
        None

        """

        # Sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.player_list = []
        self.playercount = 0
        self.walls = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()

        self.startx = 166
        self.starty = 326
        self.checkx = self.startx
        self.checky = self.starty

        self.level = level

        # Checkpoints for AI pathing
        self.checkpoints_list = []
        for i in range (0, 10):
            self.checkpoints_list.append([])
        #
        self.checkpoint = 0

        # Generations
        self.generation = 0
        self.best_moves = ''
        self.best_moves_num = 0
        self.rewind = False


        # Map maker
        with open(map_path, 'r') as file:
            data = file.readlines()

        # The line number of the level in the map file
        index = data.index(">>>>>>>>>>>>>>>> Level " + str(self.level) + "\n")

        # Walls ; Green Space ; borders
        for y in range (index + 2, index + 33):
            for x in range (0, 41):
                # Map symbol in the map file
                symbol = data[y][x]

                if (y - 2 - index) % 2 == 0 or x % 2 == 0:
                    # Symbols on the sides of tiles (borders)
                    # Respective coordinates on the actual game window
                    mapx = x * tile_size / 2
                    mapy = (y - 2 - index) * tile_size / 2
                    if symbol == '-' or symbol == '|':
                        Border(self, mapx, mapy, tile_size, 4, black, (y - 2 - index) % 2)
                else:
                    # Symbols on the centres of tiles
                    # Respective coordinates on the actual game window
                    mapx = (x - 1) / 2 * tile_size
                    mapy = (y - 3 - index) / 2 * tile_size
                    if symbol == '1':
                        Wall(self, mapx, mapy, tile_size, lightsteelblue)

                    if symbol == 'g' or symbol == 'h' or symbol == 'j' or symbol == 's':
                        Zone(self, mapx, mapy, tile_size, palegreen, symbol)
                        if symbol == 's':
                            self.startx = (x - 1)/2 * tile_size
                            self.starty = (y - 2 - index)/2 * tile_size
                            self.checkx = self.startx
                            self.checky = self.starty

        # Coins
        for y in range (index + 34, index + 65):
            for x in range(0, 41):
                # Map symbol in the map file
                symbol = data[y][x]

        # Checkpoints
        for y in range(index + 66, index + 81):
            for x in range(0, 20):
                # Map symbol in the map file
                symbol = data[y][x]
                if symbol != '.':
                    self.checkpoints_list[int(symbol)].append(x * tile_size)
                    self.checkpoints_list[int(symbol)].append((y - 66) * tile_size)

        # Create enemies
        EnemyLinear(self, 22, 4.65, 251, 220, [[251, 220], [549, 220]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 549, 260, [[549, 260], [251, 260]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 251, 300, [[251, 300], [549, 300]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 549, 340, [[549, 340], [251, 340]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 251, 380, [[251, 380], [549, 380]], blue, midnightblue)

    def new_player(self, control, number):
        """
        Creates multiple new players at a time

        Parameters
        ----------
        control : str
            The level of this game with its specific map data in the map file
        number : int
            The number of players to create
        Returns
        -------
        None

        """

        for i in range (0, number):
            self.player = Player(self, control, self.checkx, self.checky, 2, 28, red, maroon)
            self.player_list.append(self.player)
        self.player_count = number

    def end_gen(self):
        """
        Sorts the ended generation's moves, begins rewind phase and then makes the next generation

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # End the generation
        with open(moves_path, 'a') as file:
            file.write("END OF GENERATION " + str(self.generation) + "\n")

        # Sort moves based on their scores
        bubble_sort((self.player_count + 1) * self.generation,
                    (self.player_count + 1) * self.generation + self.player_count - 1)

        with open(moves_path, 'r') as file:
            data = file.readlines()

        # Add best moves from this generation to best moves string
        moves = data[(self.generation + 1) * (self.player_count + 1) - 2]
        moves = moves[22 : len(moves)]
        self.best_moves += moves.rstrip()
        self.best_moves_num = len(self.best_moves)

        # Update most recent checkpoint

        self.generation += 1
        self.rewind = True

        # Player to replay best moves up to next generation
        self.rewinder = Player(self, 'random', self.startx, self.starty, 2, 28, lime, black)
        self.player_list.append(self.rewinder)

        # Reset all enemy positions
        for enemy in self.enemies:
            enemy.reset()

    def run(self):
        """
        Primary loop to update and draw game contents

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # game loop - set self.playing = False to end the game
        self.run = True
        while self.run:
            # dt is the time between each frame in seconds
            self.dt = self.clock.tick(FPS) / 1000
            # print(self.dt)

            self.events()

            # New generation
            if len(self.player_list) == 0:
                self.end_gen()

            # Speed up game
            for i in range(zoom):
                self.update()
            self.draw()

    def update(self):
        """
        Updates all game sprites

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # update sprites
        self.all_sprites.update()

    def draw_map(self):
        """
        Draws map grid and squares

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        for y in range(0, 15):
            for x in range(0, 20):
                fill = lavender
                # Checkerboard pattern
                if (x + y) % 2 == 0:
                    fill = ghostwhite
                # Draw grid squares
                pygame.draw.rect(self.screen, fill, [0 + x * tile_size, 0 + y * tile_size, tile_size, tile_size])

    def draw(self):
        """
        Draws all game sprites

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        self.screen.fill(black)
        self.draw_map()
        self.all_sprites.draw(self.screen)

        for border in self.borders:
            border.draw()

        pygame.display.update()

    def events(self):
        """
        Listens for any events such as keypresses

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # All events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()

    def quit(self):
        """
        Closes the Pygame window and quits the program

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        pygame.quit()
        sys.exit()