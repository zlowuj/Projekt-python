import sys, pygame, map
size = width, height = 1200, 1200
dimension = 40
startingWidth = dimension*1.5
startingHeight = dimension*1.5
black = 0, 0, 0
mode=0
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont = pygame.font.SysFont('Corbel', 35)
text = smallfont.render('play', True, color)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(dimension, dimension)):
        super(Player, self).__init__()
        self.points=0
        self.boardX = startingWidth//dimension
        self.boardY = startingHeight//dimension
        self.speed = [0,0]
        self.speedNew = [0,0]
        self.flagW = self.flagS = self.flagA = self.flagD = 0
        self.board = map.Map(width//dimension)
        #self.board.changePosition(self.boardX, self.boardY)
        #print(self.board.mapPrint())
        self.original_image = pygame.Surface(size)
        pac_man = pygame.image.load("pac_man.png")
        pac_man = pygame.transform.scale(pac_man, (dimension, dimension))
        self.original_image = pac_man
        self.image = self.original_image
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.angle = 0

    def draw(self):
        for x in range(width//dimension):
            for y in range(width//dimension):
                if self.board.getElement(x, y) == 2:
                    pygame.draw.rect(screen, (255, 0, 0), (x*dimension,y*dimension, dimension-1, dimension-1))
                if self.board.getElement(x, y) == 1:
                    pygame.draw.circle(screen, 	(255,255,0), (x*dimension+dimension/2,y*dimension+dimension/2), 5)

    def up(self):
        if self.flagW == 1:
            self.angle = 90
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speedNew[0] = 0
            self.speedNew[1] = -1

    def down(self):
        if self.flagS == 1:
            self.angle = 270
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speedNew[0] = 0
            self.speedNew[1] = 1

    def left(self):
        if self.flagA == 1:
            self.angle = 180
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speedNew[0] = -1
            self.speedNew[1] = 0

    def right(self):
        if self.flagD == 1:
            self.angle = 0
            x, y = self.rect.center
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speedNew[0] = 1
            self.speedNew[1] = 0

    def check(self):
        if self.board.getElement(self.boardX-1, self.boardY) == 2 and self.flagA == 1:
            self.speedNew[0] = 0
            self.flagA = 0
        elif self.board.getElement(self.boardX-1, self.boardY) != 2:
            self.flagA = 1
        if self.board.getElement(self.boardX+1, self.boardY) == 2 and self.flagD == 1:
            self.speedNew[0] = 0
            self.flagD = 0
        elif self.board.getElement(self.boardX+1, self.boardY) != 2:
            self.flagD = 1
        if self.board.getElement(self.boardX, self.boardY-1) == 2 and self.flagW == 1:
            self.speedNew[1] = 0
            self.flagW = 0
        elif self.board.getElement(self.boardX, self.boardY-1) != 2:
            self.flagW = 1
        if self.board.getElement(self.boardX, self.boardY+1) == 2 and self.flagS == 1:
            self.speedNew[1] = 0
            self.flagS = 0
        elif self.board.getElement(self.boardX, self.boardY+1) != 2:
            self.flagS = 1

    def playerMove(self):
        x, y = self.rect.center
        if x % dimension == dimension/2 and y % dimension == dimension/2:
            temp1, temp2 = self.speedNew
            self.speed[0] = temp1
            self.speed[1] = temp2
            self.image = pygame.transform.rotate(self.original_image, self.angle)
        self.boardX = x // dimension
        self.boardY = y // dimension
        if self.board.getElement(self.boardX, self.boardY) == 1:
            self.board.eat(self.boardX, self.boardY)
        self.rect = self.rect.move(self.speed)
        #print(self.board.mapPrint())
        #print(self.speed)

def main():
    player = Player(pos=(startingWidth, startingHeight))
    while 1:
        while 1 and mode==1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        player.up()
                    if event.key == pygame.K_s:
                        player.down()
                    if event.key == pygame.K_a:
                        player.left()
                    if event.key == pygame.K_d:
                        player.right()
                    if event.key == pygame.K_ESCAPE:
                        mode=0
            pygame.display.set_caption("Pac-man")
            player.playerMove()
            player.check()
            screen.fill(black)
            screen.blit(player.image, player.rect)
            player.draw()
            pygame.display.update()
            pygame.display.flip()

        while 1 and mode == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                        mode=1
            mouse = pygame.mouse.get_pos()
            if width / 2 <= mouse[0] <= width / 2 + 140 and height / 2 <= mouse[1] <= height / 2 + 40:
                pygame.draw.rect(screen, color_light, [width / 2, height / 2, 140, 40])

            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height / 2, 140, 40])
            screen.blit(text, (width / 2 + 50, height / 2))
            pygame.display.update()
            pygame.display.flip()


if __name__ == '__main__':

    screen = pygame.display.set_mode(size)
    main()