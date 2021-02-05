import sys, pygame
from random import seed
from random import randint
class Ghost():
    def __init__(self, map, dimension, startingWidth, startingHeight):
        super(Ghost, self).__init__()
        self.rotation = 0
        self.dimension = dimension
        pos = (startingWidth, startingHeight)
        self.speed = [0,0]
        self.speedNew = [0,0]
        self.board = map
        self.flagW = self.flagS = self.flagA = self.flagD = 0
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


    def up(self):
        if self.flagW == 1:
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speedNew[0] = 0
            self.speedNew[1] = -1

    def down(self):
        if self.flagS == 1:
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speedNew[0] = 0
            self.speedNew[1] = 1

    def left(self):
        if self.flagA == 1:
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.rotation = 1
            self.speedNew[0] = -1
            self.speedNew[1] = 0

    def right(self):
        if self.flagD == 1:
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.rotation = 0
            self.speedNew[0] = 1
            self.speedNew[1] = 0

    def check(self):
        if self.board.getElement(int(self.boardX-1), int(self.boardY)) == 2 and self.flagA == 1:
            self.speedNew[0] = 0
            self.flagA = 0
        elif self.board.getElement(int(self.boardX-1), int(self.boardY)) != 2:
            self.flagA = 1
        if self.board.getElement(int(self.boardX+1), int(self.boardY)) == 2 and self.flagD == 1:
            self.speedNew[0] = 0
            self.flagD = 0
        elif self.board.getElement(int(self.boardX+1), int(self.boardY)) != 2:
            self.flagD = 1
        if self.board.getElement(int(self.boardX), int(self.boardY-1)) == 2 and self.flagW == 1:
            self.speedNew[1] = 0
            self.flagW = 0
        elif self.board.getElement(int(self.boardX), int(self.boardY-1)) != 2:
            self.flagW = 1
        if self.board.getElement(int(self.boardX), int(self.boardY+1)) == 2 and self.flagS == 1:
            self.speedNew[1] = 0
            self.flagS = 0
        elif self.board.getElement(int(self.boardX), int(self.boardY+1)) != 2:
            self.flagS = 1

    def playerMove(self):
        x, y = self.rect.center
        if x % self.dimension == self.dimension/2 and y % self.dimension == self.dimension/2:
            #seed(2)
            value = randint(0, 4)
            #print("wartość: ")
            #print(value)
            if value == 1:
                self.up()
            elif value == 2:
                self.down()
            elif value == 3:
                self.left()
            elif value == 4:
                self.right()
            temp1, temp2 = self.speedNew
            self.speed[0] = temp1
            self.speed[1] = temp2
            #self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.boardX = x // self.dimension
        self.boardY = y // self.dimension
        self.rect = self.rect.move(self.speed)
        #self.board.changePosition(int(self.boardX), int(self.boardY))