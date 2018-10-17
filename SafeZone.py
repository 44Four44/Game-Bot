import pygame
import sys

pygame.init()

# size of the square tiles that make up the map
tile_size = 40
screen_width = tile_size * 20
screen_height = tile_size * 15

# true if the game is running
run = True

# File path for map data
file_path = '/Users/EthanWang/Game_Bot/map.txt'

# Game settings
FPS = 60
Title = "mmmmmmmmmm"

# Colors
red = (255, 0, 0)
black = (0, 0, 0)
lavender = (224, 218, 254)
ghostwhite = (248, 247, 255)
lightsteelblue = (170, 165, 255)
maroon = (127, 0,0)
palegreen = (170, 238, 187)

class SafeZone(pygame.sprite.Sprite):
    """
    Safe / green zones for checkpoints

    Attributes
    ----------
    x : float
        The x coordinate of the zone
    y : float
        The y coordinate of the zone
    size : int
        The side length of the square zone
    color : int list
        The color of the zone in RGB
    type : char
        The type of green space, g - start, h - checkpoint, j - end



    Methods
    -------
    die(None) -> None
        Deletes the player
    reset(None) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

    """
    def __init__(self, game, x, y, size, color, type):
        self.groups = game.players, game.zones
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * tile_size
        self.rect.y = y * tile_size
        self.type = type