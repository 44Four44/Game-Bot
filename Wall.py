from SafeZone import *

class Wall(pygame.sprite.Sprite):
    """
    A wall that serves as an obstacle for the player

    Attributes
    ----------
    game : Game
        The game that this wall is in
    groups : sprite group
        All sprite groups this sprite belongs in
    x : float
        The x coordinate of the wall
    y : float
        The y coordinate of the wall
    size : int
        The side length of the square wall
    color : int list
        The color of the wall in RGB

    Methods
    -------
    None

    """
    def __init__(self, game, x, y, size, color):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.size = size
        self.color = color
