from const import *
from square import *


class Board:
    def __init__(self, surface):
        self.surface = surface
        self.squares_list = []

    def create(self):
        count = 1
        for row in range(ROWS):
            for col in range(COLS):
                Xpos = col * 100
                Ypos = row * 100
                self.square = Square(self.surface, Xpos, Ypos)

                # Color squares accordingly
                color = ''
                if row == 1 or row % 2 != 0:
                    color = 'black'
                    if col == 1 or col % 2 != 0:
                        color = 'white'
                elif row == 0 or row % 2 == 0:
                    color = 'white'
                    if col == 1 or col % 2 != 0:
                        color = 'black'
                self.square.create(color)

                self.squares_list.append(self.square)
                count = count + 1

        self.add_pieces()

    def move(self):
        pass

    def add_pieces(self):
        pawn = pygame.transform.scale(pygame.image.load('../img/pawn_white.png'), [400, 400])
        self.surface.blit(pawn, [0,0])

    def promote_piece(self):
        pass

    def valid_move(self):
        pass

    def calc_move(self):
        pass

