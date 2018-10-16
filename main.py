import pygame
from functions import *

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
        pygame.display.set_caption("mmmmmmmmmmmmmmmmmmmmmm")

    def new(self):
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.player = Player(self, 10, 10)


mario = Player(100, 100, 5, 30, red)

while run:
    pygame.time.delay(5)

    # Exits the window if the user presses the exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Keys that the user is pressing
    keys = pygame.key.get_pressed()


    screen.fill(0)

    # Player
    mario.move(keys)
    mario.display()

    # Screen
    pygame.display.update()

pygame.quit()