import pygame

from const import *


class Square:
    def __init__(self, surface, row, col):
        self.surface = surface
        self.row = row
        self.col = col
        # self.alphacol = alphacol

    def create(self, color):
        rgb = ()
        if color.lower() == 'white':
            rgb = (239,238,210)
        elif color.lower() == 'black':
            rgb = (119,149,87)
        # Draw square on screen
        pygame.draw.rect(self.surface, rgb, pygame.Rect(self.row, self.col, SQSIZE, SQSIZE))
