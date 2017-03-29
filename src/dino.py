from utils import *


class dino():
    def __init__(self, params):
        char_types = {
            0: 'default',
        }
        self.position = params['pos']
        self.actual_type = char_types[params['type']]
        self.image = load_image(str(self.actual_type) + '.png')

    def get_image(self):
        return self.image

    def get_position(self):
        return self.position

    def change_type(self, type_desired):
        self.actual_type = char_types[type_desired]
        self.image = load_image(str(self.actual_type) + '.png')
