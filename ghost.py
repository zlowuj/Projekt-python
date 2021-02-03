import sys, pygame
class Ghost():
    def __init__(self, map, dimension, startingWidth, startingHeight, pos=(0, 0)):
        self.board = map
        self.boardX = startingWidth//dimension
        self.boardY = startingHeight//dimension
        self.original_image = pygame.Surface((dimension, dimension))
        self.ghost_image = pygame.image.load("ghost.png")
        ghost = self.ghost_image
        ghost = pygame.transform.scale(ghost, (dimension, dimension))
        self.original_image = ghost
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0