import pygame


class enemy():
    def __init__(self, media_name='cactus.png'):
        self.image = self.load_image(media_name)
        self.position = (0, 0)
        self.size = (self.image.get_width(), self.image.get_height())

    def get_position(self):
        return self.position

    def get_image(self):
        return self.image

    def get_size(self):
        return self.size

    def set_position(self, value):
        self.position = value

    def load_image(self, filename):
        return pygame.image.load(str('../resources/' + filename))
