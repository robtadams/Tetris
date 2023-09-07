import pygame
import random
import time

global TEST
TEST = True

class Tetris():

    def __init__(self):

        self.cellSize = 25
        self.width = 15
        self.height = self.width * 2

        self.testCellX = 5
        self.testCellY = 5

        self.clock = pygame.time.Clock()

        self.running = True

        self.screen = pygame.display.set_mode((self.cellSize * self.width,
                                                self.cellSize * self.height))

        self.gravityTimerMax = 10
        self.gravityTimer = self.gravityTimerMax

        self.blockArray = []

        for row in range(self.height):

            temp = []

            for col in range(self.width):

                temp.append(0)

            self.blockArray.append(temp)

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
