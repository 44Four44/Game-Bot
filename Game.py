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
        self.players = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.zones = pygame.sprite.Group()
        self.player = Player(self, 100, 100, 5, 30, red, maroon)

        # Map maker
        with open(file_path, 'r') as file:
            data = file.readlines()
        for y in range (0, 15):
            for x in range (0, 20):
                symbol = data[y][x]
                if symbol == '1':
                    Wall(self, x, y, tile_size, lightsteelblue)

                if symbol == 'g' or symbol == 'h' or symbol == 'j':
                    SafeZone(self, x, y, tile_size, palegreen, symbol)

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
        self.players.update()

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
        self.players.draw(self.screen)

        pygame.display.update()

    def events(self):
        # All events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.quit()
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    self.player.move(dy=-self.player.speed)
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.move(dx=-self.player.speed)
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    self.player.move(dy=self.player.speed)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.move(dx=self.player.speed)