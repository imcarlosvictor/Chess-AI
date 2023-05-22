class Piece:
    def __init__(self, name, colour, value, moved, texture=NONE, texture_rect=NONE):
        self.name = name
        self.color = colour
        self.value = value
        self.moved = moved
        self.texture = texture
        self.texture_rect = texture_rect

        self.value_sign = 1 if 'white' else -1

    def add_move(self):
        pass

    def set_textures(self):
        pass


class Pawn(Piece):
    def __init___(self, colour):
        if colour == 'white':
            self.dir = -1
        elif colour == 'black':
            self.dir = 1
        super().__init__('pawn', colour, 1.0);


class  Knight(Piece):
    def __init__(self, colour):
        super().__init__('knight', colour, 3.0)


class  Bishop(Piece):
    def __init__(self, colour):
        super().__init__('bishop', colour, 3.001)


class Rook(Piece):
    def __init__(self, colour):
        super().__init__('rook', colour, 5.0)


class Queen(Piece):
    def __init__(self, colour):
        super().__init__('queen', colour, 9.0)


class King(Piece):
    def __init__(self, colour):
        super().__init__('king', colour, 999)
