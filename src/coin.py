import pygame


class coin():
    def __init__(self, position):
        self._image = pygame.image.load('../resources/coin.png')
        self._position = position

    def get_position(self):
        return self._position

    def set_position(self, value):
        self._position = value
