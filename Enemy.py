from Wall import *

class Enemy(pygame.sprite.Sprite):
    """
    Enemies

    Attributes
    ----------
    criticals : float list

    size : int
        The diameter of the circular enemy
    color : int list
        The color of the wall in RGB



    Methods
    -------
    die(None) -> None
        Deletes the player
    reset(None) -> None
        Increases the number of attempted problems for a specific problem type by one
    reset(None) -> None
        Resets the users stats

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
