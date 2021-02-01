class Map():
    def __init__(self, dimension):
        self.dimension = dimension
        self.row=[2,2]
        for x in range(dimension-2):
            self.row.insert(1, 2)
        self.map = [self.row.copy(), self.row.copy()]
        self.row = [2, 2]
        for x in range(dimension - 2):
            self.row.insert(1, 1)
        for x in range(dimension-2):
            self.map.insert(1, self.row.copy())

    def mapPrint(self):
        for x in range(self.dimension):
            print(self.map[x])

    def getElement(self, x, y):
        return self.map[x][y]

    def eat(self, x, y):
        self.map[x][y] = 0

    def changePosition(self, x, y):
        self.map[x][y] = 3

    def changeElement(self, x, y):
        if self.getElement(x, y) == 0:
            self.map[x][y]=1
        elif self.getElement(x, y) == 1:
            self.map[x][y]=2
        elif self.getElement(x, y) == 2 and x!=0 and y!=0 and x!=self.dimension-1 and y!=self.dimension-1:
            self.map[x][y]=1

    def overwrite(self, map):
        self.map=map

    def resetMap(self):
        for x in range(self.dimension):
            for y in range(self.dimension):
                if self.getElement(x, y) == 0:
                    self.changeElement(x, y)