from const import *
from square import *
from piece import *


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

    def add_pieces(self, color):
        if color == 'white':
            # place white at the bottom of the board
            row_pawn, row_other = (6,7)
        else:
            row_pawn, row_other = (1,0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(Pawn(color), row_pawn, col)

        # Knights



        # pawn = pygame.transform.scale(pygame.image.load('../img/pawn_white.png'), [400, 400])
        # self.surface.blit(pawn, [0,0])

    def promote_piece(self):
        pass

    def valid_move(self):
        pass

    def calc_move(self):
        pass

