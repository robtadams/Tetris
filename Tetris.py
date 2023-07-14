import pygame
import random
import time

global TEST
TEST = True

class Tetris():

    def __init__(self):

        self.cellSize = 40
        self.width = 10 * self.cellSize
        self.height = 2 * self.width

        self.screen = pygame.display.set_mode((self.width, self.height))

    def main(self):

        for row in range(self.height):

            for cell in range(self.width):

                if TEST and (row + cell) % 2 == 0:

                    cellRect = [row * self.cellSize, cell * self.cellSize, self.cellSize, self.cellSize]

                    pygame.draw.rect(self.screen, "white", cellRect)

                    time.sleep(.1)

                    pygame.display.update()

myTetris = Tetris()

myTetris.main()
    
