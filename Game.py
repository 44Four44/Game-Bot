from Bot import *

class Game:
    """
    The game and functions for setting up

    Attributes
    ----------
    None

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

    def new(self, level):
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()
        self.startx = 4
        self.starty = 8


        # Map maker
        with open(file_path, 'r') as file:
            data = file.readlines()

        for y in range (1 + 33 * (level - 1), 32 + 33 * (level - 1)):
            for x in range (0, 41):
                # Map symbol in the map file
                symbol = data[y][x]

                if (y - 1 - 33 * (level - 1)) % 2 == 0 or x % 2 == 0:
                    # Symbols on the sides of tiles (borders, coins)
                    if symbol == '*':
                        Border(self, x / 2 * tile_size, (y - 1 - 33 * (level - 1)) / 2 * tile_size,
                               tile_size, 4, black, (y - 1 - 33 * (level - 1)) % 2)
                else:
                    # Symbols on the centres of tiles
                    if symbol == '1':
                        Wall(self, (x - 1)/2 * tile_size,
                             (y - 2 - 33 * (level - 1))/2 * tile_size, tile_size, lightsteelblue)

                    if symbol == 'g' or symbol == 'h' or symbol == 'j' or symbol == 's':
                        SafeZone(self, (x - 1)/2 * tile_size,
                                 (y - 2 - 33 * (level - 1))/2 * tile_size, tile_size, palegreen, symbol)
                        if symbol == 's':
                            self.startx = (x - 1)/2
                            self.starty = (y - 2 - 33 * (level - 1))/2


    def new_player(self):
        self.player = Player(self, self.startx * tile_size + 6, self.starty * tile_size + 6, 2.25, 28, red, maroon)

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