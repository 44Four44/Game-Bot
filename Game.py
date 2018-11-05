from Bot import *

class Game:
    """
    The game and functions for setting up

    Attributes
    ----------
    screen : surface
        The pygame window that displays this game
    clock : Clock
        Pygame clock
    all_sprites : sprite group
        A group for all sprites in this game
    players : sprite group
        All players in this game
    walls : sprite group
        All walls in this game
    zones : sprite group
        All green spaces such as starting/ending and checkpoints in this game
    borders : sprite group
        All bordered lines in this game
    enemies : aprite group
        All enemies in this game
    startx : int
        The x coordinate of the starting tile for this game
    starty : int
        The y coordinate of the starting tile for this game

    Methods
    -------
    die(None) -> None
        Deletes the player
    reset(None) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

    """

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()
        pygame.key.set_repeat(1, 1)
        # Frame count
        self.tick = 0

    def new(self, level):
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.player_list = []
        self.walls = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.startx = 4
        self.starty = 8
        self.level = level
        # Checkpoints for AI pathing
        self.checkpoints_list = []
        self.checkpoints = pygame.sprite.Group()
        for i in range (0, 10):
            self.checkpoints_list.append([])


        # Map maker
        with open(map_path, 'r') as file:
            data = file.readlines()

        # The line number of the level in the map file
        index = data.index(">>>>>>>>>>>>>>>> Level " + str(self.level) + "\n")
        print(index)

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
                        SafeZone(self, mapx, mapy, tile_size, palegreen, symbol)
                        if symbol == 's':
                            self.startx = (x - 1)/2
                            self.starty = (y - 2 - index)/2
        # Coins
        for y in range (index + 34, index + 64):
            for x in range(0, 41):
                # Map symbol in the map file
                symbol = data[y][x]

        # Checkpoints
        for y in range(index + 66, index + 80):
            print(y)
            for x in range(0, 41):
                # Map symbol in the map file
                # symbol = data[y][x]
                x = 2
        # Create enemies
        EnemyLinear(self, 22, 4.65, 251, 220, [[251, 220], [549, 220]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 549, 260, [[549, 260], [251, 260]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 251, 300, [[251, 300], [549, 300]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 549, 340, [[549, 340], [251, 340]], blue, midnightblue)
        EnemyLinear(self, 22, 4.65, 251, 380, [[251, 380], [549, 380]], blue, midnightblue)



        """
                # Checkpoints
                if symbol in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        self.checkpoints_list[int(symbol)].append([mapx, mapy])

        # Remove empty checkpoints
        #self.checkpoints_list = filter(None, self.checkpoints_list)
        """


    def new_random(self):
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.startx = 4
        self.starty = 8

        for y in range (0, 30):
            for x in range (0, 40):

                if y % 2 == 0 or x % 2 == 0:
                    # Symbols on the sides of tiles (borders, coins)
                    flip = random.uniform(0, 1)
                    if flip < 0.5:
                        Border(self, x / 2 * tile_size, y * tile_size, tile_size, 4, black, y % 2)
                else:
                    # Symbols on the centres of tiles
                    flip = random.uniform(0, 1)
                    if flip < 1/3:
                        Wall(self, (x - 1)/2 * tile_size, y * tile_size, tile_size, lightsteelblue)

                    if flip >= 1/3 and flip < 2/3:
                        SafeZone(self, (x - 1)/2 * tile_size, y * tile_size, tile_size, palegreen, 'g')

    def new_player(self, control):
        self.player = Player(self, control, self.startx * tile_size + 6, self.starty * tile_size + 6, 2, 28, red, maroon)
        self.player_list.append(self.player)
  
    def run(self):
        # game loop - set self.playing = False to end the game
        self.run = True
        while self.run:
            # dt is the time between each frame in seconds
            self.dt = self.clock.tick(FPS) / 1000
            # print(self.dt)
            self.events()
            self.update()
            self.draw()
            # Update frame
            self.tick += 1

    def quit(self):
        pygame.quit()
        sys.exit()

    def update(self):
        # update sprites
        self.all_sprites.update()

    def draw_map(self):
        for y in range(0, 15):
            for x in range(0, 20):
                fill = lavender
                # Checkerboard pattern
                if (x + y) % 2 == 0:
                    fill = ghostwhite
                # Draw grid squares
                pygame.draw.rect(self.screen, fill, [0 + x * tile_size, 0 + y * tile_size, tile_size, tile_size])

    def draw(self):
        self.screen.fill(black)
        self.draw_map()
        self.all_sprites.draw(self.screen)
        for border in self.borders:
            border.draw()
        pygame.display.update()

    def events(self):
        # All events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
