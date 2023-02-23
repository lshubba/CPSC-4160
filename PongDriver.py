import pygame
from PongController import PongController
from PongModel import PongModel
from PongView import PongView


if __name__ == '__main__':
    pygame.init()
    screen_width = 640
    screen_height = 480
    model = PongModel(screen_width, screen_height)
    view = PongView(screen_width, screen_height)
    controller = PongController(model, view)
    controller.run()
    pygame.quit()
