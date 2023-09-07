class Piece():

    def __init__(self):

        self.locations = []

    def Square(self):

        self.locations = [[7, -2], [8, -2], [7, -1], [8, -1]]

    def Line(self):

        self.locations = [[7, -4], [7, -3], [7, -2], [7, -1]]

    def LBlockRight(self):

        self.locations = [[7, -3], [7, -2], [7, -1], [8, -1]]

    def LBlockLeft(self):

        self.locations = [[7, -3], [7, -2], [7, -1], [6, -1]]

    def ZBlockRight(self):

        self.locations = [[6, -1], [7, -1], [7, -2], [8, -2]]

    def ZBlockLeft(self):

        self.locations = [[6, -2], [7, -2], [7, -1], [8, -1]]

    def TBlock(self):

        self.locations = [[6, -2], [7, -2], [7, -1], [8, -2]]

    
