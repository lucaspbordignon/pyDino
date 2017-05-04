import pygame


class coin():
    def __init__(self, position, value=1):
        self._image = pygame.image.load('../resources/coin.png')
        self._position = position
        self._value = value

    def get_position(self):
        return self._position

    def get_size(self):
        return (self._image.get_width(), self._image.get_height())

    def get_image(self):
        return self._image

    def value(self):
        return self._value

    def set_position(self, value):
        self._position = value

    def hitted(self, char_pos, char_size):
        coin_pos = self.get_position()
        coin_size = self.get_size()
        if (coin_pos[0] <= char_pos[0] + char_size[0] <= coin_pos[0] + coin_size[0]):
            if (coin_pos[1] <= char_pos[1] <= coin_pos[1] + coin_size[1]):
                return True
        return False
