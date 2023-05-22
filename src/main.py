import pygame
import sys

from const import *
# from square import *
from board import *


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Chess Game')
        self.screen = pygame.display.set_mode((800,800))
        self.clock = pygame.time.Clock()
        self.running = True

        self.screen.fill('black')
        self.board = Board(self.screen)
        self.board.create()
        pygame.display.flip()

#         self.square = Square(self.screen, 0, 0, 0 , 'black')

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # # Fill screen with color
            # self.screen.fill("white")

            # RENDER GAME 
            # self.square.create_square()

            # flip() the display to put work to screen
            pygame.display.flip()

            self.clock.tick(60) # limit FPS to 60

        pygame.quit()



if __name__ == '__main__':
    main = Main()
    main.mainloop()
