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