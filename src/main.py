import pygame
import sys

from const import *


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Chess Game')
        self.screen = pygame.display.set_mode((900,900))
        self.clock = pygame.time.Clock()
        self.running = True

    def mainloop(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill screen with color
            self.screen.fill("white")

            # RENDER GAME 


            # flip() the display to put work to screen
            pygame.display.flip()

            self.clock.tick(60) # limit FPS to 60

        pygame.quit()



if __name__ == '__main__':
    main = Main()
    main.mainloop()
