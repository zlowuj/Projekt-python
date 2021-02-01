import sys, pygame, map
pygame.init()
size = width, height = 1200, 1200
dimension = 120
startingWidth = dimension*1.5
startingHeight = dimension*1.5
black = 0, 0, 0
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
smallfont = pygame.font.SysFont('Corbel', 35)
mediumfont = pygame.font.SysFont('Corbel', 70)
bigfont = pygame.font.SysFont('Corbel', 200)
text1 = smallfont.render('play', True, color)
text2 = smallfont.render('edit map', True, color)
text3 = smallfont.render('play edited map', True, color)
text4 = bigfont.render('GAME OVER', True, color)
text5 = bigfont.render('YOU WIN', True, color)
text6 = mediumfont.render('press escape to go back to menu', True, color)

class Player(pygame.sprite.Sprite):
    def __init__(self, pos=(0, 0), size=(dimension, dimension)):
        super(Player, self).__init__()
        self.animationTime=0
        self.points=1
        self.stop=0
        self.boardX = startingWidth//dimension
        self.boardY = startingHeight//dimension
        self.speed = [0,0]
        self.speedNew = [0,0]
        self.flagW = self.flagS = self.flagA = self.flagD = 0
        self.board = map.Map(width//dimension)
        self.board.map[int(self.boardX)][int(self.boardY)] = 3
        #print(self.board.mapPrint())
        self.original_image = pygame.Surface(size)
        self.pac_mans = [pygame.image.load("pac_man_1.png"), pygame.image.load("pac_man_2.png")]
        pac_man = self.pac_mans[1]
        pac_man = pygame.transform.scale(pac_man, (dimension, dimension))
        self.pac_mans[1] = pac_man
        pac_man = self.pac_mans[0]
        pac_man = pygame.transform.scale(pac_man, (dimension, dimension))
        self.pac_mans[0] = pac_man
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
                    pygame.draw.circle(screen, 	(255,255,0), (x*dimension+dimension/2,y*dimension+dimension/2), dimension/10)

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
        if self.board.checkPoints(self.points) == 1:
            self.stop=1

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
            self.points += 1
            #print(self.points)
        self.rect = self.rect.move(self.speed)
        self.board.changePosition(int(self.boardX), int(self.boardY))
        #print(self.board.mapPrint())
        #self.animationTime += 1
        #if self.animationTime == 30 and self.image==self.pac_mans[0]:
        #    self.original_image=self.pac_mans[1]
        #    self.image = self.original_image
        #    self.animationTime = 0
        #elif self.animationTime == 30:
        #    self.original_image = self.pac_mans[0]
        #    self.image = self.original_image
        #    self.animationTime = 0
        #print(self.board.mapPrint())
        #print(self.speed)

def main():
    player = Player(pos=(startingWidth, startingHeight))
    playerEdit = Player(pos=(startingWidth, startingHeight))
    newMap = playerEdit.board.map.copy()
    newPoints = playerEdit.board.maxPoints
    mode=0
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
                        player.stop = 0
            if player.stop == 0:
                player.playerMove()
                player.check()
                screen.fill(black)
                screen.blit(player.image, player.rect)
                player.draw()
                pygame.display.set_caption("Pac-man: GAME")
                pygame.display.update()
                pygame.display.flip()
            else:
                screen.blit(text5, (1, height/2))
                screen.blit(text6, (width / 8, height / 1.5))
                pygame.display.update()
                pygame.display.flip()

        width1 = width / 2
        width11 = width1 + width/5
        height1 = height / 4
        height11 = height1 + height/20
        height2 = height / 3
        height22 = height2 + height / 20
        height3 = height / 3 * 2
        height33 = height3 + height / 20
        while 1 and mode == 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width1 <= mouse[0] <= width11 and height1 <= mouse[1] <= height11:
                        mode=1
                        player = Player(pos=(startingWidth, startingHeight))
                    if width1 <= mouse[0] <= width11 and height2 <= mouse[1] <= height22:
                        mode=2
                        playerEdit.board.resetMap()
                        newMap=playerEdit.board.map.copy()
                        playerEdit = Player(pos=(startingWidth, startingHeight))
                        playerEdit.board.overwrite(newMap.copy())
                        playerEdit.board.changePosition(int(playerEdit.boardX), int(playerEdit.boardY))

                    if width1 <= mouse[0] <= width11 and height3 <= mouse[1] <= height33:
                        mode=3
                        playerEdit.board.resetMap()
                        playerEdit = Player(pos=(startingWidth, startingHeight))
                        playerEdit.board.overwrite(newMap.copy())
            mouse = pygame.mouse.get_pos()
            screen.fill(black)
            if width1 <= mouse[0] <= width11 and height1 <= mouse[1] <= height11:
                pygame.draw.rect(screen, color_light, [width / 2, height / 4, width/5, height/20])
            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height / 4, width/5, height/20])

            if width1 <= mouse[0] <= width11 and height2 <= mouse[1] <= height22:
                pygame.draw.rect(screen, color_light, [width / 2, height / 3, width/5, height/20])
            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height / 3, width/5, height/20])

            if width1 <= mouse[0] <= width11 and height3 <= mouse[1] <= height33:
                pygame.draw.rect(screen, color_light, [width / 2, height3, width/5, height/20])
            else:
                pygame.draw.rect(screen, color_dark, [width / 2, height3, width/5, height/20])
            screen.blit(text1, (width / 2 + 50, height / 4))
            screen.blit(text2, (width / 2 + 50, height / 3))
            screen.blit(text3, (width / 2, height3))
            pygame.display.set_caption("Pac-man: MENU")
            pygame.display.update()
            pygame.display.flip()

        while 1 and mode == 2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    playerEdit.board.changeElement(mouse[0]//dimension, mouse[1]//dimension)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        mode=0
            mouse = pygame.mouse.get_pos()
            screen.fill(black)
            screen.blit(playerEdit.image, playerEdit.rect)
            playerEdit.draw()
            pygame.display.set_caption("Pac-man: EDIT MAP")
            pygame.display.update()
            pygame.display.flip()

        while 1 and mode==3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        playerEdit.up()
                    if event.key == pygame.K_s:
                        playerEdit.down()
                    if event.key == pygame.K_a:
                        playerEdit.left()
                    if event.key == pygame.K_d:
                        playerEdit.right()
                    if event.key == pygame.K_ESCAPE:
                        mode=0
                        playerEdit.stop=0
            if playerEdit.stop == 0:
                playerEdit.playerMove()
                playerEdit.check()
                screen.fill(black)
                screen.blit(playerEdit.image, playerEdit.rect)
                playerEdit.draw()
                pygame.display.set_caption("Pac-man: GAME: edited map")
                pygame.display.update()
                pygame.display.flip()
            else:
                screen.blit(text5, (1, height/2))
                screen.blit(text6, (width / 8, height / 1.5))
                pygame.display.update()
                pygame.display.flip()

if __name__ == '__main__':

    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Pac-man")
    main()