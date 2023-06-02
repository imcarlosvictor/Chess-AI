from const import *
from square import *
from piece import *


class Board:
    def __init__(self, surface):
        self.surface = surface
        self.squares_list = []

        self.create()
        self.add_pieces('white')
        self.add_pieces('black')

    def create(self):
        count = 1
        for row in range(ROWS):
            for col in range(COLS):
                Xpos = col * 100
                Ypos = row * 100
                self.square = Square(Xpos, Ypos, self.surface)

                # Color squares accordingly
                # color = ''
                rgb = ()
                if row == 1 or row % 2 != 0:
                    # black
                    rgb = (119,149,87)
                    if col == 1 or col % 2 != 0:
                        # white
                        rgb = (239,238,210) # white
                elif row == 0 or row % 2 == 0:
                    # white
                    rgb = (239,238,210)
                    if col == 1 or col % 2 != 0:
                        # black
                        rgb = (119,149,87)
                pygame.draw.rect(self.surface, rgb, pygame.Rect(Xpos, Ypos, SQSIZE, SQSIZE))

                self.squares_list.append(self.square)
                count = count + 1

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
            self.square_list[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights
        self.squares_list[1] = Square(row_other, 1, Knight(color))
        self.squares_list[6] = Square(row_other, 6, Knight(color))

        # Bishops
        self.squares_list[2] = Square(row_other, 2, Bishop(color))
        self.squares_list[5] = Square(row_other, 5, Bishop(color))

        # Rooks 
        self.squares_list[0] = Square(row_other, 0, Rook(color))
        self.squares_list[7] = Square(row_other, 7, Rook(color))

        # Queen 
        self.squares_list[3] = Square(row_other, 3, Queen(color))

        # King 
        self.squares_list[4] = Square(row_other, 4, King(color))

        # pawn = pygame.transform.scale(pygame.image.load('../img/pawn_white.png'), [400, 400])
        # self.surface.blit(pawn, [0,0])

    def promote_piece(self):
        pass

    def valid_move(self):
        pass

    def calc_move(self):
        pass

