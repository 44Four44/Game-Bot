from Player import *

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

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.borders = pygame.sprite.Group()


        # Map maker
        with open(file_path, 'r') as file:
            data = file.readlines()
        for y in range (0, 30):
            for x in range (0, 40):
                # Map symbol in the map file
                symbol = data[y][x]

                if y % 2 == 0 or x % 2 == 0:
                    # Symbols on the sides of tiles (borders, coins)
                    if symbol == '*':
                        Border(self, x / 2 * tile_size, y / 2 * tile_size, tile_size, 4, black, y % 2)
                else:
                    # Symbols on the centres of tiles
                    if symbol == '1':
                        Wall(self, (x - 1)/2, (y - 1)/2, tile_size, lightsteelblue)

                    if symbol == 'g' or symbol == 'h' or symbol == 'j':
                        SafeZone(self, (x - 1)/2, (y - 1)/2, tile_size, palegreen, symbol)

        self.player = Player(self, 125, 245, 2.5, 30, red, maroon)



    def run(self):
        # game loop - set self.playing = False to end the game
        self.run = True
        while self.run:
            self.dt = self.clock.tick(FPS) / 1000
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
                keys = pygame.key.get_pressed()
                print(keys.index(True))
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if  keys[273] or keys[119]:
                    self.player.move(dy=-self.player.speed)
                if keys[276] or keys[97]:
                    self.player.move(dx=-self.player.speed)
                if keys[274] or keys[115]:
                    self.player.move(dy=self.player.speed)
                if keys[275] or keys[100]:
                    self.player.move(dx=self.player.speed)