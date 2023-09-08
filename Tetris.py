import pygame
import random
import time

from Pieces import Piece

global TEST
TEST = True

class Tetris():

    def __init__(self):

        """ Initialization """

        # cellSize: the size of each cell in the game
        self.cellSize = 25

        # width: the width of the screen
        self.width = 15

        # height: the height of the screen
        self.height = self.width * 2

        # clock: pygame's internal clock
        self.clock = pygame.time.Clock()

        # running: whether the game is currently running or not
        self.running = True

        # screen: the game screen
        self.screen = pygame.display.set_mode((self.cellSize * self.width,
                                                self.cellSize * self.height))

        # gravityTimerMax: the max number of ticks for gravity to apply to the current piece
        self.gravityTimerMax = 10

        # gravityTimer: the number of remaining ticks before gravity is applied to the current piece
        self.gravityTimer = self.gravityTimerMax

        # createPiece: whether a piece needs to be created or not
        self.createPiece = True

        # piece: the piece the player is currently controlling
        self.piece = None

        """ Constructing Block Array """

        # blockArray: a 2D array of all the cells in the game
        self.blockArray = []

        # For each row in the game...
        for row in range(self.height):

            # ... make a temp list
            temp = []

            # For each column in the row...
            for col in range(self.width):

                # ... append a 0 to the temp list
                temp.append(0)

            # Append the temp list to the block array
            self.blockArray.append(temp)

        """ Print Init Values """

        if TEST:

            print("=== Init Values ===")
            print("Celll Size: {0}\nWidth: {1}\nHeight: {2}".format(self.cellSize, self.width, self.height))
            print("\nGravity Timer Max: {0}\nGravity Timer: {1}".format(self.gravityTimerMax, self.gravityTimer))
            print("\nBlock Array: 0 = Empty | 1 = Active | -1 = Static")
            for row in self.blockArray:
                for col in row:
                    print(col, end=" ")
                print()
            print()

    def cleanup(self):

        """ Cleanup """

        # For each row in the block array...
        for y, row in enumerate(self.blockArray):

            # ... for each column in the row...
            for x, col in enumerate(row):

                # ... if the cell has an active block in it...
                if col == 1:

                    # ... remove the active block from the cell
                    self.blockArray[y][x] = 0

                    # Build the outside (gray) rectangle
                    outsideX = x * self.cellSize
                    outsideY = y * self.cellSize
                    outsideRect = [outsideX, outsideY, self.cellSize, self.cellSize]

                    # Build the inside (black) rectangle
                    insideX = x * self.cellSize + 1
                    insideY = y * self.cellSize + 1
                    insideRect = [insideX, insideY, self.cellSize - 2, self.cellSize - 2]

                    # Draw over the active cell with a grid cell
                    pygame.draw.rect(self.screen, (25, 25, 25), outsideRect)
                    pygame.draw.rect(self.screen, (0 , 0 , 0 ), insideRect)
                    

    def update(self):

        """ Update """

        # For each location in the piece's locations...
        for location in self.piece.locations:

            # ... get the X and Y coordinates of the cell
            pieceX = location[0]
            pieceY = location[1]

            # If the cell is within the boundaries of the game...
            if pieceX >= 0 and pieceY >= 0:

                # Set the respective cell in the blockArray to 1 (active)
                self.blockArray[pieceY][pieceX] = 1

                # Get the X and Y coordinates for the cell
                xCoord = pieceX * self.cellSize
                yCoord = pieceY * self.cellSize
                drawRect = [xCoord, yCoord, self.cellSize, self.cellSize]

                # Draw the active cell onto the screen
                pygame.draw.rect(self.screen, (0, 255, 155), drawRect)
                
    def main(self):

        """ Draw Game Board """

        # For each row in the board...
        for y in range(self.width):

            # ... for each column in the row...
            for x in range(self.height):

                # ... build the outside (gray) square
                outsideRect = [y * self.cellSize, x * self.cellSize,
                               self.cellSize, self.cellSize]

                # Build the inside (black) square
                insideRect = [y * self.cellSize + 1, x * self.cellSize + 1,
                              self.cellSize - 2, self.cellSize - 2]
                
                pygame.draw.rect(self.screen, (25, 25, 25), outsideRect)
                pygame.draw.rect(self.screen, (0 , 0 , 0 ), insideRect)

        # Update the display
        pygame.display.update()

        """ Main Game Loop """

        # While running is True...
        while self.running:

            time.sleep(.1)

            # Check if piece needs to be made...
            if self.createPiece:

                # ... create a new piece
                self.piece = Piece()

                if TEST:
                    print("=== New Piece Value ===\nPiece Name: {}".format(self.piece.name))
                
                self.createPiece = False

            # Check if piece needs to fall...
            if self.gravityTimer <= 0:

                # Reset the gravit timer
                self.gravityTimer = self.gravityTimerMax

                # Remove all 1s (active pieces) from the board
                self.cleanup()

                # Move the active piece down 1 square
                self.piece.fall()

                # Update the blockArray with the new piece locations
                self.update()

                pygame.display.update()

                if TEST:
                    print("\nBlock Array: 0 = Empty | 1 = Active | -1 = Static")
                    for row in self.blockArray:
                        for col in row:
                            print(col, end=" ")
                        print()
                    print()

            else:
                self.gravityTimer -= 1

            # Check if piece is being moved by the player...

            # Cleanup the screen

            # Draw piece

Game = Tetris()
Game.main()
