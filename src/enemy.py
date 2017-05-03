import pygame


class enemy():
    def __init__(self, screen_size, ground, media_name='cactus.png'):
        self._image = pygame.image.load('../resources/' + media_name)
        self._size = (self._image.get_width(), self._image.get_height())
        self._position = (screen_size[0], ground['y_threshold'] - self._size[1])
        self.alreadyHit = False

    def get_position(self):
        return self._position

    def get_image(self):
        return self._image

    def get_size(self):
        return self._size

    def get_alreadyHit(self):
        return self.alreadyHit

    def set_alreadyHit(self, value):
        self.alreadyHit = value

    def set_position(self, value):
        self._position = value
