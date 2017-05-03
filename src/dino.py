import pygame


class dino():
    def __init__(self, position, type, lives=3, smoothness_rate=0.3):
        self.actual_type = type
        self._image = pygame.image.load('../resources/' + self.actual_type + '.png')
        self._size = (self._image.get_width(), self._image.get_height())
        self._position = position
        self._movement = 1
        self._smoothness_rate = smoothness_rate
        self._jumping = False
        self._lives = lives
        self._coins = 0

    def get_image(self):
        return self._image

    def get_position(self):
        return self._position

    def get_movement(self):
        return self._movement

    def get_size(self):
        return self._size

    def get_lives(self):
        return self._lives

    def get_coins(self):
        return self._coins

    def is_jumping(self):
        return self._jumping

    def set_position(self, value):
        self._position = value

    def set_movement(self, value):
        self._movement = value

    def set_jumping(self, value):
        self._jumping = value

    def set_lives(self, value):
        self._lives = value

    def set_coins(self, value, type='default'):
        if (type is 'default'):
            self._coins = value
        if (type is 'increment'):
            self._coins += value

    def jump(self, threshold):
        if (self._movement):
            self.set_movement(self._movement - self._smoothness_rate)
        self.set_position((threshold[0], threshold[1] - self._movement))
