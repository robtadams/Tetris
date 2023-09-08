import random

class Piece():

    def __init__(self):

        """ Initialization """

        # locations: the current location of each segment in the piece
        self.locations = []

        # name: the name of the piece
        self.name = None

        # remainingShapes: the pieces that have yet to be picked in the set
        self.remainingShapes = [1, 2, 3, 4, 5, 6, 7]

        # Pick one of the pieces among the list of remaining shapes
        self.generatePiece()

    def generatePiece(self):

        """ Generate New Piece """

        # If there are no more pieces remaining...
        if len(self.remainingShapes) <= 0:

            # ... reset the list of remaining pieces
            self.remainingShapes = [1, 2, 3, 4, 5, 6, 7]

        # Grab a piece from the list of remaining pieces
        value = random.randint(1, len(self.remainingShapes))

        # Remove the chosen piece from the list of remaining pieces
        self.remainingShapes.remove(value)

        # Find the piece that was chosen
        match value:

            # Square
            case 1:
                self.Square()
                self.name = "Square"

            # Line
            case 2:
                self.Line()
                self.name = "Line"

            # L Block Right
            case 3:
                self.LBlockRight()
                self.name = "L Block Right"

            # L Block Left
            case 4:
                self.LBlockLeft()
                self.name = "L Block Left"

            # Z Block Right
            case 5:
                self.ZBlockRight()
                self.name = "Z Block Right"

            # Z Block Left
            case 6:
                self.ZBlockLeft()
                self.name = "Z Block Left"

            # T Block
            case 7:
                self.TBlock()
                self.name = "T Block"

    def fall(self):

        for location in self.locations:

            location[1] += 1

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

    
