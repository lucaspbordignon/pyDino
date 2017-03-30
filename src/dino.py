import pygame


class dino():
    def __init__(self, params):
        self.char_types = {
            0: 'default',
        }
        self.params = params
        self.actual_type = self.char_types[params['type']]
        self.image = self.load_image(str(self.actual_type) + '.png')

    def get_image(self):
        return self.image

    def get_position(self):
        return self.params['pos']

    def set_position(self, value):
        self.params['pos'] = value

    def change_type(self, type_desired):
        self.actual_type = self.char_types[type_desired]
        self.image = self.load_image(str(self.actual_type) + '.png')

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
