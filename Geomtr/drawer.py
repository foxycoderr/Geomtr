from logger import Logger
import pygame
import ctypes


class Drawer:
    """ Draws out points and lines using coordinates worked out by the coordinator. """
    def __init__(self):
        pygame.init()
        user32 = ctypes.windll.user32
        self.screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)  # get screen size
        self.screensize = self.screensize[0], self.screensize[1]-60
        self.screen = pygame.display.set_mode(self.screensize)  # create screen
        self.clock = pygame.time.Clock()
        self.screen.fill("white")
        pygame.display.flip()  # update display

    def draw(self):  # just displays a white screen for now
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill("white")

            pygame.display.flip()

        pygame.quit()


drawer = Drawer()
drawer.draw()
