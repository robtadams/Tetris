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

    def main(self):

        """ Draw Game Board """

        for y in range(self.width):

            for x in range(self.height):

                outsideRect = [y * self.cellSize, x * self.cellSize,
                               self.cellSize, self.cellSize]

                insideRect = [y * self.cellSize + 1, x * self.cellSize + 1,
                              self.cellSize - 2, self.cellSize - 2]

                pygame.draw.rect(self.screen, (25, 25, 25), outsideRect)
                pygame.draw.rect(self.screen, (0 , 0 , 0 ), insideRect)

        pygame.display.update()

Game = Tetris()
Game.main()
