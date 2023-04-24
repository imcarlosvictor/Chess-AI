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
                if row == 1 or row % 2 != 0:
                    self.square.create('black')
                    if col == 1 or col % 2 != 0:
                        self.square.create('white')
                elif row == 0 or row % 2 == 0:
                    self.square.create('white')
                    if col == 1 or col % 2 != 0:
                        self.square.create('black')

                self.squares_list.append(self.square)
                count = count + 1
        pass

    def add_pieces():
        pass

    def promote_piece():
        pass

    def valid_move():
        pass

    def calc_move():
        pass

