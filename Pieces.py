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

    def fall(self, gameHeight, blockArray):

        """ Boundry Check """

        # tempLocations: A temporary list that will contain the locations of
        #                the piece's next locations.
        tempLocations = []

        # For each location in the piece's locations...
        for location in self.locations:

            # ... if the piece doesn't fall out of bounds ...
            if location[1] + 1 < gameHeight:

                # ... calculate the piece's next location
                tempLocation = [location[0], location[1] + 1]

            # If the piece falls out of bounds...
            else:

                # ... stop falling
                return False

            # Add the next location to tempLocations
            tempLocations.append(tempLocation)

        """ Collision Check """

        # For each new location...
        for location in tempLocations:

            # Get the X and Y coordinates for the parts of the piece
            x = location[0]
            y = location[1]

            # ... Check if the piece will collide with another piece...
            if blockArray[y][x] == -1:

                # ... stop falling
                return False

        """ Update Locations """

        # Update locations with the new locations
        self.locations = tempLocations

        # Allow the piece to fall down
        return True

    def goRight(self, gameWidth):

        """ Move the Piece Right """

        # tempLocations: A temporary list that will contain the locations of
        #                the piece's next locations.
        tempLocations = []

        # For each location in the piece's locations...
        for location in self.locations:

            # ... if the piece is moving inside the boundry...
            if location[0] + 1 < gameWidth:

                # ... calculate the piece's next location
                tempLocation = [location[0] + 1, location[1]]

            # If the piece moves out of bounds...
            else:

                # ... Stop moving
                return False

            # Add the next location to tempLocations
            tempLocations.append(tempLocation)

        # Update the locations with the new locations
        self.locations = tempLocations

        # Allow the piece to move Right
        return True

    def goLeft(self):

        """ Move the Piece Left """

        # tempLocations: A temporary list that will contain the locations of
        #                the piece's next locations.
        tempLocations = []

        # For each location in the piece's locations...
        for location in self.locations:

            # ... if the piece is moving inside the boundry...
            if location[0] - 1 >= 0:

                # ... calculate the piece's next location
                tempLocation = [location[0] - 1, location[1]]

            # If the piece moves out of bounds...
            else:

                # ... Stop moving
                return False

            # Add the next location to tempLocations
            tempLocations.append(tempLocation)

        # Update the locations with the new locations
        self.locations = tempLocations

        # Allow the piece to move Left
        return True

    """ Define the piece's default locations """
    
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

    
