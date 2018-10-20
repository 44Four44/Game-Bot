from settings import *

class Border(pygame.sprite.Sprite):
    """
    Borders

    Attributes
    ----------
    game : Game
        The game that this border is in
    groups : sprite group
        All sprite groups this sprite belongs in
    x : float
        The x coordinate of the border
    y : float
        The y coordinate of the border
    length : int
        The length of the border
    color : int list
        The color of the wall in RGB
    align : int
        The alignment of the border, 0 = horizontal, 1 = vertical



    Methods
    -------
    None

    """
    def __init__(self, game, x, y, length, width, color, align):
        self.groups = game.all_sprites, game.borders
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((length, length))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.length = length
        self.width = width
        self.color = color
        self.align = align
        self.rect.x = x * tile_size - tile_size/2
        self.rect.y = y * tile_size - tile_size/2

    def draw(self):
        """
        Draws the borders (separate from sprites)

        Parameters
        ----------
        None

        Returns
        -------
        None

        """

        # If the border is horizontal
        if self.align == 0:
            pygame.draw.line(self.game.screen, self.color,
                             [self.x - tile_size/2, self.y],
                             [self.x + tile_size/2, self.y], self.width)
        else:
        # If the border is vertical
            pygame.draw.line(self.game.screen, self.color,
                             [self.x, self.y - tile_size/2],
                             [self.x, self.y + tile_size/2], self.width)

