from Border import *
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
        self.groups = game.all_sprites, game.zones
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