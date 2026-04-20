import pygame
# Initialize Pygame
pygame.init()

class Window():
    def __init__(self, caption, wsize):
        self.info = pygame.display.Info()
        # Define window dimensions
        self.WIDTH, self.HEIGHT = wsize[0], wsize[1]
        self.WSIZE = wsize
        self.SCREEN = pygame.display.set_mode(self.WSIZE)
        self.caption = caption
        pygame.display.set_caption(self.caption)
        self.monitor_width, monitor_height = self.info.current_w, self.info.current_h

        # Define colors using RGB values
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.BLUE = (15, 15, 255)
        self.DARK_GREEN = (40, 255, 40)
        # Fill the screen
        self.SCREEN.fill(self.BLACK)
        # Create a clock object to control the frame rate
        self.CLOCK = pygame.time.Clock()

    #clears the screen
    def clear(self):
        pygame.display.flip()
        self.SCREEN.fill(self.BLACK)
    #convert coordinates to 0, 0 being at the center of the canvas
    def convertcanvas(self, coordinate):
        return(coordinate+self.WIDTH/2)