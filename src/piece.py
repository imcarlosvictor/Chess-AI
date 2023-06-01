import os


class Piece:
    def __init__(self, name, color, value, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        self.value = value
        self.moves = [] # Store previous moves
        self.moved = False 
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect

        # Values for white and black pieces
        value_sign = 1 if 'white' else -1
        self.value = value * value_sign

    def set_texture(self, size=80):
        "Get the respective image for the chess piece."

        self.texture = os.path.join(f'img/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)


class Pawn(Piece):
    def __init___(self, color):
        if color == 'white':
            self.dir = -1
        elif color == 'black':
            self.dir = 1
        super().__init__('pawn', color, 1.0);


class  Knight(Piece):
    def __init__(self, color):
        super().__init__('knight', color, 3.0)


class  Bishop(Piece):
    def __init__(self, color):
        super().__init__('bishop', color, 3.001)


class Rook(Piece):
    def __init__(self, color):
        super().__init__('rook', color, 5.0)


class Queen(Piece):
    def __init__(self, color):
        super().__init__('queen', color, 9.0)


class King(Piece):
    def __init__(self, color):
        super().__init__('king', color, 999)
