import random

class Piece():

    def __init__(self, shapeVal):

        """ Initialization """

        # locations: the current location of each segment in the piece
        self.locations = []

        # name: the name of the piece
        self.name = None

        # color: the color of the piece
        self.color = None

        # Pick one of the pieces among the list of remaining shapes
        self.generatePiece(shapeVal)

    def generatePiece(self, shapeVal):

        """ Generate New Piece """

        # Find the piece that was chosen
        match shapeVal:

            # Square
            case 1:
                self.Square()
                self.name = "Square"
                self.color = "yellow"

            # Line
            case 2:
                self.Line()
                self.name = "Line"
                self.color = "cyan"

            # L Block Right
            case 3:
                self.LBlockRight()
                self.name = "L Block Right"
                self.color = "orange"

            # L Block Left
            case 4:
                self.LBlockLeft()
                self.name = "L Block Left"
                self.color = "blue"

            # Z Block Right
            case 5:
                self.ZBlockRight()
                self.name = "Z Block Right"
                self.color = "light green"

            # Z Block Left
            case 6:
                self.ZBlockLeft()
                self.name = "Z Block Left"
                self.color = "red"

            # T Block
            case 7:
                self.TBlock()
                self.name = "T Block"
                self.color = "purple"

    def fall(self, gameHeight):

        tempLocations = []

        for location in self.locations:

            if location[1] + 1 < gameHeight:

                tempLocation = [location[0], location[1] + 1]

            else:

                return False

            tempLocations.append(tempLocation)

        self.locations = tempLocations

        return True

    def goRight(self, gameWidth):

        tempLocations = []

        for location in self.locations:

            if location[0] + 1 < gameWidth:

                tempLocation = [location[0] + 1, location[1]]

            else:

                return False

            tempLocations.append(tempLocation)

        self.locations = tempLocations

        return True

    def goLeft(self):

        tempLocations = []

        for location in self.locations:

            if location[0] - 1 >= 0:

                tempLocation = [location[0] - 1, location[1]]

            else:

                return False

            tempLocations.append(tempLocation)

        self.locations = tempLocations

        return True
    
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

    
