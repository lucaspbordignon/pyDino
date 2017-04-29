import pygame


class dino():
    def __init__(self, params, lives=1, smoothness_rate=0.3):
        self.char_types = {
            0: 'default',
            1: 'albino',
        }
        self.params = params
        self.actual_type = self.char_types[params['type']]
        self._image = self.load_image(str(self.actual_type) + '.png')
        self._size = (self._image.get_width(), self._image.get_height())
        self._movement = 1
        self._smoothness_rate = smoothness_rate
        self._jumping = False
        self._lives = lives

    def get_image(self):
        return self._image

    def get_position(self):
        return self.params['pos']

    def get_movement(self):
        return self._movement

    def get_size(self):
        return self._size

    def get_lives(self):
        return self._lives

    def is_jumping(self):
        return self._jumping

    def set_position(self, value):
        self.params['pos'] = value

    def set_movement(self, value):
        self._movement = value

    def set_jumping(self, value):
        self._jumping = value

    def set_lives(self, value):
        self._lives = value

    def jump(self, threshold):
        if (self._movement):
            self.set_movement(self._movement - self._smoothness_rate)
        # Updates the position
        self.set_position((threshold[0], threshold[1] - self._movement))

    def change_type(self, type_desired):
        self.actual_type = self.char_types[type_desired]
        self._image = self.load_image(str(self.actual_type) + '.png')

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
